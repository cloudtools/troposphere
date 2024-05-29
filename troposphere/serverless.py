# Copyright (c) 2017-2022, Fernando Freire <fernando.freire@nike.com>
# All rights reserved.
#
# See LICENSE file for full license.

import types
from typing import Tuple, Type

from . import AWSHelperFn, AWSObject, AWSProperty, PropsDictType
from .apigateway import AccessLogSetting, CanarySetting, MethodSetting
from .apigatewayv2 import AccessLogSettings, RouteSettings
from .awslambda import (
    Cors,
    DestinationConfig,
    Environment,
    EphemeralStorage,
    FileSystemConfig,
    FilterCriteria,
    ImageConfig,
    ProvisionedConcurrencyConfiguration,
    RuntimeManagementConfig,
    SnapStart,
    SourceAccessConfiguration,
    VPCConfig,
    validate_memory_size,
    validate_package_type,
)
from .dynamodb import ProvisionedThroughput, SSESpecification
from .s3 import Filter
from .stepfunctions import LoggingConfiguration, TracingConfiguration
from .validators import (
    boolean,
    double,
    exactly_one,
    integer,
    integer_range,
    mutually_exclusive,
    positive_integer,
)

try:
    from awacs.aws import PolicyDocument

    policytypes: Tuple[Type, ...] = (dict, list, str, PolicyDocument)
except ImportError:
    policytypes = (dict, list, str)

assert types  # silence pyflakes


SERVERLESS_TRANSFORM = "AWS::Serverless-2016-10-31"


def primary_key_type_validator(x):
    valid_types = ["String", "Number", "Binary"]
    if x not in valid_types:
        raise ValueError("KeyType must be one of: %s" % ", ".join(valid_types))
    return x


class DeadLetterQueue(AWSProperty):
    props: PropsDictType = {
        "Type": (str, False),
        "TargetArn": (str, False),
    }

    def validate(self):
        valid_types = ["SQS", "SNS"]
        if "Type" in self.properties and self.properties["Type"] not in valid_types:
            raise ValueError("Type must be either SQS or SNS")


class S3Location(AWSProperty):
    props: PropsDictType = {
        "Bucket": (str, True),
        "Key": (str, True),
        "Version": (str, False),
    }


class Hooks(AWSProperty):
    props: PropsDictType = {
        "PreTraffic": (str, False),
        "PostTraffic": (str, False),
    }


class DeploymentPreference(AWSProperty):
    props: PropsDictType = {
        "Type": (str, True),
        "Alarms": (list, False),
        "Hooks": (Hooks, False),
        "Enabled": (bool, False),
        "Role": (str, False),
    }


class EventInvokeDestination(AWSProperty):
    props: PropsDictType = {
        "Destination": (str, False),
        "Type": (str, False),
    }

    def validate(self):
        dest = self.properties.get("Destination")
        tp = self.properties.get("Type")

        if not dest and tp in ["Lambda", "EventBridge"]:
            raise ValueError(
                "Destination is required when Type is " "set to Lambda or EventBridge."
            )

        if tp not in ["SQS", "SNS", "Lambda", "EventBridge"]:
            raise ValueError(
                "Type must be one of the following: " "SQS, SNS, Lambda, EventBridge"
            )


class OnFailure(EventInvokeDestination):
    pass


class OnSuccess(EventInvokeDestination):
    pass


class DestinationConfiguration(AWSProperty):
    props: PropsDictType = {
        "OnFailure": (OnFailure, False),
        "OnSuccess": (OnSuccess, False),
    }


class EventInvokeConfiguration(AWSProperty):
    props: PropsDictType = {
        "DestinationConfig": (DestinationConfiguration, False),
        "MaximumEventAgeInSeconds": (integer, False),
        "MaximumRetryAttempts": (integer, False),
    }


def validate_authtype(authtype):
    VALID_AUTHTYPE = [
        "AWS_IAM",
        "NONE",
    ]

    if authtype not in VALID_AUTHTYPE:
        raise ValueError("AuthType must be one of: %s" % ", ".join(VALID_AUTHTYPE))
    return authtype


