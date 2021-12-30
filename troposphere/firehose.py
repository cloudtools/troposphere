# Copyright (c) 2016-2017, troposphere project
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer, positive_integer


def processor_type_validator(x):
    valid_types = [
        "Lambda",
        "MetadataExtraction",
        "RecordDeAggregation",
        "AppendDelimiterToRecord",
    ]
    if x not in valid_types:
        raise ValueError("Type must be one of: %s" % ", ".join(valid_types))
    return x


def delivery_stream_type_validator(x):
    valid_types = ["DirectPut", "KinesisStreamAsSource"]
    if x not in valid_types:
        raise ValueError(
            "DeliveryStreamType must be one of: %s" % ", ".join(valid_types)
        )
    return x


def index_rotation_period_validator(x):
    valid_types = ["NoRotation", "OneHour", "OneDay", "OneWeek", "OneMonth"]
    if x not in valid_types:
        raise ValueError(
            "IndexRotationPeriod must be one of: %s" % ", ".join(valid_types)
        )
    return x


def s3_backup_mode_elastic_search_validator(x):
    valid_types = ["FailedDocumentsOnly", "AllDocuments"]
    if x not in valid_types:
        raise ValueError("S3BackupMode must be one of: %s" % ", ".join(valid_types))
    return x


def s3_backup_mode_extended_s3_validator(x):
    valid_types = ["Disabled", "Enabled"]
    if x not in valid_types:
        raise ValueError("S3BackupMode must be one of: %s" % ", ".join(valid_types))
    return x


class AmazonopensearchserviceBufferingHints(AWSProperty):
    props = {
        "IntervalInSeconds": (integer, False),
        "SizeInMBs": (integer, False),
    }


class AmazonopensearchserviceRetryOptions(AWSProperty):
    props = {
        "DurationInSeconds": (integer, False),
    }


class BufferingHints(AWSProperty):
    props = {
        "IntervalInSeconds": (positive_integer, True),
        "SizeInMBs": (positive_integer, True),
    }


class DeliveryStreamEncryptionConfigurationInput(AWSProperty):
    props = {
        "KeyARN": (str, False),
        "KeyType": (str, True),
    }


class CloudWatchLoggingOptions(AWSProperty):
    props = {
        "Enabled": (boolean, False),
        "LogGroupName": (str, False),  # Conditional
        "LogStreamName": (str, False),  # Conditional
    }


class RetryOptions(AWSProperty):
    props = {
        "DurationInSeconds": (positive_integer, True),
    }


class KMSEncryptionConfig(AWSProperty):
    props = {
        "AWSKMSKeyARN": (str, True),
    }


class EncryptionConfiguration(AWSProperty):
    props = {
        "KMSEncryptionConfig": (KMSEncryptionConfig, False),
        "NoEncryptionConfig": (str, False),
    }


class S3Configuration(AWSProperty):
    props = {
        "BucketARN": (str, True),
        "BufferingHints": (BufferingHints, True),
        "CloudWatchLoggingOptions": (CloudWatchLoggingOptions, False),
        "CompressionFormat": (str, True),
        "EncryptionConfiguration": (EncryptionConfiguration, False),
        "Prefix": (str, False),
        "RoleARN": (str, True),
    }


class CopyCommand(AWSProperty):
    props = {
        "CopyOptions": (str, False),
        "DataTableColumns": (str, False),
        "DataTableName": (str, True),
    }


class ProcessorParameter(AWSProperty):
    props = {
        "ParameterName": (str, True),
        "ParameterValue": (str, True),
    }


class Processor(AWSProperty):
    props = {
        "Parameters": ([ProcessorParameter], True),
        "Type": (processor_type_validator, True),
    }


class ProcessingConfiguration(AWSProperty):
    props = {
        "Enabled": (boolean, True),
        "Processors": ([Processor], True),
    }


class RedshiftRetryOptions(AWSProperty):
    props = {
        "DurationInSeconds": (integer, False),
    }


class S3DestinationConfiguration(AWSProperty):
    props = {
        "BucketARN": (str, True),
        "BufferingHints": (BufferingHints, False),
        "CloudWatchLoggingOptions": (CloudWatchLoggingOptions, False),
        "CompressionFormat": (str, False),
        "EncryptionConfiguration": (EncryptionConfiguration, False),
        "ErrorOutputPrefix": (str, False),
        "Prefix": (str, False),
        "RoleARN": (str, True),
    }


class VpcConfiguration(AWSProperty):
    props = {
        "RoleARN": (str, True),
        "SecurityGroupIds": ([str], True),
        "SubnetIds": ([str], True),
    }


