# Converted from S3_Bucket.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import Output, Ref, Template
from troposphere.s3 import Bucket, PublicRead


t = Template()

t.set_description(
    "AWS CloudFormation Sample Template S3_Bucket: Sample template showing "
    "how to create a publicly accessible S3 bucket. "
    "**WARNING** This template creates an Amazon S3 Bucket. "
    "You will be billed for the AWS resources used if you create "
    "a stack from this template.")

s3bucket = t.add_resource(Bucket("S3Bucket", AccessControl=PublicRead,))

t.add_output(Output(
    "BucketName",
    Value=Ref(s3bucket),
    Description="Name of S3 bucket to hold website content"
))

print(t.to_json())
