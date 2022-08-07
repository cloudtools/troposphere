# Extend the official tutorial to be more close to production, the original tutorial is located at:
# https://docs.aws.amazon.com/batch/latest/userguide/batch_sns_tutorial.html
# This example would send successful job every 1 minute and failed job every 3 minutes.
# The failed jobs would invoke the lambda function through SNS.

from awacs.aws import Allow, PolicyDocument, Principal, Statement
from awacs.batch import SubmitJob
from awacs.sns import Publish
from troposphere import GetAtt, Join, Parameter, Ref, Region, Template
from troposphere.awslambda import Environment, Permission, Function, Code
from troposphere.batch import (
    ComputeEnvironment,
    ComputeEnvironmentOrder,
    ComputeResources,
    ContainerProperties,
    FargatePlatformConfiguration,
    JobDefinition,
    JobQueue,
    LogConfiguration,
    NetworkConfiguration,
    ResourceRequirement,
    RetryStrategy,
    Timeout,
)
from troposphere.events import BatchParameters, Rule, Target
from troposphere.iam import Policy, Role
from troposphere.sns import Subscription, Topic, TopicPolicy


t = Template(Description="Setup cron jobs with a job queue and send message through sns when a job fails.")
t.set_version("2010-09-09")
t.set_transform("AWS::Serverless-2016-10-31")

BatchSG = t.add_parameter(
    Parameter(
        "BatchSG",
        Type="String",
    )
)

SubnetList = [
    t.add_parameter(
        Parameter(
            f"Subnet{i}",
            Type="String",
        )
    )
    for i in range(1, 4)
]

Region = t.add_parameter(
    Parameter(
        "Region",
        Type="String",
    )
)

ProjectId = t.add_parameter(
    Parameter(
        "ProjectId",
        Type="String",
    )
)


EventBridgeInvokeBatchJobQueueRole = t.add_resource(
    Role(
        "EventBridgeInvokeBatchJobQueueRole",
        AssumeRolePolicyDocument={
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"Service": ["events.amazonaws.com"]},
                    "Action": ["sts:AssumeRole"],
                }
            ]
        },
        Policies=[
            Policy(
                PolicyDocument=PolicyDocument(
                    Version="2012-10-17",
                    Statement=[
                        Statement(
                            Effect=Allow,
                            Action=[SubmitJob],
                            Resource=["*"],
                        ),
                    ],
                ),
                PolicyName="EventBridgeInvokeBatchJobQueuePolicy",
            )
        ],
    )
)

BatchTaskFargateRole = t.add_resource(
    Role(
        "BatchTaskFargateRole",
        ManagedPolicyArns=[
            "arn:aws:iam::aws:policy/CloudWatchLogsFullAccess",
        ],
        AssumeRolePolicyDocument={
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"Service": ["ecs-tasks.amazonaws.com"]},
                    "Action": ["sts:AssumeRole"],
                }
            ]
        },
    )
)


BatchComputeEnvironment = t.add_resource(
    ComputeEnvironment(
        "ComputeEnvironment",
        Type="MANAGED",
        ComputeEnvironmentName="cron-compute",
        ComputeResources=ComputeResources(
            MaxvCpus=16,
            SecurityGroupIds=[Ref(BatchSG)],
            Subnets=[Ref(SubNet) for SubNet in SubnetList],
            Type="FARGATE",
        ),
        ServiceRole=Join(":", ["arn:aws:iam:", Ref(ProjectId), "role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch"]),
        State="ENABLED",
    )
)

JobQueueCron = t.add_resource(
    JobQueue(
        "JobQueueCron",
        JobQueueName="cron-queue",
        ComputeEnvironmentOrder=[
            ComputeEnvironmentOrder(ComputeEnvironment=Ref(BatchComputeEnvironment), Order=1),
        ],
        Priority=60,
        State="ENABLED",
    )
)

# Make a failed job every 3 minutes, which should trigger the alert sns
JobDefinitionFailCron = t.add_resource(
    JobDefinition(
        "JobDefinitionFailCron",
        Type="container",
        ContainerProperties=ContainerProperties(
            Command=["/bin/sh", "-c", "exit 1"],
            Image="public.ecr.aws/amazonlinux/amazonlinux:latest",
            ExecutionRoleArn=GetAtt(BatchTaskFargateRole, "Arn"),
            FargatePlatformConfiguration=FargatePlatformConfiguration(PlatformVersion="1.4.0"),
            NetworkConfiguration=NetworkConfiguration(AssignPublicIp="ENABLED"),
            ResourceRequirements=[
                ResourceRequirement(Type="MEMORY", Value="8192"),
                ResourceRequirement(Type="VCPU", Value="1"),
            ],
            JobRoleArn=GetAtt(BatchTaskFargateRole, "Arn"),
            LogConfiguration=LogConfiguration(LogDriver="awslogs"),
        ),
        RetryStrategy=RetryStrategy(Attempts=3),
        Timeout=Timeout(AttemptDurationSeconds=3600),
        PlatformCapabilities=["FARGATE"],
        JobDefinitionName="cron-fail",
    )
)

