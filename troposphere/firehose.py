# Copyright (c) 2016-2017, troposphere project
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, integer, positive_integer


def processor_type_validator(x):
    valid_types = ["Lambda"]
    if x not in valid_types:
        raise ValueError("Type must be one of: %s" %
                         ", ".join(valid_types))
    return x


def delivery_stream_type_validator(x):
    valid_types = ["DirectPut", "KinesisStreamAsSource"]
    if x not in valid_types:
        raise ValueError("DeliveryStreamType must be one of: %s" %
                         ", ".join(valid_types))
    return x


def index_rotation_period_validator(x):
    valid_types = ["NoRotation", "OneHour", "OneDay", "OneWeek", "OneMonth"]
    if x not in valid_types:
        raise ValueError("IndexRotationPeriod must be one of: %s" %
                         ", ".join(valid_types))
    return x


def s3_backup_mode_elastic_search_validator(x):
    valid_types = ["FailedDocumentsOnly", "AllDocuments"]
    if x not in valid_types:
        raise ValueError("S3BackupMode must be one of: %s" %
                         ", ".join(valid_types))
    return x


def s3_backup_mode_extended_s3_validator(x):
    valid_types = ["Disabled", "Enabled"]
    if x not in valid_types:
        raise ValueError("S3BackupMode must be one of: %s" %
                         ", ".join(valid_types))
    return x


class BufferingHints(AWSProperty):
    props = {
        'IntervalInSeconds': (positive_integer, True),
        'SizeInMBs': (positive_integer, True)
    }


class CloudWatchLoggingOptions(AWSProperty):
    props = {
        'Enabled': (boolean, False),
        'LogGroupName': (basestring, False),  # Conditional
        'LogStreamName': (basestring, False),  # Conditional
    }


class RetryOptions(AWSProperty):
    props = {
        'DurationInSeconds': (positive_integer, True),
    }


class KMSEncryptionConfig(AWSProperty):
    props = {
        'AWSKMSKeyARN': (basestring, True),
    }


class EncryptionConfiguration(AWSProperty):
    props = {
        'KMSEncryptionConfig': (KMSEncryptionConfig, False),
        'NoEncryptionConfig': (basestring, False),
    }


class S3Configuration(AWSProperty):
    props = {
        'BucketARN': (basestring, True),
        'BufferingHints': (BufferingHints, True),
        'CloudWatchLoggingOptions': (CloudWatchLoggingOptions, False),
        'CompressionFormat': (basestring, True),
        'EncryptionConfiguration': (EncryptionConfiguration, False),
        'Prefix': (basestring, False),
        'RoleARN': (basestring, True)
    }


class CopyCommand(AWSProperty):
    props = {
        'CopyOptions': (basestring, False),
        'DataTableColumns': (basestring, False),
        'DataTableName': (basestring, True),
    }


class ProcessorParameter(AWSProperty):
    props = {
        'ParameterName': (basestring, True),
        'ParameterValue': (basestring, True),
    }


class Processor(AWSProperty):
    props = {
        'Parameters': ([ProcessorParameter], True),
        'Type': (processor_type_validator, True),
    }


class ProcessingConfiguration(AWSProperty):
    props = {
        'Enabled': (boolean, True),
        'Processors': ([Processor], True),
    }


class VpcConfiguration(AWSProperty):
    props = {
        'RoleARN': (basestring, True),
        'SecurityGroupIds': ([basestring], True),
        'SubnetIds': ([basestring], True),
    }


class ElasticsearchDestinationConfiguration(AWSProperty):
    props = {
        'BufferingHints': (BufferingHints, True),
        'CloudWatchLoggingOptions': (CloudWatchLoggingOptions, False),
        'ClusterEndpoint': (basestring, False),
        'DomainARN': (basestring, True),
        'IndexName': (basestring, True),
        'IndexRotationPeriod': (index_rotation_period_validator, True),
        'ProcessingConfiguration': (ProcessingConfiguration, False),
        'RetryOptions': (RetryOptions, False),
        'RoleARN': (basestring, True),
        'S3BackupMode': (s3_backup_mode_elastic_search_validator, True),
        'S3Configuration': (S3Configuration, False),
        'TypeName': (basestring, False),
        'VpcConfiguration': (VpcConfiguration, False),
    }


class RedshiftDestinationConfiguration(AWSProperty):
    props = {
        'CloudWatchLoggingOptions': (CloudWatchLoggingOptions, False),
        'ClusterJDBCURL': (basestring, True),
        'CopyCommand': (CopyCommand, True),
        'Password': (basestring, True),
        'ProcessingConfiguration': (ProcessingConfiguration, False),
        'RoleARN': (basestring, True),
        'S3Configuration': (S3Configuration, True),
        'Username': (basestring, True),
    }


class S3DestinationConfiguration(AWSProperty):
    props = {
        'BucketARN': (basestring, True),
        'BufferingHints': (BufferingHints, False),
        'CloudWatchLoggingOptions': (CloudWatchLoggingOptions, False),
        'CompressionFormat': (basestring, False),
        'EncryptionConfiguration': (EncryptionConfiguration, False),
        'ErrorOutputPrefix': (basestring, False),
        'Prefix': (basestring, False),
        'RoleARN': (basestring, True),
    }