class FunctionUrlConfig(AWSProperty):
    props: PropsDictType = {
        "AuthType": (validate_authtype, True),
        "Cors": (Cors, False),
    }


class Function(AWSObject):
    resource_type = "AWS::Serverless::Function"

    props: PropsDictType = {
        "Architectures": ([str], False),
        "AssumeRolePolicyDocument": (policytypes, False),
        "AutoPublishAlias": (str, False),
        "AutoPublishCodeSha256": (str, False),
        "CodeSigningConfigArn": (str, False),
        "CodeUri": ((S3Location, str), False),
        "DeadLetterQueue": (DeadLetterQueue, False),
        "DeploymentPreference": (DeploymentPreference, False),
        "Description": (str, False),
        "EphemeralStorage": (EphemeralStorage, False),
        "Environment": (Environment, False),
        "EventInvokeConfig": (EventInvokeConfiguration, False),
        "Events": (dict, False),
        "FileSystemConfigs": ([FileSystemConfig], False),
        "FunctionName": (str, False),
        "FunctionUrlConfig": (FunctionUrlConfig, False),
        "Handler": (str, False),
        "ImageConfig": (ImageConfig, False),
        "ImageUri": ((AWSHelperFn, str, dict), False),
        "InlineCode": (str, False),
        "KmsKeyArn": (str, False),
        "Layers": ([str], False),
        "MemorySize": (validate_memory_size, False),
        "PackageType": (validate_package_type, False),
        "PermissionsBoundary": (str, False),
        "Policies": (policytypes, False),
        "ProvisionedConcurrencyConfig": (ProvisionedConcurrencyConfiguration, False),
        "ReservedConcurrentExecutions": (positive_integer, False),
        "Role": (str, False),
        "Runtime": (str, False),
        "RuntimeManagementConfig": (RuntimeManagementConfig, False),
        "SnapStart": (SnapStart, False),
        "Tags": (dict, False),
        "Timeout": (positive_integer, False),
        "Tracing": (str, False),
        "VersionDescription": (str, False),
        "VpcConfig": (VPCConfig, False),
    }

    def validate(self):
        image_uri = self.properties.get("ImageUri")
        code_uri = self.properties.get("CodeUri")
        inline_code = self.properties.get("InlineCode")

        if not (image_uri or code_uri or inline_code) and not self.properties.get(
            "Metadata"
        ):
            raise ValueError(
                "You must specify local container image information in "
                "the Metadata of the Function if you are not specifying "
                "ImageUri, CodeUri or InlineCode."
            )
        if image_uri or code_uri or inline_code:
            conds = [
                "CodeUri",
                "InlineCode",
                "ImageUri",
            ]
            exactly_one(self.__class__.__name__, self.properties, conds)


class FunctionForPackaging(Function):
    """Render Function without requiring 'CodeUri'.

    This exception to the Function spec is for use with the
    `cloudformation/sam package` commands which add CodeUri automatically.
    """

    resource_type = Function.resource_type
    props = Function.props.copy()
    props["CodeUri"] = (props["CodeUri"][0], False)

    def validate(self):
        pass


class CognitoAuthIdentity(AWSProperty):
    props: PropsDictType = {
        "Header": (str, False),
        "ValidationExpression": (str, False),
    }


class LambdaTokenAuthIdentity(AWSProperty):
    props: PropsDictType = {
        "Header": (str, False),
        "ValidationExpression": (str, False),
        "ReauthorizeEvery": (str, False),
    }


class LambdaRequestAuthIdentity(AWSProperty):
    props: PropsDictType = {
        "Headers": ([str], False),
        "QueryStrings": ([str], False),
        "StageVariables": ([str], False),
        "Context": ([str], False),
        "ReauthorizeEvery": (str, False),
    }


class CognitoAuth(AWSProperty):
    props: PropsDictType = {
        "UserPoolArn": (str, False),
        "Identity": (CognitoAuthIdentity, False),
    }


class LambdaTokenAuth(AWSProperty):
    props: PropsDictType = {
        "FunctionPayloadType": (str, False),
        "FunctionArn": (str, False),
        "FunctionInvokeRole": (str, False),
        "Identity": (LambdaTokenAuthIdentity, False),
    }


