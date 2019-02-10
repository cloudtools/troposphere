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


class Api(AWSObject):
    resource_type = "AWS::ApiGatewayV2::Api"

    props = {
        "ApiKeySelectionExpression": (basestring, False),
        "Description": (basestring, False),
        "DisableSchemaValidation": (boolean, False),
        "Name": (basestring, True),
        "ProtocolType": (basestring, True),
        "RouteSelectionExpression": (basestring, True),
        "Version": (basestring, False)
    }


class Authorizer(AWSObject):
    resource_type = "AWS::ApiGatewayV2::Authorizer"

    props =
        "ApiId":  (basestring, True),
        "AuthorizerCredentialsArn":  (basestring, False),
        "AuthorizerResultTtlInSeconds": (integer, False),
        "AuthorizerType":  (basestring, True),
        "AuthorizerUri":  (basestring, True),
        "IdentitySource": ([basestring], True),
        "IdentityValidationExpression":  (basestring, False),
        "Name":  (basestring, True)
    }

class Deployment(AWSObject):

    resource_type = "AWS::ApiGatewayV2::Deployment"

    props = {
        "ApiId": (basestring, True),
        "Description": (basestring, False),
        "StageName": (basestring, False),
    }

class Integration(AWSObject):

    resource_type = "AWS::ApiGatewayV2::Integration"

    props = {
        "ApiId": (basestring, True),
        "ConnectionType": (basestring, False),
        "ContentHandlingStrategy": (basestring, False),
        "CredentialsArn": (basestring, False),
        "Description": (basestring, False),
        "IntegrationMethod": (basestring, False),
        "IntegrationType": (basestring, True),
        "IntegrationUri": (basestring, False),
        "PassthroughBehavior": (basestring, False),
        "RequestParameters": (dict, False),
        "RequestTemplates": (dict, False),
        "TemplateSelectionExpression": (basestring, False),
        "TimeoutInMillis": (integer, False)
    }

class IntegrationResponse(AWSObject):

    resource_type = "AWS::ApiGatewayV2::IntegrationResponse"

    props = {
        "ApiId": (basestring, True),
        "ContentHandlingStrategy": (basestring, False),
        "IntegrationId": (basestring, True),
        "IntegrationResponseKey": (basestring, True),
        "ResponseParameters": (dict, False),
        "ResponseTemplates": (dict, False),
        "TemplateSelectionExpression": (basestring, False)
    }

class Route(AWSObject):

    resource_type = "AWS::ApiGatewayV2::Model"

    props = {
        "ApiId": (basestring, True),
        "ContentType": (basestring, False),
        "Description": (basestring, False),
        "Name": (basestring, True),
        "Schema": (dict, False)
    }

class Route(AWSObject):

    resource_type = "AWS::ApiGatewayV2::Route"

    props = {
        "ApiId": (basestring, True),
        "ApiKeyRequired": (boolean, False),
        "AuthorizationScopes": ([basestring], False),
        "AuthorizationType": (basestring, False),
        "AuthorizerId": (basestring, False),
        "ModelSelectionExpression": (basestring, False),
        "OperationName": (basestring, False),
        "RequestModels": (dict, False),
        "RequestParameters": (dict, False),
        "RouteKey": (basestring, True),
        "RouteResponseSelectionExpression": (basestring, False),
        "Target": (basestring, False)
    }


class RouteResponse(AWSObject):

    resource_type = "AWS::ApiGatewayV2::RouteResponse"

    props = {
        "ApiId": (basestring, True),
        "ModelSelectionExpression": (basestring, False),
        "ResponseModels": (dict, False),
        "ResponseParameters": (dict, False),
        "RouteId": (basestring, True),
        "RouteResponseKey": (basestring, True)
    }

class Stage(AWSObject):

    resource_type = "AWS::ApiGatewayV2::Stage"

    props = {
        "AccessLogSettings": AccessLogSettings,
        "ApiId": (basestring, True),
        "ClientCertificateId": (basestring, False),
        "DefaultRouteSettings": RouteSettings,
        "DeploymentId": (basestring, False),
        "Description": (basestring, False),
        "RouteSettings": (dict, False),
        "StageName": (basestring, True),
        "StageVariables": (dict, False)
    }


class AccessLogSettings(AWSProperty):

    props = {
        "DestinationArn": (basestring, False),
        "Format": (basestring, False)
    }

class RouteSettings(AWSProperty):

    props = {
        "DataTraceEnabled": (basestring, False),
        "DetailedMetricsEnabled": (boolean, False),
        "LoggingLevel": (basestring, False),
        "ThrottlingBurstLimit": (integer, False),
        "ThrottlingRateLimit": (double, False)
    }
