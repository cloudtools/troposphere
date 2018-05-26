# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, integer


class ApiKey(AWSObject):
    resource_type = "AWS::AppSync::ApiKey"

    props = {
        'ApiId': (basestring, True),
        'Description': (basestring, False),
        'Expires': (integer, False),
    }


class DynamoDBConfig(AWSProperty):
    props = {
        'AwsRegion': (basestring, True),
        'TableName': (basestring, True),
        'UseCallerCredentials': (boolean, False),
    }


class ElasticsearchConfig(AWSProperty):
    props = {
        'AwsRegion': (basestring, True),
        'Endpoint': (basestring, True),
    }


class LambdaConfig(AWSProperty):
    props = {
        'LambdaFunctionArn': (basestring, True),
    }


class DataSource(AWSObject):
    resource_type = "AWS::AppSync::DataSource"

    props = {
        'ApiId': (basestring, True),
        'Description': (basestring, False),
        'DynamoDBConfig': (DynamoDBConfig, False),
        'ElasticsearchConfig': (ElasticsearchConfig, False),
        'LambdaConfig': (LambdaConfig, False),
        'Name': (basestring, True),
        'ServiceRoleArn': (basestring, False),
        'Type': (basestring, True),
    }


class LogConfig(AWSProperty):
    props = {
        'CloudWatchLogsRoleArn': (basestring, False),
        'FieldLogLevel': (basestring, False),
    }


class OpenIDConnectConfig(AWSProperty):
    props = {
        'AuthTTL': (float, False),
        'ClientId': (basestring, False),
        'IatTTL': (float, False),
        'Issuer': (basestring, True),
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
        'AuthenticationType': (basestring, True),
        'LogConfig': (LogConfig, False),
        'Name': (basestring, True),
        'OpenIDConnectConfig': (OpenIDConnectConfig, False),
        'UserPoolConfig': (UserPoolConfig, False),
    }


class GraphQLSchema(AWSObject):
    resource_type = "AWS::AppSync::GraphQLSchema"

    props = {
        'ApiId': (basestring, True),
        'Definition': (basestring, False),
        'DefinitionS3Location': (basestring, False),
    }


class Resolver(AWSObject):
    resource_type = "AWS::AppSync::Resolver"

    props = {
        'ApiId': (basestring, True),
        'DataSourceName': (basestring, True),
        'FieldName': (basestring, True),
        'RequestMappingTemplate': (basestring, False),
        'RequestMappingTemplateS3Location': (basestring, False),
        'ResponseMappingTemplate': (basestring, False),
        'ResponseMappingTemplateS3Location': (basestring, False),
        'TypeName': (basestring, True),
    }
