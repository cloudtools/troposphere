"""
Batch.

Create the AWS Batch Compute environment and roles.
"""

from troposphere import GetAtt, Output, Parameter, Ref, Tags, Template
from troposphere.batch import (ComputeEnvironment, ComputeEnvironmentOrder,
                               ComputeResources, JobQueue,
                               LaunchTemplateSpecification)
from troposphere.ec2 import SecurityGroup
from troposphere.iam import InstanceProfile, Role

t = Template('AWS Batch')
t.add_version()

PrivateSubnetA = t.add_parameter(Parameter(
    'PrivateSubnetA',
    Type='String'
))

PrivateSubnetB = t.add_parameter(Parameter(
    'PrivateSubnetB',
    Type='String'
))

Vpc = t.add_parameter(Parameter(
    'Vpc',
    ConstraintDescription='Must be a valid VPC ID.',
    Type='AWS::EC2::VPC::Id'
))

BatchServiceRole = t.add_resource(Role(
    'BatchServiceRole',
    Path='/',
    Policies=[],
    ManagedPolicyArns=[
        'arn:aws:iam::aws:policy/service-role/AWSBatchServiceRole',
    ],
    AssumeRolePolicyDocument={'Statement': [{
        'Action': ['sts:AssumeRole'],
        'Effect': 'Allow',
        'Principal': {'Service': ['batch.amazonaws.com']}
    }]},
))

BatchInstanceRole = t.add_resource(Role(
    'BatchInstanceRole',
    Path='/',
    Policies=[],
    ManagedPolicyArns=[
        'arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role',  # NOQA
    ],
    AssumeRolePolicyDocument={'Statement': [{
        'Action': ['sts:AssumeRole'],
        'Effect': 'Allow',
        'Principal': {'Service': ['ec2.amazonaws.com']}
    }]},
))

BatchInstanceProfile = t.add_resource(InstanceProfile(
    'BatchInstanceProfile',
    Path='/',
    Roles=[Ref(BatchInstanceRole)],
))

BatchSecurityGroup = t.add_resource(SecurityGroup(
    'BatchSecurityGroup',
    VpcId=Ref(Vpc),
    GroupDescription='Enable access to Batch instances',
    Tags=Tags(Name='batch-sg')
))

BatchComputeEnvironment = t.add_resource(ComputeEnvironment(
    'BatchComputeEnvironment',
    Type='MANAGED',
    ServiceRole=Ref(BatchServiceRole),
    ComputeResources=ComputeResources(
        'BatchComputeResources',
        Type='EC2',
        DesiredvCpus=0,
        MinvCpus=0,
        MaxvCpus=10,
        PlacementGroup="ExampleClusterGroup",
        InstanceTypes=['m4.large'],
        LaunchTemplate=LaunchTemplateSpecification(
            LaunchTemplateName='container-volume-encrypt'
        ),
        InstanceRole=Ref(BatchInstanceProfile),
        SecurityGroupIds=[GetAtt(BatchSecurityGroup, 'GroupId')],
        Subnets=[
            Ref(PrivateSubnetA),
            Ref(PrivateSubnetB)
        ],
        Tags=dict(
            Name='batch-compute-environment',
            Project='example'
        )
    )
))

ExampleJobQueue = t.add_resource(JobQueue(
    'ExampleJobQueue',
    ComputeEnvironmentOrder=[
        ComputeEnvironmentOrder(
            ComputeEnvironment=Ref(BatchComputeEnvironment),
            Order=1
        ),
    ],
    Priority=1,
    State='ENABLED',
    JobQueueName='example-job-queue'
))

t.add_output([
    Output('BatchComputeEnvironment', Value=Ref(BatchComputeEnvironment)),
    Output('BatchSecurityGroup', Value=Ref(BatchSecurityGroup)),
    Output('ExampleJobQueue', Value=Ref(ExampleJobQueue))
])

print(t.to_json())
