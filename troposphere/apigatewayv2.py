# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 10.0.0


from . import AWSObject, AWSProperty
from .validators import (
    boolean,
    double,
    integer,
    integer_range,
    json_checker,
    positive_integer,
)


def validate_integration_type(integration_type):

    valid_integration_types = ["AWS", "AWS_PROXY", "HTTP", "HTTP_PROXY", "MOCK"]
    if integration_type not in valid_integration_types:
        raise ValueError("{} is not a valid IntegrationType".format(integration_type))
    return integration_type


def validate_authorizer_type(authorizer_type):

    valid_authorizer_types = ["REQUEST", "JWT"]
    if authorizer_type not in valid_authorizer_types:
        raise ValueError("{} is not a valid AuthorizerType".format(authorizer_type))
    return authorizer_type


def validate_logging_level(logging_level):

    valid_logging_levels = ["WARN", "INFO", "DEBUG"]
    if logging_level not in valid_logging_levels:
        raise ValueError("{} is not a valid LoggingLevel".format(logging_level))
    return logging_level


def validate_passthrough_behavior(passthrough_behavior):

    valid_passthrough_behaviors = ["WHEN_NO_MATCH", "WHEN_NO_TEMPLATES", "NEVER"]
    if passthrough_behavior not in valid_passthrough_behaviors:
        raise ValueError(
            "{} is not a valid PassthroughBehavior".format(passthrough_behavior)
        )
    return passthrough_behavior


def validate_content_handling_strategy(content_handling_strategy):

    valid_handling_strategy_values = ["CONVERT_TO_TEXT", "CONVERT_TO_BINARY"]
    if content_handling_strategy not in valid_handling_strategy_values:
        raise ValueError(
            "{} is not a valid ContentHandlingStrategy".format(
                content_handling_strategy
            )
        )
    return content_handling_strategy


def validate_authorizer_ttl(ttl_value):
    """Validate authorizer ttl timeout
    :param ttl_value: The TTL timeout in seconds
    :return: The provided TTL value if valid
    """
    ttl_value = int(positive_integer(ttl_value))
    if ttl_value > 3600:
        raise ValueError("The AuthorizerResultTtlInSeconds should be <= 3600")
    return ttl_value


class BodyS3Location(AWSProperty):
    props = {
        "Bucket": (str, False),
        "Etag": (str, False),
        "Key": (str, False),
        "Version": (str, False),
    }


class Cors(AWSProperty):
    props = {
        "AllowCredentials": (boolean, False),
        "AllowHeaders": ([str], False),
        "AllowMethods": ([str], False),
        "AllowOrigins": ([str], False),
        "ExposeHeaders": ([str], False),
        "MaxAge": (integer, False),
    }


class Api(AWSObject):
    resource_type = "AWS::ApiGatewayV2::Api"

    props = {
        "ApiKeySelectionExpression": (str, False),
        "BasePath": (str, False),
        "Body": (dict, False),
        "BodyS3Location": (BodyS3Location, False),
        "CorsConfiguration": (Cors, False),
        "CredentialsArn": (str, False),
        "Description": (str, False),
        "DisableExecuteApiEndpoint": (boolean, False),
        "DisableSchemaValidation": (boolean, False),
        "FailOnWarnings": (boolean, False),
        "Name": (str, False),
        "ProtocolType": (str, False),
        "RouteKey": (str, False),
        "RouteSelectionExpression": (str, False),
        "Tags": (dict, False),
        "Target": (str, False),
        "Version": (str, False),
    }


class ApiMapping(AWSObject):
    resource_type = "AWS::ApiGatewayV2::ApiMapping"

    props = {
        "ApiId": (str, True),
        "ApiMappingKey": (str, False),
        "DomainName": (str, True),
        "Stage": (str, True),
    }


class JWTConfiguration(AWSProperty):
    props = {
        "Audience": ([str], False),
        "Issuer": (str, False),
    }


class Authorizer(AWSObject):
    resource_type = "AWS::ApiGatewayV2::Authorizer"

    props = {
        "ApiId": (str, True),
        "AuthorizerCredentialsArn": (str, False),
        "AuthorizerPayloadFormatVersion": (str, False),
        "AuthorizerResultTtlInSeconds": (validate_authorizer_ttl, False),
        "AuthorizerType": (validate_authorizer_type, True),
        "AuthorizerUri": (str, False),
        "EnableSimpleResponses": (boolean, False),
        "IdentitySource": ([str], True),
        "IdentityValidationExpression": (str, False),
        "JwtConfiguration": (JWTConfiguration, False),
        "Name": (str, True),
    }


class Deployment(AWSObject):
    resource_type = "AWS::ApiGatewayV2::Deployment"

    props = {
        "ApiId": (str, True),
        "Description": (str, False),
        "StageName": (str, False),
    }


