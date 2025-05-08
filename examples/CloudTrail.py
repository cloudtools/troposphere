# Converted from CloudTrail example.
# http://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudtrail-trail.html.

from troposphere import GetAtt, Join, Parameter, Ref, Template
from troposphere.cloudtrail import Trail
from troposphere.s3 import Bucket, BucketPolicy
from troposphere.sns import Subscription, Topic, TopicPolicy

t = Template()

t.set_version("2010-09-09")

OperatorEmail = t.add_parameter(
    Parameter(
        "OperatorEmail",
        Type="String",
        Description="Email address to notify when new logs are published.",
    )
)

S3Bucket = t.add_resource(Bucket("S3Bucket", DeletionPolicy="Retain"))

topic = t.add_resource(
    Topic(
        "Topic",
        Subscription=[
            Subscription(
                Endpoint=Ref(OperatorEmail),
                Protocol="email",
            ),
        ],
    )
)

topic_policy = t.add_resource(
    TopicPolicy(
        "TopicPolicy",
        Topics=[Ref(topic)],
        PolicyDocument={
            "Version": "2008-10-17",
            "Statement": [
                {
                    "Action": "SNS:Publish",
                    "Principal": {"Service": "cloudtrail.amazonaws.com"},
                    "Resource": "*",
                    "Effect": "Allow",
                    "Sid": "AWSCloudTrailSNSPolicy",
                }
            ],
        },
    )
)

bucket_policy = t.add_resource(
    BucketPolicy(
        "BucketPolicy",
        PolicyDocument={
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "s3:GetBucketAcl",
                    "Principal": {"Service": "cloudtrail.amazonaws.com"},
                    "Resource": Join("", ["arn:aws:s3:::", Ref(S3Bucket)]),
                    "Effect": "Allow",
                    "Sid": "AWSCloudTrailAclCheck",
                },
                {
                    "Action": "s3:PutObject",
                    "Principal": {"Service": "cloudtrail.amazonaws.com"},
                    "Resource": Join(
                        "",
                        [
                            "arn:aws:s3:::",
                            Ref(S3Bucket),
                            "/AWSLogs/",
                            Ref("AWS::AccountId"),
                            "/*",
                        ],
                    ),
                    "Effect": "Allow",
                    "Sid": "AWSCloudTrailWrite",
                    "Condition": {
                        "StringEquals": {"s3:x-amz-acl": "bucket-owner-full-control"}
                    },
                },
            ],
        },
        Bucket=Ref(S3Bucket),
    )
)

myTrail = t.add_resource(
    Trail(
        "myTrail",
        IsLogging=True,
        S3BucketName=Ref(S3Bucket),
        SnsTopicName=GetAtt(topic, "TopicName"),
        DependsOn=[bucket_policy, topic_policy],
    )
)

print(t.to_json())
