troposphere - library to create AWS CloudFormation descriptions

The troposphere library allows for easier creation of the AWS CloudFormation
JSON by writing Python code to describe the AWS resources. To facilitate
catching CloudFormation or JSON errors early the library has property and type
checking built into the classes.

Currently supported AWS resource types:
- AWS::AutoScaling
- AWS::EC2
- AWS::ElasticLoadBalancing

Todo:
- Add named objects for easier use across objects
- Add missing AWS resource types:
  - AWS::CloudFormation
  - AWS::CloudFront
  - AWS::CloudWatch
  - AWS::DynamoDB
  - AWS::ElastiCache
  - AWS::ElasticBeanstalk
  - AWS::IAM
  - AWS::RDS
  - AWS::Route53
  - AWS::S3
  - AWS::SDB
  - AWS::SNS
  - AWS::SQS

Duplicating a single instance sample would look like this:
https://s3.amazonaws.com/cloudformation-templates-us-east-1/EC2InstanceSample.template

```from troposphere import Base64, FindInMap, GetAtt
from troposphere import Parameter, Output, Ref, Template
import troposphere.ec2 as ec2

EC2_INSTANCE = "Ec2Instance"

template = Template()

template.parameters['KeyName'] = Parameter(
    Description="Name of an existing EC2 KeyPair to enable SSH "
                "access to the instance",
    Type="String",
)

template.mappings['RegionMap'] = {
    "us-east-1":      {"AMI": "ami-7f418316"},
    "us-west-1":      {"AMI": "ami-951945d0"},
    "us-west-2":      {"AMI": "ami-16fd7026"},
    "eu-west-1":      {"AMI": "ami-24506250"},
    "sa-east-1":      {"AMI": "ami-3e3be423"},
    "ap-southeast-1": {"AMI": "ami-74dda626"},
    "ap-northeast-1": {"AMI": "ami-dcfa4edd"}
}

template.resources[EC2_INSTANCE] = ec2.Instance(
    ImageId=FindInMap("RegionMap", Ref("AWS::Region"), "AMI"),
    InstanceType="t1.micro",
    KeyName=Ref("KeyName"),
    UserData=Base64("80")
)

template.outputs.update({
    "InstanceId": Output(
        Description="InstanceId of the newly created EC2 instance",
        Value=Ref(EC2_INSTANCE),
    ),
    "AZ": Output(
        Description="Availability Zone of the newly created EC2 instance",
        Value=GetAtt(EC2_INSTANCE, "AvailabilityZone"),
    ),
    "PublicIP": Output(
        Description="Public IP address of the newly created EC2 instance",
        Value=GetAtt(EC2_INSTANCE, "PublicIp"),
    ),
    "PrivateIP": Output(
        Description="Private IP address of the newly created EC2 instance",
        Value=GetAtt(EC2_INSTANCE, "PrivateIp"),
    ),
    "PublicDNS": Output(
        Description="Public DNSName of the newly created EC2 instance",
        Value=GetAtt(EC2_INSTANCE, "PublicDnsName"),
    ),
    "PrivateDNS": Output(
        Description="Private DNSName of the newly created EC2 instance",
        Value=GetAtt(EC2_INSTANCE, "PrivateDnsName"),
    ),
})

print template.to_json()```
