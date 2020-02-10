# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import AWSObject
from . import AWSProperty
from troposphere import Tags
from .validators import boolean
from .validators import double


def resolver_kind_validator(x):
    valid_types = ["UNIT", "PIPELINE"]
    if x not in valid_types:
        raise ValueError("Kind must be one of: %s" % ", ".join(valid_types))
    return x


class ApiCache(AWSObject):
    resource_type = "AWS::AppSync::ApiCache"

    props = {
        'ApiCachingBehavior': (basestring, True),
        'ApiId': (basestring, True),
        'AtRestEncryptionEnabled': (boolean, False),
        'TransitEncryptionEnabled': (boolean, False),
        'Ttl': (double, True),
        'Type': (basestring, True),
    }


class ApiKey(AWSObject):
    resource_type = "AWS::AppSync::ApiKey"

    props = {
        'ApiId': (basestring, True),
        'Description': (basestring, False),
        'Expires': (double, False),
    }


class DeltaSyncConfig(AWSProperty):
    props = {
        'BaseTableTTL': (basestring, True),
        'DeltaSyncTableName': (basestring, True),
        'DeltaSyncTableTTL': (basestring, True),
    }


class DynamoDBConfig(AWSProperty):
    props = {
        'AwsRegion': (basestring, True),
        'DeltaSyncConfig': (DeltaSyncConfig, False),
        'TableName': (basestring, True),
        'UseCallerCredentials': (boolean, False),
        'Versioned': (boolean, False),
    }


class ElasticsearchConfig(AWSProperty):
    props = {
        'AwsRegion': (basestring, True),
        'Endpoint': (basestring, True),
    }


class AwsIamConfig(AWSProperty):
    props = {
        'SigningRegion': (basestring, False),
        'SigningServiceName': (basestring, False),
    }


class AuthorizationConfig(AWSProperty):
    props = {
        'AuthorizationType': (basestring, True),
        'AwsIamConfig': (AwsIamConfig, False),
    }


class HttpConfig(AWSProperty):
    props = {
        'AuthorizationConfig': (AuthorizationConfig, False),
        'Endpoint': (basestring, True),
    }


class LambdaConfig(AWSProperty):
    props = {
        'LambdaFunctionArn': (basestring, True),
    }


class RdsHttpEndpointConfig(AWSProperty):
    props = {
        'AwsRegion': (basestring, True),
        'AwsSecretStoreArn': (basestring, True),
        'DatabaseName': (basestring, False),
        'DbClusterIdentifier': (basestring, True),
        'Schema': (basestring, False),
    }


class RelationalDatabaseConfig(AWSProperty):
    props = {
        'RdsHttpEndpointConfig': (RdsHttpEndpointConfig, False),
        'RelationalDatasourceType': (basestring, True),
    }


class DataSource(AWSObject):
    resource_type = "AWS::AppSync::DataSource"

    props = {
        'ApiId': (basestring, True),
        'Description': (basestring, False),
        'DynamoDBConfig': (DynamoDBConfig, False),
        'ElasticsearchConfig': (ElasticsearchConfig, False),
        'HttpConfig': (HttpConfig, False),
        'LambdaConfig': (LambdaConfig, False),
        'Name': (basestring, True),
        'RelationalDatabaseConfig': (RelationalDatabaseConfig, False),
        'ServiceRoleArn': (basestring, False),
        'Type': (basestring, True),
    }


class FunctionConfiguration(AWSObject):
    resource_type = "AWS::AppSync::FunctionConfiguration"

    props = {
        'ApiId': (basestring, True),
        'DataSourceName': (basestring, True),
        'Description': (basestring, False),
        'FunctionVersion': (basestring, True),
        'Name': (basestring, True),
        'RequestMappingTemplate': (basestring, False),
        'RequestMappingTemplateS3Location': (basestring, False),
        'ResponseMappingTemplate': (basestring, False),
        'ResponseMappingTemplateS3Location': (basestring, False),
    }


class CognitoUserPoolConfig(AWSProperty):
    props = {
        'AppIdClientRegex': (basestring, False),
        'AwsRegion': (basestring, False),
        'UserPoolId': (basestring, False),
    }


class OpenIDConnectConfig(AWSProperty):
    props = {
        'AuthTTL': (double, False),
        'ClientId': (basestring, False),
        'IatTTL': (double, False),
        'Issuer': (basestring, False),
    }


class AdditionalAuthenticationProvider(AWSProperty):
    props = {
        'AuthenticationType': (basestring, True),
        'OpenIDConnectConfig': (OpenIDConnectConfig, False),
        'UserPoolConfig': (CognitoUserPoolConfig, False),
    }


class LogConfig(AWSProperty):
    props = {
        'CloudWatchLogsRoleArn': (basestring, False),
        'ExcludeVerboseContent': (boolean, False),
        'FieldLogLevel': (basestring, False),
    }


class UserPoolConfig(AWSProperty):
    props = {
        'AppIdClientRegex': (basestring, False),
        'AwsRegion': (basestring, False),
        'DefaultAction': (basestring, False),
        'UserPoolId': (basestring, False),
    }


class GraphQLApi(AWSObject):
    resource_type = "AWS::AppSync::GraphQLApi"

    props = {
        'AdditionalAuthenticationProviders':
            ([AdditionalAuthenticationProvider], False),
        'AuthenticationType': (basestring, True),
        'LogConfig': (LogConfig, False),
        'Name': (basestring, True),
        'OpenIDConnectConfig': (OpenIDConnectConfig, False),
        'Tags': (Tags, False),
        'UserPoolConfig': (UserPoolConfig, False),
        'XrayEnabled': (boolean, False),
    }


class GraphQLSchema(AWSObject):
    resource_type = "AWS::AppSync::GraphQLSchema"

    props = {
        'ApiId': (basestring, True),
        'Definition': (basestring, False),
        'DefinitionS3Location': (basestring, False),
    }


class CachingConfig(AWSProperty):
    props = {
        'CachingKeys': ([basestring], False),
        'Ttl': (double, False),
    }


class PipelineConfig(AWSProperty):
    props = {
        'Functions': ([basestring], False),
    }


class LambdaConflictHandlerConfig(AWSProperty):
    props = {
        'LambdaConflictHandlerArn': (basestring, False),
    }


class SyncConfig(AWSProperty):
    props = {
        'ConflictDetection': (basestring, True),
        'ConflictHandler': (basestring, False),
        'LambdaConflictHandlerConfig': (LambdaConflictHandlerConfig, False),
    }


class Resolver(AWSObject):
    resource_type = "AWS::AppSync::Resolver"

    props = {
        'ApiId': (basestring, True),
        'CachingConfig': (CachingConfig, False),
        'DataSourceName': (basestring, False),
        'FieldName': (basestring, True),
        'Kind': (resolver_kind_validator, False),
        'PipelineConfig': (PipelineConfig, False),
        'RequestMappingTemplate': (basestring, False),
        'RequestMappingTemplateS3Location': (basestring, False),
        'ResponseMappingTemplate': (basestring, False),
        'ResponseMappingTemplateS3Location': (basestring, False),
        'SyncConfig': (SyncConfig, False),
        'TypeName': (basestring, True),
    }
