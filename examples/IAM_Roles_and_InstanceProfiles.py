from troposphere import Template, Ref

from troposphere.iam import Role, InstanceProfile

from awacs.aws import Allow, Statement, Principal, PolicyDocument
from awacs.sts import AssumeRole

t = Template()

t.set_description("AWS CloudFormation Sample Template: This template "
                  "demonstrates the creation of IAM Roles and "
                  "InstanceProfiles.")

cfnrole = t.add_resource(Role(
    "CFNRole",
    AssumeRolePolicyDocument=PolicyDocument(
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

print(t.to_json())
