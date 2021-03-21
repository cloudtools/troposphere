# Converted from IAM_Users_Groups_and_Policies.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import GetAtt, Output, Ref, Template
from troposphere.iam import AccessKey, Group, LoginProfile, PolicyType
from troposphere.iam import User, UserToGroupAddition


t = Template()

t.set_description("AWS CloudFormation Sample Template: This template "
                  "demonstrates the creation of IAM User/Group.")

cfnuser = t.add_resource(User(
    "CFNUser",
    LoginProfile=LoginProfile(Password="Password"))
)

cfnusergroup = t.add_resource(Group("CFNUserGroup"))
cfnadmingroup = t.add_resource(Group("CFNAdminGroup"))

cfnkeys = t.add_resource(AccessKey(
    "CFNKeys",
    Status="Active",
    UserName=Ref(cfnuser))
)

users = t.add_resource(UserToGroupAddition(
    "Users",
    GroupName=Ref(cfnusergroup),
    Users=[Ref(cfnuser)],
))

admins = t.add_resource(UserToGroupAddition(
    "Admins",
    GroupName=Ref(cfnadmingroup),
    Users=[Ref(cfnuser)],
))

t.add_resource(PolicyType(
    "CFNUserPolicies",
    PolicyName="CFNUsers",
    Groups=[Ref(cfnadmingroup)],
    PolicyDocument={
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": [
                "cloudformation:Describe*",
                "cloudformation:List*",
                "cloudformation:Get*"
            ],
            "Resource": "*"
        }],
    }
))

t.add_output(Output(
    "AccessKey",
    Value=Ref(cfnkeys),
    Description="AWSAccessKeyId of new user",
))

t.add_output(Output(
    "SecretKey",
    Value=GetAtt(cfnkeys, "SecretAccessKey"),
    Description="AWSSecretKey of new user",
))

print(t.to_json())
