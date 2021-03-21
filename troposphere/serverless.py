# Copyright (c) 2017, Fernando Freire <fernando.freire@nike.com>
# All rights reserved.
#
# See LICENSE file for full license.

import types

from . import AWSObject, AWSProperty
from .apigateway import AccessLogSetting, CanarySetting, MethodSetting
from .awslambda import (
    Environment, ProvisionedConcurrencyConfiguration, DestinationConfig
)
from .awslambda import VPCConfig, validate_memory_size
from .dynamodb import ProvisionedThroughput, SSESpecification
from .s3 import Filter
from .validators import (
    exactly_one, positive_integer, mutually_exclusive, integer_range
)


try:
    from awacs.aws import PolicyDocument

    policytypes = (dict, list, str, PolicyDocument)
except ImportError:
    policytypes = (dict, list, str)

assert types  # silence pyflakes


def primary_key_type_validator(x):
    valid_types = ["String", "Number", "Binary"]
    if x not in valid_types:
        raise ValueError("KeyType must be one of: %s" % ", ".join(valid_types))
    return x


class DeadLetterQueue(AWSProperty):
    props = {
        'Type': (str, False),
        'TargetArn': (str, False)
    }

    def validate(self):
        valid_types = ['SQS', 'SNS']
        if ('Type' in self.properties and
                self.properties['Type'] not in valid_types):
            raise ValueError('Type must be either SQS or SNS')


class S3Location(AWSProperty):
    props = {
        "Bucket": (str, True),
        "Key": (str, True),
        "Version": (str, False),
    }


class Hooks(AWSProperty):
    props = {
        "PreTraffic": (str, False),
        "PostTraffic": (str, False),
    }


class DeploymentPreference(AWSProperty):
    props = {
        "Type": (str, True),
        "Alarms": (list, False),
        "Hooks": (Hooks, False),
        "Enabled": (bool, False),
        "Role": (str, False),
    }


class Function(AWSObject):
    resource_type = "AWS::Serverless::Function"

    props = {
        'Handler': (str, True),
        'Runtime': (str, True),
        'CodeUri': ((S3Location, str), False),
        'InlineCode': (str, False),
        'FunctionName': (str, False),
        'Description': (str, False),
        'MemorySize': (validate_memory_size, False),
        'Timeout': (positive_integer, False),
        'Role': (str, False),
        'Policies': (policytypes, False),
        'Environment': (Environment, False),
        'VpcConfig': (VPCConfig, False),
        'Events': (dict, False),
        'Tags': (dict, False),
        'Tracing': (str, False),
        'KmsKeyArn': (str, False),
        'DeadLetterQueue': (DeadLetterQueue, False),
        'DeploymentPreference': (DeploymentPreference, False),
        'Layers': ([str], False),
        'AutoPublishAlias': (str, False),
        'ReservedConcurrentExecutions': (positive_integer, False),
        'ProvisionedConcurrencyConfig':
            (ProvisionedConcurrencyConfiguration, False),
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
        'Header': (str, False),
        'ValidationExpression': (str, False),
    }


class LambdaTokenAuthIdentity(AWSProperty):
    props = {
        'Header': (str, False),
        'ValidationExpression': (str, False),
        'ReauthorizeEvery': (str, False),
    }


class LambdaRequestAuthIdentity(AWSProperty):
    props = {
        'Headers': ([str], False),
        'QueryStrings': ([str], False),
        'StageVariables': ([str], False),
        'Context': ([str], False),
        'ReauthorizeEvery': (str, False),
    }


class CognitoAuth(AWSProperty):
    props = {
        'UserPoolArn': (str, False),
        'Identity': (CognitoAuthIdentity, False),
    }


class LambdaTokenAuth(AWSProperty):
    props = {
        'FunctionPayloadType': (str, False),
        'FunctionArn': (str, False),
        'FunctionInvokeRole': (str, False),
        'Identity': (LambdaTokenAuthIdentity, False),
    }


