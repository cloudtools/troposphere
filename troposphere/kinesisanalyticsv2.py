# Copyright (c) 2014, Guillem Anguera <ganguera@gmail.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import integer, boolean, json_checker


VALID_RUNTIME_ENVIRONMENTS = ('SQL-1.0', 'FLINK-1_6')


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
        'ZipFileContent': (basestring, False),
        'S3ContentLocation': S3ContentLocation,
        'TextContent': (basestring, False),
    }


class ApplicationCodeConfiguration(AWSProperty):
    props = {
        'CodeContentType': (basestring, True),
        'CodeContent': (CodeContent, True),
    }


class PropertyGroup(AWSProperty):
    props = {
        'PropertyMap': (json_checker, False),
        'PropertyGroupId': (basestring, False),
    }


class EnvironmentProperties(AWSProperty):
    props = {
        'PropertyGroups': ([PropertyGroup], False),
    }


class CheckpointConfiguration(AWSProperty):
    props = {
        'ConfigurationType': (basestring, True),
        'CheckpointInterval': (integer, False),
        'MinPauseBetweenCheckpoints': (integer, False),
        'CheckpointingEnabled': (boolean, False)
    }


class MonitoringConfiguration(AWSProperty):
    props = {
        'ConfigurationType': (basestring, True),
        'MetricsLevel': (basestring, False),
        'LogLevel': (basestring, False),
    }


class ParallelismConfiguration(AWSProperty):
    props = {
        'ConfigurationType': (basestring, True),
        'ParallelismPerKPU': (integer, False),
        'AutoScalingEnabled': (boolean, False),
        'Parallelism': (integer, False),
    }


class FlinkApplicationConfiguration(AWSProperty):
    props = {
        'CheckpointConfiguration': (CheckpointConfiguration, False),
        'ParallelismConfiguration': (ParallelismConfiguration, False),
        'MonitoringConfiguration': (MonitoringConfiguration, False),
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
        'SqlType': (basestring, True),
        'Name': (basestring, True),
    }


class JSONMappingParameters(AWSProperty):
    props = {
        'RecordRowPath': (basestring, True),
    }


class CSVMappingParameters(AWSProperty):
    props = {
        'RecordRowDelimiter': (basestring, True),
        'RecordColumnDelimiter': (basestring, True),
    }


class MappingParameters(AWSProperty):
    props = {
        'JSONMappingParameters': (JSONMappingParameters, False),
        'CSVMappingParameters': (CSVMappingParameters, False),
    }


class RecordFormat(AWSProperty):
    props = {
        'MappingParameters': (MappingParameters, False),
        'RecordFormatType': (basestring, True),
    }


class InputSchema(AWSProperty):
    props = {
        'RecordEncoding': (basestring, False),
        'RecordColumns': ([RecordColumn], True),
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
        'NamePrefix': (basestring, False),
        'InputSchema': (InputSchema, True),
        'KinesisStreamsInput': (KinesisStreamsInput, False),
        'KinesisFirehoseInput': (KinesisFirehoseInput, False),
        'InputProcessingConfiguration': (InputProcessingConfiguration, False),
        'InputParallelism': (InputParallelism, False),
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
        'EnvironmentProperties': (EnvironmentProperties, False),
        'FlinkApplicationConfiguration': (FlinkApplicationConfiguration, False),  # NOQA
        'SqlApplicationConfiguration': (SqlApplicationConfiguration, False),
        'ApplicationSnapshotConfiguration': (ApplicationSnapshotConfiguration, False),  # NOQA
    }


class Application(AWSObject):
    resource_type = "AWS::KinesisAnalyticsV2::Application"

    props = {
        'ApplicationName': (basestring, False),
        'RuntimeEnvironment': (validate_runtime_environment, True),
        'ApplicationConfiguration': (ApplicationConfiguration, False),
        'ApplicationDescription': (basestring, False),
        'ServiceExecutionRole': (basestring, True),
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
