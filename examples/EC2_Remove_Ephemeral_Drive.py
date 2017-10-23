from troposphere import FindInMap, GetAtt, Output, Parameter, Ref, Template
from troposphere.ec2 import NO_DEVICE

import troposphere.ec2 as ec2


template = Template()

keyname_param = template.add_parameter(Parameter(
    "KeyName",
    Description="Name of an existing EC2 KeyPair to enable SSH "
                "access to the instance",
    Type="String",
))

template.add_mapping('RegionMap', {
      "ap-northeast-1": {"AMI": "ami-6959870f"},
      "ap-northeast-2": {"AMI": "ami-08d77266"},
      "ap-south-1": {"AMI": "ami-50591a3f"},
      "ap-southeast-1": {"AMI": "ami-d9dca7ba"},
      "ap-southeast-2": {"AMI": "ami-02ad4060"},
      "ca-central-1": {"AMI": "ami-13e45c77"},
      "eu-central-1": {"AMI": "ami-e613ac89"},
      "eu-west-1": {"AMI": "ami-eed00d97"},
      "eu-west-2": {"AMI": "ami-ba5f42de"},
      "sa-east-1": {"AMI": "ami-1ca7d970"},
      "us-east-1": {"AMI": "ami-bcdc16c6"},
      "us-east-2": {"AMI": "ami-49426e2c"},
      "us-west-1": {"AMI": "ami-1b17257b"},
      "us-west-2": {"AMI": "ami-19e92861"}
    })

ec2_instance = template.add_resource(ec2.Instance(
    "Ec2Instance",
    ImageId=FindInMap("RegionMap", Ref("AWS::Region"), "AMI"),
    InstanceType="t2.micro",
    KeyName=Ref(keyname_param),
    SecurityGroups=["default"],
    BlockDeviceMappings=[
        ec2.BlockDeviceMapping(
            DeviceName='/dev/sdb',
            NoDevice=NO_DEVICE),
        ec2.BlockDeviceMapping(
            DeviceName='/dev/sdc',
            NoDevice=NO_DEVICE),
    ]
))

template.add_output([
    Output(
        "InstanceId",
        Description="InstanceId of the newly created EC2 instance",
        Value=Ref(ec2_instance),
    ),
    Output(
        "AZ",
        Description="Availability Zone of the newly created EC2 instance",
        Value=GetAtt(ec2_instance, "AvailabilityZone"),
    ),
    Output(
        "PublicIP",
        Description="Public IP address of the newly created EC2 instance",
        Value=GetAtt(ec2_instance, "PublicIp"),
    ),
    Output(
        "PrivateIP",
        Description="Private IP address of the newly created EC2 instance",
        Value=GetAtt(ec2_instance, "PrivateIp"),
    ),
    Output(
        "PublicDNS",
        Description="Public DNSName of the newly created EC2 instance",
        Value=GetAtt(ec2_instance, "PublicDnsName"),
    ),
    Output(
        "PrivateDNS",
        Description="Private DNSName of the newly created EC2 instance",
        Value=GetAtt(ec2_instance, "PrivateDnsName"),
    ),
])

print(template.to_json())
