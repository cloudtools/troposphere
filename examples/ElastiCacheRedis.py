#!/usr/bin/env python
"""
Converted from ElastiCache_Redis.template located at:
http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

In addition to troposphere, this script requires awacs (Amazon Web Access Control Subsystem)
"""
from __future__ import absolute_import, division, print_function

import troposphere.ec2 as ec2
import troposphere.elasticache as elasticache
import troposphere.iam as iam

from awacs.aws import (Allow,
                       Statement,
                       Principal,
                       Policy)
from awacs.sts import AssumeRole

from troposphere import (Base64,
                         cloudformation,
                         FindInMap,
                         GetAtt,
                         GetAZs,
                         Join,
                         Parameter,
                         Output,
                         Ref,
                         Select,
                         Tags,
                         Template)
#from troposphere.ec2 import (SecurityGroup,
#                             SecurityGroupIngress,
#                             SecurityGroupRule)


def main():
    """
    Create a ElastiCache Redis Node and EC2 Instance
    """

    template = Template()

    # Description
    template.add_description('AWS CloudFormation Sample Template ElastiCache_Redis:'
                             'Sample template showIing how to create an Amazon'
                             'ElastiCache Redis Cluster. **WARNING** This template'
                             'creates an Amazon EC2 Instance and an Amazon ElastiCache'
                             'Cluster. You will be billed for the AWS resources used'
                             'if you create a stack from this template.')

    # Mappings