class LambdaRequestAuth(AWSProperty):
    props: PropsDictType = {
        "FunctionPayloadType": (str, False),
        "FunctionArn": (str, False),
        "FunctionInvokeRole": (str, False),
        "Identity": (LambdaRequestAuthIdentity, False),
    }


class Authorizers(AWSProperty):
    props: PropsDictType = {
        "DefaultAuthorizer": (str, False),
        "CognitoAuth": (CognitoAuth, False),
        "LambdaTokenAuth": (LambdaTokenAuth, False),
        "LambdaRequestAuth": (LambdaRequestAuth, False),
    }


class ResourcePolicyStatement(AWSProperty):
    props: PropsDictType = {
        "AwsAccountBlacklist": (list, False),
        "AwsAccountWhitelist": (list, False),
        "CustomStatements": (list, False),
        "IpRangeBlacklist": (list, False),
        "IpRangeWhitelist": (list, False),
        "SourceVpcBlacklist": (list, False),
        "SourceVpcWhitelist": (list, False),
    }


class Auth(AWSProperty):
    props: PropsDictType = {
        "AddDefaultAuthorizerToCorsPreflight": (bool, False),
        "ApiKeyRequired": (bool, False),
        "Authorizers": (Authorizers, False),
        "DefaultAuthorizer": (str, False),
        "InvokeRole": (str, False),
        "ResourcePolicy": (ResourcePolicyStatement, False),
    }


class Cors(AWSProperty):
    props: PropsDictType = {
        "AllowCredentials": (str, False),
        "AllowHeaders": (str, False),
        "AllowMethods": (str, False),
        "AllowOrigin": (str, True),
        "MaxAge": (str, False),
    }


class Route53(AWSProperty):
    props: PropsDictType = {
        "DistributionDomainName": (str, False),
        "EvaluateTargetHealth": (bool, False),
        "HostedZoneId": (str, False),
        "HostedZoneName": (str, False),
        "IpV6": (bool, False),
    }

    def validate(self):
        conds = [
            "HostedZoneId",
            "HostedZoneName",
        ]
        mutually_exclusive(self.__class__.__name__, self.properties, conds)


class Domain(AWSProperty):
    props: PropsDictType = {
        "BasePath": (list, False),
        "CertificateArn": (str, True),
        "DomainName": (str, True),
        "EndpointConfiguration": (str, False),
        "Route53": (Route53, False),
    }

    def validate(self):
        valid_types = ["REGIONAL", "EDGE"]
        if (
            "EndpointConfiguration" in self.properties
            and self.properties["EndpointConfiguration"] not in valid_types
        ):
            raise ValueError("EndpointConfiguration must be either REGIONAL or EDGE")


class EndpointConfiguration(AWSProperty):
    props: PropsDictType = {"Type": (str, False), "VPCEndpointIds": (list, False)}

    def validate(self):
        valid_types = ["REGIONAL", "EDGE", "PRIVATE"]
        if "Type" in self.properties and self.properties["Type"] not in valid_types:
            raise ValueError(
                "EndpointConfiguration Type must be REGIONAL, EDGE or PRIVATE"
            )


class ApiDefinition(AWSProperty):
    props: PropsDictType = {
        "Bucket": (str, True),
        "Key": (str, True),
        "Version": (str, False),
    }


class Api(AWSObject):
    resource_type = "AWS::Serverless::Api"

    props: PropsDictType = {
        "AccessLogSetting": (AccessLogSetting, False),
        "Auth": (Auth, False),
        "BinaryMediaTypes": ([str], False),
        "CacheClusterEnabled": (bool, False),
        "CacheClusterSize": (str, False),
        "CanarySetting": (CanarySetting, False),
        "Cors": ((str, Cors), False),
        "DefinitionBody": (dict, False),
        "DefinitionUri": ((str, ApiDefinition), False),
        "Description": (str, False),
        "DisableExecuteApiEndpoint": (bool, False),
        "Domain": (Domain, False),
        "EndpointConfiguration": (EndpointConfiguration, False),
        "MethodSettings": ([MethodSetting], False),
        "MinimumCompressionSize": (integer_range(0, 10485760), False),
        "Mode": (str, False),
        "Models": (dict, False),
        "Name": (str, False),
        "OpenApiVersion": (str, False),
        "StageName": (str, True),
        "Tags": (dict, False),
        "TracingEnabled": (bool, False),
        "Variables": (dict, False),
    }

    def validate(self):
        conds = [
            "DefinitionBody",
            "DefinitionUri",
        ]
        mutually_exclusive(self.__class__.__name__, self.properties, conds)


