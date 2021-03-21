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
        'ApiCachingBehavior': (str, True),
        'ApiId': (str, True),
        'AtRestEncryptionEnabled': (boolean, False),
        'TransitEncryptionEnabled': (boolean, False),
        'Ttl': (double, True),
        'Type': (str, True),
    }


class ApiKey(AWSObject):
    resource_type = "AWS::AppSync::ApiKey"

    props = {
        'ApiId': (str, True),
        'ApiKeyId': (str, False),
        'Description': (str, False),
        'Expires': (double, False),
    }


class DeltaSyncConfig(AWSProperty):
    props = {
        'BaseTableTTL': (str, True),
        'DeltaSyncTableName': (str, True),
        'DeltaSyncTableTTL': (str, True),
    }


class DynamoDBConfig(AWSProperty):
    props = {
        'AwsRegion': (str, True),
        'DeltaSyncConfig': (DeltaSyncConfig, False),
        'TableName': (str, True),
        'UseCallerCredentials': (boolean, False),
        'Versioned': (boolean, False),
    }


class ElasticsearchConfig(AWSProperty):
    props = {
        'AwsRegion': (str, True),
        'Endpoint': (str, True),
    }


class AwsIamConfig(AWSProperty):
    props = {
        'SigningRegion': (str, False),
        'SigningServiceName': (str, False),
    }


class AuthorizationConfig(AWSProperty):
    props = {
        'AuthorizationType': (str, True),
        'AwsIamConfig': (AwsIamConfig, False),
    }


class HttpConfig(AWSProperty):
    props = {
        'AuthorizationConfig': (AuthorizationConfig, False),
        'Endpoint': (str, True),
    }


class LambdaConfig(AWSProperty):
    props = {
        'LambdaFunctionArn': (str, True),
    }


class RdsHttpEndpointConfig(AWSProperty):
    props = {
        'AwsRegion': (str, True),
        'AwsSecretStoreArn': (str, True),
        'DatabaseName': (str, False),
        'DbClusterIdentifier': (str, True),
        'Schema': (str, False),
    }


class RelationalDatabaseConfig(AWSProperty):
    props = {
        'RdsHttpEndpointConfig': (RdsHttpEndpointConfig, False),
        'RelationalDatasourceType': (str, True),
    }


class DataSource(AWSObject):
    resource_type = "AWS::AppSync::DataSource"

    props = {
        'ApiId': (str, True),
        'Description': (str, False),
        'DynamoDBConfig': (DynamoDBConfig, False),
        'ElasticsearchConfig': (ElasticsearchConfig, False),
        'HttpConfig': (HttpConfig, False),
        'LambdaConfig': (LambdaConfig, False),
        'Name': (str, True),
        'RelationalDatabaseConfig': (RelationalDatabaseConfig, False),
        'ServiceRoleArn': (str, False),
        'Type': (str, True),
    }


class FunctionConfiguration(AWSObject):
    resource_type = "AWS::AppSync::FunctionConfiguration"

    props = {
        'ApiId': (str, True),
        'DataSourceName': (str, True),
        'Description': (str, False),
        'FunctionVersion': (str, True),
        'Name': (str, True),
        'RequestMappingTemplate': (str, False),
        'RequestMappingTemplateS3Location': (str, False),
        'ResponseMappingTemplate': (str, False),
        'ResponseMappingTemplateS3Location': (str, False),
    }


class CognitoUserPoolConfig(AWSProperty):
    props = {
        'AppIdClientRegex': (str, False),
        'AwsRegion': (str, False),
        'UserPoolId': (str, False),
    }


class OpenIDConnectConfig(AWSProperty):
    props = {
        'AuthTTL': (double, False),
        'ClientId': (str, False),
        'IatTTL': (double, False),
        'Issuer': (str, False),
    }


class AdditionalAuthenticationProvider(AWSProperty):
    props = {
        'AuthenticationType': (str, True),
        'OpenIDConnectConfig': (OpenIDConnectConfig, False),
        'UserPoolConfig': (CognitoUserPoolConfig, False),
    }


class LogConfig(AWSProperty):
    props = {
        'CloudWatchLogsRoleArn': (str, False),
        'ExcludeVerboseContent': (boolean, False),
        'FieldLogLevel': (str, False),
    }


class UserPoolConfig(AWSProperty):
    props = {
        'AppIdClientRegex': (str, False),
        'AwsRegion': (str, False),
        'DefaultAction': (str, False),
        'UserPoolId': (str, False),
    }


class GraphQLApi(AWSObject):
    resource_type = "AWS::AppSync::GraphQLApi"

    props = {
        'AdditionalAuthenticationProviders':
            ([AdditionalAuthenticationProvider], False),
        'AuthenticationType': (str, True),
        'LogConfig': (LogConfig, False),
        'Name': (str, True),
        'OpenIDConnectConfig': (OpenIDConnectConfig, False),
        'Tags': (Tags, False),
        'UserPoolConfig': (UserPoolConfig, False),
        'XrayEnabled': (boolean, False),
    }


class GraphQLSchema(AWSObject):
    resource_type = "AWS::AppSync::GraphQLSchema"

    props = {
        'ApiId': (str, True),
        'Definition': (str, False),
        'DefinitionS3Location': (str, False),
    }


class CachingConfig(AWSProperty):
    props = {
        'CachingKeys': ([str], False),
        'Ttl': (double, False),
    }


class PipelineConfig(AWSProperty):
    props = {
        'Functions': ([str], False),
    }


class LambdaConflictHandlerConfig(AWSProperty):
    props = {
        'LambdaConflictHandlerArn': (str, False),
    }


class SyncConfig(AWSProperty):
    props = {
        'ConflictDetection': (str, True),
        'ConflictHandler': (str, False),
        'LambdaConflictHandlerConfig': (LambdaConflictHandlerConfig, False),
    }


class Resolver(AWSObject):
    resource_type = "AWS::AppSync::Resolver"

    props = {
        'ApiId': (str, True),
        'CachingConfig': (CachingConfig, False),
        'DataSourceName': (str, False),
        'FieldName': (str, True),
        'Kind': (resolver_kind_validator, False),
        'PipelineConfig': (PipelineConfig, False),
        'RequestMappingTemplate': (str, False),
        'RequestMappingTemplateS3Location': (str, False),
        'ResponseMappingTemplate': (str, False),
        'ResponseMappingTemplateS3Location': (str, False),
        'SyncConfig': (SyncConfig, False),
        'TypeName': (str, True),
    }
