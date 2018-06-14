from troposphere import Template, Ref

from troposphere.iam import Role, InstanceProfile

from awacs.aws import Allow, Statement, Principal, Policy
from awacs.sts import AssumeRole

t = Template()

t.add_description("AWS CloudFormation Sample Template: This template "
                  "demonstrates the creation of IAM Roles and "
                  "InstanceProfiles.")

cfnrole = t.add_resource(Role(
    "CFNRole",
    AssumeRolePolicyDocument=Policy(
        Statement=[
            Statement(
                Effect=Allow,
                Action=[AssumeRole],
                Principal=Principal("Service", ["ec2.amazonaws.com"])
            )
        ]
    )
))

cfninstanceprofile = t.add_resource(InstanceProfile(
    "CFNInstanceProfile",
    Roles=[Ref(cfnrole)]
))

cfninstancepolicy = t.add_resource(PolicyType(
    "CFNInstancePolicy",
    PolicyName="CFNPolicy",
    PolicyDocument={
        "Version": "2018-06-14",
        "Statement": [{
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeAddresses",
                "ec2:AllocateAddress",
                "ec2:DescribeInstances",
                "ec2:AssociateAddress",
            ],
            "Resource": "*"
        }],
    },
    Roles=[Ref("cfnrole")],
))

print(t.to_json())
