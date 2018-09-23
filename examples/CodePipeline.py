# Converted from CodePipeline example located at:
# http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-pipeline.html # noqa

from troposphere import Parameter, Ref, Template
from troposphere.codepipeline import (
    Pipeline, Stages, Actions, ActionTypeId, OutputArtifacts, InputArtifacts,
    ArtifactStore, DisableInboundStageTransitions)

t = Template()


CodePipelineServiceRole = t.add_parameter(Parameter(
    "CodePipelineServiceRole",
    Description="The CodePipelineServiceRole ARN to use",
    Type="String"
))

ArtifactStoreS3Location = t.add_parameter(Parameter(
    "ArtifactStoreS3Location",
    Description="This should be an S3 bucket resource or bucket name",
    Type="String"
))

pipeline = t.add_resource(Pipeline(
    "AppPipeline",
    RoleArn=Ref(CodePipelineServiceRole),
    Stages=[
        Stages(
            Name="Source",
            Actions=[
                Actions(
                    Name="SourceAction",
                    ActionTypeId=ActionTypeId(
                        Category="Source",
                        Owner="AWS",
                        Version="1",
                        Provider="S3"
                    ),
                    OutputArtifacts=[
                        OutputArtifacts(
                            Name="SourceOutput"
                        )
                    ],
                    Configuration={
                        "S3Bucket": {"Ref": "SourceS3Bucket"},
                        "S3ObjectKey": {"Ref": "SourceS3ObjectKey"}
                    },
                    RunOrder="1"
                )
            ]
        ),
        Stages(
            Name="Beta",
            Actions=[
                Actions(
                    Name="BetaAction",
                    InputArtifacts=[
                        InputArtifacts(
                            Name="SourceOutput"
                        )
                    ],
                    ActionTypeId=ActionTypeId(
                        Category="Deploy",
                        Owner="AWS",
                        Version="1",
                        Provider="CodeDeploy"
                    ),
                    Configuration={
                        "ApplicationName": {"Ref": "ApplicationName"},
                        "DeploymentGroupName": {"Ref": "DeploymentGroupName"}
                    },
                    RunOrder="1"
                )
            ]
        ),
        Stages(
            Name="Release",
            Actions=[
                Actions(
                    Name="ReleaseAction",
                    InputArtifacts=[
                        InputArtifacts(
                            Name="SourceOutput"
                        )
                    ],
                    ActionTypeId=ActionTypeId(
                        Category="Deploy",
                        Owner="AWS",
                        Version="1",
                        Provider="CodeDeploy"
                    ),
                    Configuration={
                        "ApplicationName": {"Ref": "ApplicationName"},
                        "DeploymentGroupName": {"Ref": "DeploymentGroupName"}
                    },
                    RunOrder="1"
                )
            ]
        )
    ],
    ArtifactStore=ArtifactStore(
        Type="S3",
        Location=Ref(ArtifactStoreS3Location)
    ),
    DisableInboundStageTransitions=[
        DisableInboundStageTransitions(
            StageName="Release",
            Reason="Disabling the transition until "
                   "integration tests are completed"
        )
    ]
))


print(t.to_json())
