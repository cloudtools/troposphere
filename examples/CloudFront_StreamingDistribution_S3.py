# Converted from CloudFront_S3.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import GetAtt, Join, Output
from troposphere import Parameter, Ref, Template
from troposphere.cloudfront import StreamingDistribution
from troposphere.cloudfront import StreamingDistributionConfig
from troposphere.cloudfront import S3Origin
from troposphere.cloudfront import TrustedSigners


t = Template()

t.set_description(
    "AWS CloudFormation Sample Template CloudFront_S3: Sample template "
    "showing how to create an Amazon CloudFront Streaming distribution "
    "using an S3 origin. "
    "**WARNING** This template creates a CloudFront distribution. "
    "You will be billed for the AWS resources used if you create "
    "a stack from this template.")

s3dnsname = t.add_parameter(Parameter(
    "S3DNSName",
    Description="The DNS name of an existing S3 bucket to use as the "
                "Cloudfront distribution origin",
    Type="String",
))

myDistribution = t.add_resource(StreamingDistribution(
    "myDistribution",
    StreamingDistributionConfig=StreamingDistributionConfig(
        Comment="Streaming distribution",
        Enabled=True,
        S3Origin=S3Origin(DomainName=Ref(s3dnsname)),
        TrustedSigners=TrustedSigners(
            Enabled=False,
        ),
    )
))

t.add_output([
    Output("DistributionId", Value=Ref(myDistribution)),
    Output(
        "DistributionName",
        Value=Join("", ["http://", GetAtt(myDistribution, "DomainName")])),
])

print(t.to_json())
