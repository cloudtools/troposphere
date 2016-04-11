#!/usr/bin/env python
"""
Converted from AutoScalingMultiAZWithNotifications.template located at:
http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

XXX In addition to troposphere, this script requires awacs (Amazon Web Access
Control Subsystem)
"""
from __future__ import absolute_import, division, print_function

from awacs.aws import (
    Allow,
    Statement,
    Principal,
    Policy,
    )
from awacs.sts import AssumeRole

from troposphere import (
    autoscaling,
    Base64,
    cloudformation,
    cloudwatch,
    constants,
    ec2,
    FindInMap,
    GetAtt,
    GetAZs,
    Join,
    Parameter,
    Output,
    Ref,
    sns,
    Tags,
    Template,
    )
import troposphere.elasticloadbalancing as elb
# from troposphere.autoscaling import (
#     AutoScalingGroup,
#     BlockDeviceMapping,
#     EBSBlockDevice,
#     LaunchConfiguration,
#     Tag,
#     )
from troposphere.policies import (
    AutoScalingRollingUpdate,
    CreationPolicy,
    ResourceSignal,
    UpdatePolicy,
    )

def main():
    """
    Create a multi-az, load balanced and Auto Scaled sample web site
    """

    template = Template()

    template.add_version("2010-09-09")

    # Description
    template.add_description(
        'AWS CloudFormation Sample Template AutoScalingMultiAZWithNotifications: '
        'Create a multi-az, load balanced and Auto Scaled sample web site '
        'running on an Apache Web Serever. The application is configured to '
        'span all Availability Zones in the region and is Auto-Scaled based on '
        'the CPU utilization of the web servers. Notifications will be sent to '
        'the operator email address on scaling events. The instances are load '
        'balanced with a simple health check against the default web page. '
        '**WARNING** This template creates one or more Amazon EC2 instances and '
        'an Elastic Load Balancer. You will be billed for the AWS resources '
        'used if you create a stack from this template.'
        )


    # Mappings
    template.add_mapping(
        'AWSInstanceType2Arch', {
            "t1.micro"    :{"Arch" : "PV64"},
            "t2.nano"     :{"Arch" : "HVM64"},
            "t2.micro"    :{"Arch" : "HVM64"},
            "t2.small"    :{"Arch" : "HVM64"},
            "t2.medium"   :{"Arch" : "HVM64"},
            "t2.large"    :{"Arch" : "HVM64"},
            "m1.small"    :{"Arch" : "PV64"},
            "m1.medium"   :{"Arch" : "PV64"},
            "m1.large"    :{"Arch" : "PV64"},
            "m1.xlarge"   :{"Arch" : "PV64"},
            "m2.xlarge"   :{"Arch" : "PV64"},
            "m2.2xlarge"  :{"Arch" : "PV64"},
            "m2.4xlarge"  :{"Arch" : "PV64"},
            "m3.medium"   :{"Arch" : "HVM64"},
            "m3.large"    :{"Arch" : "HVM64"},
            "m3.xlarge"   :{"Arch" : "HVM64"},
            "m3.2xlarge"  :{"Arch" : "HVM64"},
            "m4.large"    :{"Arch" : "HVM64"},
            "m4.xlarge"   :{"Arch" : "HVM64"},
            "m4.2xlarge"  :{"Arch" : "HVM64"},
            "m4.4xlarge"  :{"Arch" : "HVM64"},
            "m4.10xlarge" :{"Arch" : "HVM64"},
            "c1.medium"   :{"Arch" : "PV64"},
            "c1.xlarge"   :{"Arch" : "PV64"},
            "c3.large"    :{"Arch" : "HVM64"},
            "c3.xlarge"   :{"Arch" : "HVM64"},
            "c3.2xlarge"  :{"Arch" : "HVM64"},
            "c3.4xlarge"  :{"Arch" : "HVM64"},
            "c3.8xlarge"  :{"Arch" : "HVM64"},
            "c4.large"    :{"Arch" : "HVM64"},
            "c4.xlarge"   :{"Arch" : "HVM64"},
            "c4.2xlarge"  :{"Arch" : "HVM64"},
            "c4.4xlarge"  :{"Arch" : "HVM64"},
            "c4.8xlarge"  :{"Arch" : "HVM64"},
            "g2.2xlarge"  :{"Arch" : "HVMG2"},
            "g2.8xlarge"  :{"Arch" : "HVMG2"},
            "r3.large"    :{"Arch" : "HVM64"},
            "r3.xlarge"   :{"Arch" : "HVM64"},
            "r3.2xlarge"  :{"Arch" : "HVM64"},
            "r3.4xlarge"  :{"Arch" : "HVM64"},
            "r3.8xlarge"  :{"Arch" : "HVM64"},
            "i2.xlarge"   :{"Arch" : "HVM64"},
            "i2.2xlarge"  :{"Arch" : "HVM64"},
            "i2.4xlarge"  :{"Arch" : "HVM64"},
            "i2.8xlarge"  :{"Arch" : "HVM64"},
            "d2.xlarge"   :{"Arch" : "HVM64"},
            "d2.2xlarge"  :{"Arch" : "HVM64"},
            "d2.4xlarge"  :{"Arch" : "HVM64"},
            "d2.8xlarge"  :{"Arch" : "HVM64"},
            "hi1.4xlarge" :{"Arch" : "HVM64"},
            "hs1.8xlarge" :{"Arch" : "HVM64"},
            "cr1.8xlarge" :{"Arch" : "HVM64"},
            "cc2.8xlarge" :{"Arch" : "HVM64"},
            }
        )

    template.add_mapping(
        "AWSInstanceType2NATArch", {
            "t1.micro"    :{"Arch" : "NATPV64"},
            "t2.nano"     :{"Arch" : "NATHVM64"},
            "t2.micro"    :{"Arch" : "NATHVM64"},
            "t2.small"    :{"Arch" : "NATHVM64"},
            "t2.medium"   :{"Arch" : "NATHVM64"},
            "t2.large"    :{"Arch" : "NATHVM64"},
            "m1.small"    :{"Arch" : "NATPV64"},
            "m1.medium"   :{"Arch" : "NATPV64"},
            "m1.large"    :{"Arch" : "NATPV64"},
            "m1.xlarge"   :{"Arch" : "NATPV64"},
            "m2.xlarge"   :{"Arch" : "NATPV64"},
            "m2.2xlarge"  :{"Arch" : "NATPV64"},
            "m2.4xlarge"  :{"Arch" : "NATPV64"},
            "m3.medium"   :{"Arch" : "NATHVM64"},
            "m3.large"    :{"Arch" : "NATHVM64"},
            "m3.xlarge"   :{"Arch" : "NATHVM64"},
            "m3.2xlarge"  :{"Arch" : "NATHVM64"},
            "m4.large"    :{"Arch" : "NATHVM64"},
            "m4.xlarge"   :{"Arch" : "NATHVM64"},
            "m4.2xlarge"  :{"Arch" : "NATHVM64"},
            "m4.4xlarge"  :{"Arch" : "NATHVM64"},
            "m4.10xlarge" :{"Arch" : "NATHVM64"},
            "c1.medium"   :{"Arch" : "NATPV64"},
            "c1.xlarge"   :{"Arch" : "NATPV64"},
            "c3.large"    :{"Arch" : "NATHVM64"},
            "c3.xlarge"   :{"Arch" : "NATHVM64"},
            "c3.2xlarge"  :{"Arch" : "NATHVM64"},
            "c3.4xlarge"  :{"Arch" : "NATHVM64"},
            "c3.8xlarge"  :{"Arch" : "NATHVM64"},
            "c4.large"    :{"Arch" : "NATHVM64"},
            "c4.xlarge"   :{"Arch" : "NATHVM64"},
            "c4.2xlarge"  :{"Arch" : "NATHVM64"},
            "c4.4xlarge"  :{"Arch" : "NATHVM64"},
            "c4.8xlarge"  :{"Arch" : "NATHVM64"},
            "g2.2xlarge"  :{"Arch" : "NATHVMG2"},
            "g2.8xlarge"  :{"Arch" : "NATHVMG2"},
            "r3.large"    :{"Arch" : "NATHVM64"},
            "r3.xlarge"   :{"Arch" : "NATHVM64"},
            "r3.2xlarge"  :{"Arch" : "NATHVM64"},
            "r3.4xlarge"  :{"Arch" : "NATHVM64"},
            "r3.8xlarge"  :{"Arch" : "NATHVM64"},
            "i2.xlarge"   :{"Arch" : "NATHVM64"},
            "i2.2xlarge"  :{"Arch" : "NATHVM64"},
            "i2.4xlarge"  :{"Arch" : "NATHVM64"},
            "i2.8xlarge"  :{"Arch" : "NATHVM64"},
            "d2.xlarge"   :{"Arch" : "NATHVM64"},
            "d2.2xlarge"  :{"Arch" : "NATHVM64"},
            "d2.4xlarge"  :{"Arch" : "NATHVM64"},
            "d2.8xlarge"  :{"Arch" : "NATHVM64"},
            "hi1.4xlarge" :{"Arch" : "NATHVM64"},
            "hs1.8xlarge" :{"Arch" : "NATHVM64"},
            "cr1.8xlarge" :{"Arch" : "NATHVM64"},
            "cc2.8xlarge" :{"Arch" : "NATHVM64"},
            }
        )

    template.add_mapping(
        "AWSRegionArch2AMI", {
            "us-east-1"      :{"PV64" : "ami-22111148", "HVM64" : "ami-08111162", "HVMG2" : "ami-ebcec381"},
            "us-west-2"      :{"PV64" : "ami-792bc219", "HVM64" : "ami-c229c0a2", "HVMG2" : "ami-0f28c06f"},
            "us-west-1"      :{"PV64" : "ami-0e087a6e", "HVM64" : "ami-1b0f7d7b", "HVMG2" : "ami-ab9defcb"},
            "eu-west-1"      :{"PV64" : "ami-a5368cd6", "HVM64" : "ami-31328842", "HVMG2" : "ami-d1d652a2"},
            "eu-central-1"   :{"PV64" : "ami-2bde3944", "HVM64" : "ami-e2df388d", "HVMG2" : "ami-5240a73d"},
            "ap-northeast-1" :{"PV64" : "ami-37020959", "HVM64" : "ami-f80e0596", "HVMG2" : "ami-34a9a35a"},
            "ap-northeast-2" :{"PV64" : "NOT_SUPPORTED", "HVM64" : "ami-6598510b", "HVMG2" : "NOT_SUPPORTED"},
            "ap-southeast-1" :{"PV64" : "ami-ff0cc79c", "HVM64" : "ami-e90dc68a", "HVMG2" : "ami-6f6ca70c"},
            "ap-southeast-2" :{"PV64" : "ami-f5210196", "HVM64" : "ami-f2210191", "HVMG2" : "ami-88c1e1eb"},
            "sa-east-1"      :{"PV64" : "ami-661e930a", "HVM64" : "ami-1e159872", "HVMG2" : "NOT_SUPPORTED"},
            "cn-north-1"     :{"PV64" : "ami-08ef2465", "HVM64" : "ami-49e22924", "HVMG2" : "NOT_SUPPORTED"}
            }
        )

    template.add_mapping(
        "Region2Examples", {
            "us-east-1"     :{"Examples":"https://s3.amazonaws.com/cloudformation-examples-us-east-1"},
            "us-west-2"     :{"Examples":"https://s3-us-west-2.amazonaws.com/cloudformation-examples-us-west-2"},
            "us-west-1"     :{"Examples":"https://s3-us-west-1.amazonaws.com/cloudformation-examples-us-west-1"},
            "eu-west-1"     :{"Examples":"https://s3-eu-west-1.amazonaws.com/cloudformation-examples-eu-west-1"},
            "eu-central-1"  :{"Examples":"https://s3-eu-central-1.amazonaws.com/cloudformation-examples-eu-central-1"},
            "ap-southeast-1":{"Examples":"https://s3-ap-southeast-1.amazonaws.com/cloudformation-examples-ap-southeast-1"},
            "ap-northeast-1":{"Examples":"https://s3-ap-northeast-1.amazonaws.com/cloudformation-examples-ap-northeast-1"},
            "ap-northeast-2":{"Examples":"https://s3-ap-northeast-2.amazonaws.com/cloudformation-examples-ap-northeast-2"},
            "ap-southeast-2":{"Examples":"https://s3-ap-southeast-2.amazonaws.com/cloudformation-examples-ap-southeast-2"},
            "sa-east-1"     :{"Examples":"https://s3-sa-east-1.amazonaws.com/cloudformation-examples-sa-east-1"},
            "cn-north-1"    :{"Examples":"https://s3.cn-north-1.amazonaws.com.cn/cloudformation-examples-cn-north-1"}
            }
        )


    # Parameters

    allowedinstancetype = [
        "t1.micro",
        "t2.nano",
        "t2.micro",
        "t2.small",
        "t2.medium",
        "t2.large",
        "m1.small",
        "m1.medium",
        "m1.large",
        "m1.xlarge",
        "m2.xlarge",
        "m2.2xlarge",
        "m2.4xlarge",
        "m3.medium",
        "m3.large",
        "m3.xlarge",
        "m3.2xlarge",
        "m4.large",
        "m4.xlarge",
        "m4.2xlarge",
        "m4.4xlarge",
        "m4.10xlarge",
        "c1.medium",
        "c1.xlarge",
        "c3.large",
        "c3.xlarge",
        "c3.2xlarge",
        "c3.4xlarge",
        "c3.8xlarge",
        "c4.large",
        "c4.xlarge",
        "c4.2xlarge",
        "c4.4xlarge",
        "c4.8xlarge",
        "g2.2xlarge",
        "g2.8xlarge",
        "r3.large",
        "r3.xlarge",
        "r3.2xlarge",
        "r3.4xlarge",
        "r3.8xlarge",
        "i2.xlarge",
        "i2.2xlarge",
        "i2.4xlarge",
        "i2.8xlarge",
        "d2.xlarge",
        "d2.2xlarge",
        "d2.4xlarge",
        "d2.8xlarge",
        "hi1.4xlarge",
        "hs1.8xlarge",
        "cr1.8xlarge",
        "cc2.8xlarge",
        "cg1.4xlarge",
        ]

    instancetype = template.add_parameter(Parameter(
        'InstanceType',
        Description='WebServer EC2 instance type',
        Type='String',
        Default='t2.small',
        AllowedValues=allowedinstancetype,
        ConstraintDescription='must be a valid EC2 instance type.',
        ))

    keyname = template.add_parameter(Parameter(
        'KeyName',
        Description='The EC2 Key Pair to allow SSH access to the instances',
        Type='AWS::EC2::KeyPair::KeyName',
        ConstraintDescription='must be the name of an existing EC2 KeyPair.',
        ))

    operatoremail = template.add_parameter(Parameter(
        'OperatorEMail',
        AllowedPattern=(
            '([a-zA-Z0-9_\\-\\.]+)@((\\[[0-9]{1,3}\\.'
            '[0-9]{1,3}\\.[0-9]{1,3}\\.)|(([a-zA-Z0-9'
            '\\-]+\\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\\]?)'
            ),
        ConstraintDescription="must be a valid email address.",
        Description="EMail address to notify if there are any scaling operations",
        Type=constants.STRING,
        ))

    sshlocation = template.add_parameter(Parameter(
        'SSHLocation',
        Description='The IP address range that can be used to SSH to'
                    ' the EC2 instances',
        Type='String',
        MinLength='9',
        MaxLength='18',
        Default='0.0.0.0/0',
        AllowedPattern=(
            '(\\d{1,3})\\.(\\d{1,3})\\.'
            '(\\d{1,3})\\.(\\d{1,3})/(\\d{1,2})'
            ),
        ConstraintDescription='must be a valid IP CIDR range of the'
                              ' form x.x.x.x/x.'
        ))

    # XXX Resources

    cpualarmhigh = template.add_resource(
        cloudwatch.Alarm(
            'CPUAlarmHigh',
            # XXX
            AlarmActions=[Ref('WebServerScaleUpPolicy')],
            AlarmDescription='Scale-up if CPU > 90% for 10 minutes',
            ComparisonOperator='GreaterThanThreshold',
            Dimensions=[cloudwatch.MetricDimension(
                Name='AutoScalingGroupName',
                # XXX
                Value=Ref('WebServerGroup'),
                )],
            EvaluationPeriods='2',
            MetricName='CPUUtilization',
            Namespace='AWS/EC2',
            Period='300',
            Statistic='Average',
            Threshold='90',
            )
        )

    cpualarmlow = template.add_resource(
        cloudwatch.Alarm(
            'CPUAlarmLow',
            # XXX
            AlarmActions=[Ref('WebServerScaleDownPolicy')],
            AlarmDescription='Scale-down if CPU < 70% for 10 minutes',
            ComparisonOperator='LessThanThreshold',
            Dimensions=[cloudwatch.MetricDimension(
                Name='AutoScalingGroupName',
                # XXX
                Value=Ref('WebServerGroup'),
                )],
            EvaluationPeriods='2',
            MetricName='CPUUtilization',
            Namespace='AWS/EC2',
            Period='300',
            Statistic='Average',
            Threshold='70',
            )
        )

    r_elb = template.add_resource(
        elb.LoadBalancer(
            'ElasticLoadBalancer',
            AvailabilityZones=GetAZs(''),
            CrossZone=True,
            HealthCheck=elb.HealthCheck(
                HealthyThreshold='3',
                Interval='30',
                Target='HTTP:80/',
                Timeout='5',
                UnhealthyThreshold='5',
                ),
            Listeners=[
                elb.Listener(
                    InstancePort='80',
                    LoadBalancerPort='80',
                    Protocol='HTTP',
                    )
                ],
            )
        )

    r_snstopic = template.add_resource(
        sns.Topic(
            'NotificationTopic',
            Subscription=[
                sns.Subscription(
                    'NotificationSubscription',
                    Endpoint=Ref(operatoremail),
                    Protocol='email',
                    )
                ]
            )
        )
    webservergroup = template.add_resource(autoscaling.AutoScalingGroup(
        'WebServerGroup',
        AvailabilityZones=GetAZs(''),
        CreationPolicy=CreationPolicy(
            ResourceSignal=ResourceSignal(
                Count='1',
                Timeout='PT15M',
                )
            ),
        LaunchConfigurationName=Ref('LaunchConfig'),
        LoadBalancerNames=[Ref('ElasticLoadBalancer')],
        MinSize='1',
        MaxSize='3',
        NotificationConfigurations=[
            # XXX Example isn't in a list but troposphere wont build unless it is a list
            autoscaling.NotificationConfigurations(
                NotificationTypes=[
                    "autoscaling:EC2_INSTANCE_LAUNCH",
                    "autoscaling:EC2_INSTANCE_LAUNCH_ERROR",
                    "autoscaling:EC2_INSTANCE_TERMINATE",
                    "autoscaling:EC2_INSTANCE_TERMINATE_ERROR"
                    ],
                TopicARN=Ref('NotificationTopic'),
                )
            ],
        UpdatePolicy=UpdatePolicy(
            AutoScalingRollingUpdate=AutoScalingRollingUpdate(
                PauseTime='PT15M',
                MinInstancesInService="1",
                MaxBatchSize='1',
                WaitOnResourceSignals=True
                )
            )
        ))

    webservscaleup_policy = template.add_resource(autoscaling.ScalingPolicy(
        "WebServerScaleUpPolicy",
        AdjustmentType='ChangeInCapacity',
        AutoScalingGroupName=Ref(webservergroup),
        Cooldown='60',
        ScalingAdjustment='1',
        ))

    webservscaledown_policy = template.add_resource(autoscaling.ScalingPolicy(
        "WebServerScaleDownPolicy",
        AdjustmentType='ChangeInCapacity',
        AutoScalingGroupName=Ref(webservergroup),
        Cooldown='60',
        ScalingAdjustment='-1',
        ))

    webserversg = template.add_resource(ec2.SecurityGroup(
        'InstanceSecurityGroup',
        GroupDescription='Enable SSH access and HTTP from the load balancer only',
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
                SourceSecurityGroupName=GetAtt(
                    'ElasticLoadBalancer',
                    'SourceSecurityGroup.GroupName',
                    ),
                SourceSecurityGroupOwnerId=GetAtt(
                    'ElasticLoadBalancer',
                    'SourceSecurityGroup.OwnerAlias',
                    ),
                )
            ]
        ))

    r_launchconfig = template.add_resource(
        autoscaling.LaunchConfiguration(
            'LaunchConfig',
            Metadata=cloudformation.Metadata(
                cloudformation.Init({
                    'config': cloudformation.InitConfig(
                        packages={
                            'yum': {
                                'httpd':     [],
                                }
                            },

                        files=cloudformation.InitFiles({
                            '/var/www/html/index.html': cloudformation.InitFile(
                                content=Join('\n', [
                                    "<img src=\"",
                                    FindInMap(
                                        'Region2Examples',
                                        Ref('AWS::Region'),
                                        'Examples',
                                        ),
                                    '/cloudformation_graphic.png\" alt=\"AWS CloudFormation Logo\"/>',
                                    '<h1>Congratulations, you have successfully launched the AWS CloudFormation sample.</h1>',
                                    ]),
                                mode='000644',
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
                                        'path=Resources.LaunchConfig.Metadata'
                                        '.AWS::CloudFormation::Init\n',
                                        'action=/opt/aws/bin/cfn-init -v ',
                                        '         --stack ', Ref('AWS::StackName'),
                                        '         --resource LaunchConfig ',
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
                        ),
                    }),
                cloudformation.Comment('Install a simple application'),
                ),
            # XXX How do I add the comment to the Metadata? Troposphere errors out
            ImageId=FindInMap('AWSRegionArch2AMI', Ref('AWS::Region'),
                              FindInMap('AWSInstanceType2Arch',
                                        Ref(instancetype), 'Arch')),
            InstanceType=Ref(instancetype),
            SecurityGroups=[Ref(webserversg)],
            KeyName=Ref(keyname),
            UserData=Base64(Join('', [
                '#!/bin/bash -xe\n',
                'yum update -y aws-cfn-bootstrap\n',

                '/opt/aws/bin/cfn-init -v ',
                '         --stack ', Ref('AWS::StackName'),
                '         --resource LaunchConfig ',
                '         --region ', Ref('AWS::Region'), '\n',

                '/opt/aws/bin/cfn-signal -e $? ',
                '         --stack ', Ref('AWS::StackName'),
                '         --resource WebServerGroup ',
                '         --region ', Ref('AWS::Region'), '\n'
                ])),
            #Tags=autoscaling.Tags(Application=Ref('AWS::StackId'),
            #          Details='Created using Troposhpere')
            ))

    # Outputs
    template.add_output([
        Output(
            'URL',
            Description='The URL of the website',
            # XXX
            Value=Join('', [
                'http://',
                GetAtt('ElasticLoadBalancer', 'DNSName'),
                ])
            )
        ])

    # Print CloudFormation Template
    print(template.to_json())


if __name__ == '__main__':
    main()
