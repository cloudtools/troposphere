# Copyright (c) 2014, Guillem Anguera <ganguera@gmail.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import integer, boolean, json_checker


VALID_RUNTIME_ENVIRONMENTS = ('SQL-1_0', 'FLINK-1_6', 'FLINK-1_8')


def validate_runtime_environment(runtime_environment):
    """Validate RuntimeEnvironment for Application"""

    if runtime_environment not in VALID_RUNTIME_ENVIRONMENTS:
        raise ValueError("Application RuntimeEnvironment must be one of: %s" %
                         ", ".join(VALID_RUNTIME_ENVIRONMENTS))
    return runtime_environment


class S3ContentLocation(AWSProperty):
    props = {
        'BucketARN': (basestring, False),
        'FileKey': (basestring, False),
        'ObjectVersion': (basestring, False)
    }


class CodeContent(AWSProperty):
    props = {
        'S3ContentLocation': (S3ContentLocation, False),
        'TextContent': (basestring, False),
        'ZipFileContent': (basestring, False),
    }


class ApplicationCodeConfiguration(AWSProperty):
    props = {
        'CodeContent': (CodeContent, True),
        'CodeContentType': (basestring, True),
    }


class PropertyGroup(AWSProperty):
    props = {
        'PropertyGroupId': (basestring, False),
        'PropertyMap': (json_checker, False),
    }


class EnvironmentProperties(AWSProperty):
    props = {
        'PropertyGroups': ([PropertyGroup], False),
    }


class CheckpointConfiguration(AWSProperty):
    props = {
        'ConfigurationType': (basestring, True),
        'CheckpointInterval': (integer, False),
        'CheckpointingEnabled': (boolean, False),
        'MinPauseBetweenCheckpoints': (integer, False),
    }


class MonitoringConfiguration(AWSProperty):
    props = {
        'ConfigurationType': (basestring, True),
        'LogLevel': (basestring, False),
        'MetricsLevel': (basestring, False),
    }


class ParallelismConfiguration(AWSProperty):
    props = {
        'AutoScalingEnabled': (boolean, False),
        'ConfigurationType': (basestring, True),
        'Parallelism': (integer, False),
        'ParallelismPerKPU': (integer, False),
    }


class FlinkApplicationConfiguration(AWSProperty):
    props = {
        'CheckpointConfiguration': (CheckpointConfiguration, False),
        'MonitoringConfiguration': (MonitoringConfiguration, False),
        'ParallelismConfiguration': (ParallelismConfiguration, False),
    }


class InputParallelism(AWSProperty):
    props = {
        'Count': (integer, False),
    }


class InputLambdaProcessor(AWSProperty):
    props = {
        'ResourceARN': (basestring, True),
    }


class InputProcessingConfiguration(AWSProperty):
    props = {
        'InputLambdaProcessor': (InputLambdaProcessor, False),
    }


class RecordColumn(AWSProperty):
    props = {
        'Mapping': (basestring, False),
        'Name': (basestring, True),
        'SqlType': (basestring, True),
    }


class JSONMappingParameters(AWSProperty):
    props = {
        'RecordRowPath': (basestring, True),
    }


class CSVMappingParameters(AWSProperty):
    props = {
        'RecordColumnDelimiter': (basestring, True),
        'RecordRowDelimiter': (basestring, True),
    }


class MappingParameters(AWSProperty):
    props = {
        'CSVMappingParameters': (CSVMappingParameters, False),
        'JSONMappingParameters': (JSONMappingParameters, False),
    }


class RecordFormat(AWSProperty):
    props = {
        'MappingParameters': (MappingParameters, False),
        'RecordFormatType': (basestring, True),
    }


class InputSchema(AWSProperty):
    props = {
        'RecordColumns': ([RecordColumn], True),
        'RecordEncoding': (basestring, False),
        'RecordFormat': (RecordFormat, True),
    }


class KinesisStreamsInput(AWSProperty):
    props = {
        'ResourceARN': (basestring, True),
    }


