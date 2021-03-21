# Converted from IAM_Users_Groups_and_Policies.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import GetAtt, Ref, Template
from troposphere.iam import LoginProfile, Policy, User
import awacs
import awacs.aws
import awacs.sns
import awacs.sqs


t = Template()

t.add_resource(User(
    "myuser",
    Path="/",
    LoginProfile=LoginProfile(Password="myP@ssW0rd"),
    Policies=[
        Policy(
            PolicyName="giveaccesstoqueueonly",
            PolicyDocument=awacs.aws.PolicyDocument(
                Statement=[
                    awacs.aws.Statement(
                        Effect=awacs.aws.Allow,
                        Action=[awacs.aws.Action("sqs", "*")],
                        Resource=[GetAtt("myqueue", "Arn")],
                    ),
                    awacs.aws.Statement(
                        Effect=awacs.aws.Deny,
                        Action=[awacs.aws.Action("sqs", "*")],
                        NotResource=[GetAtt("myqueue", "Arn")],
                    ),
                ],
            )
        ),
        Policy(
            PolicyName="giveaccesstotopiconly",
            PolicyDocument=awacs.aws.PolicyDocument(
                Statement=[
                    awacs.aws.Statement(
                        Effect=awacs.aws.Allow,
                        Action=[awacs.aws.Action("sns", "*")],
                        Resource=[Ref("mytopic")],
                    ),
                    awacs.aws.Statement(
                        Effect=awacs.aws.Deny,
                        Action=[awacs.aws.Action("sns", "*")],
                        NotResource=[Ref("mytopic")],
                    ),
                ],
            )
        ),
    ]
))

print(t.to_json())