class OAuth2Authorizer(AWSProperty):
    props: PropsDictType = {
        "AuthorizationScopes": (list, False),
        "IdentitySource": (str, False),
        "JwtConfiguration": (dict, False),
    }


class LambdaAuthorizationIdentity(AWSProperty):
    props: PropsDictType = {
        "Context": (list, False),
        "Headers": (list, False),
        "QueryStrings": (list, False),
        "ReauthorizeEvery": (integer, False),
        "StageVariables": (list, False),
    }


class LambdaAuthorizer(AWSProperty):
    props: PropsDictType = {
        "AuthorizerPayloadFormatVersion": (str, True),
        "EnableSimpleResponses": (boolean, False),
        "FunctionArn": (str, True),
        "FunctionInvokeRole": (str, False),
        "Identity": (LambdaAuthorizationIdentity, False),
    }


class HttpApiAuth(AWSProperty):
    props: PropsDictType = {
        "Authorizers": ((OAuth2Authorizer, LambdaAuthorizer), False),
        "DefaultAuthorizer": (str, False),
    }


class HttpApiCorsConfiguration(AWSProperty):
    props: PropsDictType = {
        "AllowCredentials": (boolean, False),
        "AllowHeaders": (list, False),
        "AllowMethods": (list, False),
        "AllowOrigins": (list, False),
        "ExposeHeaders": (list, False),
        "MaxAge": (integer, False),
    }


class HttpApiDefinition(ApiDefinition):
    pass


class HttpApiDomainConfiguration(Domain):
    pass


class HttpApi(AWSObject):
    resource_type = "AWS::Serverless::HttpApi"

    props: PropsDictType = {
        "AccessLogSettings": (AccessLogSettings, False),
        "Auth": (HttpApiAuth, False),
        "CorsConfiguration": ((str, HttpApiCorsConfiguration), False),
        "DefaultRouteSettings": (RouteSettings, False),
        "DefinitionBody": (dict, False),
        "DefinitionUri": ((str, HttpApiDefinition), False),
        "Description": (str, False),
        "DisableExecuteApiEndpoint": (boolean, False),
        "Domain": (HttpApiDomainConfiguration, False),
        "FailOnWarnings": (boolean, False),
        "RouteSettings": (dict, False),
        "StageName": (str, False),
        "StageVariables": (dict, False),
        "Tags": (dict, False),
    }

    def validate(self):
        conds = [
            "DefinitionBody",
            "DefinitionUri",
        ]
        mutually_exclusive(self.__class__.__name__, self.properties, conds)


class PrimaryKey(AWSProperty):
    props: PropsDictType = {
        "Name": (str, False),
        "Type": (primary_key_type_validator, False),
    }


class SimpleTable(AWSObject):
    resource_type = "AWS::Serverless::SimpleTable"

    props: PropsDictType = {
        "PrimaryKey": (PrimaryKey, False),
        "ProvisionedThroughput": (ProvisionedThroughput, False),
        "SSESpecification": (SSESpecification, False),
        "Tags": (dict, False),
        "TableName": (str, False),
    }


class LayerVersion(AWSObject):
    resource_type = "AWS::Serverless::LayerVersion"

    props: PropsDictType = {
        "CompatibleArchitectures": ([str], False),
        "CompatibleRuntimes": ([str], False),
        "ContentUri": ((S3Location, str), True),
        "Description": (str, False),
        "LayerName": (str, False),
        "LicenseInfo": (str, False),
        "RetentionPolicy": (str, False),
    }


class S3Event(AWSObject):
    resource_type = "S3"

    props: PropsDictType = {
        "Bucket": (str, True),
        "Events": (list, True),
        "Filter": (Filter, False),
    }


