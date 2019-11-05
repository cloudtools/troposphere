# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import AWSObject
from . import AWSProperty
from .validators import integer


class Condition(AWSProperty):
    props = {
        'Key': (basestring, False),
        'Type': (basestring, False),
        'Value': (basestring, False),
    }


class EventBus(AWSObject):
    resource_type = "AWS::Events::EventBus"

    props = {
        'EventSourceName': (basestring, False),
        'Name': (basestring, True)
    }


class EventBusPolicy(AWSObject):
    resource_type = "AWS::Events::EventBusPolicy"

    props = {
        'Action': (basestring, True),
        'Condition': (Condition, False),
        'EventBusName': (basestring, False),
        'Principal': (basestring, True),
        'StatementId': (basestring, True),
    }


class AwsVpcConfiguration(AWSProperty):
    props = {
        'AssignPublicIp': (basestring, False),
        'SecurityGroups': ([basestring], False),
        'Subnets': ([basestring], True),
    }


class NetworkConfiguration(AWSProperty):
    props = {
        'AwsVpcConfiguration': (AwsVpcConfiguration, False),
    }


class EcsParameters(AWSProperty):
    props = {
        'Group': (basestring, False),
        'LaunchType': (basestring, False),
        'NetworkConfiguration': (NetworkConfiguration, False),
        'PlatformVersion': (basestring, False),
        'TaskCount': (integer, False),
        'TaskDefinitionArn': (basestring, True),
    }


class InputTransformer(AWSProperty):
    props = {
        'InputPathsMap': (dict, False),
        'InputTemplate': (basestring, True),
    }


class KinesisParameters(AWSProperty):
    props = {
        'PartitionKeyPath': (basestring, True),
    }


class RunCommandTarget(AWSProperty):
    props = {
        'Key': (basestring, True),
        'Values': ([basestring], True),
    }


class RunCommandParameters(AWSProperty):
    props = {
        'RunCommandTargets': ([RunCommandTarget], True),
    }


class SqsParameters(AWSProperty):
    props = {
        'MessageGroupId': (basestring, True),
    }


class Target(AWSProperty):
    props = {
        'Arn': (basestring, True),
        'EcsParameters': (EcsParameters, False),
        'Id': (basestring, True),
        'Input': (basestring, False),
        'InputPath': (basestring, False),
        'InputTransformer': (InputTransformer, False),
        'KinesisParameters': (KinesisParameters, False),
        'RoleArn': (basestring, False),
        'RunCommandParameters': (RunCommandParameters, False),
        'SqsParameters': (SqsParameters, False),
    }


class Rule(AWSObject):
    resource_type = "AWS::Events::Rule"

    props = {
        'Description': (basestring, False),
        'EventBusName': (basestring, False),
        'EventPattern': (dict, False),
        'Name': (basestring, False),
        'RoleArn': (basestring, False),
        'ScheduleExpression': (basestring, False),
        'State': (basestring, False),
        'Targets': ([Target], False),
    }
