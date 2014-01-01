# Converted from EC2InstanceSample.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import Base64, FindInMap, Mapping
from troposphere import Parameter, Output, Ref, Template
import troposphere.ec2 as ec2


template = Template()

KeyName = Parameter(
    Description="Name of an existing EC2 KeyPair to enable SSH "
                "access to the instance",
    Type="String",
)

RegionMap = Mapping({
    "us-east-1": {"AMI": "ami-7f418316"},
    "us-west-1": {"AMI": "ami-951945d0"},
    "us-west-2": {"AMI": "ami-16fd7026"},
    "eu-west-1": {"AMI": "ami-24506250"},
    "sa-east-1": {"AMI": "ami-3e3be423"},
    "ap-southeast-1": {"AMI": "ami-74dda626"},
    "ap-northeast-1": {"AMI": "ami-dcfa4edd"}
})

Ec2Instance = ec2.Instance(
    ImageId=FindInMap("RegionMap", Ref("AWS::Region"), "AMI"),
    InstanceType="t1.micro",
    KeyName=KeyName,
    SecurityGroups=["default"],
    UserData=Base64("80")
)

InstanceId = Output(
        Description="InstanceId of the newly created EC2 instance",
        Value=Ec2Instance,
        )
AZ = Output(
        Description="Availability Zone of the newly created EC2 instance",
        Value=Ec2Instance.AvailabilityZone,
        )

PublicIP = Output(
        Description="Public IP address of the newly created EC2 instance",
        Value=Ec2Instance.PublicIp,
    )
PrivateIP = Output(
        Description="Private IP address of the newly created EC2 instance",
        Value=Ec2Instance.PrivateIp,
    )
PublicDNS = Output(
        Description="Public DNSName of the newly created EC2 instance",
        Value=Ec2Instance.PublicDnsName,
    )
PrivateDNS = Output(
        Description="Private DNSName of the newly created EC2 instance",
        Value=Ec2Instance.PrivateDnsName,
    )

template.add_half_baked(locals())

print(template.to_json())
