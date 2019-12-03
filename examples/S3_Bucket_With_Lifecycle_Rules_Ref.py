# Converted from S3_Bucket.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import Output, Parameter, Ref, Template
from troposphere.s3 import Bucket, PublicRead, \
    LifecycleConfiguration, LifecycleRule

t = Template()

t.set_description(
    "AWS CloudFormation Sample Template S3_Bucket: Sample template showing :"
    "How to create a publicly accessible S3 bucket. "
    "How to set a lifecycle rule using a Ref. "
    "**WARNING** This template creates an Amazon S3 Bucket. "
    "You will be billed for the AWS resources used if you create "
    "a stack from this template.")

lifecycleDays = t.add_parameter(Parameter("LifecycleRuleDaysRef",
                                Type="Number", Default=3))

s3bucket = t.add_resource(Bucket(
    "S3Bucket",
    # Make public Read
    AccessControl=PublicRead,
    # Turn on Versioning to the whole S3 Bucket
    # Attach a LifeCycle Configuration

    LifecycleConfiguration=LifecycleConfiguration(Rules=[
        # Add a rule to
        LifecycleRule(
            # Rule attributes
            Id="S3BucketRule001",
            Prefix="/only-this-sub-dir",
            Status="Enabled",
            # use a reference rather than a literal
            ExpirationInDays=Ref(lifecycleDays)
        )
    ])
))

t.add_output(Output(
    "BucketName",
    Value=Ref(s3bucket),
    Description="Name of S3 bucket to hold website content"
))

print(t.to_json())
