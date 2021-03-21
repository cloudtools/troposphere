from . import AWSObject, AWSProperty, Tags
from .validators import (
    boolean, double, integer_range, json_checker, positive_integer
)


def validate_authorizer_ttl(ttl_value):
    """ Validate authorizer ttl timeout
    :param ttl_value: The TTL timeout in seconds
    :return: The provided TTL value if valid
    """
    ttl_value = int(positive_integer(ttl_value))
    if ttl_value > 3600:
        raise ValueError("The AuthorizerResultTtlInSeconds should be <= 3600")
    return ttl_value


class AccessLogSetting(AWSProperty):

    props = {
        "DestinationArn": (str, False),
        "Format": (str, False)
    }


class Account(AWSObject):
    resource_type = "AWS::ApiGateway::Account"

    props = {
        "CloudWatchRoleArn": (str, False)
    }


class StageKey(AWSProperty):

    props = {
        "RestApiId": (str, False),
        "StageName": (str, False)
    }


class ApiKey(AWSObject):
    resource_type = "AWS::ApiGateway::ApiKey"

    props = {
        "CustomerId": (str, False),
        "Description": (str, False),
        "Enabled": (boolean, False),
        "GenerateDistinctId": (boolean, False),
        "Name": (str, False),
        "StageKeys": ([StageKey], False),
        "Tags": (Tags, False),
        "Value": (str, False)
    }


class Authorizer(AWSObject):
    resource_type = "AWS::ApiGateway::Authorizer"

    props = {
        "AuthType": (str, False),
        "AuthorizerCredentials": (str, False),
        "AuthorizerResultTtlInSeconds": (validate_authorizer_ttl, False),
        "AuthorizerUri": (str, True),
        "IdentitySource": (str, True),
        "IdentityValidationExpression": (str, False),
        "Name": (str, True),
        "ProviderARNs": ([str], False),
        "RestApiId": (str, False),
        "Type": (str, True)
    }


class BasePathMapping(AWSObject):
    resource_type = "AWS::ApiGateway::BasePathMapping"

    props = {
        "BasePath": (str, False),
        "DomainName": (str, True),
        "RestApiId": (str, True),
        "Stage": (str, False)
    }


# Represents:
# https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-canarysetting.html
class CanarySetting(AWSProperty):

    props = {
        "DeploymentId": (str, False),
        "PercentTraffic": ([double], False),
        "StageVariableOverrides": (dict, False),
        "UseStageCache": (boolean, False),
    }


StageCanarySetting = CanarySetting


class ClientCertificate(AWSObject):
    resource_type = "AWS::ApiGateway::ClientCertificate"

    props = {
        "Description": (str, False),
        "Tags": (Tags, False),
    }


# Represents:
# http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-canarysetting.html
# and
# https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-deploymentcanarysettings.html
class DeploymentCanarySettings(AWSProperty):

    props = {
        "PercentTraffic": ([double], False),
        "StageVariableOverrides": (dict, False),
        "UseStageCache": (boolean, False),
    }


DeploymentCanarySetting = DeploymentCanarySettings


class MethodSetting(AWSProperty):

    props = {
        "CacheDataEncrypted": (bool, False),
        "CacheTtlInSeconds": (positive_integer, False),
        "CachingEnabled": (bool, False),
        "DataTraceEnabled": (bool, False),
        "HttpMethod": (str, True),
        "LoggingLevel": (str, False),
        "MetricsEnabled": (bool, False),
        "ResourcePath": (str, True),
        "ThrottlingBurstLimit": (positive_integer, False),
        "ThrottlingRateLimit": (positive_integer, False)
    }


class StageDescription(AWSProperty):

    props = {
        "AccessLogSetting": (AccessLogSetting, False),
        "CacheClusterEnabled": (bool, False),
        "CacheClusterSize": (str, False),
        "CacheDataEncrypted": (bool, False),
        "CacheTtlInSeconds": (positive_integer, False),
        "CachingEnabled": (bool, False),
        "CanarySetting": (DeploymentCanarySettings, False),
        "ClientCertificateId": (str, False),
        "DataTraceEnabled": (bool, False),
        "Description": (str, False),
        "LoggingLevel": (str, False),
        "MethodSettings": ([MethodSetting], False),
        "MetricsEnabled": (bool, False),
        "StageName": (str, False),
        "Tags": ((Tags, list), False),
        "ThrottlingBurstLimit": (positive_integer, False),
        "ThrottlingRateLimit": (positive_integer, False),
        "Variables": (dict, False),
    }

    def validate(self):
        if 'StageName' in self.properties:
            raise DeprecationWarning(
                "The StageName property has been deprecated "
                "in StageDescription"
            )


