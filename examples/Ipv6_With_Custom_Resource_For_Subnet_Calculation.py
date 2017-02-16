#!/usr/bin/env python

from troposphere import GetAtt, Select, Join, Ref, Template, Tags, GetAZs
from troposphere.awslambda import Function, Code, MEMORY_VALUES, Permission
from troposphere.iam import PolicyType as IAMPolicy
from troposphere import ec2
from awacs.aws import Allow, Statement, Action as Action, Principal, Policy
from troposphere.iam import Role
from awacs.sts import AssumeRole
from troposphere.cloudformation import AWSCustomObject
import awacs.logs

class Ipv6SubnetCalculator(AWSCustomObject):

     resource_type = "Custom::Ipv6SubnetCalculator"

     props = {
      'ServiceToken': (str, True),
      'AllocatedSubnet': (str, True),
      'SubnetIndexStart': (str, True),
     }

template = Template()

template.add_description("""\
Create VPC ipv6 example stack
""")

Ipv6SubnetCalculatorCode = [
    "import socket",
    "from binascii import hexlify",
    "import cfnresponse",
    "responseData={}",
    "def IPV6_to_int(ipv6_addr):",
    " return int(hexlify(socket.inet_pton(socket.AF_INET6,ipv6_addr)),16)",
    "def long2ip(l):",
    " hex_str='%032x'%l",
    " hextets=['%x'%int(hex_str[x:x+4],16)for x in range(0,32,4)]",
    " dc_start,dc_len=(-1,0)",
    " run_start,run_len=(-1,0)",
    " for idx,hextet in enumerate(hextets):",
    "  if '0'==hextet:",
    "   run_len+=1",
    "   if-1==run_start:",
    "    run_start=idx",
    "   if run_len>dc_len:",
    "    dc_len,dc_start=(run_len,run_start)",
    "  else:",
    "   run_len,run_start=(0,-1)",
    " if dc_len>1:",
    "  dc_end=dc_start+dc_len",
    "  if dc_end==len(hextets):",
    "   hextets+=['']",
    "  hextets[dc_start:dc_end]=['']",
    "  if dc_start==0:",
    "   hextets=['']+hextets",
    " return ':'.join(hextets)",
    "def lambda_handler(event,context):",
    " if event['RequestType'] is not 'delete':",
    "  create(event,context)",
    " if event['RequestType'] is 'delete':",
    "  delete(event,context)",
    "def delete(event,context):",
    " cfnresponse.send(event,context,cfnresponse.SUCCESS,responseData,"")",
    "def create(event,context):",
    " v6sm=event['ResourceProperties']['AllocatedSubnet']",
    " print(v6sm)",
    " v6snm=v6sm.split('/')[0]",
    " sis=int(event['ResourceProperties']['SubnetIndexStart'])",
    " dec=long(IPV6_to_int(v6snm))",
    " S64S=(2**64)",
    " o64d= dec+((sis)*long(S64S))",
    " o64s=(str(long2ip(o64d))+'/64')",
    " responseData['SubnetIndexStart']=sis",
    " cfnresponse.send(event,context,cfnresponse.SUCCESS,responseData,o64s)",
]

Ipv6SubnetCalculatorFunction = template.add_resource(Function(
    "Ipv6SubnetCalculatorFunction",
    Description="Calculates Ipv6 Subnets for Cloudformation",
    Code=Code(
        ZipFile=Join("\n", Ipv6SubnetCalculatorCode)
    ),
    Handler="index.lambda_handler",
    Role=GetAtt("Ipv6SubnetCalculatorExecutionLambdaRole", "Arn"),
    Runtime="python2.7",
    MemorySize=128,
    Timeout=30
))

template.add_resource(Role(
"Ipv6SubnetCalculatorExecutionLambdaRole",
     AssumeRolePolicyDocument=Policy(
        Statement=[
            Statement(
                Effect=Allow, Action=[AssumeRole],
                Principal=Principal(
                    "Service", ["lambda.amazonaws.com"]
                ),
            )
        ]
   ),
Path="/"
))

template.add_resource(IAMPolicy(
    "Ipv6SubnetCalculatorExecutionLambdaPolicy",
    PolicyName="Ipv6SubnetCalculatorExecutionLambdaPolicy",
    Roles=[Ref("Ipv6SubnetCalculatorExecutionLambdaRole")],
    PolicyDocument=Policy(
        Statement=[
            Statement(
                    Effect=Allow,
                    Action=[Action("logs", "*")],
                Resource=["arn:aws:logs:*:*:*"],
            )
        ],
    ),
))

vpcid = template.add_resource(ec2.VPC(
    "Example",
    CidrBlock="10.254.0.0/16",
    EnableDnsHostnames=True,
    EnableDnsSupport=True,
))

ipv6cidrblock = template.add_resource(ec2.VPCCidrBlock(
    "ExampleIPV6Block",
    AmazonProvidedIpv6CidrBlock=True,
    VpcId=Ref(vpcid),
    ))

ipv6calculation = template.add_resource(Ipv6SubnetCalculator(
    "ipv6calculation",
    ServiceToken=GetAtt(Ipv6SubnetCalculatorFunction, "Arn"),
    AllocatedSubnet=Select(0, GetAtt(vpcid, "Ipv6CidrBlocks")),
    SubnetIndexStart='0',
    DependsOn="ExampleIPV6Block"
))

examplesubnet1 = template.add_resource(ec2.Subnet(
    "ExampleSubnet1",
    VpcId=Ref(vpcid),
    CidrBlock="10.254.1.0/24",
    AvailabilityZone=Select(0, GetAZs(Ref("AWS::Region"))),
))

exampleipv6subnet = template.add_resource(ec2.SubnetCidrBlock(
    "ExampleIPV6Subnet",
    Ipv6CidrBlock=Ref(ipv6calculation),
    SubnetId=Ref(examplesubnet1)
    ))

print(template.to_json())