class AmazonopensearchserviceDestinationConfiguration(AWSProperty):
    props = {
        "BufferingHints": (AmazonopensearchserviceBufferingHints, False),
        "CloudWatchLoggingOptions": (CloudWatchLoggingOptions, False),
        "ClusterEndpoint": (str, False),
        "DomainARN": (str, False),
        "IndexName": (str, True),
        "IndexRotationPeriod": (str, False),
        "ProcessingConfiguration": (ProcessingConfiguration, False),
        "RetryOptions": (AmazonopensearchserviceRetryOptions, False),
        "RoleARN": (str, True),
        "S3BackupMode": (str, False),
        "S3Configuration": (S3DestinationConfiguration, True),
        "TypeName": (str, False),
        "VpcConfiguration": (VpcConfiguration, False),
    }


class ElasticsearchDestinationConfiguration(AWSProperty):
    props = {
        "BufferingHints": (BufferingHints, True),
        "CloudWatchLoggingOptions": (CloudWatchLoggingOptions, False),
        "ClusterEndpoint": (str, False),
        "DomainARN": (str, True),
        "IndexName": (str, True),
        "IndexRotationPeriod": (index_rotation_period_validator, True),
        "ProcessingConfiguration": (ProcessingConfiguration, False),
        "RetryOptions": (RetryOptions, False),
        "RoleARN": (str, True),
        "S3BackupMode": (s3_backup_mode_elastic_search_validator, True),
        "S3Configuration": (S3Configuration, False),
        "TypeName": (str, False),
        "VpcConfiguration": (VpcConfiguration, False),
    }


class RedshiftDestinationConfiguration(AWSProperty):
    props = {
        "CloudWatchLoggingOptions": (CloudWatchLoggingOptions, False),
        "ClusterJDBCURL": (str, True),
        "CopyCommand": (CopyCommand, True),
        "Password": (str, True),
        "ProcessingConfiguration": (ProcessingConfiguration, False),
        "RetryOptions": (RedshiftRetryOptions, False),
        "RoleARN": (str, True),
        "S3Configuration": (S3Configuration, True),
        "Username": (str, True),
    }


class HiveJsonSerDe(AWSProperty):
    props = {
        "TimestampFormats": ([str], False),
    }


class OpenXJsonSerDe(AWSProperty):
    props = {
        "CaseInsensitive": (boolean, False),
        "ColumnToJsonKeyMappings": (dict, False),
        "ConvertDotsInJsonKeysToUnderscores": (boolean, False),
    }


class Deserializer(AWSProperty):
    props = {
        "HiveJsonSerDe": (HiveJsonSerDe, False),
        "OpenXJsonSerDe": (OpenXJsonSerDe, False),
    }


class InputFormatConfiguration(AWSProperty):
    props = {
        "Deserializer": (Deserializer, True),
    }


class OrcSerDe(AWSProperty):
    props = {
        "BlockSizeBytes": (integer, False),
        "BloomFilterColumns": ([str], False),
        "BloomFilterFalsePositiveProbability": (float, False),
        "Compression": (str, False),
        "DictionaryKeyThreshold": (float, False),
        "EnablePadding": (boolean, False),
        "FormatVersion": (str, False),
        "PaddingTolerance": (float, False),
        "RowIndexStride": (integer, False),
        "StripeSizeBytes": (integer, False),
    }


class ParquetSerDe(AWSProperty):
    props = {
        "BlockSizeBytes": (integer, False),
        "Compression": (str, False),
        "EnableDictionaryCompression": (boolean, False),
        "MaxPaddingBytes": (integer, False),
        "PageSizeBytes": (integer, False),
        "WriterVersion": (str, False),
    }


class Serializer(AWSProperty):
    props = {
        "OrcSerDe": (OrcSerDe, False),
        "ParquetSerDe": (ParquetSerDe, False),
    }


class OutputFormatConfiguration(AWSProperty):
    props = {
        "Serializer": (Serializer, True),
    }


class SchemaConfiguration(AWSProperty):
    props = {
        "CatalogId": (str, True),
        "DatabaseName": (str, True),
        "Region": (str, True),
        "RoleARN": (str, True),
        "TableName": (str, True),
        "VersionId": (str, True),
    }


class DataFormatConversionConfiguration(AWSProperty):
    props = {
        "Enabled": (boolean, True),
        "InputFormatConfiguration": (InputFormatConfiguration, True),
        "OutputFormatConfiguration": (OutputFormatConfiguration, True),
        "SchemaConfiguration": (SchemaConfiguration, True),
    }