class HiveJsonSerDe(AWSProperty):
    props = {
        'TimestampFormats': ([basestring], False),
    }


class OpenXJsonSerDe(AWSProperty):
    props = {
        'CaseInsensitive': (boolean, False),
        'ColumnToJsonKeyMappings': (dict, False),
        'ConvertDotsInJsonKeysToUnderscores': (boolean, False),
    }


class Deserializer(AWSProperty):
    props = {
        'HiveJsonSerDe': (HiveJsonSerDe, False),
        'OpenXJsonSerDe': (OpenXJsonSerDe, False),
    }


class InputFormatConfiguration(AWSProperty):
    props = {
        'Deserializer': (Deserializer, True),
    }


class OrcSerDe(AWSProperty):
    props = {
        'BlockSizeBytes': (integer, False),
        'BloomFilterColumns': ([basestring], False),
        'BloomFilterFalsePositiveProbability': (float, False),
        'Compression': (basestring, False),
        'DictionaryKeyThreshold': (float, False),
        'EnablePadding': (boolean, False),
        'FormatVersion': (basestring, False),
        'PaddingTolerance': (float, False),
        'RowIndexStride': (integer, False),
        'StripeSizeBytes': (integer, False),
    }


class ParquetSerDe(AWSProperty):
    props = {
        'BlockSizeBytes': (integer, False),
        'Compression': (basestring, False),
        'EnableDictionaryCompression': (boolean, False),
        'MaxPaddingBytes': (integer, False),
        'PageSizeBytes': (integer, False),
        'WriterVersion': (basestring, False),
    }


class Serializer(AWSProperty):
    props = {
        'OrcSerDe': (OrcSerDe, False),
        'ParquetSerDe': (ParquetSerDe, False),
    }


class OutputFormatConfiguration(AWSProperty):
    props = {
        'Serializer': (Serializer, True),
    }


class SchemaConfiguration(AWSProperty):
    props = {
        'CatalogId': (basestring, True),
        'DatabaseName': (basestring, True),
        'Region': (basestring, True),
        'RoleARN': (basestring, True),
        'TableName': (basestring, True),
        'VersionId': (basestring, True),
    }


class DataFormatConversionConfiguration(AWSProperty):
    props = {
        'Enabled': (boolean, True),
        'InputFormatConfiguration': (InputFormatConfiguration, True),
        'OutputFormatConfiguration': (OutputFormatConfiguration, True),
        'SchemaConfiguration': (SchemaConfiguration, True),
    }


class ExtendedS3DestinationConfiguration(AWSProperty):
    props = {
        'BucketARN': (basestring, True),
        'BufferingHints': (BufferingHints, False),
        'CloudWatchLoggingOptions': (CloudWatchLoggingOptions, False),
        'CompressionFormat': (basestring, False),
        'DataFormatConversionConfiguration':
            (DataFormatConversionConfiguration, False),
        'EncryptionConfiguration': (EncryptionConfiguration, False),
        'ErrorOutputPrefix': (basestring, False),
        'Prefix': (basestring, False),
        'ProcessingConfiguration': (ProcessingConfiguration, False),
        'RoleARN': (basestring, True),
        'S3BackupConfiguration': (S3DestinationConfiguration, False),
        'S3BackupMode': (s3_backup_mode_extended_s3_validator, False),
    }


class KinesisStreamSourceConfiguration(AWSProperty):
    props = {
        'KinesisStreamARN': (basestring, True),
        'RoleARN': (basestring, True)
    }


class SplunkRetryOptions(AWSProperty):
    props = {
        'DurationInSeconds': (positive_integer, True),
    }


class SplunkDestinationConfiguration(AWSProperty):
    props = {
        'CloudWatchLoggingOptions': (CloudWatchLoggingOptions, False),
        'HECAcknowledgmentTimeoutInSeconds': (positive_integer, False),
        'HECEndpoint': (basestring, True),
        'HECEndpointType': (basestring, True),
        'HECToken': (basestring, True),
        'ProcessingConfiguration': (ProcessingConfiguration, False),
        'RetryOptions': (SplunkRetryOptions, False),
        'S3BackupMode': (basestring, False),
        'S3Configuration': (S3DestinationConfiguration, True),
    }


class DeliveryStream(AWSObject):
    resource_type = "AWS::KinesisFirehose::DeliveryStream"

    props = {
        'DeliveryStreamName': (basestring, False),
        'DeliveryStreamType': (delivery_stream_type_validator, False),
        'ElasticsearchDestinationConfiguration': (ElasticsearchDestinationConfiguration, False),  # noqa
        'ExtendedS3DestinationConfiguration': (ExtendedS3DestinationConfiguration, False),  # noqa
        'KinesisStreamSourceConfiguration': (KinesisStreamSourceConfiguration, False),  # noqa
        'RedshiftDestinationConfiguration': (RedshiftDestinationConfiguration, False),  # noqa
        'S3DestinationConfiguration': (S3DestinationConfiguration, False),
        'SplunkDestinationConfiguration':
            (SplunkDestinationConfiguration, False),
    }