class SNSEvent(AWSObject):
    resource_type = "SNS"

    props: PropsDictType = {
        "FilterPolicy": (dict, False),
        "Region": (str, False),
        "SqsSubscription": (bool, False),
        "Topic": (str, True),
    }


def starting_position_validator(x):
    valid_types = ["TRIM_HORIZON", "LATEST"]
    if x not in valid_types:
        raise ValueError("StartingPosition must be one of: %s" % ", ".join(valid_types))
    return x


class KinesisEvent(AWSObject):
    resource_type = "Kinesis"

    props: PropsDictType = {
        "Stream": (str, True),
        "StartingPosition": (starting_position_validator, True),
        "BatchSize": (positive_integer, False),
        "BisectBatchOnFunctionError": (bool, False),
        "DestinationConfig": (DestinationConfig, False),
        "Enabled": (bool, False),
        "FilterCriteria": (FilterCriteria, False),
        "MaximumBatchingWindowInSeconds": (positive_integer, False),
        "MaximumRecordAgeInSeconds": (integer_range(60, 604800), False),
        "MaximumRetryAttempts": (positive_integer, False),
        "ParallelizationFactor": (integer_range(1, 10), False),
    }


class DynamoDBEvent(AWSObject):
    resource_type = "DynamoDB"

    props: PropsDictType = {
        "Stream": (str, True),
        "StartingPosition": (starting_position_validator, True),
        "BatchSize": (positive_integer, False),
    }


class ApiFunctionAuth(AWSProperty):
    props: PropsDictType = {
        "ApiKeyRequired": (bool, False),
        "AuthorizationScopes": (list, False),
        "Authorizer": (str, False),
        "InvokeRole": (str, False),
        "ResourcePolicy": (ResourcePolicyStatement, False),
    }


class RequestModel(AWSProperty):
    props: PropsDictType = {
        "Model": (str, True),
        "Required": (bool, False),
        "ValidateBody": (bool, False),
        "ValidateParameters": (bool, False),
    }


def api_function_auth_validator(auth):
    if not isinstance(auth, (Auth, ApiFunctionAuth)):
        raise TypeError(
            f"Value {auth} of type {type(auth)}, expected {Auth} or {ApiFunctionAuth}"
        )

    if isinstance(auth, Auth):
        from warnings import warn

        warn(
            f"The use of {Auth} in ApiEvent is deprecated. Please use {ApiFunctionAuth} instead",
            DeprecationWarning,
        )

    return auth


class ApiEvent(AWSObject):
    resource_type = "Api"

    props: PropsDictType = {
        "Auth": (api_function_auth_validator, False),
        "Path": (str, True),
        "Method": (str, True),
        "RequestModel": (RequestModel, False),
        "RequestParameters": (str, False),
        "RestApiId": (str, False),
    }


class ScheduleEvent(AWSObject):
    resource_type = "Schedule"

    props: PropsDictType = {
        "Schedule": (str, True),
        "Input": (str, False),
        "Description": (str, False),
        "Enabled": (bool, False),
        "Name": (str, False),
    }


class DeadLetterConfig(AWSProperty):
    props: PropsDictType = {
        "Arn": (str, False),
        "QueueLogicalId": (str, False),
        "Type": (str, False),
    }


class FlexibleTimeWindow(AWSProperty):
    props: PropsDictType = {
        "MaximumWindowInMinutes": (double, False),
        "Mode": (str, True),
    }


class RetryPolicy(AWSProperty):
    props: PropsDictType = {
        "MaximumEventAgeInSeconds": (double, False),
        "MaximumRetryAttempts": (double, False),
    }


class ScheduleV2Event(AWSObject):
    resource_type = "ScheduleV2"

    props: PropsDictType = {
        "DeadLetterConfig": (DeadLetterConfig, False),
        "Description": (str, False),
        "EndDate": (str, False),
        "FlexibleTimeWindow": (FlexibleTimeWindow, False),
        "GroupName": (str, False),
        "Input": (str, False),
        "KmsKeyArn": (str, False),
        "Name": (str, False),
        "OmitName": (bool, False),
        "PermissionsBoundary": (str, False),
        "RetryPolicy": (RetryPolicy, False),
        "RoleArn": (str, False),
        "ScheduleExpression": (str, True),
        "ScheduleExpressionTimezone": (str, False),
        "StartDate": (str, False),
        "State": (str, False),
    }