JobDefinitionSuccessCron = t.add_resource(
    JobDefinition(
        "JobDefinitionSuccessCron",
        Type="container",
        ContainerProperties=ContainerProperties(
            Command=["echo", "'Success'"],
            Image="public.ecr.aws/amazonlinux/amazonlinux:latest",
            ExecutionRoleArn=GetAtt(BatchTaskFargateRole, "Arn"),
            FargatePlatformConfiguration=FargatePlatformConfiguration(PlatformVersion="1.4.0"),
            NetworkConfiguration=NetworkConfiguration(AssignPublicIp="ENABLED"),
            ResourceRequirements=[
                ResourceRequirement(Type="MEMORY", Value="8192"),
                ResourceRequirement(Type="VCPU", Value="1"),
            ],
            JobRoleArn=GetAtt(BatchTaskFargateRole, "Arn"),
            LogConfiguration=LogConfiguration(LogDriver="awslogs"),
        ),
        RetryStrategy=RetryStrategy(Attempts=3),
        Timeout=Timeout(AttemptDurationSeconds=3600),
        PlatformCapabilities=["FARGATE"],
        JobDefinitionName="cron-success",
    )
)


JobFailRevision = 1
EventRuleCronFailJob = t.add_resource(
    Rule(
        "EventRuleCronFailJob",
        Name="cron-fail",
        ScheduleExpression="cron(*/3 * ? * * *)",
        State="ENABLED",
        Targets=[
            Target(
                "JobQueueFailCronAsTarget",
                Arn=Ref(JobQueueCron),
                RoleArn=GetAtt(EventBridgeInvokeBatchJobQueueRole, "Arn"),
                BatchParameters=BatchParameters(
                    JobDefinition=Join(":", ["arn:aws:batch", Ref(Region), Ref(ProjectId), "job-definition/cron-fail", JobFailRevision]),
                    JobName="cron-fail-eventbridge",
                ),
                Id="cron-fail",
            ),
        ],
    )
)

JobSuccessRevision = 1
EventRuleCronSuccessJob = t.add_resource(
    Rule(
        "EventRuleCronSuccessJob",
        Name="cron-success",
        ScheduleExpression="cron(*/1 * ? * * *)",
        State="ENABLED",
        Targets=[
            Target(
                "JobQueueSuccessCronAsTarget",
                Arn=Ref(JobQueueCron),
                RoleArn=GetAtt(EventBridgeInvokeBatchJobQueueRole, "Arn"),
                BatchParameters=BatchParameters(
                    JobDefinition=Join(":", ["arn:aws:batch", Ref(Region), Ref(ProjectId), "job-definition/cron-success", JobSuccessRevision]),
                    JobName="cron-success-eventbridge",
                ),
                Id="cron-success",
            ),
        ],
    )
)


LambdaExecutionRole = t.add_resource(
    Role(
        "LambdaExecutionRole",
        Path="/",
        Policies=[
            Policy(
                PolicyName="root",
                PolicyDocument={
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Action": ["logs:*"],
                            "Resource": "arn:aws:logs:*:*:*",
                            "Effect": "Allow",
                        },
                        {"Action": ["lambda:*"], "Resource": "*", "Effect": "Allow"},
                    ],
                },
            )
        ],
        AssumeRolePolicyDocument={
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": ["sts:AssumeRole"],
                    "Effect": "Allow",
                    "Principal": {"Service": ["lambda.amazonaws.com"]},
                }
            ],
        },
    )
)


LambdaCronFailNotify = t.add_resource(
    Function(
        "LambdaCronFailNotify",
        Handler="app.lambda_handler",
        Code=Code(
            ZipFile="""
import boto3
import json


def lambda_handler(event, context):
    print(event)  # implement notification code here, ex; to slack, telegram, etc.
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "ok",
        })
    }
"""
        ),
        FunctionName="lambda_cron_fail_notify",
        Role=GetAtt(LambdaExecutionRole, "Arn"),
        Runtime="python3.9",
        MemorySize=128,
        Timeout=900,
    )
)


SnsTopicCronFailed = t.add_resource(
    Topic(
        "SnsTopicCronFailed",
        Subscription=[
            Subscription(
                Endpoint=GetAtt(LambdaCronFailNotify, "Arn"),
                Protocol="lambda",
            )
        ],
        DisplayName="SnsTopicCronFailed",
        TopicName="SnsTopicCronFailed",
    )
)


t.add_resource(
    TopicPolicy(
        "CronFailedTopicPolicy",
        PolicyDocument=PolicyDocument(
            Statement=[
                Statement(
                    Effect=Allow,
                    Action=[Publish],
                    Principal=Principal("Service", ["events.amazonaws.com"]),
                    Resource=[Ref(SnsTopicCronFailed)],
                ),
            ],
        ),
        Topics=[Ref(SnsTopicCronFailed)],
    )
)


EventRuleCronFailed = t.add_resource(
    Rule(
        "EventRuleCronFailed",
        Name="cron-failed",
        Description="Send SNS for cron jobs of cron-queue for which status are FAILED",
        State="ENABLED",
        EventPattern={"detail-type": ["Batch Job State Change"], "source": ["aws.batch"], "detail": {"status": ["FAILED"], "jobQueue": [Ref(JobQueueCron)]}},
        Targets=[
            Target(
                "CronFailedAsTarget",
                Arn=Ref(SnsTopicCronFailed),
                Id="cron-failed",
            ),
        ],
    )
)

LambdaInvokePermissionCronFailed = t.add_resource(
    Permission(
        "LambdaInvokePermissionCronFailed",
        Action="lambda:InvokeFunction",
        FunctionName=Ref(LambdaCronFailNotify),
        Principal="sns.amazonaws.com",
        SourceArn=Ref(SnsTopicCronFailed),
    )
)


print(t.to_yaml())
