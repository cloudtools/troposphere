#!/usr/bin/env python
"""
Converted from ElastiCache_Redis.template located at:
http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

In addition to troposphere, this script requires awacs (Amazon Web Access
Control Subsystem)
"""
from __future__ import absolute_import, division, print_function

import troposphere.ec2 as ec2
import troposphere.elasticache as elasticache
import troposphere.iam as iam
import awacs

from awacs.aws import (Allow,
                       Statement,
                       Principal,
                       PolicyDocument)
from awacs.sts import AssumeRole

from troposphere import (Base64,
                         cloudformation,
                         FindInMap,
                         GetAtt,
                         Join,
                         Parameter,
                         Output,
                         Ref,
                         Tags,
                         Template)
from troposphere.policies import (CreationPolicy,
                                  ResourceSignal)


def main():
    """
    Create a ElastiCache Redis Node and EC2 Instance
    """

    template = Template()

    # Description
    template.set_description(
        'AWS CloudFormation Sample Template ElastiCache_Redis:'
        'Sample template showing how to create an Amazon'
        'ElastiCache Redis Cluster. **WARNING** This template'
        'creates an Amazon EC2 Instance and an Amazon ElastiCache'
        'Cluster. You will be billed for the AWS resources used'
        'if you create a stack from this template.')

    # Mappings
    template.add_mapping('AWSInstanceType2Arch', {
        't1.micro':     {'Arch': 'PV64'},
        't2.micro':     {'Arch': 'HVM64'},
        't2.small':     {'Arch': 'HVM64'},
        't2.medium':    {'Arch': 'HVM64'},
        'm1.small':     {'Arch': 'PV64'},
        'm1.medium':    {'Arch': 'PV64'},
        'm1.large':     {'Arch': 'PV64'},
        'm1.xlarge':    {'Arch': 'PV64'},
        'm2.xlarge':    {'Arch': 'PV64'},
        'm2.2xlarge':   {'Arch': 'PV64'},
        'm2.4xlarge':   {'Arch': 'PV64'},
        'm3.medium':    {'Arch': 'HVM64'},
        'm3.large':     {'Arch': 'HVM64'},
        'm3.xlarge':    {'Arch': 'HVM64'},
        'm3.2xlarge':   {'Arch': 'HVM64'},
        'c1.medium':    {'Arch': 'PV64'},
        'c1.xlarge':    {'Arch': 'PV64'},
        'c3.large':     {'Arch': 'HVM64'},
        'c3.xlarge':    {'Arch': 'HVM64'},
        'c3.2xlarge':   {'Arch': 'HVM64'},
        'c3.4xlarge':   {'Arch': 'HVM64'},
        'c3.8xlarge':   {'Arch': 'HVM64'},
        'c4.large':     {'Arch': 'HVM64'},
        'c4.xlarge':    {'Arch': 'HVM64'},
        'c4.2xlarge':   {'Arch': 'HVM64'},
        'c4.4xlarge':   {'Arch': 'HVM64'},
        'c4.8xlarge':   {'Arch': 'HVM64'},
        'g2.2xlarge':   {'Arch': 'HVMG2'},
        'r3.large':     {'Arch': 'HVM64'},
        'r3.xlarge':    {'Arch': 'HVM64'},
        'r3.2xlarge':   {'Arch': 'HVM64'},
        'r3.4xlarge':   {'Arch': 'HVM64'},
        'r3.8xlarge':   {'Arch': 'HVM64'},
        'i2.xlarge':    {'Arch': 'HVM64'},
        'i2.2xlarge':   {'Arch': 'HVM64'},
        'i2.4xlarge':   {'Arch': 'HVM64'},
        'i2.8xlarge':   {'Arch': 'HVM64'},
        'd2.xlarge':    {'Arch': 'HVM64'},
        'd2.2xlarge':   {'Arch': 'HVM64'},
        'd2.4xlarge':   {'Arch': 'HVM64'},
        'd2.8xlarge':   {'Arch': 'HVM64'},
        'hi1.4xlarge':  {'Arch': 'HVM64'},
        'hs1.8xlarge':  {'Arch': 'HVM64'},
        'cr1.8xlarge':  {'Arch': 'HVM64'},
        'cc2.8xlarge':  {'Arch': 'HVM64'}
        })

    template.add_mapping('AWSRegionArch2AMI', {
        'us-east-1': {'PV64': 'ami-0f4cfd64',
                      'HVM64': 'ami-0d4cfd66',
                      'HVMG2': 'ami-5b05ba30'},
        'us-west-2': {'PV64': 'ami-d3c5d1e3',
                      'HVM64': 'ami-d5c5d1e5',
                      'HVMG2': 'ami-a9d6c099'},
        'us-west-1': {'PV64': 'ami-85ea13c1',
                      'HVM64': 'ami-87ea13c3',
                      'HVMG2': 'ami-37827a73'},
        'eu-west-1': {'PV64': 'ami-d6d18ea1',
                      'HVM64': 'ami-e4d18e93',
                      'HVMG2': 'ami-72a9f105'},
        'eu-central-1': {'PV64': 'ami-a4b0b7b9',
                         'HVM64': 'ami-a6b0b7bb',
                         'HVMG2': 'ami-a6c9cfbb'},
        'ap-northeast-1': {'PV64': 'ami-1a1b9f1a',
                           'HVM64': 'ami-1c1b9f1c',
                           'HVMG2': 'ami-f644c4f6'},
        'ap-southeast-1': {'PV64': 'ami-d24b4280',
                           'HVM64': 'ami-d44b4286',
                           'HVMG2': 'ami-12b5bc40'},
        'ap-southeast-2': {'PV64': 'ami-ef7b39d5',
                           'HVM64': 'ami-db7b39e1',
                           'HVMG2': 'ami-b3337e89'},
        'sa-east-1': {'PV64': 'ami-5b098146',
                      'HVM64': 'ami-55098148',
                      'HVMG2': 'NOT_SUPPORTED'},
        'cn-north-1': {'PV64': 'ami-bec45887',
                       'HVM64': 'ami-bcc45885',
                       'HVMG2': 'NOT_SUPPORTED'}
        })

    template.add_mapping('Region2Principal', {
        'us-east-1': {'EC2Principal': 'ec2.amazonaws.com',
                      'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
        'us-west-2': {'EC2Principal': 'ec2.amazonaws.com',
                      'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
        'us-west-1': {'EC2Principal': 'ec2.amazonaws.com',
                      'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
        'eu-west-1': {'EC2Principal': 'ec2.amazonaws.com',
                      'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
        'ap-southeast-1': {'EC2Principal': 'ec2.amazonaws.com',
                           'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
        'ap-northeast-1': {'EC2Principal': 'ec2.amazonaws.com',
                           'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
        'ap-southeast-2': {'EC2Principal': 'ec2.amazonaws.com',
                           'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
        'sa-east-1': {'EC2Principal': 'ec2.amazonaws.com',
                      'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
        'cn-north-1': {'EC2Principal': 'ec2.amazonaws.com.cn',
                       'OpsWorksPrincipal': 'opsworks.amazonaws.com.cn'},
        'eu-central-1': {'EC2Principal': 'ec2.amazonaws.com',
                         'OpsWorksPrincipal': 'opsworks.amazonaws.com'}
        })

    # Parameters
    cachenodetype = template.add_parameter(Parameter(
        'ClusterNodeType',
        Description='The compute and memory capacity of the nodes in the Redis'
                    ' Cluster',
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

    keyname = template.add_parameter(Parameter(
        'KeyName',
        Description='Name of an existing EC2 KeyPair to enable SSH access'
                    ' to the instance',
        Type='AWS::EC2::KeyPair::KeyName',
        ConstraintDescription='must be the name of an existing EC2 KeyPair.',
        ))

    sshlocation = template.add_parameter(Parameter(
        'SSHLocation',
        Description='The IP address range that can be used to SSH to'
                    ' the EC2 instances',
        Type='String',
        MinLength='9',
        MaxLength='18',
        Default='0.0.0.0/0',
        AllowedPattern='(\\d{1,3})\\.(\\d{1,3})\\.'
                       '(\\d{1,3})\\.(\\d{1,3})/(\\d{1,2})',
        ConstraintDescription='must be a valid IP CIDR range of the'
                              ' form x.x.x.x/x.'
        ))

    # Resources
    webserverrole = template.add_resource(iam.Role(
        'WebServerRole',
        AssumeRolePolicyDocument=PolicyDocument(
            Statement=[
                Statement(
                    Effect=Allow,
                    Action=[AssumeRole],
                    Principal=Principal('Service',
                                        [FindInMap('Region2Principal',
                                                   Ref('AWS::Region'),
                                                   'EC2Principal')]),
                    )
                ]
            ),
        Path='/',
    ))

    template.add_resource(iam.PolicyType(
        'WebServerRolePolicy',
        PolicyName='WebServerRole',
        PolicyDocument=PolicyDocument(
            Statement=[awacs.aws.Statement(
                Action=[awacs.aws.Action("elasticache",
                        "DescribeCacheClusters")],
                Resource=["*"],
                Effect=awacs.aws.Allow
            )]
        ),
        Roles=[Ref(webserverrole)],
    ))

    webserverinstanceprofile = template.add_resource(iam.InstanceProfile(
        'WebServerInstanceProfile',
        Path='/',
        Roles=[Ref(webserverrole)],
    ))

    webserversg = template.add_resource(ec2.SecurityGroup(
        'WebServerSecurityGroup',
        GroupDescription='Enable HTTP and SSH access',
        SecurityGroupIngress=[
            ec2.SecurityGroupRule(
                IpProtocol='tcp',
                FromPort='22',
                ToPort='22',
                CidrIp=Ref(sshlocation),
                ),
            ec2.SecurityGroupRule(
                IpProtocol='tcp',
                FromPort='80',
                ToPort='80',
                CidrIp='0.0.0.0/0',
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
                            'httpd':     [],
                            'php':       [],
                            'php-devel': [],
                            'gcc':       [],
                            'make':      []
                            }
                        },

                    files=cloudformation.InitFiles({
                        '/var/www/html/index.php': cloudformation.InitFile(
                            content=Join('', [
                                '<?php\n',
                                'echo \"<h1>AWS CloudFormation sample'
                                ' application for Amazon ElastiCache'
                                ' Redis Cluster</h1>\";\n',
                                '\n',
                                '$cluster_config = json_decode('
                                'file_get_contents(\'/tmp/cacheclusterconfig\''
                                '), true);\n',
                                '$endpoint = $cluster_config[\'CacheClusters'
                                '\'][0][\'CacheNodes\'][0][\'Endpoint\'][\'Add'
                                'ress\'];\n',
                                '$port = $cluster_config[\'CacheClusters\'][0]'
                                '[\'CacheNodes\'][0][\'Endpoint\'][\'Port\'];'
                                '\n',
                                '\n',
                                'echo \"<p>Connecting to Redis Cache Cluster '
                                'node \'{$endpoint}\' on port {$port}</p>\";'
                                '\n',
                                '\n',
                                '$redis=new Redis();\n',
                                '$redis->connect($endpoint, $port);\n',
                                '$redis->set(\'testkey\', \'Hello World!\');'
                                '\n',
                                '$return = $redis->get(\'testkey\');\n',
                                '\n',
                                'echo \"<p>Retrieved value: $return</p>\";'
                                '\n',
                                '?>\n'
                                ]),
                            mode='000644',
                            owner='apache',
                            group='apache'
                            ),
                        '/etc/cron.d/get_cluster_config':
                            cloudformation.InitFile(
                                content='*/5 * * * * root'
                                        ' /usr/local/bin/get_cluster_config',
                                mode='000644',
                                owner='root',
                                group='root'
                                ),
                        '/usr/local/bin/get_cluster_config':
                            cloudformation.InitFile(
                                content=Join('', [
                                    '#! /bin/bash\n',
                                    'aws elasticache describe-cache-clusters ',
                                    '         --cache-cluster-id ',
                                    Ref('RedisCluster'),
                                    '         --show-cache-node-info'
                                    ' --region ', Ref('AWS::Region'),
                                    ' > /tmp/cacheclusterconfig\n'
                                    ]),
                                mode='000755',
                                owner='root',
                                group='root'
                                ),
                        '/usr/local/bin/install_phpredis':
                            cloudformation.InitFile(
                                content=Join('', [
                                    '#! /bin/bash\n',
                                    'cd /tmp\n',
                                    'wget https://github.com/nicolasff/'
                                    'phpredis/zipball/master -O phpredis.zip'
                                    '\n',
                                    'unzip phpredis.zip\n',
                                    'cd nicolasff-phpredis-*\n',
                                    'phpize\n',
                                    './configure\n',
                                    'make && make install\n',
                                    'touch /etc/php.d/redis.ini\n',
                                    'echo extension=redis.so > /etc/php.d/'
                                    'redis.ini\n'
                                    ]),
                                mode='000755',
                                owner='root',
                                group='root'
                                ),
                        '/etc/cfn/cfn-hup.conf': cloudformation.InitFile(
                            content=Join('', [
                                '[main]\n',
                                'stack=', Ref('AWS::StackId'), '\n',
                                'region=', Ref('AWS::Region'), '\n'
                                ]),
                            mode='000400',
                            owner='root',
                            group='root'
                            ),
                        '/etc/cfn/hooks.d/cfn-auto-reloader.conf':
                            cloudformation.InitFile(
                                content=Join('', [
                                    '[cfn-auto-reloader-hook]\n',
                                    'triggers=post.update\n',
                                    'path=Resources.WebServerInstance.Metadata'
                                    '.AWS::CloudFormation::Init\n',
                                    'action=/opt/aws/bin/cfn-init -v ',
                                    '         --stack ', Ref('AWS::StackName'),
                                    '         --resource WebServerInstance ',
                                    '         --region ', Ref('AWS::Region'),
                                    '\n',
                                    'runas=root\n'
                                    ]),
                                # Why doesn't the Amazon template have this?
                                # mode='000400',
                                # owner='root',
                                # group='root'
                                ),
                        }),

                    commands={
                        '01-install_phpredis': {
                            'command': '/usr/local/bin/install_phpredis'
                            },
                        '02-get-cluster-config': {
                            'command': '/usr/local/bin/get_cluster_config'
                            }
                        },

                    services={
                        "sysvinit": cloudformation.InitServices({
                            "httpd": cloudformation.InitService(
                                enabled=True,
                                ensureRunning=True,
                                ),
                            "cfn-hup": cloudformation.InitService(
                                enabled=True,
                                ensureRunning=True,
                                files=['/etc/cfn/cfn-hup.conf',
                                       '/etc/cfn/hooks.d/'
                                       'cfn-auto-reloader.conf']
                                ),
                            }),
                        },
                    )
                })
            ),
        ImageId=FindInMap('AWSRegionArch2AMI', Ref('AWS::Region'),
                          FindInMap('AWSInstanceType2Arch',
                                    Ref(instancetype), 'Arch')),
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
            ])),
        CreationPolicy=CreationPolicy(
            ResourceSignal=ResourceSignal(Timeout='PT15M')
            ),
        Tags=Tags(Application=Ref('AWS::StackId'),
                  Details='Created using Troposhpere')
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

    template.add_resource(elasticache.CacheCluster(
        'RedisCluster',
        Engine='redis',
        CacheNodeType=Ref(cachenodetype),
        NumCacheNodes='1',
        CacheSecurityGroupNames=[Ref(redisclustersg)],
        ))

    # Outputs
    template.add_output([
        Output(
            'WebsiteURL',
            Description='Application URL',
            Value=Join('', [
                'http://',
                GetAtt(webserverinstance, 'PublicDnsName'),

                ])
            )
        ])

    # Print CloudFormation Template
    print(template.to_json())


if __name__ == '__main__':
    main()
