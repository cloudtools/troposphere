# Converted from Route53_RoundRobin.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import Join
from troposphere import Parameter, Ref, Template
from troposphere.route53 import RecordSet, RecordSetGroup


t = Template()

t.set_description(
    "AWS CloudFormation Sample Template Route53_RoundRobin: Sample template "
    "showing how to use weighted round robin (WRR) DNS entried via Amazon "
    "Route 53. This contrived sample uses weighted CNAME records to "
    "illustrate that the weighting influences the return records. It assumes "
    " that you already have a Hosted Zone registered with Amazon Route 53. "
    "**WARNING** This template creates an Amazon EC2 instance. "
    "You will be billed for the AWS resources used if you create "
    "a stack from this template.")

hostedzone = t.add_parameter(Parameter(
    "HostedZone",
    Description="The DNS name of an existing Amazon Route 53 hosted zone",
    Type="String",
))

myDNSRecord = t.add_resource(RecordSetGroup(
    "myDNSRecord",
    HostedZoneName=Join("", [Ref(hostedzone), "."]),
    Comment="Contrived example to redirect to aws.amazon.com 75% of the time "
            "and www.amazon.com 25% of the time.",
    RecordSets=[
        RecordSet(
            SetIdentifier=Join(" ", [Ref("AWS::StackName"), "AWS"]),
            Name=Join("", [Ref("AWS::StackName"), ".", Ref("AWS::Region"), ".",
                      Ref(hostedzone), "."]),
            Type="CNAME",
            TTL="900",
            ResourceRecords=["aws.amazon.com"],
            Weight="3",
        ),
        RecordSet(
            SetIdentifier=Join(" ", [Ref("AWS::StackName"), "Amazon"]),
            Name=Join("", [Ref("AWS::StackName"), ".", Ref("AWS::Region"), ".",
                      Ref(hostedzone), "."]),
            Type="CNAME",
            TTL="900",
            ResourceRecords=["www.amazon.com"],
            Weight="1",
        ),
    ],
))


print(t.to_json())
