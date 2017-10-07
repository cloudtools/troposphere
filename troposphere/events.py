# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty


class EcsParameters(AWSProperty):
    props = {
        "TaskCount": (int, False),
        "TaskDefinitionArn": (basestring, True),
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


class Target(AWSProperty):
    props = {
        'Arn': (basestring, True),
        "EcsParameters": (EcsParameters, False),
        'Id': (basestring, True),
        'Input': (basestring, False),
        'InputPath': (basestring, False),
        'InputTransformer': (InputTransformer, False),
        'KinesisParameters': (KinesisParameters, False),
        'RoleArn': (basestring, False),
        'RunCommandParameters': (RunCommandParameters, False),
    }


class Rule(AWSObject):
    resource_type = "AWS::Events::Rule"

    props = {

        'Description': (basestring, False),
        'EventPattern': (dict, False),
        'Name': (basestring, False),
        'ScheduleExpression': (basestring, False),
        'State': (basestring, False),
        'Targets': ([Target], False),
    }
