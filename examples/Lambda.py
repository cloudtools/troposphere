from troposphere import FindInMap, GetAtt, Join, Output, Parameter, Ref, Template
from troposphere.awslambda import MAXIMUM_MEMORY, MINIMUM_MEMORY, Code, Function
from troposphere.cloudformation import CustomResource
from troposphere.constants import NUMBER
from troposphere.ec2 import Instance, SecurityGroup
from troposphere.iam import Policy, Role

t = Template()

t.set_version("2010-09-09")

ExistingVPC = t.add_parameter(
    Parameter(
        "ExistingVPC",
        Type="AWS::EC2::VPC::Id",
        Description=(
            "The VPC ID that includes the security groups in the "
            "ExistingSecurityGroups parameter."
        ),
    )
)

InstanceType = t.add_parameter(
    Parameter(
        "InstanceType",
        Default="t2.micro",
        Type="String",
        AllowedValues=["t2.micro", "m1.small"],
    )
)

ExistingSecurityGroups = t.add_parameter(
    Parameter(
        "ExistingSecurityGroups",
        Type="List<AWS::EC2::SecurityGroup::Id>",
    )
)

MemorySize = t.add_parameter(
    Parameter(
        "LambdaMemorySize",
        Type=NUMBER,
        Description="Amount of memory to allocate to the Lambda Function",
        Default="128",
        MinValue=MINIMUM_MEMORY,
        MaxValue=MAXIMUM_MEMORY,
    )
)

Timeout = t.add_parameter(
    Parameter(
        "LambdaTimeout",
        Type=NUMBER,
        Description="Timeout in seconds for the Lambda function",
        Default="60",
    )
)

t.add_mapping(
    "AWSInstanceType2Arch",
    {"m1.small": {"Arch": "PV64"}, "t2.micro": {"Arch": "HVM64"}},
)

t.add_mapping(
    "AWSRegionArch2AMI",
    {
        "ap-northeast-1": {"HVM64": "ami-cbf90ecb", "PV64": "ami-27f90e27"},
        "ap-southeast-1": {"HVM64": "ami-68d8e93a", "PV64": "ami-acd9e8fe"},
        "ap-southeast-2": {"HVM64": "ami-fd9cecc7", "PV64": "ami-ff9cecc5"},
        "cn-north-1": {"HVM64": "ami-f239abcb", "PV64": "ami-fa39abc3"},
        "eu-central-1": {"HVM64": "ami-a8221fb5", "PV64": "ami-ac221fb1"},
        "eu-west-1": {"HVM64": "ami-a10897d6", "PV64": "ami-bf0897c8"},
        "sa-east-1": {"HVM64": "ami-b52890a8", "PV64": "ami-bb2890a6"},
        "us-east-1": {"HVM64": "ami-1ecae776", "PV64": "ami-1ccae774"},
        "us-west-1": {"HVM64": "ami-d114f295", "PV64": "ami-d514f291"},
        "us-west-2": {"HVM64": "ami-e7527ed7", "PV64": "ami-ff527ecf"},
    },
)

code = [
    "var response = require('cfn-response');",
    "exports.handler = function(event, context) {",
    "   var responseData = {Value: event.ResourceProperties.List};",
    "   responseData.Value.push(event.ResourceProperties.AppendedItem);",
    "   response.send(event, context, response.SUCCESS, responseData);",
    "};",
]

AppendItemToListFunction = t.add_resource(
    Function(
        "AppendItemToListFunction",
        Code=Code(ZipFile=Join("", code)),
        Handler="index.handler",
        Role=GetAtt("LambdaExecutionRole", "Arn"),
        Runtime="nodejs",
        MemorySize=Ref(MemorySize),
        Timeout=Ref(Timeout),
    )
)

LambdaExecutionRole = t.add_resource(
    Role(
        "LambdaExecutionRole",
        Path="/",
        Policies=[
            Policy(
                PolicyName="root",
                PolicyDocument={
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Action": ["logs:*"],
                            "Resource": "arn:aws:logs:*:*:*",
                            "Effect": "Allow",
                        }
                    ],
                },
            )
        ],
        AssumeRolePolicyDocument={
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": ["sts:AssumeRole"],
                    "Effect": "Allow",
                    "Principal": {"Service": ["lambda.amazonaws.com"]},
                }
            ],
        },
    )
)

MyEC2Instance = t.add_resource(
    Instance(
        "MyEC2Instance",
        SecurityGroupIds=GetAtt("AllSecurityGroups", "Value"),
        InstanceType=Ref(InstanceType),
        ImageId=FindInMap(
            "AWSRegionArch2AMI",
            Ref("AWS::Region"),
            FindInMap("AWSInstanceType2Arch", Ref(InstanceType), "Arch"),
        ),
    )
)

AllSecurityGroups = t.add_resource(
    CustomResource(
        "AllSecurityGroups",
        List=Ref(ExistingSecurityGroups),
        AppendedItem=Ref("SecurityGroup"),
        ServiceToken=GetAtt(AppendItemToListFunction, "Arn"),
    )
)

t.add_resource(
    SecurityGroup(
        "SecurityGroup",
        SecurityGroupIngress=[
            {
                "ToPort": "80",
                "IpProtocol": "tcp",
                "CidrIp": "0.0.0.0/0",
                "FromPort": "80",
            }
        ],
        VpcId=Ref(ExistingVPC),
        GroupDescription="Allow HTTP traffic to the host",
        SecurityGroupEgress=[
            {
                "ToPort": "80",
                "IpProtocol": "tcp",
                "CidrIp": "0.0.0.0/0",
                "FromPort": "80",
            }
        ],
    )
)

AllSecurityGroups = t.add_output(
    Output(
        "AllSecurityGroups",
        Description="Security Groups that are associated with the EC2 instance",
        Value=Join(", ", GetAtt(AllSecurityGroups, "Value")),
    )
)

print(t.to_json())
