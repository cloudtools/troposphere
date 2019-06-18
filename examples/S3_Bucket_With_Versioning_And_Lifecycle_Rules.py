# Converted from S3_Bucket.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import Output, Ref, Template
from troposphere.s3 import Bucket, PublicRead, VersioningConfiguration, \
    LifecycleConfiguration, LifecycleRule, NoncurrentVersionTransition, \
    LifecycleRuleTransition

t = Template()

t.set_description(
    "AWS CloudFormation Sample Template S3_Bucket: Sample template showing :"
    "How to create a publicly accessible S3 bucket. "
    "How to enable bucket object versions. "
    "How to archive and delete current objects. "
    "How to archive and delete non current (versioned) objects. "
    "**WARNING** This template creates an Amazon S3 Bucket. "
    "You will be billed for the AWS resources used if you create "
    "a stack from this template.")

s3bucket = t.add_resource(Bucket(
    "S3Bucket",
    # Make public Read
    AccessControl=PublicRead,
    # Turn on Versioning to the whole S3 Bucket
    VersioningConfiguration=VersioningConfiguration(
        Status="Enabled",
    ),
    # Attach a LifeCycle Configuration

    LifecycleConfiguration=LifecycleConfiguration(Rules=[
        # Add a rule to
        LifecycleRule(
            # Rule attributes
            Id="S3BucketRule001",
            Prefix="/only-this-sub-dir",
            Status="Enabled",
            # Applies to current objects
            ExpirationInDays=3650,
            Transitions=[
                LifecycleRuleTransition(
                    StorageClass="STANDARD_IA",
                    TransitionInDays=60,
                ),
            ],
            # Applies to Non Current objects
            NoncurrentVersionExpirationInDays=365,
            NoncurrentVersionTransitions=[
                NoncurrentVersionTransition(
                    StorageClass="STANDARD_IA",
                    TransitionInDays=30,
                ),
                NoncurrentVersionTransition(
                    StorageClass="GLACIER",
                    TransitionInDays=120,
                ),
            ],
        ),
    ]),

))

t.add_output(Output(
    "BucketName",
    Value=Ref(s3bucket),
    Description="Name of S3 bucket to hold website content"
))

print(t.to_json())
