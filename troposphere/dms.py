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
        'CertificateIdentifier': (str, False),
        'CertificatePem': (str, False),
        'CertificateWallet': (str, False),
    }


class DocDbSettings(AWSProperty):
    props = {
        'SecretsManagerAccessRoleArn': (str, False),
        'SecretsManagerSecretId': (str, False),
    }


class DynamoDbSettings(AWSProperty):
    props = {
        'ServiceAccessRoleArn': (str, False),
    }


class ElasticsearchSettings(AWSProperty):
    props = {
        'EndpointUri': (str, False),
        'ErrorRetryDuration': (integer, False),
        'FullLoadErrorPercentage': (integer, False),
        'ServiceAccessRoleArn': (str, False),
    }


class IbmDb2Settings(AWSProperty):
    props = {
        'SecretsManagerAccessRoleArn': (str, False),
        'SecretsManagerSecretId': (str, False),
    }


class KafkaSettings(AWSProperty):
    props = {
        'Broker': (str, False),
        'Topic': (str, False),
    }


class KinesisSettings(AWSProperty):
    props = {
        'MessageFormat': (str, False),
        'ServiceAccessRoleArn': (str, False),
        'StreamArn': (str, False),
    }


class MicrosoftSqlServerSettings(AWSProperty):
    props = {
        'SecretsManagerAccessRoleArn': (str, False),
        'SecretsManagerSecretId': (str, False),
    }


class MongoDbSettings(AWSProperty):
    props = {
        'AuthMechanism': (str, False),
        'AuthSource': (str, False),
        'AuthType': (str, False),
        'DatabaseName': (str, False),
        'DocsToInvestigate': (str, False),
        'ExtractDocId': (str, False),
        'NestingLevel': (str, False),
        'Password': (str, False),
        'Port': (network_port, False),
        'SecretsManagerAccessRoleArn': (str, False),
        'SecretsManagerSecretId': (str, False),
        'ServerName': (str, False),
        'Username': (str, False),
    }


class MySqlSettings(AWSProperty):
    props = {
        'SecretsManagerAccessRoleArn': (str, False),
        'SecretsManagerSecretId': (str, False),
    }


class NeptuneSettings(AWSProperty):
    props = {
        'ErrorRetryDuration': (integer, False),
        'IamAuthEnabled': (boolean, False),
        'MaxFileSize': (integer, False),
        'MaxRetryCount': (integer, False),
        'S3BucketFolder': (str, False),
        'S3BucketName': (str, False),
        'ServiceAccessRoleArn': (str, False),
    }


class OracleSettings(AWSProperty):
    props = {
        'SecretsManagerAccessRoleArn': (str, False),
        'SecretsManagerOracleAsmAccessRoleArn': (str, False),
        'SecretsManagerOracleAsmSecretId': (str, False),
        'SecretsManagerSecretId': (str, False),
    }


class PostgreSqlSettings(AWSProperty):
    props = {
        'SecretsManagerAccessRoleArn': (str, False),
        'SecretsManagerSecretId': (str, False),
    }


class RedshiftSettings(AWSProperty):
    props = {
        'SecretsManagerAccessRoleArn': (str, False),
        'SecretsManagerSecretId': (str, False),
    }


class S3Settings(AWSProperty):
    props = {
        'BucketFolder': (str, False),
        'BucketName': (str, False),
        'CompressionType': (str, False),
        'CsvDelimiter': (str, False),
        'CsvRowDelimiter': (str, False),
        'ExternalTableDefinition': (str, False),
        'ServiceAccessRoleArn': (str, False),
    }


class SybaseSettings(AWSProperty):
    props = {
        'SecretsManagerAccessRoleArn': (str, False),
        'SecretsManagerSecretId': (str, False),
    }


class Endpoint(AWSObject):
    resource_type = "AWS::DMS::Endpoint"

    props = {
        'CertificateArn': (str, False),
        'DatabaseName': (str, False),
        'DocDbSettings': (DocDbSettings, False),
        'DynamoDbSettings': (DynamoDbSettings, False),
        'ElasticsearchSettings': (ElasticsearchSettings, False),
        'EndpointIdentifier': (str, False),
        'EndpointType': (str, True),
        'EngineName': (str, True),
        'ExtraConnectionAttributes': (str, False),
        'IbmDb2Settings': (IbmDb2Settings, False),
        'KafkaSettings': (KafkaSettings, False),
        'KinesisSettings': (KinesisSettings, False),
        'KmsKeyId': (str, False),
        'MicrosoftSqlServerSettings': (MicrosoftSqlServerSettings, False),
        'MongoDbSettings': (MongoDbSettings, False),
        'MySqlSettings': (MySqlSettings, False),
        'NeptuneSettings': (NeptuneSettings, False),
        'OracleSettings': (OracleSettings, False),
        'Password': (str, False),
        'Port': (network_port, False),
        'PostgreSqlSettings': (PostgreSqlSettings, False),
        'RedshiftSettings': (RedshiftSettings, False),
        'S3Settings': (S3Settings, False),
        'ServerName': (str, False),
        'SslMode': (str, False),
        'SybaseSettings': (SybaseSettings, False),
        'Tags': (Tags, False),
        'Username': (str, False),
    }


class EventSubscription(AWSObject):
    resource_type = "AWS::DMS::EventSubscription"

    props = {
        'Enabled': (boolean, False),
        'EventCategories': ([str], False),
        'SnsTopicArn': (str, True),
        'SourceIds': ([str], False),
        'SourceType': (str, False),
        'SubscriptionName': (str, False),
        'Tags': (Tags, False),
    }


class ReplicationInstance(AWSObject):
    resource_type = "AWS::DMS::ReplicationInstance"

    props = {
        'AllocatedStorage': (integer, False),
        'AllowMajorVersionUpgrade': (boolean, False),
        'AutoMinorVersionUpgrade': (boolean, False),
        'AvailabilityZone': (str, False),
        'EngineVersion': (str, False),
        'KmsKeyId': (str, False),
        'MultiAZ': (boolean, False),
        'PreferredMaintenanceWindow': (str, False),
        'PubliclyAccessible': (boolean, False),
        'ReplicationInstanceClass': (str, True),
        'ReplicationInstanceIdentifier': (str, False),
        'ReplicationSubnetGroupIdentifier': (str, False),
        'Tags': (Tags, False),
        'VpcSecurityGroupIds': ([str], False),
    }


class ReplicationSubnetGroup(AWSObject):
    resource_type = "AWS::DMS::ReplicationSubnetGroup"

    props = {
        'ReplicationSubnetGroupDescription': (str, True),
        'ReplicationSubnetGroupIdentifier': (str, False),
        'SubnetIds': ([str], True),
        'Tags': (Tags, False),
    }


class ReplicationTask(AWSObject):
    resource_type = "AWS::DMS::ReplicationTask"

    props = {
        'CdcStartPosition': (str, False),
        'CdcStartTime': (positive_integer, False),
        'CdcStopPosition': (str, False),
        'MigrationType': (str, True),
        'ReplicationInstanceArn': (str, True),
        'ReplicationTaskIdentifier': (str, False),
        'ReplicationTaskSettings': (str, False),
        'SourceEndpointArn': (str, True),
        'TableMappings': (str, True),
        'Tags': (Tags, False),
        'TargetEndpointArn': (str, True),
        'TaskData': (str, False),
    }