class DomainNameConfiguration(AWSProperty):
    props = {
        "CertificateArn": (str, False),
        "CertificateName": (str, False),
        "EndpointType": (str, False),
    }


class MutualTlsAuthentication(AWSProperty):
    props = {
        "TruststoreUri": (str, False),
        "TruststoreVersion": (str, False),
    }


class DomainName(AWSObject):
    resource_type = "AWS::ApiGatewayV2::DomainName"

    props = {
        "DomainName": (str, True),
        "DomainNameConfigurations": ([DomainNameConfiguration], False),
        "MutualTlsAuthentication": (MutualTlsAuthentication, False),
        "Tags": (dict, False),
    }


class TlsConfig(AWSProperty):
    props = {
        "ServerNameToVerify": (str, False),
    }


class Integration(AWSObject):
    resource_type = "AWS::ApiGatewayV2::Integration"

    props = {
        "ApiId": (str, True),
        "ConnectionType": (str, False),
        "ConnectionId": (str, False),
        "ContentHandlingStrategy": (validate_content_handling_strategy, False),
        "CredentialsArn": (str, False),
        "Description": (str, False),
        "IntegrationMethod": (str, False),
        "IntegrationSubtype": (str, False),
        "IntegrationType": (validate_integration_type, True),
        "IntegrationUri": (str, False),
        "PassthroughBehavior": (validate_passthrough_behavior, False),
        "PayloadFormatVersion": (str, False),
        "RequestParameters": (dict, False),
        "RequestTemplates": (dict, False),
        "TemplateSelectionExpression": (str, False),
        "TimeoutInMillis": (integer_range(50, 29000), False),
        "TlsConfig": (TlsConfig, False),
    }


class IntegrationResponse(AWSObject):
    resource_type = "AWS::ApiGatewayV2::IntegrationResponse"

    props = {
        "ApiId": (str, True),
        "ContentHandlingStrategy": (validate_content_handling_strategy, False),
        "IntegrationId": (str, True),
        "IntegrationResponseKey": (str, True),
        "ResponseParameters": (dict, False),
        "ResponseTemplates": (dict, False),
        "TemplateSelectionExpression": (str, False),
    }


class Model(AWSObject):
    resource_type = "AWS::ApiGatewayV2::Model"

    props = {
        "ApiId": (str, True),
        "ContentType": (str, False),
        "Description": (str, False),
        "Name": (str, True),
        "Schema": ((str, dict), True),
    }

    def validate(self):
        name = "Schema"
        if name in self.properties:
            schema = self.properties.get(name)
            self.properties[name] = json_checker(schema)


class Route(AWSObject):
    resource_type = "AWS::ApiGatewayV2::Route"

    props = {
        "ApiId": (str, True),
        "ApiKeyRequired": (boolean, False),
        "AuthorizationScopes": ([str], False),
        "AuthorizationType": (str, False),
        "AuthorizerId": (str, False),
        "ModelSelectionExpression": (str, False),
        "OperationName": (str, False),
        "RequestModels": (dict, False),
        "RequestParameters": (dict, False),
        "RouteKey": (str, True),
        "RouteResponseSelectionExpression": (str, False),
        "Target": (str, False),
    }


class RouteResponse(AWSObject):
    resource_type = "AWS::ApiGatewayV2::RouteResponse"

    props = {
        "ApiId": (str, True),
        "ModelSelectionExpression": (str, False),
        "ResponseModels": (dict, False),
        "ResponseParameters": (dict, False),
        "RouteId": (str, True),
        "RouteResponseKey": (str, True),
    }


class AccessLogSettings(AWSProperty):
    props = {
        "DestinationArn": (str, False),
        "Format": (str, False),
    }


class RouteSettings(AWSProperty):
    props = {
        "DataTraceEnabled": (boolean, False),
        "DetailedMetricsEnabled": (boolean, False),
        "LoggingLevel": (validate_logging_level, False),
        "ThrottlingBurstLimit": (integer, False),
        "ThrottlingRateLimit": (double, False),
    }


class Stage(AWSObject):
    resource_type = "AWS::ApiGatewayV2::Stage"

    props = {
        "AccessLogSettings": (AccessLogSettings, False),
        "ApiId": (str, True),
        "AutoDeploy": (boolean, False),
        "ClientCertificateId": (str, False),
        "DefaultRouteSettings": (RouteSettings, False),
        "DeploymentId": (str, False),
        "Description": (str, False),
        "RouteSettings": (dict, False),
        "StageName": (str, True),
        "StageVariables": (dict, False),
        "Tags": (dict, False),
    }


class VpcLink(AWSObject):
    resource_type = "AWS::ApiGatewayV2::VpcLink"

    props = {
        "Name": (str, True),
        "SecurityGroupIds": ([str], False),
        "SubnetIds": ([str], True),
        "Tags": (dict, False),
    }
