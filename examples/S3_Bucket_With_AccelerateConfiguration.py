# Converted from S3_Bucket.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import Output, Ref, Template
from troposphere.s3 import Bucket, PublicRead, AccelerateConfiguration

t = Template()

t.set_description(
    "AWS CloudFormation Sample Template S3_Bucket: Sample template showing :"
    "How to create a publicly accessible S3 bucket. "
    "How to enable S3 Transfer Acceleration. "
    "**WARNING** This template creates an Amazon S3 Bucket. "
    "You will be billed for the AWS resources used if you create "
    "a stack from this template.")

s3bucket = t.add_resource(Bucket(
    "S3Bucket",
    # Make public Read
    AccessControl=PublicRead,
    # Enable s3 Transfer Acceleration
    AccelerateConfiguration=AccelerateConfiguration(
        AccelerationStatus="Enabled",
    ),
))

t.add_output(Output(
    "BucketName",
    Value=Ref(s3bucket),
    Description="Name of S3 bucket with s3 transfer acceleration enabled",
))

print(t.to_json())
