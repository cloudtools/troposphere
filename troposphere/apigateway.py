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
        "DestinationArn": (basestring, False),
        "Format": (basestring, False)
    }


class Account(AWSObject):
    resource_type = "AWS::ApiGateway::Account"

    props = {
        "CloudWatchRoleArn": (basestring, False)
    }


class StageKey(AWSProperty):

    props = {
        "RestApiId": (basestring, False),
        "StageName": (basestring, False)
    }


class ApiKey(AWSObject):
    resource_type = "AWS::ApiGateway::ApiKey"

    props = {
        "CustomerId": (basestring, False),
        "Description": (basestring, False),
        "Enabled": (boolean, False),
        "GenerateDistinctId": (boolean, False),
        "Name": (basestring, False),
        "StageKeys": ([StageKey], False),
        "Tags": (Tags, False),
        "Value": (basestring, False)
    }


class Authorizer(AWSObject):
    resource_type = "AWS::ApiGateway::Authorizer"

    props = {
        "AuthType": (basestring, False),
        "AuthorizerCredentials": (basestring, False),
        "AuthorizerResultTtlInSeconds": (validate_authorizer_ttl, False),
        "AuthorizerUri": (basestring, True),
        "IdentitySource": (basestring, True),
        "IdentityValidationExpression": (basestring, False),
        "Name": (basestring, True),
        "ProviderARNs": ([basestring], False),
        "RestApiId": (basestring, False),
        "Type": (basestring, True)
    }


class BasePathMapping(AWSObject):
    resource_type = "AWS::ApiGateway::BasePathMapping"

    props = {
        "BasePath": (basestring, False),
        "DomainName": (basestring, True),
        "RestApiId": (basestring, True),
        "Stage": (basestring, False)
    }


# Represents:
# https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-canarysetting.html
class CanarySetting(AWSProperty):

    props = {
        "DeploymentId": (basestring, False),
        "PercentTraffic": ([double], False),
        "StageVariableOverrides": (dict, False),
        "UseStageCache": (boolean, False),
    }


StageCanarySetting = CanarySetting


class ClientCertificate(AWSObject):
    resource_type = "AWS::ApiGateway::ClientCertificate"

    props = {
        "Description": (basestring, False),
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
        "HttpMethod": (basestring, True),
        "LoggingLevel": (basestring, False),
        "MetricsEnabled": (bool, False),
        "ResourcePath": (basestring, True),
        "ThrottlingBurstLimit": (positive_integer, False),
        "ThrottlingRateLimit": (positive_integer, False)
    }


class StageDescription(AWSProperty):

    props = {
        "AccessLogSetting": (AccessLogSetting, False),
        "CacheClusterEnabled": (bool, False),
        "CacheClusterSize": (basestring, False),
        "CacheDataEncrypted": (bool, False),
        "CacheTtlInSeconds": (positive_integer, False),
        "CachingEnabled": (bool, False),
        "CanarySetting": (DeploymentCanarySettings, False),
        "ClientCertificateId": (basestring, False),
        "DataTraceEnabled": (bool, False),
        "Description": (basestring, False),
        "LoggingLevel": (basestring, False),
        "MethodSettings": ([MethodSetting], False),
        "MetricsEnabled": (bool, False),
        "StageName": (basestring, False),
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
        "Description": (basestring, False),
        "RestApiId": (basestring, True),
        "StageDescription": (StageDescription, False),
        "StageName": (basestring, False)
    }


class Location(AWSProperty):
    props = {
        "Method": (basestring, False),
        "Name": (basestring, False),
        "Path": (basestring, False),
        "StatusCode": (basestring, False),
        "Type": (basestring, False),
    }


class DocumentationPart(AWSObject):
    resource_type = "AWS::ApiGateway::DocumentationPart"

    props = {
        "Location": (Location, True),
        "Properties": (basestring, True),
        "RestApiId": (basestring, True),
    }


class DocumentationVersion(AWSObject):
    resource_type = "AWS::ApiGateway::DocumentationVersion"

    props = {
        "Description": (basestring, False),
        "DocumentationVersion": (basestring, True),
        "RestApiId": (basestring, True),
    }


class EndpointConfiguration(AWSProperty):

    props = {
        "Types": ([basestring], False),
        "VpcEndpointIds": ([basestring], False),
    }


class MutualTlsAuthentication(AWSProperty):
    props = {
        'TruststoreUri': (basestring, False),
        'TruststoreVersion': (basestring, False),
    }


class DomainName(AWSObject):
    resource_type = "AWS::ApiGateway::DomainName"

    props = {
        "CertificateArn": (basestring, False),
        "DomainName": (basestring, True),
        "EndpointConfiguration": (EndpointConfiguration, False),
        'MutualTlsAuthentication': (MutualTlsAuthentication, False),
        "RegionalCertificateArn": (basestring, False),
        "SecurityPolicy": (basestring, False),
        "Tags": (Tags, False),
    }


class IntegrationResponse(AWSProperty):

    props = {
        "ContentHandling": (basestring, False),
        "ResponseParameters": (dict, False),
        "ResponseTemplates": (dict, False),
        "SelectionPattern": (basestring, False),
        "StatusCode": (basestring, False)
    }


