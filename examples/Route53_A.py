# Converted from Route53_A.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import FindInMap, GetAtt, Join, Output
from troposphere import Parameter, Ref, Template
from troposphere.ec2 import Instance
from troposphere.route53 import RecordSetType


t = Template()

t.set_description(
    "AWS CloudFormation Sample Template Route53_A: "
    "Sample template showing how to create an Amazon Route 53 A record that "
    "maps to the public IP address of an EC2 instance. It assumes that you "
    "already have a Hosted Zone registered with Amazon Route 53. **WARNING** "
    "This template creates an Amazon EC2 instance. You will be billed for "
    "the AWS resources used if you create a stack from this template.")

hostedzone = t.add_parameter(Parameter(
    "HostedZone",
    Description="The DNS name of an existing Amazon Route 53 hosted zone",
    Type="String",
))

t.add_mapping('RegionMap', {
    "us-east-1": {"AMI": "ami-7f418316"},
    "us-west-1": {"AMI": "ami-951945d0"},
    "us-west-2": {"AMI": "ami-16fd7026"},
    "eu-west-1": {"AMI": "ami-24506250"},
    "sa-east-1": {"AMI": "ami-3e3be423"},
    "ap-southeast-1": {"AMI": "ami-74dda626"},
    "ap-northeast-1": {"AMI": "ami-dcfa4edd"}
})

instance = t.add_resource(Instance(
    "Ec2Instance",
    ImageId=FindInMap("RegionMap", Ref("AWS::Region"), "AMI"),
    InstanceType="m1.small",
))

myDNSRecord = t.add_resource(RecordSetType(
    "myDNSRecord",
    HostedZoneName=Join("", [Ref(hostedzone), "."]),
    Comment="DNS name for my instance.",
    Name=Join("", [Ref(instance), ".", Ref("AWS::Region"), ".",
              Ref(hostedzone), "."]),
    Type="A",
    TTL="900",
    ResourceRecords=[GetAtt("Ec2Instance", "PublicIp")],
))


t.add_output(Output("DomainName", Value=Ref(myDNSRecord)))

print(t.to_json())
