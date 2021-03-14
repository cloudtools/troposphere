# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer, network_port, positive_integer


CDC = "cdc"
FULL_LOAD = "full-load"
FULL_LOAD_AND_CDC = "full-load-and-cdc"


class Certificate(AWSObject):
    resource_type = "AWS::DMS::Certificate"

    props = {
        'CertificateIdentifier': (basestring, False),
        'CertificatePem': (basestring, False),
        'CertificateWallet': (basestring, False),
    }


class DocDbSettings(AWSProperty):
    props = {
        'SecretsManagerAccessRoleArn': (basestring, False),
        'SecretsManagerSecretId': (basestring, False),
    }


class DynamoDbSettings(AWSProperty):
    props = {
        'ServiceAccessRoleArn': (basestring, False),
    }


class ElasticsearchSettings(AWSProperty):
    props = {
        'EndpointUri': (basestring, False),
        'ErrorRetryDuration': (integer, False),
        'FullLoadErrorPercentage': (integer, False),
        'ServiceAccessRoleArn': (basestring, False),
    }


class IbmDb2Settings(AWSProperty):
    props = {
        'SecretsManagerAccessRoleArn': (basestring, False),
        'SecretsManagerSecretId': (basestring, False),
    }


class KafkaSettings(AWSProperty):
    props = {
        'Broker': (basestring, False),
        'Topic': (basestring, False),
    }


class KinesisSettings(AWSProperty):
    props = {
        'MessageFormat': (basestring, False),
        'ServiceAccessRoleArn': (basestring, False),
        'StreamArn': (basestring, False),
    }


class MicrosoftSqlServerSettings(AWSProperty):
    props = {
        'SecretsManagerAccessRoleArn': (basestring, False),
        'SecretsManagerSecretId': (basestring, False),
    }


class MongoDbSettings(AWSProperty):
    props = {
        'AuthMechanism': (basestring, False),
        'AuthSource': (basestring, False),
        'AuthType': (basestring, False),
        'DatabaseName': (basestring, False),
        'DocsToInvestigate': (basestring, False),
        'ExtractDocId': (basestring, False),
        'NestingLevel': (basestring, False),
        'Password': (basestring, False),
        'Port': (network_port, False),
        'SecretsManagerAccessRoleArn': (basestring, False),
        'SecretsManagerSecretId': (basestring, False),
        'ServerName': (basestring, False),
        'Username': (basestring, False),
    }


class MySqlSettings(AWSProperty):
    props = {
        'SecretsManagerAccessRoleArn': (basestring, False),
        'SecretsManagerSecretId': (basestring, False),
    }


class NeptuneSettings(AWSProperty):
    props = {
        'ErrorRetryDuration': (integer, False),
        'IamAuthEnabled': (boolean, False),
        'MaxFileSize': (integer, False),
        'MaxRetryCount': (integer, False),
        'S3BucketFolder': (basestring, False),
        'S3BucketName': (basestring, False),
        'ServiceAccessRoleArn': (basestring, False),
    }


class OracleSettings(AWSProperty):
    props = {
        'SecretsManagerAccessRoleArn': (basestring, False),
        'SecretsManagerOracleAsmAccessRoleArn': (basestring, False),
        'SecretsManagerOracleAsmSecretId': (basestring, False),
        'SecretsManagerSecretId': (basestring, False),
    }


class PostgreSqlSettings(AWSProperty):
    props = {
        'SecretsManagerAccessRoleArn': (basestring, False),
        'SecretsManagerSecretId': (basestring, False),
    }


class RedshiftSettings(AWSProperty):
    props = {
        'SecretsManagerAccessRoleArn': (basestring, False),
        'SecretsManagerSecretId': (basestring, False),
    }


class S3Settings(AWSProperty):
    props = {
        'BucketFolder': (basestring, False),
        'BucketName': (basestring, False),
        'CompressionType': (basestring, False),
        'CsvDelimiter': (basestring, False),
        'CsvRowDelimiter': (basestring, False),
        'ExternalTableDefinition': (basestring, False),
        'ServiceAccessRoleArn': (basestring, False),
    }


