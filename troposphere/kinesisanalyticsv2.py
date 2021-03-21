# Copyright (c) 2014, Guillem Anguera <ganguera@gmail.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import integer, boolean


VALID_RUNTIME_ENVIRONMENTS = ('SQL-1_0', 'FLINK-1_6', 'FLINK-1_8',
                              'FLINK-1_11')


def validate_runtime_environment(runtime_environment):
    """Validate RuntimeEnvironment for Application"""

    if runtime_environment not in VALID_RUNTIME_ENVIRONMENTS:
        raise ValueError("Application RuntimeEnvironment must be one of: %s" %
                         ", ".join(VALID_RUNTIME_ENVIRONMENTS))
    return runtime_environment


class S3ContentLocation(AWSProperty):
    props = {
        'BucketARN': (str, False),
        'FileKey': (str, False),
        'ObjectVersion': (str, False)
    }


class CodeContent(AWSProperty):
    props = {
        'S3ContentLocation': (S3ContentLocation, False),
        'TextContent': (str, False),
        'ZipFileContent': (str, False),
    }


class ApplicationCodeConfiguration(AWSProperty):
    props = {
        'CodeContent': (CodeContent, True),
        'CodeContentType': (str, True),
    }


class PropertyGroup(AWSProperty):
    props = {
        'PropertyGroupId': (str, False),
        'PropertyMap': (dict, False),
    }


class EnvironmentProperties(AWSProperty):
    props = {
        'PropertyGroups': ([PropertyGroup], False),
    }


class CheckpointConfiguration(AWSProperty):
    props = {
        'ConfigurationType': (str, True),
        'CheckpointInterval': (integer, False),
        'CheckpointingEnabled': (boolean, False),
        'MinPauseBetweenCheckpoints': (integer, False),
    }


class MonitoringConfiguration(AWSProperty):
    props = {
        'ConfigurationType': (str, True),
        'LogLevel': (str, False),
        'MetricsLevel': (str, False),
    }


class ParallelismConfiguration(AWSProperty):
    props = {
        'AutoScalingEnabled': (boolean, False),
        'ConfigurationType': (str, True),
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
        'ResourceARN': (str, True),
    }


class InputProcessingConfiguration(AWSProperty):
    props = {
        'InputLambdaProcessor': (InputLambdaProcessor, False),
    }


class RecordColumn(AWSProperty):
    props = {
        'Mapping': (str, False),
        'Name': (str, True),
        'SqlType': (str, True),
    }


class JSONMappingParameters(AWSProperty):
    props = {
        'RecordRowPath': (str, True),
    }


class CSVMappingParameters(AWSProperty):
    props = {
        'RecordColumnDelimiter': (str, True),
        'RecordRowDelimiter': (str, True),
    }


class MappingParameters(AWSProperty):
    props = {
        'CSVMappingParameters': (CSVMappingParameters, False),
        'JSONMappingParameters': (JSONMappingParameters, False),
    }


class RecordFormat(AWSProperty):
    props = {
        'MappingParameters': (MappingParameters, False),
        'RecordFormatType': (str, True),
    }


class InputSchema(AWSProperty):
    props = {
        'RecordColumns': ([RecordColumn], True),
        'RecordEncoding': (str, False),
        'RecordFormat': (RecordFormat, True),
    }


class KinesisStreamsInput(AWSProperty):
    props = {
        'ResourceARN': (str, True),
    }


class KinesisFirehoseInput(AWSProperty):
    props = {
        'ResourceARN': (str, True),
    }


class Input(AWSProperty):
    props = {
        'InputParallelism': (InputParallelism, False),
        'InputProcessingConfiguration': (InputProcessingConfiguration, False),
        'InputSchema': (InputSchema, True),
        'KinesisFirehoseInput': (KinesisFirehoseInput, False),
        'KinesisStreamsInput': (KinesisStreamsInput, False),
        'NamePrefix': (str, False),
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
        'ApplicationDescription': (str, False),
        'ApplicationName': (str, False),
        'RuntimeEnvironment': (validate_runtime_environment, True),
        'ServiceExecutionRole': (str, True),
    }


class CloudWatchLoggingOption(AWSProperty):
    props = {
        'LogStreamARN': (str, True),
    }


class ApplicationCloudWatchLoggingOption(AWSObject):
    resource_type = \
        "AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption"

    props = {
        'ApplicationName': (str, True),
        'CloudWatchLoggingOption': (CloudWatchLoggingOption, True),
    }


class S3ReferenceDataSource(AWSProperty):
    props = {
        'BucketARN': (str, False),
        'FileKey': (str, False),
    }


class ReferenceSchema(AWSProperty):
    props = {
        'RecordEncoding': (str, False),
        'RecordColumns': ([RecordColumn], True),
        'RecordFormat': (RecordFormat, True),
    }


class ReferenceDataSource(AWSProperty):
    props = {
        'ReferenceSchema': (ReferenceSchema, True),
        'TableName': (str, False),
        'S3ReferenceDataSource': (S3ReferenceDataSource, False),
    }


class ApplicationReferenceDataSource(AWSObject):
    resource_type = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource"

    props = {
        'ApplicationName': (str, True),
        'ReferenceDataSource': (ReferenceDataSource, True),
    }


class LambdaOutput(AWSProperty):
    props = {
        'ResourceARN': (str, True),
    }


class KinesisFirehoseOutput(AWSProperty):
    props = {
        'ResourceARN': (str, True),
    }


class KinesisStreamsOutput(AWSProperty):
    props = {
        'ResourceARN': (str, True),
    }


class DestinationSchema(AWSProperty):
    props = {
        'RecordFormatType': (str, False),
    }


class Output(AWSProperty):
    props = {
        "DestinationSchema": (DestinationSchema, True),
        "LambdaOutput": (LambdaOutput, False),
        "KinesisFirehoseOutput": (KinesisFirehoseOutput, False),
        "KinesisStreamsOutput": (KinesisStreamsOutput, False),
        "Name": (str, False),
    }


class ApplicationOutput(AWSObject):
    resource_type = "AWS::KinesisAnalyticsV2::ApplicationOutput"

    props = {
        'ApplicationName': (str, True),
        'Output': (Output, True),
    }