class DynamicPartitioningConfiguration(AWSProperty):
    props = {
        "Enabled": (boolean, False),
        "RetryOptions": (RetryOptions, False),
    }


class ExtendedS3DestinationConfiguration(AWSProperty):
    props = {
        "BucketARN": (str, True),
        "BufferingHints": (BufferingHints, False),
        "CloudWatchLoggingOptions": (CloudWatchLoggingOptions, False),
        "CompressionFormat": (str, False),
        "DataFormatConversionConfiguration": (DataFormatConversionConfiguration, False),
        "DynamicPartitioningConfiguration": (DynamicPartitioningConfiguration, False),
        "EncryptionConfiguration": (EncryptionConfiguration, False),
        "ErrorOutputPrefix": (str, False),
        "Prefix": (str, False),
        "ProcessingConfiguration": (ProcessingConfiguration, False),
        "RoleARN": (str, True),
        "S3BackupConfiguration": (S3DestinationConfiguration, False),
        "S3BackupMode": (s3_backup_mode_extended_s3_validator, False),
    }


class HttpEndpointConfiguration(AWSProperty):
    props = {
        "AccessKey": (str, False),
        "Name": (str, False),
        "Url": (str, True),
    }


class HttpEndpointCommonAttribute(AWSProperty):
    props = {
        "AttributeName": (str, True),
        "AttributeValue": (str, True),
    }


class HttpEndpointRequestConfiguration(AWSProperty):
    props = {
        "CommonAttributes": ([HttpEndpointCommonAttribute], False),
        "ContentEncoding": (str, False),
    }


class HttpEndpointDestinationConfiguration(AWSProperty):
    props = {
        "BufferingHints": (BufferingHints, False),
        "CloudWatchLoggingOptions": (CloudWatchLoggingOptions, False),
        "EndpointConfiguration": (HttpEndpointConfiguration, True),
        "ProcessingConfiguration": (ProcessingConfiguration, False),
        "RequestConfiguration": (HttpEndpointRequestConfiguration, False),
        "RetryOptions": (RetryOptions, False),
        "RoleARN": (str, False),
        "S3BackupMode": (str, False),
        "S3Configuration": (S3DestinationConfiguration, True),
    }


class KinesisStreamSourceConfiguration(AWSProperty):
    props = {"KinesisStreamARN": (str, True), "RoleARN": (str, True)}


class SplunkRetryOptions(AWSProperty):
    props = {
        "DurationInSeconds": (positive_integer, True),
    }


class SplunkDestinationConfiguration(AWSProperty):
    props = {
        "CloudWatchLoggingOptions": (CloudWatchLoggingOptions, False),
        "HECAcknowledgmentTimeoutInSeconds": (positive_integer, False),
        "HECEndpoint": (str, True),
        "HECEndpointType": (str, True),
        "HECToken": (str, True),
        "ProcessingConfiguration": (ProcessingConfiguration, False),
        "RetryOptions": (SplunkRetryOptions, False),
        "S3BackupMode": (str, False),
        "S3Configuration": (S3DestinationConfiguration, True),
    }


class DeliveryStream(AWSObject):
    resource_type = "AWS::KinesisFirehose::DeliveryStream"

    props = {
        "AmazonopensearchserviceDestinationConfiguration": (
            AmazonopensearchserviceDestinationConfiguration,
            False,
        ),
        "DeliveryStreamEncryptionConfigurationInput": (
            DeliveryStreamEncryptionConfigurationInput,
            False,
        ),
        "DeliveryStreamName": (str, False),
        "DeliveryStreamType": (delivery_stream_type_validator, False),
        "ElasticsearchDestinationConfiguration": (
            ElasticsearchDestinationConfiguration,
            False,
        ),  # noqa
        "ExtendedS3DestinationConfiguration": (
            ExtendedS3DestinationConfiguration,
            False,
        ),  # noqa
        "HttpEndpointDestinationConfiguration": (
            HttpEndpointDestinationConfiguration,
            False,
        ),
        "KinesisStreamSourceConfiguration": (
            KinesisStreamSourceConfiguration,
            False,
        ),  # noqa
        "RedshiftDestinationConfiguration": (
            RedshiftDestinationConfiguration,
            False,
        ),  # noqa
        "S3DestinationConfiguration": (S3DestinationConfiguration, False),
        "SplunkDestinationConfiguration": (SplunkDestinationConfiguration, False),
        "Tags": (Tags, False),
    }
