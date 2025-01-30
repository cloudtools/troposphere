#!/usr/bin/python
# Converted from VPC_With_VPN_Connection.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates

from troposphere import (
    Base64,
    FindInMap,
    GetAtt,
    Join,
    Output,
    Parameter,
    Ref,
    Tags,
    Template,
)
from troposphere.autoscaling import Metadata
from troposphere.cloudformation import (
    Init,
    InitConfig,
    InitFile,
    InitFiles,
    InitService,
    InitServices,
)
from troposphere.ec2 import (
    EIP,
    VPC,
    Instance,
    InternetGateway,
    NetworkAcl,
    NetworkAclEntry,
    NetworkAclEntryPortRange,
    NetworkInterfaceProperty,
    Route,
    RouteTable,
    SecurityGroup,
    SecurityGroupRule,
    Subnet,
    SubnetNetworkAclAssociation,
    SubnetRouteTableAssociation,
    VPCGatewayAttachment,
)
from troposphere.policies import CreationPolicy, ResourceSignal

t = Template()

t.set_version("2010-09-09")

t.set_description(
    """\
AWS CloudFormation Sample Template VPC_Single_Instance_In_Subnet: Sample \
template showing how to create a VPC and add an EC2 instance with an Elastic \
IP address and a security group. \
**WARNING** This template creates an Amazon EC2 instance. You will be billed \
for the AWS resources used if you create a stack from this template."""
)

keyname_param = t.add_parameter(
    Parameter(
        "KeyName",
        ConstraintDescription="must be the name of an existing EC2 KeyPair.",
        Description="Name of an existing EC2 KeyPair to enable SSH access to \
the instance",
        Type="AWS::EC2::KeyPair::KeyName",
    )
)

sshlocation_param = t.add_parameter(
    Parameter(
        "SSHLocation",
        Description=" The IP address range that can be used to SSH to the EC2 \
instances",
        Type="String",
        MinLength="9",
        MaxLength="18",
        Default="0.0.0.0/0",
        AllowedPattern=r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2})",
        ConstraintDescription=("must be a valid IP CIDR range of the form x.x.x.x/x."),
    )
)

instanceType_param = t.add_parameter(
    Parameter(
        "InstanceType",
        Type="String",
        Description="WebServer EC2 instance type",
        Default="m1.small",
        AllowedValues=[
            "t1.micro",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "g2.2xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "cr1.8xlarge",
            "cc2.8xlarge",
            "cg1.4xlarge",
        ],
        ConstraintDescription="must be a valid EC2 instance type.",
    )
)

t.add_mapping(
    "AWSInstanceType2Arch",
    {
        "t1.micro": {"Arch": "PV64"},
        "t2.micro": {"Arch": "HVM64"},
        "t2.small": {"Arch": "HVM64"},
        "t2.medium": {"Arch": "HVM64"},
        "m1.small": {"Arch": "PV64"},
        "m1.medium": {"Arch": "PV64"},
        "m1.large": {"Arch": "PV64"},
        "m1.xlarge": {"Arch": "PV64"},
        "m2.xlarge": {"Arch": "PV64"},
        "m2.2xlarge": {"Arch": "PV64"},
        "m2.4xlarge": {"Arch": "PV64"},
        "m3.medium": {"Arch": "HVM64"},
        "m3.large": {"Arch": "HVM64"},
        "m3.xlarge": {"Arch": "HVM64"},
        "m3.2xlarge": {"Arch": "HVM64"},
        "c1.medium": {"Arch": "PV64"},
        "c1.xlarge": {"Arch": "PV64"},
        "c3.large": {"Arch": "HVM64"},
        "c3.xlarge": {"Arch": "HVM64"},
        "c3.2xlarge": {"Arch": "HVM64"},
        "c3.4xlarge": {"Arch": "HVM64"},
        "c3.8xlarge": {"Arch": "HVM64"},
        "g2.2xlarge": {"Arch": "HVMG2"},
        "r3.large": {"Arch": "HVM64"},
        "r3.xlarge": {"Arch": "HVM64"},
        "r3.2xlarge": {"Arch": "HVM64"},
        "r3.4xlarge": {"Arch": "HVM64"},
        "r3.8xlarge": {"Arch": "HVM64"},
        "i2.xlarge": {"Arch": "HVM64"},
        "i2.2xlarge": {"Arch": "HVM64"},
        "i2.4xlarge": {"Arch": "HVM64"},
        "i2.8xlarge": {"Arch": "HVM64"},
        "hi1.4xlarge": {"Arch": "HVM64"},
        "hs1.8xlarge": {"Arch": "HVM64"},
        "cr1.8xlarge": {"Arch": "HVM64"},
        "cc2.8xlarge": {"Arch": "HVM64"},
    },
)

