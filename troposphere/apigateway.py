from . import AWSObject, AWSProperty
from .validators import positive_integer


def validate_authorizer_ttl(ttl_value):
    """ Validate authorizer ttl timeout
    :param ttl_value: The TTL timeout in seconds
    :return: The provided TTL value if valid
    """
    ttl_value = int(positive_integer(ttl_value))
    if ttl_value > 3600:
        raise ValueError("The AuthorizerResultTtlInSeconds should be <= 3600")
    return ttl_value


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
        "Description": (basestring, False),
        "Enabled": (bool, False),
        "Name": (basestring, False),
        "StageKeys": ([StageKey], False)
    }


class Authorizer(AWSObject):
    resource_type = "AWS::ApiGateway::Authorizer"

    props = {
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


class ClientCertificate(AWSObject):
    resource_type = "AWS::ApiGateway::ClientCertificate"

    props = {
        "Description": (basestring, False)
    }


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
        "CacheClusterEnabled": (bool, False),
        "CacheClusterSize": (basestring, False),
        "CacheDataEncrypted": (bool, False),
        "CacheTtlInSeconds": (positive_integer, False),
        "CachingEnabled": (bool, False),
        "ClientCertificateId": (basestring, False),
        "DataTraceEnabled": (bool, False),
        "Description": (basestring, False),
        "LoggingLevel": (basestring, False),
        "MethodSettings": ([MethodSetting], False),
        "MetricsEnabled": (bool, False),
        "StageName": (basestring, False),
        "ThrottlingBurstLimit": (positive_integer, False),
        "ThrottlingRateLimit": (positive_integer, False),
        "Variables": (dict, False)
    }


class Deployment(AWSObject):
    resource_type = "AWS::ApiGateway::Deployment"

    props = {
        "Description": (basestring, False),
        "RestApiId": (basestring, True),
        "StageDescription": (StageDescription, False),
        "StageName": (basestring, False)
    }


class IntegrationResponse(AWSProperty):

    props = {
        "ResponseParameters": (dict, False),
        "ResponseTemplates": (dict, False),
        "SelectionPattern": (basestring, False),
        "StatusCode": (basestring, False)
    }


class Integration(AWSProperty):

    props = {
        "CacheKeyParameters": ([basestring], False),
        "CacheNamespace": (basestring, False),
        "Credentials": (basestring, False),
        "IntegrationHttpMethod": (basestring, False),
        "IntegrationResponses": ([IntegrationResponse], False),
        "PassthroughBehavior": (basestring, False),
        "RequestParameters": (dict, False),
        "RequestTemplates": (dict, False),
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
        "AuthorizationType": (basestring, True),
        "AuthorizerId": (basestring, False),
        "HttpMethod": (basestring, True),
        "Integration": (Integration, False),
        "MethodResponses": ([MethodResponse], False),
        "RequestModels": (dict, False),
        "RequestParameters": (dict, False),
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
        "Schema": (basestring, False)
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
        "Body": (dict, False),
        "BodyS3Location": (S3Location, False),
        "CloneFrom": (basestring, False),
        "Description": (basestring, False),
        "FailOnWarnings": (basestring, False),
        "Name": (basestring, False),
        "Parameters": ([basestring], False)
    }


class Stage(AWSObject):
    resource_type = "AWS::ApiGateway::Stage"

    props = {
        "CacheClusterEnabled": (bool, False),
        "CacheClusterSize": (basestring, False),
        "ClientCertificateId": (basestring, False),
        "DeploymentId": (basestring, True),
        "Description": (basestring, False),
        "MethodSettings": ([MethodSetting], False),
        "RestApiId": (basestring, True),
        "StageName": (basestring, True),
        "Variables": (dict, False)
    }


class ApiStage(AWSProperty):
    props = {
        "ApiId": (basestring, False),
        "Stage": (basestring, False),
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


class UsagePlan(AWSObject):
    resource_type = "AWS::ApiGateway::UsagePlan"

    props = {
        "ApiStages": ([ApiStage], False),
        "Description": (basestring, False),
        "Quota": (QuotaSettings, False),
        "Throttle": (ThrottleSettings, False),
        "UsagePlanName": (basestring, False),
    }