class Deployment(AWSObject):
    resource_type = "AWS::ApiGateway::Deployment"

    props = {
        "DeploymentCanarySettings": (DeploymentCanarySettings, False),
        "Description": (str, False),
        "RestApiId": (str, True),
        "StageDescription": (StageDescription, False),
        "StageName": (str, False)
    }


class Location(AWSProperty):
    props = {
        "Method": (str, False),
        "Name": (str, False),
        "Path": (str, False),
        "StatusCode": (str, False),
        "Type": (str, False),
    }


class DocumentationPart(AWSObject):
    resource_type = "AWS::ApiGateway::DocumentationPart"

    props = {
        "Location": (Location, True),
        "Properties": (str, True),
        "RestApiId": (str, True),
    }


class DocumentationVersion(AWSObject):
    resource_type = "AWS::ApiGateway::DocumentationVersion"

    props = {
        "Description": (str, False),
        "DocumentationVersion": (str, True),
        "RestApiId": (str, True),
    }


class EndpointConfiguration(AWSProperty):

    props = {
        "Types": ([str], False),
        "VpcEndpointIds": ([str], False),
    }


class MutualTlsAuthentication(AWSProperty):
    props = {
        'TruststoreUri': (str, False),
        'TruststoreVersion': (str, False),
    }


class DomainName(AWSObject):
    resource_type = "AWS::ApiGateway::DomainName"

    props = {
        "CertificateArn": (str, False),
        "DomainName": (str, True),
        "EndpointConfiguration": (EndpointConfiguration, False),
        'MutualTlsAuthentication': (MutualTlsAuthentication, False),
        "RegionalCertificateArn": (str, False),
        "SecurityPolicy": (str, False),
        "Tags": (Tags, False),
    }


class IntegrationResponse(AWSProperty):

    props = {
        "ContentHandling": (str, False),
        "ResponseParameters": (dict, False),
        "ResponseTemplates": (dict, False),
        "SelectionPattern": (str, False),
        "StatusCode": (str, False)
    }


class Integration(AWSProperty):

    props = {
        "CacheKeyParameters": ([str], False),
        "CacheNamespace": (str, False),
        "ConnectionId": (str, False),
        "ConnectionType": (str, False),
        "ContentHandling": (str, False),
        "Credentials": (str, False),
        "IntegrationHttpMethod": (str, False),
        "IntegrationResponses": ([IntegrationResponse], False),
        "PassthroughBehavior": (str, False),
        "RequestParameters": (dict, False),
        "RequestTemplates": (dict, False),
        "TimeoutInMillis": (integer_range(50, 29000), False),
        "Type": (str, True),
        "Uri": (str, False)
    }


class MethodResponse(AWSProperty):

    props = {
        "ResponseModels": (dict, False),
        "ResponseParameters": (dict, False),
        "StatusCode": (str, True)
    }


class Method(AWSObject):
    resource_type = "AWS::ApiGateway::Method"

    props = {
        "ApiKeyRequired": (bool, False),
        "AuthorizationScopes": ([str], False),
        "AuthorizationType": (str, True),
        "AuthorizerId": (str, False),
        "HttpMethod": (str, True),
        "Integration": (Integration, False),
        "MethodResponses": ([MethodResponse], False),
        "OperationName": (str, False),
        "RequestModels": (dict, False),
        "RequestParameters": (dict, False),
        "RequestValidatorId": (str, False),
        "ResourceId": (str, True),
        "RestApiId": (str, True)
    }


class Model(AWSObject):
    resource_type = "AWS::ApiGateway::Model"

    props = {
        "ContentType": (str, False),
        "Description": (str, False),
        "Name": (str, False),
        "RestApiId": (str, True),
        "Schema": ((str, dict), False)
    }

    def validate(self):
        name = 'Schema'
        if name in self.properties:
            schema = self.properties.get(name)
            self.properties[name] = json_checker(schema)


class RequestValidator(AWSObject):
    resource_type = "AWS::ApiGateway::RequestValidator"

    props = {
        "Name": (str, True),
        "RestApiId": (str, True),
        "ValidateRequestBody": (boolean, False),
        "ValidateRequestParameters": (boolean, False),
    }


class Resource(AWSObject):
    resource_type = "AWS::ApiGateway::Resource"

    props = {
        "ParentId": (str, True),
        "PathPart": (str, True),
        "RestApiId": (str, True)
    }


