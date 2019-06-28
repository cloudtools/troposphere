# Converted from IAM_Policies_SNS_Publish_To_SQS.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import GetAtt, Output, Ref, Template
from troposphere.sns import Subscription, Topic
from troposphere.sqs import Queue, QueuePolicy


t = Template()

t.set_description("AWS CloudFormation Sample Template: This template "
                  "demonstrates the creation of a DynamoDB table.")

sqsqueue = t.add_resource(Queue("SQSQueue"))

snstopic = t.add_resource(Topic(
    "SNSTopic",
    Subscription=[Subscription(
        Protocol="sqs",
        Endpoint=GetAtt(sqsqueue, "Arn")
    )]
))

t.add_output(Output(
    "QueueArn",
    Value=GetAtt(sqsqueue, "Arn"),
    Description="ARN of SQS Queue",
))

t.add_resource(QueuePolicy(
    "AllowSNS2SQSPolicy",
    Queues=[Ref(sqsqueue)],
    PolicyDocument={
        "Version": "2008-10-17",
        "Id": "PublicationPolicy",
        "Statement": [{
            "Sid": "Allow-SNS-SendMessage",
            "Effect": "Allow",
            "Principal": {
              "AWS": "*"
            },
            "Action": ["sqs:SendMessage"],
            "Resource": GetAtt(sqsqueue, "Arn"),
            "Condition": {
                "ArnEquals": {"aws:SourceArn": Ref(snstopic)}
            }
        }]
    }
))

print(t.to_json())
