# Copyright (c) 2017, Fernando Freire <fernando.freire@nike.com>
# All rights reserved.
#
# See LICENSE file for full license.

import types

from . import AWSObject, AWSProperty
from .awslambda import Environment, VPCConfig, validate_memory_size
from .dynamodb import ProvisionedThroughput
from .s3 import Filter
from .validators import exactly_one, positive_integer
try:
    from awacs.aws import PolicyDocument
    policytypes = (dict, list, basestring, PolicyDocument)
except ImportError:
    policytypes = (dict, list, basestring)

assert types  # silence pyflakes


def primary_key_type_validator(x):
    valid_types = ["String", "Number", "Binary"]
    if x not in valid_types:
        raise ValueError("KeyType must be one of: %s" % ", ".join(valid_types))
    return x


class DeadLetterQueue(AWSProperty):
    props = {
        'Type': (basestring, False),
        'TargetArn': (basestring, False)
    }

    def validate(self):
        valid_types = ['SQS', 'SNS']
        if ('Type' in self.properties and
                self.properties['Type'] not in valid_types):
            raise ValueError('Type must be either SQS or SNS')


class S3Location(AWSProperty):
    props = {
        "Bucket": (basestring, True),
        "Key": (basestring, True),
        "Version": (basestring, False)
    }


class Function(AWSObject):
    resource_type = "AWS::Serverless::Function"

    props = {
        'Handler': (basestring, True),
        'Runtime': (basestring, True),
        'CodeUri': ((S3Location, basestring), True),
        'FunctionName': (basestring, False),
        'Description': (basestring, False),
        'MemorySize': (validate_memory_size, False),
        'Timeout': (positive_integer, False),
        'Role': (basestring, False),
        'Policies': (policytypes, False),
        'Environment': (Environment, False),
        'VpcConfig': (VPCConfig, False),
        'Events': (dict, False),
        'Tags': (dict, False),
        'Tracing': (basestring, False),
        'KmsKeyArn': (basestring, False),
        'DeadLetterQueue': (DeadLetterQueue, False),
        'AutoPublishAlias': (basestring, False)
    }


class FunctionForPackaging(Function):
    """Render Function without requiring 'CodeUri'.

    This exception to the Function spec is for use with the
    `cloudformation/sam package` commands which add CodeUri automatically.
    """

    resource_type = Function.resource_type
    props = Function.props.copy()
    props['CodeUri'] = (props['CodeUri'][0], False)


class Api(AWSObject):
    resource_type = "AWS::Serverless::Api"

    props = {
        'StageName': (basestring, True),
        'DefinitionBody': (dict, False),
        'DefinitionUri': (basestring, False),
        'CacheClusterEnabled': (bool, False),
        'CacheClusterSize': (basestring, False),
        'Variables': (dict, False),
    }

    def validate(self):
        conds = [
            'DefinitionBody',
            'DefinitionUri',
        ]
        exactly_one(self.__class__.__name__, self.properties, conds)


class PrimaryKey(AWSProperty):
    props = {
        'Name': (basestring, False),
        'Type': (primary_key_type_validator, False)
    }


class SimpleTable(AWSObject):
    resource_type = "AWS::Serverless::SimpleTable"

    props = {
        'PrimaryKey': (PrimaryKey, False),
        'ProvisionedThroughput': (ProvisionedThroughput, False)
    }


class S3Event(AWSObject):
    resource_type = 'S3'

    props = {
        'Bucket': (basestring, True),
        'Events': (list, True),
        'Filter': (Filter, False)
    }


class SNSEvent(AWSObject):
    resource_type = 'SNS'

    props = {
        'Topic': (basestring, True)
    }


def starting_position_validator(x):
    valid_types = ['TRIM_HORIZON', 'LATEST']
    if x not in valid_types:
        raise ValueError(
            "StartingPosition must be one of: %s"
            % ", ".join(valid_types)
        )
    return x


class KinesisEvent(AWSObject):
    resource_type = 'Kinesis'

    props = {
        'Stream': (basestring, True),
        'StartingPosition': (starting_position_validator, True),
        'BatchSize': (positive_integer, False)
    }


class DynamoDBEvent(AWSObject):
    resource_type = 'DynamoDB'

    props = {
        'Stream': (basestring, True),
        'StartingPosition': (starting_position_validator, True),
        'BatchSize': (positive_integer, False)
    }


class ApiEvent(AWSObject):
    resource_type = 'Api'

    props = {
        'Path': (basestring, True),
        'Method': (basestring, True),
        'RestApiId': (basestring, False)
    }


class ScheduleEvent(AWSObject):
    resource_type = 'Schedule'

    props = {
        'Schedule': (basestring, True),
        'Input': (basestring, False)
    }


class CloudWatchEvent(AWSObject):
    resource_type = 'CloudWatchEvent'

    props = {
        'Pattern': (dict, True),
        'Input': (basestring, False),
        'InputPath': (basestring, False)
    }


class IoTRuleEvent(AWSObject):
    resource_type = 'IoTRule'

    props = {
        'Sql': (basestring, True),
        'AwsIotSqlVersion': (basestring, False)
    }


class AlexaSkillEvent(AWSObject):
    resource_type = 'AlexaSkill'
    props = {}
