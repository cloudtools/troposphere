# Converted from S3_Website_Bucket_With_Retain_On_Delete.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import GetAtt, Join, Output, Template
from troposphere.s3 import Bucket, PublicRead, WebsiteConfiguration


t = Template()

t.set_description(
    "AWS CloudFormation Sample Template "
    "S3_Website_Bucket_With_Retain_On_Delete: Sample template showing how to "
    "create a publicly accessible S3 bucket configured for website access "
    "with a deletion policy of retail on delete. "
    "**WARNING** This template creates an Amazon EC2 instance. "
    "You will be billed for the AWS resources used if you create "
    "a stack from this template.")

s3bucket = t.add_resource(Bucket(
    "S3Bucket",
    AccessControl=PublicRead,
    WebsiteConfiguration=WebsiteConfiguration(
        IndexDocument="index.html",
        ErrorDocument="error.html"
    )
))
# XXX - Add "DeletionPolicy" : "Retain" to the resource

t.add_output([
    Output(
        "WebsiteURL",
        Value=GetAtt(s3bucket, "WebsiteURL"),
        Description="URL for website hosted on S3"
    ),
    Output(
        "S3BucketSecureURL",
        Value=Join("", ["http://", GetAtt(s3bucket, "DomainName")]),
        Description="Name of S3 bucket to hold website content"
    ),
])

print(t.to_json())