class S3Location(AWSProperty):

    props = {
        "Bucket": (str, False),
        "ETag": (str, False),
        "Key": (str, False),
        "Version": (str, False)
    }


class RestApi(AWSObject):
    resource_type = "AWS::ApiGateway::RestApi"

    props = {
        "ApiKeySourceType": (str, False),
        "BinaryMediaTypes": ([str], False),
        "Body": (dict, False),
        "BodyS3Location": (S3Location, False),
        "CloneFrom": (str, False),
        "Description": (str, False),
        "EndpointConfiguration": (EndpointConfiguration, False),
        "FailOnWarnings": (boolean, False),
        "MinimumCompressionSize": (positive_integer, False),
        "Name": (str, False),
        "Parameters": (dict, False),
        "Policy": (dict, False),
        "Tags": (Tags, False),
    }


class Stage(AWSObject):
    resource_type = "AWS::ApiGateway::Stage"

    props = {
        "AccessLogSetting": (AccessLogSetting, False),
        "CacheClusterEnabled": (bool, False),
        "CacheClusterSize": (str, False),
        "CanarySetting": (StageCanarySetting, False),
        "ClientCertificateId": (str, False),
        "DeploymentId": (str, True),
        "Description": (str, False),
        "DocumentationVersion": (str, False),
        "MethodSettings": ([MethodSetting], False),
        "RestApiId": (str, True),
        "StageName": (str, True),
        "Tags": ((Tags, list), False),
        "TracingEnabled": (bool, False),
        "Variables": (dict, False),
    }


class QuotaSettings(AWSProperty):
    props = {
        "Limit": (positive_integer, False),
        "Offset": (positive_integer, False),
        "Period": (str, False),
    }


class ThrottleSettings(AWSProperty):
    props = {
        "BurstLimit": (positive_integer, False),
        "RateLimit": (positive_integer, False),
    }


class ApiStage(AWSProperty):
    props = {
        "ApiId": (str, False),
        "Stage": (str, False),
        "Throttle": (dict, False),
    }


class UsagePlan(AWSObject):
    resource_type = "AWS::ApiGateway::UsagePlan"

    props = {
        "ApiStages": ([ApiStage], False),
        "Description": (str, False),
        "Quota": (QuotaSettings, False),
        "Tags": (Tags, False),
        "Throttle": (ThrottleSettings, False),
        "UsagePlanName": (str, False),
    }


class UsagePlanKey(AWSObject):
    resource_type = "AWS::ApiGateway::UsagePlanKey"

    props = {
        "KeyId": (str, True),
        "KeyType": (str, True),
        "UsagePlanId": (str, True),
    }


def validate_gateway_response_type(response_type):
    """ Validate response type
    :param response_type: The GatewayResponse response type
    :return: The provided value if valid
    """
    valid_response_types = [
        "ACCESS_DENIED",
        "API_CONFIGURATION_ERROR",
        "AUTHORIZER_FAILURE",
        "AUTHORIZER_CONFIGURATION_ERROR",
        "BAD_REQUEST_PARAMETERS",
        "BAD_REQUEST_BODY",
        "DEFAULT_4XX",
        "DEFAULT_5XX",
        "EXPIRED_TOKEN",
        "INVALID_SIGNATURE",
        "INTEGRATION_FAILURE",
        "INTEGRATION_TIMEOUT",
        "INVALID_API_KEY",
        "MISSING_AUTHENTICATION_TOKEN",
        "QUOTA_EXCEEDED",
        "REQUEST_TOO_LARGE",
        "RESOURCE_NOT_FOUND",
        "THROTTLED",
        "UNAUTHORIZED",
        "UNSUPPORTED_MEDIA_TYPE"
    ]
    if response_type not in valid_response_types:
        raise ValueError(
            "{} is not a valid ResponseType".format(response_type)
        )
    return response_type


class GatewayResponse(AWSObject):
    resource_type = "AWS::ApiGateway::GatewayResponse"

    props = {
        "ResponseParameters": (dict, False),
        "ResponseTemplates": (dict, False),
        "ResponseType": (validate_gateway_response_type, True),
        "RestApiId": (str, True),
        "StatusCode": (str, False)
    }


class VpcLink(AWSObject):
    resource_type = "AWS::ApiGateway::VpcLink"

    props = {
        'Description': (str, False),
        'Name': (str, True),
        'TargetArns': ([str], True),
    }
