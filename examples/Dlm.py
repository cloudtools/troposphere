from awacs.aws import Allow, PolicyDocument, Principal, Statement
from awacs.sts import AssumeRole

from troposphere import GetAtt, Tags, Template
from troposphere.dlm import (
    CreateRule,
    LifecyclePolicy,
    PolicyDetails,
    RetainRule,
    Schedule,
)
from troposphere.iam import Role

t = Template()
t.set_version("2010-09-09")

dlm_role = t.add_resource(
    Role(
        "DlmRole",
        AssumeRolePolicyDocument=PolicyDocument(
            Statement=[
                Statement(
                    Effect=Allow,
                    Action=[AssumeRole],
                    Principal=Principal("Service", ["ec2.amazonaws.com"]),
                )
            ]
        ),
    )
)

lifecycle_policy = t.add_resource(
    LifecyclePolicy(
        "LifecyclePolicy",
        Description="Daily backup",
        State="ENABLED",
        ExecutionRoleArn=GetAtt(dlm_role, "Arn"),
        PolicyDetails=PolicyDetails(
            ResourceTypes=["VOLUME"],
            TargetTags=Tags(
                Backup="True",
            ),
            Schedules=[
                Schedule(
                    Name="Daily Snapshots",
                    TagsToAdd=Tags(
                        type="DailySnapshot",
                    ),
                    CreateRule=CreateRule(
                        Interval=12, IntervalUnit="HOURS", Times=["13:00"]
                    ),
                    RetainRule=RetainRule(Count=1),
                    CopyTags=True,
                )
            ],
        ),
    )
)

print(t.to_json())
