from troposphere.constants import NUMBER
from troposphere import FindInMap, GetAtt, Join, Output
from troposphere import Parameter, Ref, Template
from troposphere.awslambda import Function, Code, MEMORY_VALUES
from troposphere.cloudformation import CustomResource
from troposphere.ec2 import Instance
from troposphere.ec2 import SecurityGroup
from troposphere.iam import Role, Policy


t = Template()

t.add_version("2010-09-09")

ExistingVPC = t.add_parameter(Parameter(
    "ExistingVPC",
    Type="AWS::EC2::VPC::Id",
    Description=(
        "The VPC ID that includes the security groups in the "
        "ExistingSecurityGroups parameter."
    ),
))

InstanceType = t.add_parameter(Parameter(
    "InstanceType",
    Default="t2.micro",
    Type="String",
    AllowedValues=["t2.micro", "m1.small"],
))

ExistingSecurityGroups = t.add_parameter(Parameter(
    "ExistingSecurityGroups",
    Type="List<AWS::EC2::SecurityGroup::Id>",
))

MemorySize = t.add_parameter(Parameter(
    'LambdaMemorySize',
    Type=NUMBER,
    Description='Amount of memory to allocate to the Lambda Function',
    Default='128',
    AllowedValues=MEMORY_VALUES
))

Timeout = t.add_parameter(Parameter(
    'LambdaTimeout',
    Type=NUMBER,
    Description='Timeout in seconds for the Lambda function',
    Default='60'
))

t.add_mapping("AWSInstanceType2Arch",
              {u'm1.small': {u'Arch': u'PV64'},
               u't2.micro': {u'Arch': u'HVM64'}}
              )

t.add_mapping("AWSRegionArch2AMI",
              {u'ap-northeast-1': {u'HVM64': u'ami-cbf90ecb',
                                   u'PV64': u'ami-27f90e27'},
               u'ap-southeast-1': {u'HVM64': u'ami-68d8e93a',
                                   u'PV64': u'ami-acd9e8fe'},
               u'ap-southeast-2': {u'HVM64': u'ami-fd9cecc7',
                                   u'PV64': u'ami-ff9cecc5'},
               u'cn-north-1': {u'HVM64': u'ami-f239abcb',
                               u'PV64': u'ami-fa39abc3'},
               u'eu-central-1': {u'HVM64': u'ami-a8221fb5',
                                 u'PV64': u'ami-ac221fb1'},
               u'eu-west-1': {u'HVM64': u'ami-a10897d6',
                              u'PV64': u'ami-bf0897c8'},
               u'sa-east-1': {u'HVM64': u'ami-b52890a8',
                              u'PV64': u'ami-bb2890a6'},
               u'us-east-1': {u'HVM64': u'ami-1ecae776',
                              u'PV64': u'ami-1ccae774'},
               u'us-west-1': {u'HVM64': u'ami-d114f295',
                              u'PV64': u'ami-d514f291'},
               u'us-west-2': {u'HVM64': u'ami-e7527ed7',
                              u'PV64': u'ami-ff527ecf'}}
              )

code = [
    "var response = require('cfn-response');",
    "exports.handler = function(event, context) {",
    "   var responseData = {Value: event.ResourceProperties.List};",
    "   responseData.Value.push(event.ResourceProperties.AppendedItem);",
    "   response.send(event, context, response.SUCCESS, responseData);",
    "};",
]

AppendItemToListFunction = t.add_resource(Function(
    "AppendItemToListFunction",
    Code=Code(
        ZipFile=Join("", code)
    ),
    Handler="index.handler",
    Role=GetAtt("LambdaExecutionRole", "Arn"),
    Runtime="nodejs",
    MemorySize=Ref(MemorySize),
    Timeout=Ref(Timeout)
))

LambdaExecutionRole = t.add_resource(Role(
    "LambdaExecutionRole",
    Path="/",
    Policies=[Policy(
        PolicyName="root",
        PolicyDocument={
            "Version": "2012-10-17",
            "Statement": [{
                "Action": ["logs:*"],
                "Resource": "arn:aws:logs:*:*:*",
                "Effect": "Allow"
            }]
        })],
    AssumeRolePolicyDocument={
        "Version": "2012-10-17",
        "Statement": [{
            "Action": ["sts:AssumeRole"],
            "Effect": "Allow",
            "Principal": {
                "Service": ["lambda.amazonaws.com"]
            }
        }]
    },
))

MyEC2Instance = t.add_resource(Instance(
    "MyEC2Instance",
    SecurityGroupIds=GetAtt("AllSecurityGroups", "Value"),
    InstanceType=Ref(InstanceType),
    ImageId=FindInMap("AWSRegionArch2AMI", Ref("AWS::Region"),
                      FindInMap("AWSInstanceType2Arch", Ref(InstanceType),
                                "Arch")),
))

AllSecurityGroups = t.add_resource(CustomResource(
    "AllSecurityGroups",
    List=Ref(ExistingSecurityGroups),
    AppendedItem=Ref("SecurityGroup"),
    ServiceToken=GetAtt(AppendItemToListFunction, "Arn"),
))

SecurityGroup = t.add_resource(SecurityGroup(
    "SecurityGroup",
    SecurityGroupIngress=[
        {"ToPort": "80", "IpProtocol": "tcp", "CidrIp": "0.0.0.0/0",
         "FromPort": "80"}],
    VpcId=Ref(ExistingVPC),
    GroupDescription="Allow HTTP traffic to the host",
    SecurityGroupEgress=[
        {"ToPort": "80", "IpProtocol": "tcp", "CidrIp": "0.0.0.0/0",
         "FromPort": "80"}],
))

AllSecurityGroups = t.add_output(Output(
    "AllSecurityGroups",
    Description="Security Groups that are associated with the EC2 instance",
    Value=Join(", ", GetAtt(AllSecurityGroups, "Value")),
))

print(t.to_json())