class LambdaRequestAuth(AWSProperty):
    props = {
        'FunctionPayloadType': (str, False),
        'FunctionArn': (str, False),
        'FunctionInvokeRole': (str, False),
        'Identity': (LambdaRequestAuthIdentity, False),
    }


class Authorizers(AWSProperty):
    props = {
        'DefaultAuthorizer': (str, False),
        'CognitoAuth': (CognitoAuth, False),
        'LambdaTokenAuth': (LambdaTokenAuth, False),
        'LambdaRequestAuth': (LambdaRequestAuth, False),
    }


class ResourcePolicyStatement(AWSProperty):
    props = {
        'AwsAccountBlacklist': (list, False),
        'AwsAccountWhitelist': (list, False),
        'CustomStatements': (list, False),
        'IpRangeBlacklist': (list, False),
        'IpRangeWhitelist': (list, False),
        'SourceVpcBlacklist': (list, False),
        'SourceVpcWhitelist': (list, False),
    }


class Auth(AWSProperty):
    props = {
        'AddDefaultAuthorizerToCorsPreflight': (bool, False),
        'ApiKeyRequired': (bool, False),
        'Authorizers': (Authorizers, False),
        'DefaultAuthorizer': (str, False),
        'InvokeRole': (str, False),
        'ResourcePolicy': (ResourcePolicyStatement, False),
    }


class Cors(AWSProperty):
    props = {
        'AllowCredentials': (str, False),
        'AllowHeaders': (str, False),
        'AllowMethods': (str, False),
        'AllowOrigin': (str, True),
        'MaxAge': (str, False),
    }


class Route53(AWSProperty):
    props = {
        'DistributionDomainName': (str, False),
        'EvaluateTargetHealth': (bool, False),
        'HostedZoneId': (str, False),
        'HostedZoneName': (str, False),
        'IpV6': (bool, False),
    }

    def validate(self):
        conds = [
            'HostedZoneId',
            'HostedZoneName',
        ]
        mutually_exclusive(self.__class__.__name__, self.properties, conds)


class Domain(AWSProperty):
    props = {
        'BasePath': (list, False),
        'CertificateArn': (str, True),
        'DomainName': (str, True),
        'EndpointConfiguration': (str, False),
        'Route53': (Route53, False),
    }

    def validate(self):
        valid_types = ['REGIONAL', 'EDGE']
        if ('EndpointConfiguration' in self.properties and
                self.properties['EndpointConfiguration'] not in valid_types):
            raise ValueError(
                'EndpointConfiguration must be either REGIONAL or EDGE'
            )


class EndpointConfiguration(AWSProperty):
    props = {
        "Type": (str, False),
        "VPCEndpointIds": (list, False)
    }

    def validate(self):
        valid_types = ["REGIONAL", "EDGE", "PRIVATE"]
        if (
            "Type" in self.properties
            and self.properties["Type"]
            not in valid_types
        ):
            raise ValueError(
                "EndpointConfiguration Type must be REGIONAL, EDGE or PRIVATE"
            )


class Api(AWSObject):
    resource_type = "AWS::Serverless::Api"

    props = {
        'AccessLogSetting': (AccessLogSetting, False),
        'Auth': (Auth, False),
        'BinaryMediaTypes': ([str], False),
        'CacheClusterEnabled': (bool, False),
        'CacheClusterSize': (str, False),
        'CanarySetting': (CanarySetting, False),
        'Cors': ((str, Cors), False),
        'DefinitionBody': (dict, False),
        'DefinitionUri': (str, False),
        'Domain': (Domain, False),
        'EndpointConfiguration': (EndpointConfiguration, False),
        'MethodSettings': ([MethodSetting], False),
        'Name': (str, False),
        'OpenApiVersion': (str, False),
        'StageName': (str, True),
        "TracingEnabled": (bool, False),
        'Variables': (dict, False),
    }

    def validate(self):
        conds = [
            'DefinitionBody',
            'DefinitionUri',
        ]
        mutually_exclusive(self.__class__.__name__, self.properties, conds)


