# Copyright (c) 2016, troposphere project
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, positive_integer


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
        'Prefix': (basestring, True),
        'RoleARN': (basestring, True)
    }


class CopyCommand(AWSProperty):
    props = {
        'CopyOptions': (basestring, False),
        'DataTableColumns': (basestring, False),
        'DataTableName': (basestring, True),
    }


class ElasticsearchDestinationConfiguration(AWSProperty):
    props = {
        'BufferingHints': (BufferingHints, True),
        'CloudWatchLoggingOptions': (CloudWatchLoggingOptions, False),
        'DomainARN': (basestring, True),
        'IndexName': (basestring, True),
        'IndexRotationPeriod': (basestring, True),
        'RetryOptions': (RetryOptions, False),
        'RoleARN': (basestring, True),
        'S3BackupMode': (basestring, True),
        'S3Configuration': (S3Configuration, False),
        'TypeName': (basestring, True),
    }


class RedshiftDestinationConfiguration(AWSProperty):
    props = {
        'CloudWatchLoggingOptions': (CloudWatchLoggingOptions, False),
        'ClusterJDBCURL': (basestring, True),
        'CopyCommand': (CopyCommand, True),
        'Password': (basestring, True),
        'RoleARN': (basestring, True),
        'S3Configuration': (S3Configuration, True),
        'Username': (basestring, True),
    }


class S3DestinationConfiguration(AWSProperty):
    props = {
        'BucketARN': (basestring, True),
        'BufferingHints': (BufferingHints, True),
        'CloudWatchLoggingOptions': (CloudWatchLoggingOptions, False),
        'CompressionFormat': (basestring, True),
        'EncryptionConfiguration': (EncryptionConfiguration, False),
        'Prefix': (basestring, True),
        'RoleARN': (basestring, True),
    }


class ProcessorParameter(AWSProperty):
    props = {
        'ParameterName': (basestring, True),
        'ParameterValue': (basestring, True),
    }


class Processor(AWSProperty):
    props = {
        'Parameters': ([ProcessorParameter], True),
        'Type': (basestring, True),
    }


class ProcessingConfiguration(AWSProperty):
    props = {
        'Enabled': (boolean, True),
        'Processors': ([Processor], True),
    }


class ExtendedS3DestinationConfiguration(AWSProperty):
    props = {
        'BucketARN': (basestring, True),
        'BufferingHints': (BufferingHints, True),
        'CloudWatchLoggingOptions': (CloudWatchLoggingOptions, False),
        'CompressionFormat': (basestring, True),
        'EncryptionConfiguration': (EncryptionConfiguration, False),
        'Prefix': (basestring, True),
        'ProcessingConfiguration': (ProcessingConfiguration, False),
        'RoleARN': (basestring, True),
        'S3BackupConfiguration': (S3DestinationConfiguration, False),
        'S3BackupMode': (basestring, False),
    }


class KinesisStreamSourceConfiguration(AWSProperty):
    props = {
        'KinesisStreamARN': (basestring, True),
        'RoleARN': (basestring, True)
    }


class DeliveryStream(AWSObject):
    resource_type = "AWS::KinesisFirehose::DeliveryStream"

    props = {
        'DeliveryStreamName': (basestring, False),
        'DeliveryStreamType': (basestring, False),
        'ElasticsearchDestinationConfiguration': (ElasticsearchDestinationConfiguration, False),  # noqa
        'ExtendedS3DestinationConfiguration': (ExtendedS3DestinationConfiguration, False),  # noqa
        'KinesisStreamSourceConfiguration': (KinesisStreamSourceConfiguration, False),  # noqa
        'RedshiftDestinationConfiguration': (RedshiftDestinationConfiguration, False),  # noqa
        'S3DestinationConfiguration': (S3DestinationConfiguration, False),
    }
