from troposphere import Base64, Ref, FindInMap, Template, Join,  GetAtt,  Sub,  Output
import troposphere.ec2 as ec2

# New Template
template = Template()

# Mapping
template.add_mapping('RegionMap',{
    "us-east-1":    {"32":  "ami-8c1be5f6"},
    "us-east-2":    {"32":  "ami-c5062ba0"},
    "us-west-1":    {"32":  "ami-02eada62"},
    "us-west-2":    {"32":  "ami-e689729e"},
    "eu-west-1":    {"32":  "ami-acd005d5"},
    "eu-west-2":    {"32":  "ami-1a7f6d7e"},
    "ap-southeast-1":    {"32":  "ami-0797ea64"},
    "ap-southeast-2":    {"32":  "ami-8536d6e7"},
    "ap-northeast-1":    {"32":  "ami-2a69be4c"},
    "ap-northeast-2":    {"32":  "ami-9bec36f5"},
    "ap-south-1":    {"32":  "ami-4fc58420"},
    "eu-central-1":    {"32":  "ami-c7ee5ca8"},
    "ca-central-1":    {"32":  "ami-fd55ec99"},
    "sa-east-1":    {"32":  "ami-f1344b9d"},
})

# EC2 Instance with user data
ec2_instance = template.add_resource(ec2.Instance(
    "Ec2Instance",
    ImageId= FindInMap("RegionMap", Ref("AWS::Region"), "32"),
    InstanceType="t2.micro",
    KeyName="chef-demo",
    SecurityGroups=["default"],
    UserData=Base64(
        Join("\n",["#!/bin/bash",
          "yum install httpd -y",
          "yum update -y",
          "service httpd start",
          "echo \"<html><h1>Running</h1></html>\"> /var/www/html/index.html"]
    ))
))

template.add_output([
    Output(
        "InstanceId",
        Description="InstanceId of the newly created EC2 instance",
        Value=Ref(ec2_instance),
    )
])

print(template.to_json())