class SybaseSettings(AWSProperty):
    props = {
        'SecretsManagerAccessRoleArn': (basestring, False),
        'SecretsManagerSecretId': (basestring, False),
    }


class Endpoint(AWSObject):
    resource_type = "AWS::DMS::Endpoint"

    props = {
        'CertificateArn': (basestring, False),
        'DatabaseName': (basestring, False),
        'DocDbSettings': (DocDbSettings, False),
        'DynamoDbSettings': (DynamoDbSettings, False),
        'ElasticsearchSettings': (ElasticsearchSettings, False),
        'EndpointIdentifier': (basestring, False),
        'EndpointType': (basestring, True),
        'EngineName': (basestring, True),
        'ExtraConnectionAttributes': (basestring, False),
        'IbmDb2Settings': (IbmDb2Settings, False),
        'KafkaSettings': (KafkaSettings, False),
        'KinesisSettings': (KinesisSettings, False),
        'KmsKeyId': (basestring, False),
        'MicrosoftSqlServerSettings': (MicrosoftSqlServerSettings, False),
        'MongoDbSettings': (MongoDbSettings, False),
        'MySqlSettings': (MySqlSettings, False),
        'NeptuneSettings': (NeptuneSettings, False),
        'OracleSettings': (OracleSettings, False),
        'Password': (basestring, False),
        'Port': (network_port, False),
        'PostgreSqlSettings': (PostgreSqlSettings, False),
        'RedshiftSettings': (RedshiftSettings, False),
        'S3Settings': (S3Settings, False),
        'ServerName': (basestring, False),
        'SslMode': (basestring, False),
        'SybaseSettings': (SybaseSettings, False),
        'Tags': (Tags, False),
        'Username': (basestring, False),
    }


class EventSubscription(AWSObject):
    resource_type = "AWS::DMS::EventSubscription"

    props = {
        'Enabled': (boolean, False),
        'EventCategories': ([basestring], False),
        'SnsTopicArn': (basestring, True),
        'SourceIds': ([basestring], False),
        'SourceType': (basestring, False),
        'SubscriptionName': (basestring, False),
        'Tags': (Tags, False),
    }


class ReplicationInstance(AWSObject):
    resource_type = "AWS::DMS::ReplicationInstance"

    props = {
        'AllocatedStorage': (integer, False),
        'AllowMajorVersionUpgrade': (boolean, False),
        'AutoMinorVersionUpgrade': (boolean, False),
        'AvailabilityZone': (basestring, False),
        'EngineVersion': (basestring, False),
        'KmsKeyId': (basestring, False),
        'MultiAZ': (boolean, False),
        'PreferredMaintenanceWindow': (basestring, False),
        'PubliclyAccessible': (boolean, False),
        'ReplicationInstanceClass': (basestring, True),
        'ReplicationInstanceIdentifier': (basestring, False),
        'ReplicationSubnetGroupIdentifier': (basestring, False),
        'Tags': (Tags, False),
        'VpcSecurityGroupIds': ([basestring], False),
    }


class ReplicationSubnetGroup(AWSObject):
    resource_type = "AWS::DMS::ReplicationSubnetGroup"

    props = {
        'ReplicationSubnetGroupDescription': (basestring, True),
        'ReplicationSubnetGroupIdentifier': (basestring, False),
        'SubnetIds': ([basestring], True),
        'Tags': (Tags, False),
    }


class ReplicationTask(AWSObject):
    resource_type = "AWS::DMS::ReplicationTask"

    props = {
        'CdcStartPosition': (basestring, False),
        'CdcStartTime': (positive_integer, False),
        'CdcStopPosition': (basestring, False),
        'MigrationType': (basestring, True),
        'ReplicationInstanceArn': (basestring, True),
        'ReplicationTaskIdentifier': (basestring, False),
        'ReplicationTaskSettings': (basestring, False),
        'SourceEndpointArn': (basestring, True),
        'TableMappings': (basestring, True),
        'Tags': (Tags, False),
        'TargetEndpointArn': (basestring, True),
        'TaskData': (basestring, False),
    }