class CloudWatchEvent(AWSObject):
    resource_type = "CloudWatchEvent"

    props: PropsDictType = {
        "Pattern": (dict, True),
        "Input": (str, False),
        "InputPath": (str, False),
    }


class IoTRuleEvent(AWSObject):
    resource_type = "IoTRule"

    props: PropsDictType = {
        "Sql": (str, True),
        "AwsIotSqlVersion": (str, False),
    }


class AlexaSkillEvent(AWSObject):
    resource_type = "AlexaSkill"
    props: PropsDictType = {}


class SQSEvent(AWSObject):
    resource_type = "SQS"

    props: PropsDictType = {"Queue": (str, True), "BatchSize": (positive_integer, True)}

    def validate(self):
        if not 1 <= self.properties["BatchSize"] <= 10:
            raise ValueError("BatchSize must be between 1 and 10")


class MSKEvent(AWSObject):
    resource_type = "MSK"

    props: PropsDictType = {
        "ConsumerGroupId": (str, False),
        "FilterCriteria": (FilterCriteria, False),
        "MaximumBatchingWindowInSeconds": (integer, False),
        "SourceAccessConfigurations": ([SourceAccessConfiguration], False),
        "StartingPosition": (str, True),
        "StartingPositionTimestamp": (double, False),
        "Stream": (str, True),
        "Topics": ([str], True),
    }


class SelfManagedKafkaEvent(AWSObject):
    resource_type = "SelfManagedKafka"

    props: PropsDictType = {
        "BatchSize": (integer, False),
        "ConsumerGroupId": (str, False),
        "Enabled": (bool, False),
        "FilterCriteria": (FilterCriteria, False),
        "KafkaBootstrapServers": ([str], False),
        "SourceAccessConfigurations": ([SourceAccessConfiguration], True),
        "Topics": ([str], True),
    }


class MQEvent(AWSObject):
    resource_type = "MQ"

    props: PropsDictType = {
        "BatchSize": (integer, False),
        "Broker": (str, True),
        "DynamicPolicyName": (bool, False),
        "Enabled": (bool, False),
        "FilterCriteria": (FilterCriteria, False),
        "MaximumBatchingWindowInSeconds": (integer, False),
        "Queues": ([str], True),
        "SecretsManagerKmsKeyId": (str, False),
        "SourceAccessConfigurations": ([SourceAccessConfiguration], True),
    }


class DocumentDBEvent(AWSObject):
    resource_type = "DocumentDB"

    props: PropsDictType = {
        "BatchSize": (integer, False),
        "Cluster": (str, True),
        "CollectionName": (str, False),
        "DatabaseName": (str, True),
        "Enabled": (bool, False),
        "FilterCriteria": (FilterCriteria, False),
        "FullDocument": (str, False),
        "MaximumBatchingWindowInSeconds": (integer, False),
        "SecretsManagerKmsKeyId": (str, False),
        "SourceAccessConfigurations": ([str], True),
        "StartingPosition": (str, True),
        "StartingPositionTimestamp": (double, False),
    }


class Target(AWSProperty):
    props: PropsDictType = {"Id": (str, True)}


class EventBridgeRuleEvent(AWSObject):
    resource_type = "EventBridgeRule"

    props: PropsDictType = {
        "DeadLetterConfig": (DeadLetterConfig, False),
        "EventBusName": (str, False),
        "Input": (str, False),
        "InputPath": (str, False),
        "Name": (str, False),
        "Pattern": (dict, True),
        "RetryPolicy": (RetryPolicy, False),
        "State": (str, False),
        "Target": (Target, False),
    }


class ApplicationLocation(AWSProperty):
    props: PropsDictType = {
        "ApplicationId": (str, True),
        "SemanticVersion": (str, True),
    }