class Integration(AWSProperty):

    props = {
        "CacheKeyParameters": ([basestring], False),
        "CacheNamespace": (basestring, False),
        "ConnectionId": (basestring, False),
        "ConnectionType": (basestring, False),
        "ContentHandling": (basestring, False),
        "Credentials": (basestring, False),
        "IntegrationHttpMethod": (basestring, False),
        "IntegrationResponses": ([IntegrationResponse], False),
        "PassthroughBehavior": (basestring, False),
        "RequestParameters": (dict, False),
        "RequestTemplates": (dict, False),
        "TimeoutInMillis": (integer_range(50, 29000), False),
        "Type": (basestring, True),
        "Uri": (basestring, False)
    }


class MethodResponse(AWSProperty):

    props = {
        "ResponseModels": (dict, False),
        "ResponseParameters": (dict, False),
        "StatusCode": (basestring, True)
    }


class Method(AWSObject):
    resource_type = "AWS::ApiGateway::Method"

    props = {
        "ApiKeyRequired": (bool, False),
        "AuthorizationScopes": ([basestring], False),
        "AuthorizationType": (basestring, True),
        "AuthorizerId": (basestring, False),
        "HttpMethod": (basestring, True),
        "Integration": (Integration, False),
        "MethodResponses": ([MethodResponse], False),
        "OperationName": (basestring, False),
        "RequestModels": (dict, False),
        "RequestParameters": (dict, False),
        "RequestValidatorId": (basestring, False),
        "ResourceId": (basestring, True),
        "RestApiId": (basestring, True)
    }


class Model(AWSObject):
    resource_type = "AWS::ApiGateway::Model"

    props = {
        "ContentType": (basestring, False),
        "Description": (basestring, False),
        "Name": (basestring, False),
        "RestApiId": (basestring, True),
        "Schema": ((basestring, dict), False)
    }

    def validate(self):
        name = 'Schema'
        if name in self.properties:
            schema = self.properties.get(name)
            self.properties[name] = json_checker(schema)


class RequestValidator(AWSObject):
    resource_type = "AWS::ApiGateway::RequestValidator"

    props = {
        "Name": (basestring, True),
        "RestApiId": (basestring, True),
        "ValidateRequestBody": (boolean, False),
        "ValidateRequestParameters": (boolean, False),
    }


class Resource(AWSObject):
    resource_type = "AWS::ApiGateway::Resource"

    props = {
        "ParentId": (basestring, True),
        "PathPart": (basestring, True),
        "RestApiId": (basestring, True)
    }


class S3Location(AWSProperty):

    props = {
        "Bucket": (basestring, False),
        "ETag": (basestring, False),
        "Key": (basestring, False),
        "Version": (basestring, False)
    }


class RestApi(AWSObject):
    resource_type = "AWS::ApiGateway::RestApi"

    props = {
        "ApiKeySourceType": (basestring, False),
        "BinaryMediaTypes": ([basestring], False),
        "Body": (dict, False),
        "BodyS3Location": (S3Location, False),
        "CloneFrom": (basestring, False),
        "Description": (basestring, False),
        "EndpointConfiguration": (EndpointConfiguration, False),
        "FailOnWarnings": (boolean, False),
        "MinimumCompressionSize": (positive_integer, False),
        "Name": (basestring, False),
        "Parameters": (dict, False),
        "Policy": (dict, False),
        "Tags": (Tags, False),
    }


class Stage(AWSObject):
    resource_type = "AWS::ApiGateway::Stage"

    props = {
        "AccessLogSetting": (AccessLogSetting, False),
        "CacheClusterEnabled": (bool, False),
        "CacheClusterSize": (basestring, False),
        "CanarySetting": (StageCanarySetting, False),
        "ClientCertificateId": (basestring, False),
        "DeploymentId": (basestring, True),
        "Description": (basestring, False),
        "DocumentationVersion": (basestring, False),
        "MethodSettings": ([MethodSetting], False),
        "RestApiId": (basestring, True),
        "StageName": (basestring, True),
        "Tags": ((Tags, list), False),
        "TracingEnabled": (bool, False),
        "Variables": (dict, False),
    }


class QuotaSettings(AWSProperty):
    props = {
        "Limit": (positive_integer, False),
        "Offset": (positive_integer, False),
        "Period": (basestring, False),
    }


class ThrottleSettings(AWSProperty):
    props = {
        "BurstLimit": (positive_integer, False),
        "RateLimit": (positive_integer, False),
    }


class ApiStage(AWSProperty):
    props = {
        "ApiId": (basestring, False),
        "Stage": (basestring, False),
        "Throttle": (dict, False),
    }


class UsagePlan(AWSObject):
    resource_type = "AWS::ApiGateway::UsagePlan"

    props = {
        "ApiStages": ([ApiStage], False),
        "Description": (basestring, False),
        "Quota": (QuotaSettings, False),
        "Tags": (Tags, False),
        "Throttle": (ThrottleSettings, False),
        "UsagePlanName": (basestring, False),
    }


class UsagePlanKey(AWSObject):
    resource_type = "AWS::ApiGateway::UsagePlanKey"

    props = {
        "KeyId": (basestring, True),
        "KeyType": (basestring, True),
        "UsagePlanId": (basestring, True),
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
        "RestApiId": (basestring, True),
        "StatusCode": (basestring, False)
    }


class VpcLink(AWSObject):
    resource_type = "AWS::ApiGateway::VpcLink"

    props = {
        'Description': (basestring, False),
        'Name': (basestring, True),
        'TargetArns': ([basestring], True),
    }
