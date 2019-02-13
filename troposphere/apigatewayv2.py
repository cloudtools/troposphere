from . import AWSObject, AWSProperty
from .validators import (
    boolean, double, integer_range, json_checker, positive_integer
)


def validate_integration_type(integration_type):

    valid_integration_types = [
        "AWS",
        "AWS_PROXY",
        "HTTP",
        "HTTP_PROXY",
        "MOCK"
    ]
    if integration_type not in valid_integration_types:
        raise ValueError(
            "{} is not a valid IntegrationType".format(
                integration_type)
        )
    return integration_type


def validate_authorizer_type(authorizer_type):

    valid_authorizer_types = [
        "REQUEST"
    ]
    if authorizer_type not in valid_authorizer_types:
        raise ValueError(
            "{} is not a valid AuthorizerType".format(
                authorizer_type)
        )
    return authorizer_type


def validate_logging_level(logging_level):

    valid_logging_levels = [
        "WARN",
        "INFO",
        "DEBUG"
    ]
    if logging_level not in valid_logging_levels:
        raise ValueError(
            "{} is not a valid LoggingLevel".format(
                logging_level)
        )
    return logging_level


def validate_passthrough_behavior(passthrough_behavior):

    valid_passthrough_behaviors = [
        "WHEN_NO_MATCH",
        "WHEN_NO_TEMPLATES",
        "NEVER"
    ]
    if passthrough_behavior not in valid_passthrough_behaviors:
        raise ValueError(
            "{} is not a valid PassthroughBehavior".format(
                passthrough_behavior)
        )
    return passthrough_behavior


def validate_content_handling_strategy(content_handling_strategy):

    valid_handling_strategy_values = [
        "CONVERT_TO_TEXT",
        "CONVERT_TO_BINARY"
    ]
    if content_handling_strategy not in valid_handling_strategy_values:
        raise ValueError(
            "{} is not a valid ContentHandlingStrategy".format(
                content_handling_strategy)
        )
    return content_handling_strategy


def validate_authorizer_ttl(ttl_value):
    """ Validate authorizer ttl timeout
    :param ttl_value: The TTL timeout in seconds
    :return: The provided TTL value if valid
    """
    ttl_value = int(positive_integer(ttl_value))
    if ttl_value > 3600:
        raise ValueError("The AuthorizerResultTtlInSeconds should be <= 3600")
    return ttl_value


class AccessLogSettings(AWSProperty):
    props = {
        "DestinationArn": (basestring, False),
        "Format": (basestring, False)
    }


class RouteSettings(AWSProperty):
    props = {
        "DataTraceEnabled": (basestring, False),
        "DetailedMetricsEnabled": (boolean, False),
        "LoggingLevel": (validate_logging_level, False),
        "ThrottlingBurstLimit": (positive_integer, False),
        "ThrottlingRateLimit": (double, False)
    }


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

    props = {
        "ApiId":  (basestring, True),
        "AuthorizerCredentialsArn":  (basestring, False),
        "AuthorizerResultTtlInSeconds": (validate_authorizer_ttl, False),
        "AuthorizerType":  (validate_authorizer_type, True),
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
        "ContentHandlingStrategy": (validate_content_handling_strategy, False),
        "CredentialsArn": (basestring, False),
        "Description": (basestring, False),
        "IntegrationMethod": (basestring, False),
        "IntegrationType": (validate_integration_type, True),
        "IntegrationUri": (basestring, False),
        "PassthroughBehavior": (validate_passthrough_behavior, False),
        "RequestParameters": (dict, False),
        "RequestTemplates": (dict, False),
        "TemplateSelectionExpression": (basestring, False),
        "TimeoutInMillis": (integer_range(50, 29000), False)
    }


class IntegrationResponse(AWSObject):
    resource_type = "AWS::ApiGatewayV2::IntegrationResponse"

    props = {
        "ApiId": (basestring, True),
        "ContentHandlingStrategy": (validate_content_handling_strategy, False),
        "IntegrationId": (basestring, True),
        "IntegrationResponseKey": (basestring, True),
        "ResponseParameters": (dict, False),
        "ResponseTemplates": (dict, False),
        "TemplateSelectionExpression": (basestring, False)
    }


class Model(AWSObject):
    resource_type = "AWS::ApiGatewayV2::Model"

    props = {
        "ApiId": (basestring, True),
        "ContentType": (basestring, False),
        "Description": (basestring, False),
        "Name": (basestring, True),
        "Schema": ((basestring, dict), True)
    }

    def validate(self):
        name = 'Schema'
        if name in self.properties:
            schema = self.properties.get(name)
            self.properties[name] = json_checker(schema)


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
        "AccessLogSettings": (AccessLogSettings, False),
        "ApiId": (basestring, True),
        "ClientCertificateId": (basestring, False),
        "DefaultRouteSettings": (RouteSettings, False),
        "DeploymentId": (basestring, False),
        "Description": (basestring, False),
        "RouteSettings": (dict, False),
        "StageName": (basestring, True),
        "StageVariables": (dict, False)
    }