class PrimaryKey(AWSProperty):
    props = {
        'Name': (str, False),
        'Type': (primary_key_type_validator, False)
    }


class SimpleTable(AWSObject):
    resource_type = "AWS::Serverless::SimpleTable"

    props = {
        'PrimaryKey': (PrimaryKey, False),
        'ProvisionedThroughput': (ProvisionedThroughput, False),
        'SSESpecification': (SSESpecification, False),
        'Tags': (dict, False),
        'TableName': (str, False),
    }


class LayerVersion(AWSObject):
    resource_type = "AWS::Serverless::LayerVersion"

    props = {
        'CompatibleRuntimes': ([str], False),
        'ContentUri': ((S3Location, str), True),
        'Description': (str, False),
        'LayerName': (str, False),
        'LicenseInfo': (str, False),
        'RetentionPolicy': (str, False),
    }


class S3Event(AWSObject):
    resource_type = 'S3'

    props = {
        'Bucket': (str, True),
        'Events': (list, True),
        'Filter': (Filter, False)
    }


class SNSEvent(AWSObject):
    resource_type = 'SNS'

    props = {
        'Topic': (str, True)
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
        'Stream': (str, True),
        'StartingPosition': (starting_position_validator, True),
        'BatchSize': (positive_integer, False),
        'BisectBatchOnFunctionError': (bool, False),
        'DestinationConfig': (DestinationConfig, False),
        'Enabled': (bool, False),
        'MaximumBatchingWindowInSeconds': (positive_integer, False),
        'MaximumRecordAgeInSeconds': (integer_range(60, 604800), False),
        'MaximumRetryAttempts': (positive_integer, False),
        'ParallelizationFactor': (integer_range(1, 10), False)
    }


class DynamoDBEvent(AWSObject):
    resource_type = 'DynamoDB'

    props = {
        'Stream': (str, True),
        'StartingPosition': (starting_position_validator, True),
        'BatchSize': (positive_integer, False)
    }


class RequestModel(AWSProperty):
    props = {
        'Model': (str, True),
        'Required': (bool, False)
    }


class ApiEvent(AWSObject):
    resource_type = 'Api'

    props = {
        'Auth': (Auth, False),
        'Path': (str, True),
        'Method': (str, True),
        'RequestModel': (RequestModel, False),
        'RequestParameters': (str, False),
        'RestApiId': (str, False)
    }


class ScheduleEvent(AWSObject):
    resource_type = 'Schedule'

    props = {
        'Schedule': (str, True),
        'Input': (str, False),
        'Description': (str, False),
        'Enabled': (bool, False),
        'Name': (str, False)
    }


class CloudWatchEvent(AWSObject):
    resource_type = 'CloudWatchEvent'

    props = {
        'Pattern': (dict, True),
        'Input': (str, False),
        'InputPath': (str, False)
    }


class IoTRuleEvent(AWSObject):
    resource_type = 'IoTRule'

    props = {
        'Sql': (str, True),
        'AwsIotSqlVersion': (str, False)
    }


class AlexaSkillEvent(AWSObject):
    resource_type = 'AlexaSkill'
    props = {}


class SQSEvent(AWSObject):
    resource_type = 'SQS'

    props = {
        'Queue': (str, True),
        'BatchSize': (positive_integer, True)
    }

    def validate(self):
        if (not 1 <= self.properties['BatchSize'] <= 10):
            raise ValueError('BatchSize must be between 1 and 10')


class ApplicationLocation(AWSProperty):
    props = {
        "ApplicationId": (str, True),
        "SemanticVersion": (str, True),
    }


class Application(AWSObject):
    resource_type = "AWS::Serverless::Application"

    props = {
        'Location': ((ApplicationLocation, str), True),
        'NotificationARNs': ([str], False),
        'Parameters': (dict, False),
        'Tags': (dict, False),
        'TimeoutInMinutes': (positive_integer, False),
    }

    def validate(self):
        conds = [
            'DefinitionBody',
            'DefinitionUri',
        ]
        mutually_exclusive(self.__class__.__name__, self.properties, conds)