class KinesisFirehoseInput(AWSProperty):
    props = {
        'ResourceARN': (basestring, True),
    }


class Input(AWSProperty):
    props = {
        'InputParallelism': (InputParallelism, False),
        'InputProcessingConfiguration': (InputProcessingConfiguration, False),
        'InputSchema': (InputSchema, True),
        'KinesisFirehoseInput': (KinesisFirehoseInput, False),
        'KinesisStreamsInput': (KinesisStreamsInput, False),
        'NamePrefix': (basestring, False),
    }


class SqlApplicationConfiguration(AWSProperty):
    props = {
        'Inputs': ([Input], False),
    }


class ApplicationSnapshotConfiguration(AWSProperty):
    props = {
        'SnapshotsEnabled': (boolean, True),
    }


class ApplicationConfiguration(AWSProperty):
    props = {
        'ApplicationCodeConfiguration': (ApplicationCodeConfiguration, False),
        'ApplicationSnapshotConfiguration': (ApplicationSnapshotConfiguration, False),  # NOQA
        'EnvironmentProperties': (EnvironmentProperties, False),
        'FlinkApplicationConfiguration': (FlinkApplicationConfiguration, False),  # NOQA
        'SqlApplicationConfiguration': (SqlApplicationConfiguration, False),
    }


class Application(AWSObject):
    resource_type = "AWS::KinesisAnalyticsV2::Application"

    props = {
        'ApplicationConfiguration': (ApplicationConfiguration, False),
        'ApplicationDescription': (basestring, False),
        'ApplicationName': (basestring, False),
        'RuntimeEnvironment': (validate_runtime_environment, True),
        'ServiceExecutionRole': (basestring, True),
    }


class CloudWatchLoggingOption(AWSProperty):
    props = {
        'LogStreamARN': (basestring, True),
    }


class ApplicationCloudWatchLoggingOption(AWSObject):
    resource_type = \
        "AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption"

    props = {
        'ApplicationName': (basestring, True),
        'CloudWatchLoggingOption': (CloudWatchLoggingOption, True),
    }


class S3ReferenceDataSource(AWSProperty):
    props = {
        'BucketARN': (basestring, False),
        'FileKey': (basestring, False),
    }


class ReferenceSchema(AWSProperty):
    props = {
        'RecordEncoding': (basestring, False),
        'RecordColumns': ([RecordColumn], True),
        'RecordFormat': (RecordFormat, True),
    }


class ReferenceDataSource(AWSProperty):
    props = {
        'ReferenceSchema': (ReferenceSchema, True),
        'TableName': (basestring, False),
        'S3ReferenceDataSource': (S3ReferenceDataSource, False),
    }


class ApplicationReferenceDataSource(AWSObject):
    resource_type = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource"

    props = {
        'ApplicationName': (basestring, True),
        'ReferenceDataSource': (ReferenceDataSource, True),
    }


class LambdaOutput(AWSProperty):
    props = {
        'ResourceARN': (basestring, True),
    }


class KinesisFirehoseOutput(AWSProperty):
    props = {
        'ResourceARN': (basestring, True),
    }


class KinesisStreamsOutput(AWSProperty):
    props = {
        'ResourceARN': (basestring, True),
    }


class DestinationSchema(AWSProperty):
    props = {
        'RecordFormatType': (basestring, False),
    }


class Output(AWSProperty):
    props = {
        "DestinationSchema": (DestinationSchema, True),
        "LambdaOutput": (LambdaOutput, False),
        "KinesisFirehoseOutput": (KinesisFirehoseOutput, False),
        "KinesisStreamsOutput": (KinesisStreamsOutput, False),
        "Name": (basestring, False),
    }


class ApplicationOutput(AWSObject):
    resource_type = "AWS::KinesisAnalyticsV2::ApplicationOutput"

    props = {
        'ApplicationName': (basestring, True),
        'Output': (Output, True),
    }