# template.add_mapping('RegionMap', {
#     "us-east-1": {"AMI": "ami-7f418316"},
#     "us-west-1": {"AMI": "ami-951945d0"},
#     "us-west-2": {"AMI": "ami-16fd7026"},
#     "eu-west-1": {"AMI": "ami-24506250"},
#     "sa-east-1": {"AMI": "ami-3e3be423"},
#     "ap-southeast-1": {"AMI": "ami-74dda626"},
#     "ap-northeast-1": {"AMI": "ami-dcfa4edd"}
# })

    awsinstancetype2arch = template.add_mapping('AWSInstanceType2Arch', {
        't1.micro'    : {'Arch' : 'PV64'},
        't2.micro'    : {'Arch' : 'HVM64'},
        't2.small'    : {'Arch' : 'HVM64'},
        't2.medium'   : {'Arch' : 'HVM64'},
        'm1.small'    : {'Arch' : 'PV64'},
        'm1.medium'   : {'Arch' : 'PV64'},
        'm1.large'    : {'Arch' : 'PV64'},
        'm1.xlarge'   : {'Arch' : 'PV64'},
        'm2.xlarge'   : {'Arch' : 'PV64'},
        'm2.2xlarge'  : {'Arch' : 'PV64'},
        'm2.4xlarge'  : {'Arch' : 'PV64'},
        'm3.medium'   : {'Arch' : 'HVM64'},
        'm3.large'    : {'Arch' : 'HVM64'},
        'm3.xlarge'   : {'Arch' : 'HVM64'},
        'm3.2xlarge'  : {'Arch' : 'HVM64'},
        'c1.medium'   : {'Arch' : 'PV64'},
        'c1.xlarge'   : {'Arch' : 'PV64'},
        'c3.large'    : {'Arch' : 'HVM64'},
        'c3.xlarge'   : {'Arch' : 'HVM64'},
        'c3.2xlarge'  : {'Arch' : 'HVM64'},
        'c3.4xlarge'  : {'Arch' : 'HVM64'},
        'c3.8xlarge'  : {'Arch' : 'HVM64'},
        'c4.large'    : {'Arch' : 'HVM64'},
        'c4.xlarge'   : {'Arch' : 'HVM64'},
        'c4.2xlarge'  : {'Arch' : 'HVM64'},
        'c4.4xlarge'  : {'Arch' : 'HVM64'},
        'c4.8xlarge'  : {'Arch' : 'HVM64'},
        'g2.2xlarge'  : {'Arch' : 'HVMG2'},
        'r3.large'    : {'Arch' : 'HVM64'},
        'r3.xlarge'   : {'Arch' : 'HVM64'},
        'r3.2xlarge'  : {'Arch' : 'HVM64'},
        'r3.4xlarge'  : {'Arch' : 'HVM64'},
        'r3.8xlarge'  : {'Arch' : 'HVM64'},
        'i2.xlarge'   : {'Arch' : 'HVM64'},
        'i2.2xlarge'  : {'Arch' : 'HVM64'},
        'i2.4xlarge'  : {'Arch' : 'HVM64'},
        'i2.8xlarge'  : {'Arch' : 'HVM64'},
        'd2.xlarge'   : {'Arch' : 'HVM64'},
        'd2.2xlarge'  : {'Arch' : 'HVM64'},
        'd2.4xlarge'  : {'Arch' : 'HVM64'},
        'd2.8xlarge'  : {'Arch' : 'HVM64'},
        'hi1.4xlarge' : {'Arch' : 'HVM64'},
        'hs1.8xlarge' : {'Arch' : 'HVM64'},
        'cr1.8xlarge' : {'Arch' : 'HVM64'},
        'cc2.8xlarge' : {'Arch' : 'HVM64'}
        })

    awsregionarch2ami = template.add_mapping('AWSRegionArch2AMI', {
        'us-east-1'        : {'PV64' : 'ami-0f4cfd64', 'HVM64' : 'ami-0d4cfd66', 'HVMG2' : 'ami-5b05ba30'},
        'us-west-2'        : {'PV64' : 'ami-d3c5d1e3', 'HVM64' : 'ami-d5c5d1e5', 'HVMG2' : 'ami-a9d6c099'},
        'us-west-1'        : {'PV64' : 'ami-85ea13c1', 'HVM64' : 'ami-87ea13c3', 'HVMG2' : 'ami-37827a73'},
        'eu-west-1'        : {'PV64' : 'ami-d6d18ea1', 'HVM64' : 'ami-e4d18e93', 'HVMG2' : 'ami-72a9f105'},
        'eu-central-1'     : {'PV64' : 'ami-a4b0b7b9', 'HVM64' : 'ami-a6b0b7bb', 'HVMG2' : 'ami-a6c9cfbb'},
        'ap-northeast-1'   : {'PV64' : 'ami-1a1b9f1a', 'HVM64' : 'ami-1c1b9f1c', 'HVMG2' : 'ami-f644c4f6'},
        'ap-southeast-1'   : {'PV64' : 'ami-d24b4280', 'HVM64' : 'ami-d44b4286', 'HVMG2' : 'ami-12b5bc40'},
        'ap-southeast-2'   : {'PV64' : 'ami-ef7b39d5', 'HVM64' : 'ami-db7b39e1', 'HVMG2' : 'ami-b3337e89'},
        'sa-east-1'        : {'PV64' : 'ami-5b098146', 'HVM64' : 'ami-55098148', 'HVMG2' : 'NOT_SUPPORTED'},
        'cn-north-1'       : {'PV64' : 'ami-bec45887', 'HVM64' : 'ami-bcc45885', 'HVMG2' : 'NOT_SUPPORTED'}
        })

    region2principal = template.add_mapping('Region2Principal', {
        'us-east-1'      : { 'EC2Principal' : 'ec2.amazonaws.com', 'OpsWorksPrincipal' : 'opsworks.amazonaws.com' },
        'us-west-2'      : { 'EC2Principal' : 'ec2.amazonaws.com', 'OpsWorksPrincipal' : 'opsworks.amazonaws.com' },
        'us-west-1'      : { 'EC2Principal' : 'ec2.amazonaws.com', 'OpsWorksPrincipal' : 'opsworks.amazonaws.com' },
        'eu-west-1'      : { 'EC2Principal' : 'ec2.amazonaws.com', 'OpsWorksPrincipal' : 'opsworks.amazonaws.com' },
        'ap-southeast-1' : { 'EC2Principal' : 'ec2.amazonaws.com', 'OpsWorksPrincipal' : 'opsworks.amazonaws.com' },
        'ap-northeast-1' : { 'EC2Principal' : 'ec2.amazonaws.com', 'OpsWorksPrincipal' : 'opsworks.amazonaws.com' },
        'ap-southeast-2' : { 'EC2Principal' : 'ec2.amazonaws.com', 'OpsWorksPrincipal' : 'opsworks.amazonaws.com' },
        'sa-east-1'      : { 'EC2Principal' : 'ec2.amazonaws.com', 'OpsWorksPrincipal' : 'opsworks.amazonaws.com' },
        'cn-north-1'     : { 'EC2Principal' : 'ec2.amazonaws.com.cn', 'OpsWorksPrincipal' : 'opsworks.amazonaws.com.cn' },
        'eu-central-1'   : { 'EC2Principal' : 'ec2.amazonaws.com', 'OpsWorksPrincipal' : 'opsworks.amazonaws.com' }
        })


    # Parameters
    cachenodetype = template.add_parameter(Parameter(
        'ClusterNodeType',
        Description='The compute and memory capacity of the nodes in the Redis Cluster',
        Type='String',
        Default='cache.m1.small',
        AllowedValues=['cache.m1.small',
                       'cache.m1.large',
                       'cache.m1.xlarge',
                       'cache.m2.xlarge',
                       'cache.m2.2xlarge',
                       'cache.m2.4xlarge',
                       'cache.c1.xlarge'],
        ConstraintDescription='must select a valid Cache Node type.',
        ))

    keyname = template.add_parameter(Parameter(
        'KeyName',
        Description='Name of an existing EC2 KeyPair to enable SSH access to the instance',
        Type='AWS::EC2::KeyPair::KeyName',
        ConstraintDescription='must be the name of an existing EC2 KeyPair.',
        ))

    instancetype = template.add_parameter(Parameter(
        'InstanceType',
        Description='WebServer EC2 instance type',
        Type='String',
        Default='t2.micro',
        AllowedValues=['t1.micro',
                       't2.micro',
                       't2.small',
                       't2.medium',
                       'm1.small',
                       'm1.medium',
                       'm1.large',
                       'm1.xlarge',
                       'm2.xlarge',
                       'm2.2xlarge',
                       'm2.4xlarge',
                       'm3.medium',
                       'm3.large',
                       'm3.xlarge',
                       'm3.2xlarge',
                       'c1.medium',
                       'c1.xlarge',
                       'c3.large',
                       'c3.xlarge',
                       'c3.2xlarge',
                       'c3.4xlarge',
                       'c3.8xlarge',
                       'c4.large',
                       'c4.xlarge',
                       'c4.2xlarge',
                       'c4.4xlarge',
                       'c4.8xlarge',
                       'g2.2xlarge',
                       'r3.large',
                       'r3.xlarge',
                       'r3.2xlarge',
                       'r3.4xlarge',
                       'r3.8xlarge',
                       'i2.xlarge',
                       'i2.2xlarge',
                       'i2.4xlarge',
                       'i2.8xlarge',
                       'd2.xlarge',
                       'd2.2xlarge',
                       'd2.4xlarge',
                       'd2.8xlarge',
                       'hi1.4xlarge',
                       'hs1.8xlarge',
                       'cr1.8xlarge',
                       'cc2.8xlarge',
                       'cg1.4xlarge'],
        ConstraintDescription='must be a valid EC2 instance type.',
        ))


    # Resources
    webserverrole = template.add_resource(iam.Role(
        'WebServerRole',
        AssumeRolePolicyDocument=Policy(
            Statement=[
                Statement(
                    Effect=Allow,
                    Action=[AssumeRole],
                    Principal=Principal('Service',
                        [FindInMap('Region2Principal', Ref('AWS::Region'), 'EC2Principal')]),
                    )
                ]
            )
        ))

    webserverrolepolicy = template.add_resource(iam.PolicyType(
        'WebServerRolePolicy',
        PolicyName='WebServerRole',
        # PolicyDocument=Policy(
        #     Statement=[
        #         Statement(
        #             Effect=Allow,
        #             Action=['elasticache:DescribeCacheClusters'],
        #             Resource=['*'],
        #             )
        #         ]
        #     )
        ## The following can probably be fixed to use awacs (above didn't work)
        PolicyDocument={
            "Statement"    : [{
                "Effect"   : "Allow",
                "Action"   : "elasticache:DescribeCacheClusters",
                "Resource" : "*"
                }]
            }
        ))

    webserverinstanceprofile = template.add_resource(iam.InstanceProfile(
        'WebServerInstanceProfile',
        Path='/',
        Roles=Ref(webserverrole),
    ))

    webserversg = template.add_resource(ec2.SecurityGroup(
        'WebServeSecurityGroup',
        GroupDescription='Enable HTTP and SSH access',
        SecurityGroupIngress=[
            ec2.SecurityGroupRule(
                IpProtocol='tcp',
                FromPort='22',
                ToPort='22',
                CidrIp=Ref('SSHLocation'),
                ),
            ec2.SecurityGroupRule(
                IpProtocol='tcp',
                FromPort='80',
                ToPort='80',
                CidrIp=Ref('0.0.0.0/0'),
                )
            ]
        ))

    webserverinstance = template.add_resource(ec2.Instance(
        'WebServerInstance',
        Metadata=cloudformation.Metadata(
            cloudformation.Init({
                'config': cloudformation.InitConfig(
                    packages={
                        'yum': {
                            'httpd'     : [],
                            'php'       : [],
                            'php-devel' : [],
                            'gcc'       : [],
                            'make'      : []
                            }
                        },

                    files=cloudformation.InitFiles({
                        '/var/www/html/index.pup': cloudformation.InitFile(
                            content=Join('', ['TBD']),
                            mode='000644',
                            owner='apache',
                            group='apache'
                            ),
                        '/etc/cron.d/get_cluster_config': cloudformation.InitFile(
                            content='*/5 * * * * root /usr/local/bin/get_cluster_config',
                            mode='000644',
                            owner='root',
                            group='root'
                            ),
                        '/usr/local/bin/get_cluster_config': cloudformation.InitFile(
                            content="TBD",
                            mode='000755',
                            owner='root',
                            group='root'
                            ),
                        '/usr/local/bin/install_phpredis': cloudformation.InitFile(
                            content="TBD",
                            mode='000755',
                            owner='root',
                            group='root'
                            ),
                        '/etc/cfn/cfn-hup.conf': cloudformation.InitFile(
                            content="TBD",
                            mode='000400',
                            owner='root',
                            group='root'
                            ),
                        '/etc/cfn/hooks.d/cfn-auto-reloader.conf' : cloudformation.InitFile(
                            content=Join('', [
                                '[cfn-auto-reloader-hook]\n',
                                'triggers=post.update\n',
                                'path=Resources.WebServerInstance.Metadata.AWS::CloudFormation::Init\n',
                                'action=/opt/aws/bin/cfn-init -v ',
                                '         --stack ', Ref('AWS::StackName'),
                                '         --resource WebServerInstance ',
                                '         --region ', Ref('AWS::Region'), '\n',
                                'runas=root\n'
                                ]),
                            #mode='000400',
                            #owner='root',
                            #group='root'
                            ),
                        }),

                    commands={
                        '01-install_phpredis': {
                            'command': '/usr/local/bin/install_phpredis'
                            },
                        '02-get-cluster-config': {
                            'command': '/usr/local/bin/get_cluster_config'
                            }
                        }
                    )
                })
            ),
        ImageId=FindInMap(Ref(awsregionarch2ami), Ref('AWS::Region'),
                          FindInMap(Ref(awsinstancetype2arch), Ref(instancetype), 'Arch')
                         ),
        InstanceType=Ref(instancetype),
        SecurityGroups=[Ref(webserversg)],
        KeyName=Ref(keyname),
        IamInstanceProfile=Ref(webserverinstanceprofile),
        UserData=Base64(Join('', [
            '#!/bin/bash -xe\n',
            'yum update -y aws-cfn-bootstrap\n',

            '# Setup the PHP sample application\n',
            '/opt/aws/bin/cfn-init -v ',
            '         --stack ', Ref('AWS::StackName'),
            '         --resource WebServerInstance ',
            '         --region ', Ref('AWS::Region'), '\n',

            '# Signal the status of cfn-init\n',
            '/opt/aws/bin/cfn-signal -e $? ',
            '         --stack ', Ref('AWS::StackName'),
            '         --resource WebServerInstance ',
            '         --region ', Ref('AWS::Region'), '\n'
            ]))
        ))

    redisclustersg = template.add_resource(elasticache.SecurityGroup(
        'RedisClusterSecurityGroup',
        Description='Lock the cluster down',
        ))

    template.add_resource(elasticache.SecurityGroupIngress(
        'RedisClusterSecurityGroupIngress',
        CacheSecurityGroupName=Ref(redisclustersg),
        EC2SecurityGroupName=Ref(webserversg),
        ))

    rediscluster = template.add_resource(elasticache.CacheCluster(
        'RedisCluster',
        #Type='AWS::ElastiCache::CacheCluster',
        Engine='redis',
        CacheNodeType=Ref(cachenodetype),
        NumCacheNodes=1,
        CacheSecurityGroupNames=[Ref(redisclustersg)],
        ))



    # Print CloudFormation Template
    print(template.to_json())


if __name__ == '__main__':
    main()