t.add_mapping(
    "AWSRegionArch2AMI",
    {
        "us-east-1": {
            "PV64": "ami-50842d38",
            "HVM64": "ami-08842d60",
            "HVMG2": "ami-3a329952",
        },
        "us-west-2": {
            "PV64": "ami-af86c69f",
            "HVM64": "ami-8786c6b7",
            "HVMG2": "ami-47296a77",
        },
        "us-west-1": {
            "PV64": "ami-c7a8a182",
            "HVM64": "ami-cfa8a18a",
            "HVMG2": "ami-331b1376",
        },
        "eu-west-1": {
            "PV64": "ami-aa8f28dd",
            "HVM64": "ami-748e2903",
            "HVMG2": "ami-00913777",
        },
        "ap-southeast-1": {
            "PV64": "ami-20e1c572",
            "HVM64": "ami-d6e1c584",
            "HVMG2": "ami-fabe9aa8",
        },
        "ap-northeast-1": {
            "PV64": "ami-21072820",
            "HVM64": "ami-35072834",
            "HVMG2": "ami-5dd1ff5c",
        },
        "ap-southeast-2": {
            "PV64": "ami-8b4724b1",
            "HVM64": "ami-fd4724c7",
            "HVMG2": "ami-e98ae9d3",
        },
        "sa-east-1": {
            "PV64": "ami-9d6cc680",
            "HVM64": "ami-956cc688",
            "HVMG2": "NOT_SUPPORTED",
        },
        "cn-north-1": {
            "PV64": "ami-a857c591",
            "HVM64": "ami-ac57c595",
            "HVMG2": "NOT_SUPPORTED",
        },
        "eu-central-1": {
            "PV64": "ami-a03503bd",
            "HVM64": "ami-b43503a9",
            "HVMG2": "ami-b03503ad",
        },
    },
)

ref_stack_id = Ref("AWS::StackId")
ref_region = Ref("AWS::Region")
ref_stack_name = Ref("AWS::StackName")

VPCResource = t.add_resource(
    VPC("VPC", CidrBlock="10.0.0.0/16", Tags=Tags(Application=ref_stack_id))
)

subnet = t.add_resource(
    Subnet(
        "Subnet",
        CidrBlock="10.0.0.0/24",
        VpcId=Ref(VPCResource),
        Tags=Tags(Application=ref_stack_id),
    )
)

internetGateway = t.add_resource(
    InternetGateway("InternetGateway", Tags=Tags(Application=ref_stack_id))
)

gatewayAttachment = t.add_resource(
    VPCGatewayAttachment(
        "AttachGateway", VpcId=Ref(VPCResource), InternetGatewayId=Ref(internetGateway)
    )
)

routeTable = t.add_resource(
    RouteTable(
        "RouteTable", VpcId=Ref(VPCResource), Tags=Tags(Application=ref_stack_id)
    )
)

route = t.add_resource(
    Route(
        "Route",
        DependsOn="AttachGateway",
        GatewayId=Ref("InternetGateway"),
        DestinationCidrBlock="0.0.0.0/0",
        RouteTableId=Ref(routeTable),
    )
)

