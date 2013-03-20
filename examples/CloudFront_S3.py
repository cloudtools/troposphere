# Converted from CloudFront_S3.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import GetAtt, Join, Output
from troposphere import Parameter, Ref, Template
from troposphere.cloudfront import Distribution, DistributionConfig
from troposphere.cloudfront import Origin, DefaultCacheBehavior


t = Template()

t.add_description(
    "AWS CloudFormation Sample Template CloudFront_S3: Sample template "
    "showing how to create an Amazon CloudFront distribution using an "
    "S3 origin. "
    "**WARNING** This template creates an Amazon EC2 instance. "
    "You will be billed for the AWS resources used if you create "
    "a stack from this template.")

s3dnsname = t.add_parameter(Parameter(
    "S3DNSNAme",
    Description="The DNS name of an existing S3 bucket to use as the "
                "Cloudfront distribution origin",
    Type="String",
))

myDistribution = t.add_resource(Distribution(
    "myDistribution",
    DistributionConfig=DistributionConfig(
        Origins=[Origin(Id="Origin 1", DomainName=Ref(s3dnsname))],
        DefaultCacheBehavior=DefaultCacheBehavior(
            TargetOriginId="Origin 1",
            ViewerProtocolPolicy="allow-all"),
        Enabled=True
    )
))

t.add_output([
    Output("DistributionId", Value=Ref(myDistribution)),
    Output(
        "DistributionName",
        Value=Join("", ["http://", GetAtt(myDistribution, "DomainName")])),
])

print(t.to_json())