class Application(AWSObject):
    resource_type = "AWS::Serverless::Application"

    props: PropsDictType = {
        "Location": ((ApplicationLocation, str), True),
        "NotificationARNs": ([str], False),
        "Parameters": (dict, False),
        "Tags": (dict, False),
        "TimeoutInMinutes": (positive_integer, False),
    }

    def validate(self):
        conds = [
            "DefinitionBody",
            "DefinitionUri",
        ]
        mutually_exclusive(self.__class__.__name__, self.properties, conds)


class StateMachine(AWSObject):
    """
    `StateMachine <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-statemachine.html>`__
    """

    resource_type = "AWS::Serverless::StateMachine"

    props: PropsDictType = {
        "Definition": (dict, False),
        "DefinitionUri": ((S3Location, str), False),
        "DefinitionSubstitutions": (dict, False),
        "Events": (dict, False),
        "Logging": (LoggingConfiguration, False),
        "Name": (str, False),
        "PermissionsBoundary": (str, False),
        "Policies": (policytypes, False),
        "Role": (str, False),
        "Tags": (dict, False),
        "TracingConfiguration": (TracingConfiguration, False),
        "Type": (str, False),
    }

    def validate(self):
        if not self.properties.get("Policies") and not self.properties.get("Role"):
            raise ValueError("You provide either a Role or Policies.")

        valid_types = ["STANDARD", "EXPRESS"]
        if "Type" in self.properties and self.properties["Type"] not in valid_types:
            raise ValueError("StateMachine Type must be STANDARD or EXPRESS")


class FunctionGlobals(AWSProperty):
    props: PropsDictType = {
        "AssumeRolePolicyDocument": (policytypes, False),
        "AutoPublishAlias": (str, False),
        "CodeUri": ((S3Location, str), False),
        "DeadLetterQueue": (DeadLetterQueue, False),
        "DeploymentPreference": (DeploymentPreference, False),
        "Description": (str, False),
        "Environment": (Environment, False),
        "EventInvokeConfig": (EventInvokeConfiguration, False),
        "FileSystemConfigs": ([FileSystemConfig], False),
        "Handler": (str, False),
        "KmsKeyArn": (str, False),
        "Layers": ([str], False),
        "MemorySize": (validate_memory_size, False),
        "PermissionsBoundary": (str, False),
        "ProvisionedConcurrencyConfig": (ProvisionedConcurrencyConfiguration, False),
        "ReservedConcurrentExecutions": (positive_integer, False),
        "Runtime": (str, False),
        "Tags": (dict, False),
        "Timeout": (positive_integer, False),
        "Tracing": (str, False),
        "VpcConfig": (VPCConfig, False),
    }


class ApiGlobals(AWSProperty):
    props: PropsDictType = {
        "AccessLogSetting": (AccessLogSetting, False),
        "Auth": (Auth, False),
        "BinaryMediaTypes": ([str], False),
        "CacheClusterEnabled": (bool, False),
        "CacheClusterSize": (str, False),
        "CanarySetting": (CanarySetting, False),
        "Cors": ((str, Cors), False),
        "DefinitionUri": ((str, ApiDefinition), False),
        "Domain": (Domain, False),
        "EndpointConfiguration": (EndpointConfiguration, False),
        "MethodSettings": ([MethodSetting], False),
        "MinimumCompressionSize": (integer_range(0, 10485760), False),
        "Name": (str, False),
        "OpenApiVersion": (str, False),
        "TracingEnabled": (bool, False),
        "Variables": (dict, False),
    }


class HttpApiGlobals(AWSProperty):
    props: PropsDictType = {
        "AccessLogSettings": (AccessLogSettings, False),
        "Auth": (HttpApiAuth, False),
        "StageVariables": (dict, False),
        "Tags": (dict, False),
    }


class SimpleTableGlobals(AWSProperty):
    props: PropsDictType = {
        "SSESpecification": (SSESpecification, False),
    }


class Globals(AWSProperty):
    """Supported Globals properties.

    See: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy-globals.html
    """

    props: PropsDictType = {
        "Api": (ApiGlobals, False),
        "Function": (FunctionGlobals, False),
        "HttpApi": (HttpApiGlobals, False),
        "SimpleTable": (SimpleTableGlobals, False),
    }
