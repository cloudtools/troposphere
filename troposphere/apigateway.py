from . import AWSHelperFn, AWSObject, AWSProperty
from .validators import (
    positive_integer, defer, floatingpoint
)
import json

HTTP = 'HTTP'
AWS = 'AWS'
MOCK = 'MOCK'
HTTP_PROXY = 'HTTP_PROXY'
AWS_PROXY = 'AWS_PROXY'


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
        "AuthorizerUri": (defer, False),
        "IdentitySource": (basestring, True),
        "IdentityValidationExpression": (basestring, False),
        "Name": (basestring, True),
        "ProviderARNs": ([basestring], False),
        "RestApiId": (basestring, False),
        "Type": (basestring, True)
    }

    def validate(self):
        if 'Type' in self.properties:

            type_property = self.properties.get('Type', None)

            if 'TOKEN' in type_property:
                if 'AuthorizerUri' in self.properties:

                    authorizer_uri = self.properties.get('AuthorizerUri', None)

                    if not isinstance(authorizer_uri, basestring):
                            raise ValueError('AuthorizerUri value must'
                                             ' be a string')
                else:
                    raise ValueError('AuthorizerUri is required when'
                                     ' Type is set to TOKEN')


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
        "ThrottlingRateLimit": (floatingpoint, False)
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
        "ThrottlingRateLimit": (floatingpoint, False),
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

    def validate(self):
        if 'Type' in self.properties:

            valid_values = [
                HTTP,
                AWS,
                MOCK,
                HTTP_PROXY,
                AWS_PROXY,
            ]

            type_property = self.properties.get('Type', None)

            if type_property not in valid_values:
                raise ValueError('Only HTTP, AWS, MOCK, HTTP_PROXY,'
                                 ' and AWS_PROXY are valid values')

            if 'MOCK' not in type_property:
                if 'IntegrationHttpMethod' not in self.properties:
                    raise ValueError('IntegrationHttpMethod must be set when'
                                     ' Type is not defined as MOCK')


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
        "AuthorizerId": (defer, False),
        "HttpMethod": (basestring, True),
        "Integration": (Integration, False),
        "MethodResponses": ([MethodResponse], False),
        "RequestModels": (dict, False),
        "RequestParameters": (dict, False),
        "ResourceId": (basestring, True),
        "RestApiId": (basestring, True)
    }

    def validate(self):
        if 'AuthorizerId' in self.properties:
            if 'AuthorizationType' in self.properties:

                auth_type = self.properties.get('AuthorizationType', None)

                if 'CUSTOM' not in auth_type:
                    raise ValueError('AuthorizationType must be set to'
                                     'CUSTOM when AuthorizerId is defined')
            else:
                raise ValueError('AuthorizationType must be defined'
                                 ' when AuthorizerId is defined')


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
        if 'Schema' in self.properties:
            schema = self.properties.get('Schema')
            if isinstance(schema, basestring):
                # Verify it is a valid json string
                json.loads(schema)
            elif isinstance(schema, dict):
                # Convert the dict to a basestring
                self.properties['Schema'] = json.dumps(schema)
            elif isinstance(schema, AWSHelperFn):
                pass
            else:
                raise ValueError("Schema must be a str or dict")


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
        "Body": ((basestring, dict), False),
        "BodyS3Location": (S3Location, False),
        "CloneFrom": (basestring, False),
        "Description": (basestring, False),
        "FailOnWarnings": (bool, False),
        "Name": (basestring, False),
        "Parameters": ([basestring], False)
    }

    def validate(self):
        if 'Body' in self.properties:
            body = self.properties.get('Body')
            if isinstance(body, basestring):
                # Verify it is a valid json string
                json.loads(body)
            elif isinstance(body, dict):
                # Convert the dict to a basestring
                self.properties['Schema'] = json.dumps(body)
            elif isinstance(body, AWSHelperFn):
                pass
            else:
                raise ValueError("Body must be a str or dict")

        if 'Body' not in self.properties:
            if 'Name' not in self.properties:
                raise ValueError('Name must be defined when Body is undefined')


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
        "RateLimit": (floatingpoint, False),
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


class UsagePlanKey(AWSObject):
    resource_type = "AWS::ApiGateway::UsagePlanKey"

    props = {
        "KeyId": (basestring, True),
        "KeyType": (basestring, True),
        "UsagePlanId": (basestring, True),
    }