subnetRouteTableAssociation = t.add_resource(
    SubnetRouteTableAssociation(
        "SubnetRouteTableAssociation",
        SubnetId=Ref(subnet),
        RouteTableId=Ref(routeTable),
    )
)

networkAcl = t.add_resource(
    NetworkAcl(
        "NetworkAcl",
        VpcId=Ref(VPCResource),
        Tags=Tags(Application=ref_stack_id),
    )
)

inBoundPrivateNetworkAclEntry = t.add_resource(
    NetworkAclEntry(
        "InboundHTTPNetworkAclEntry",
        NetworkAclId=Ref(networkAcl),
        RuleNumber="100",
        Protocol="6",
        PortRange=NetworkAclEntryPortRange(To="80", From="80"),
        Egress="false",
        RuleAction="allow",
        CidrBlock="0.0.0.0/0",
    )
)

inboundSSHNetworkAclEntry = t.add_resource(
    NetworkAclEntry(
        "InboundSSHNetworkAclEntry",
        NetworkAclId=Ref(networkAcl),
        RuleNumber="101",
        Protocol="6",
        PortRange=NetworkAclEntryPortRange(To="22", From="22"),
        Egress="false",
        RuleAction="allow",
        CidrBlock="0.0.0.0/0",
    )
)

inboundResponsePortsNetworkAclEntry = t.add_resource(
    NetworkAclEntry(
        "InboundResponsePortsNetworkAclEntry",
        NetworkAclId=Ref(networkAcl),
        RuleNumber="102",
        Protocol="6",
        PortRange=NetworkAclEntryPortRange(To="65535", From="1024"),
        Egress="false",
        RuleAction="allow",
        CidrBlock="0.0.0.0/0",
    )
)

outBoundHTTPNetworkAclEntry = t.add_resource(
    NetworkAclEntry(
        "OutBoundHTTPNetworkAclEntry",
        NetworkAclId=Ref(networkAcl),
        RuleNumber="100",
        Protocol="6",
        PortRange=NetworkAclEntryPortRange(To="80", From="80"),
        Egress="true",
        RuleAction="allow",
        CidrBlock="0.0.0.0/0",
    )
)

outBoundHTTPSNetworkAclEntry = t.add_resource(
    NetworkAclEntry(
        "OutBoundHTTPSNetworkAclEntry",
        NetworkAclId=Ref(networkAcl),
        RuleNumber="101",
        Protocol="6",
        PortRange=NetworkAclEntryPortRange(To="443", From="443"),
        Egress="true",
        RuleAction="allow",
        CidrBlock="0.0.0.0/0",
    )
)

outBoundResponsePortsNetworkAclEntry = t.add_resource(
    NetworkAclEntry(
        "OutBoundResponsePortsNetworkAclEntry",
        NetworkAclId=Ref(networkAcl),
        RuleNumber="102",
        Protocol="6",
        PortRange=NetworkAclEntryPortRange(To="65535", From="1024"),
        Egress="true",
        RuleAction="allow",
        CidrBlock="0.0.0.0/0",
    )
)

subnetNetworkAclAssociation = t.add_resource(
    SubnetNetworkAclAssociation(
        "SubnetNetworkAclAssociation",
        SubnetId=Ref(subnet),
        NetworkAclId=Ref(networkAcl),
    )
)

instanceSecurityGroup = t.add_resource(
    SecurityGroup(
        "InstanceSecurityGroup",
        GroupDescription="Enable SSH access via port 22",
        SecurityGroupIngress=[
            SecurityGroupRule(
                IpProtocol="tcp",
                FromPort="22",
                ToPort="22",
                CidrIp=Ref(sshlocation_param),
            ),
            SecurityGroupRule(
                IpProtocol="tcp", FromPort="80", ToPort="80", CidrIp="0.0.0.0/0"
            ),
        ],
        VpcId=Ref(VPCResource),
    )
)

