# Converted from Route53_CNAME.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import Join, Output
from troposphere import Parameter, Ref, Template
from troposphere.route53 import RecordSetType


t = Template()

t.set_description(
    "AWS CloudFormation Sample Template Route53_CNAME: Sample template "
    "showing how to create an Amazon Route 53 CNAME record.  It assumes that "
    "you already  have a Hosted Zone registered with Amazon Route 53. "
    "**WARNING** This template creates an Amazon EC2 instance. "
    "You will be billed for the AWS resources used if you create "
    "a stack from this template.")

hostedzone = t.add_parameter(Parameter(
    "HostedZone",
    Description="The DNS name of an existing Amazon Route 53 hosted zone",
    Type="String",
))

myDNSRecord = t.add_resource(RecordSetType(
    "myDNSRecord",
    HostedZoneName=Join("", [Ref(hostedzone), "."]),
    Comment="CNAME redirect to aws.amazon.com.",
    Name=Join("", [Ref("AWS::StackName"), ".", Ref("AWS::Region"), ".",
              Ref(hostedzone), "."]),
    Type="CNAME",
    TTL="900",
    ResourceRecords=["aws.amazon.com"]
))


t.add_output(Output("DomainName", Value=Ref(myDNSRecord)))

print(t.to_json())
