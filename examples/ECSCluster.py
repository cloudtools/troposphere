from troposphere import Base64, Join
from troposphere import Ref, Template
from troposphere.cloudformation import Init, InitConfig, InitFiles, InitFile
from troposphere.cloudformation import InitServices, InitService
from troposphere.iam import PolicyType
from troposphere.autoscaling import LaunchConfiguration
from troposphere.iam import Role
from troposphere.ecs import Cluster
from troposphere.autoscaling import AutoScalingGroup, Metadata
from troposphere.iam import InstanceProfile

t = Template()
t.add_version('2010-09-09')

PolicyEcr = t.add_resource(PolicyType(
    'PolicyEcr',
    PolicyName='EcrPolicy',
    PolicyDocument={'Version': '2012-10-17',
                    'Statement': [{'Action': ['ecr:GetAuthorizationToken'],
                                   'Resource': ['*'],
                                   'Effect': 'Allow'},
                                  {'Action': ['ecr:GetDownloadUrlForLayer',
                                              'ecr:BatchGetImage',
                                              'ecr:BatchCheckLayerAvailability'
                                              ],
                                   'Resource': [
                                   '*'],
                                   'Effect': 'Allow',
                                   'Sid': 'AllowPull'},
                                  ]},
    Roles=[Ref('EcsClusterRole')],
))

PolicyEcs = t.add_resource(PolicyType(
    'PolicyEcs',
    PolicyName='EcsPolicy',
    PolicyDocument={'Version': '2012-10-17',
                    'Statement': [
                        {'Action': ['ecs:CreateCluster',
                                    'ecs:RegisterContainerInstance',
                                    'ecs:DeregisterContainerInstance',
                                    'ecs:DiscoverPollEndpoint',
                                    'ecs:Submit*',
                                    'ecs:Poll',
                                    'ecs:StartTelemetrySession'],
                         'Resource': '*',
                         'Effect': 'Allow'}
                    ]},
    Roles=[Ref('EcsClusterRole')],
))

PolicyCloudwatch = t.add_resource(PolicyType(
    'PolicyCloudwatch',
    PolicyName='Cloudwatch',
    PolicyDocument={'Version': '2012-10-17',
                    'Statement': [{'Action': ['cloudwatch:*'], 'Resource': '*',
                                   'Effect': 'Allow'}]},
    Roles=[Ref('EcsClusterRole')],
))


ContainerInstances = t.add_resource(LaunchConfiguration(
    'ContainerInstances',
    Metadata=Metadata(
        Init({
            'config': InitConfig(
                files=InitFiles({
                    '/etc/cfn/cfn-hup.conf': InitFile(
                        content=Join('', ['[main]\n', 'stack=', Ref('AWS::StackId'),  # NOQA
                                          '\n', 'region=', Ref('AWS::Region'), '\n']),  # NOQA
                        mode='000400',
                        owner='root',
                        group='root'
                    ),
                    '/etc/cfn/hooks.d/cfn-auto-reloader.conf': InitFile(
                        content=Join('', ['[cfn-auto-reloader-hook]\n',
                                          'triggers=post.update\n',
                                          'path=Resources.ContainerInstances.Metadata.AWS::CloudFormation::Init\n',  # NOQA
                                          'action=/opt/aws/bin/cfn-init -v ', '--stack ', Ref(  # NOQA
                                              'AWS::StackName'), ' --resource ContainerInstances ', ' --region ', Ref('AWS::Region'), '\n',  # NOQA
                                          'runas=root\n']),
                        mode='000400',
                        owner='root',
                        group='root'
                    )},
                ),
                services=InitServices({
                    'cfn-hup': InitService(
                        ensureRunning='true',
                        enabled='true',
                        files=['/etc/cfn/cfn-hup.conf',
                               '/etc/cfn/hooks.d/cfn-auto-reloader.conf']
                    )}
                ),
                commands={
                    '01_add_instance_to_cluster': {'command': Join('',
                                                                   ['#!/bin/bash\n',  # NOQA
                                                                    'echo ECS_CLUSTER=',  # NOQA
                                                                    Ref('ECSCluster'),  # NOQA
                                                                    ' >> /etc/ecs/ecs.config'])},  # NOQA
                    '02_install_ssm_agent': {'command': Join('',
                                                             ['#!/bin/bash\n',
                                                              'yum -y update\n',  # NOQA
                                                              'curl https://amazon-ssm-eu-west-1.s3.amazonaws.com/latest/linux_amd64/amazon-ssm-agent.rpm -o amazon-ssm-agent.rpm\n',  # NOQA
                                                              'yum install -y amazon-ssm-agent.rpm'  # NOQA
                                                              ])}
                }
            )
        }
        ),
    ),
    UserData=Base64(Join('',
                         ['#!/bin/bash -xe\n',
                          'yum install -y aws-cfn-bootstrap\n',
                          '/opt/aws/bin/cfn-init -v ',
                          '         --stack ',
                          Ref('AWS::StackName'),
                             '         --resource ContainerInstances ',
                             '         --region ',
                             Ref('AWS::Region'),
                             '\n',
                             '/opt/aws/bin/cfn-signal -e $? ',
                             '         --stack ',
                             Ref('AWS::StackName'),
                             '         --resource ECSAutoScalingGroup ',
                             '         --region ',
                             Ref('AWS::Region'),
                             '\n'])),
    ImageId='ami-13f84d60',
    KeyName='yourkey',
    SecurityGroups=['sg-96114ef2'],
    IamInstanceProfile=Ref('EC2InstanceProfile'),
    InstanceType='t2.micro',
    AssociatePublicIpAddress='true',
))


ECSCluster = t.add_resource(Cluster(
    'ECSCluster',
))


ECSAutoScalingGroup = t.add_resource(AutoScalingGroup(
    'ECSAutoScalingGroup',
    DesiredCapacity='1',
    MinSize='1',
    MaxSize='1',
    VPCZoneIdentifier=['subnet-72849a0a', 'subnet-72849a08'],
    AvailabilityZones=['eu-west-1a', 'eu-west-1b'],
    LaunchConfigurationName=Ref('ContainerInstances'),
))

EC2InstanceProfile = t.add_resource(InstanceProfile(
    'EC2InstanceProfile',
    Path='/',
    Roles=[Ref('EcsClusterRole')],
))

EcsClusterRole = t.add_resource(Role(
    'EcsClusterRole',
    Path='/',
    ManagedPolicyArns=[
        'arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforSSM'
    ],
    AssumeRolePolicyDocument={'Version': '2012-10-17',
                              'Statement': [{'Action': 'sts:AssumeRole',
                                             'Principal':
                                             {'Service': 'ec2.amazonaws.com'},
                                             'Effect': 'Allow',
                                             }]}
))

print(t.to_json())