instance_metadata = Metadata(
    Init(
        {
            "config": InitConfig(
                packages={"yum": {"httpd": []}},
                files=InitFiles(
                    {
                        "/var/www/html/index.html": InitFile(
                            content=Join(
                                "\n",
                                [
                                    '<img \
src="https://s3.amazonaws.com/cloudformation-examples/\
cloudformation_graphic.png" alt="AWS CloudFormation Logo"/>',
                                    "<h1>\
Congratulations, you have successfully launched the AWS CloudFormation sample.\
</h1>",
                                ],
                            ),
                            mode="000644",
                            owner="root",
                            group="root",
                        ),
                        "/etc/cfn/cfn-hup.conf": InitFile(
                            content=Join(
                                "",
                                [
                                    "[main]\n",
                                    "stack=",
                                    ref_stack_id,
                                    "\n",
                                    "region=",
                                    ref_region,
                                    "\n",
                                ],
                            ),
                            mode="000400",
                            owner="root",
                            group="root",
                        ),
                        "/etc/cfn/hooks.d/cfn-auto-reloader.conf": InitFile(
                            content=Join(
                                "",
                                [
                                    "[cfn-auto-reloader-hook]\n",
                                    "triggers=post.update\n",
                                    "path=Resources.WebServerInstance.\
Metadata.AWS::CloudFormation::Init\n",
                                    "action=/opt/aws/bin/cfn-init -v ",
                                    "         --stack ",
                                    ref_stack_name,
                                    "         --resource WebServerInstance ",
                                    "         --region ",
                                    ref_region,
                                    "\n",
                                    "runas=root\n",
                                ],
                            )
                        ),
                    }
                ),
                services={
                    "sysvinit": InitServices(
                        {
                            "httpd": InitService(enabled=True, ensureRunning=True),
                            "cfn-hup": InitService(
                                enabled=True,
                                ensureRunning=True,
                                files=[
                                    "/etc/cfn/cfn-hup.conf",
                                    "/etc/cfn/hooks.d/cfn-auto-reloader.conf",
                                ],
                            ),
                        }
                    )
                },
            )
        }
    )
)

instance = t.add_resource(
    Instance(
        "WebServerInstance",
        Metadata=instance_metadata,
        ImageId=FindInMap(
            "AWSRegionArch2AMI",
            Ref("AWS::Region"),
            FindInMap("AWSInstanceType2Arch", Ref(instanceType_param), "Arch"),
        ),
        InstanceType=Ref(instanceType_param),
        KeyName=Ref(keyname_param),
        NetworkInterfaces=[
            NetworkInterfaceProperty(
                GroupSet=[Ref(instanceSecurityGroup)],
                AssociatePublicIpAddress="true",
                DeviceIndex="0",
                DeleteOnTermination="true",
                SubnetId=Ref(subnet),
            )
        ],
        UserData=Base64(
            Join(
                "",
                [
                    "#!/bin/bash -xe\n",
                    "yum update -y aws-cfn-bootstrap\n",
                    "/opt/aws/bin/cfn-init -v ",
                    "         --stack ",
                    Ref("AWS::StackName"),
                    "         --resource WebServerInstance ",
                    "         --region ",
                    Ref("AWS::Region"),
                    "\n",
                    "/opt/aws/bin/cfn-signal -e $? ",
                    "         --stack ",
                    Ref("AWS::StackName"),
                    "         --resource WebServerInstance ",
                    "         --region ",
                    Ref("AWS::Region"),
                    "\n",
                ],
            )
        ),
        CreationPolicy=CreationPolicy(ResourceSignal=ResourceSignal(Timeout="PT15M")),
        Tags=Tags(Application=ref_stack_id),
    )
)

ipAddress = t.add_resource(
    EIP("IPAddress", DependsOn="AttachGateway", Domain="vpc", InstanceId=Ref(instance))
)

t.add_output(
    [
        Output(
            "URL",
            Description="Newly created application URL",
            Value=Join("", ["http://", GetAtt("WebServerInstance", "PublicIp")]),
        )
    ]
)

print(t.to_json())
