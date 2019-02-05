# Copyright (c) 2017, Fernando Freire <fernando.freire@nike.com>
# All rights reserved.
#
# See LICENSE file for full license.

import types

from . import AWSObject, AWSProperty
from .apigateway import AccessLogSetting, CanarySetting, MethodSetting
from .awslambda import Environment, VPCConfig, validate_memory_size
from .dynamodb import ProvisionedThroughput, SSESpecification
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
        "Version": (basestring, False),
    }


class Hooks(AWSProperty):
    props = {
        "PreTraffic": (basestring, False),
        "PostTraffic": (basestring, False),
    }


class DeploymentPreference(AWSProperty):
    props = {
        "Type": (basestring, True),
        "Alarms": (list, False),
        "Hooks": (Hooks, False),
        "Enabled": (bool, False),
    }


class Function(AWSObject):
    resource_type = "AWS::Serverless::Function"

    props = {
        'Handler': (basestring, True),
        'Runtime': (basestring, True),
        'CodeUri': ((S3Location, basestring), False),
        'InlineCode': (basestring, False),
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
        'DeploymentPreference': (DeploymentPreference, False),
        'Layers': ([basestring], False),
        'AutoPublishAlias': (basestring, False),
        'ReservedConcurrentExecutions': (positive_integer, False),
    }

    def validate(self):
        conds = [
            'CodeUri',
            'InlineCode',
        ]
        exactly_one(self.__class__.__name__, self.properties, conds)


class FunctionForPackaging(Function):
    """Render Function without requiring 'CodeUri'.

    This exception to the Function spec is for use with the
    `cloudformation/sam package` commands which add CodeUri automatically.
    """

    resource_type = Function.resource_type
    props = Function.props.copy()
    props['CodeUri'] = (props['CodeUri'][0], False)

    def validate(self):
        pass


class CognitoAuthIdentity(AWSProperty):
    props = {
        'Header': (basestring, False),
        'ValidationExpression': (basestring, False),
    }


class LambdaTokenAuthIdentity(AWSProperty):
    props = {
        'Header': (basestring, False),
        'ValidationExpression': (basestring, False),
        'ReauthorizeEvery': (basestring, False),
    }


class LambdaRequestAuthIdentity(AWSProperty):
    props = {
        'Headers': ([basestring], False),
        'QueryStrings': ([basestring], False),
        'StageVariables': ([basestring], False),
        'Context': ([basestring], False),
        'ReauthorizeEvery': (basestring, False),
    }


class CognitoAuth(AWSProperty):
    props = {
        'UserPoolArn': (basestring, False),
        'Identity': (CognitoAuthIdentity, False),
    }


class LambdaTokenAuth(AWSProperty):
    props = {
        'FunctionPayloadType': (basestring, False),
        'FunctionArn': (basestring, False),
        'FunctionInvokeRole': (basestring, False),
        'Identity': (LambdaTokenAuthIdentity, False),
    }


class LambdaRequestAuth(AWSProperty):
    props = {
        'FunctionPayloadType': (basestring, False),
        'FunctionArn': (basestring, False),
        'FunctionInvokeRole': (basestring, False),
        'Identity': (LambdaRequestAuthIdentity, False),
    }


class Authorizers(AWSProperty):
    props = {
        'DefaultAuthorizer': (basestring, False),
        'CognitoAuth': (CognitoAuth, False),
        'LambdaTokenAuth': (LambdaTokenAuth, False),
        'LambdaRequestAuth': (LambdaRequestAuth, False),
    }


class Auth(AWSProperty):
    props = {
        'DefaultAuthorizer': (basestring, False),
        'Authorizers': (Authorizers, False),
    }


class Cors(AWSProperty):
    props = {
        'AllowCredentials': (basestring, False),
        'AllowHeaders': (basestring, False),
        'AllowMethods': (basestring, False),
        'AllowOrigin': (basestring, True),
        'MaxAge': (basestring, False),
    }


class Api(AWSObject):
    resource_type = "AWS::Serverless::Api"

    props = {
        'AccessLogSetting': (AccessLogSetting, False),
        'Auth': (Auth, False),
        'BinaryMediaTypes': ([basestring], False),
        'CacheClusterEnabled': (bool, False),
        'CacheClusterSize': (basestring, False),
        'CanarySetting': (CanarySetting, False),
        'Cors': ((basestring, Cors), False),
        'DefinitionBody': (dict, False),
        'DefinitionUri': (basestring, False),
        'EndpointConfiguration': (basestring, False),
        'MethodSetting': (MethodSetting, False),
        'Name': (basestring, False),
        'StageName': (basestring, True),
        "TracingEnabled": (bool, False),
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
        'ProvisionedThroughput': (ProvisionedThroughput, False),
        'SSESpecification': (SSESpecification, False),
        'Tags': (dict, False),
        'TableName': (basestring, False),
    }


class LayerVersion(AWSObject):
    resource_type = "AWS::Serverless::LayerVersion"

    props = {
        'CompatibleRuntimes': ([basestring], False),
        'ContentUri': ((S3Location, basestring), True),
        'Description': (basestring, False),
        'LayerName': (basestring, False),
        'LicenseInfo': (basestring, False),
        'RetentionPolicy': (basestring, False),
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


class SQSEvent(AWSObject):
    resource_type = 'SQS'

    props = {
        'Queue': (basestring, True),
        'BatchSize': (positive_integer, True)
    }

    def validate(self):
        if (not 1 <= self.properties['BatchSize'] <= 10):
            raise ValueError('BatchSize must be between 1 and 10')
