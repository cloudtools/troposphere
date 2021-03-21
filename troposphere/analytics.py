# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import integer


class InputParallelism(AWSProperty):
    props = {
        'Count': (integer, True),
    }


class RecordColumn(AWSProperty):
    props = {
        'Mapping': (str, False),
        'Name': (str, True),
        'SqlType': (str, True),
    }


class CSVMappingParameters(AWSProperty):
    props = {
        'RecordColumnDelimiter': (str, True),
        'RecordRowDelimiter': (str, True),
    }


class JSONMappingParameters(AWSProperty):
    props = {
        'RecordRowPath': (str, True),
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


class KinesisFirehoseInput(AWSProperty):
    props = {
        'ResourceARN': (str, True),
        'RoleARN': (str, True),
    }


class KinesisStreamsInput(AWSProperty):
    props = {
        'ResourceARN': (str, True),
        'RoleARN': (str, True),
    }


class InputLambdaProcessor(AWSProperty):
    props = {
        'ResourceARN': (str, True),
        'RoleARN': (str, True),
    }


class InputProcessingConfiguration(AWSProperty):
    props = {
        'InputLambdaProcessor': (InputLambdaProcessor, False),
    }


class Input(AWSProperty):
    props = {
        'NamePrefix': (str, True),
        'InputParallelism': (InputParallelism, False),
        'InputSchema': (InputSchema, True),
        'KinesisFirehoseInput': (KinesisFirehoseInput, False),
        'KinesisStreamsInput': (KinesisStreamsInput, False),
        'InputProcessingConfiguration': (InputProcessingConfiguration, False),
    }


class Application(AWSObject):
    resource_type = "AWS::KinesisAnalytics::Application"

    props = {
        'ApplicationName': (str, False),
        'ApplicationDescription': (str, False),
        'ApplicationCode': (str, False),
        'Inputs': ([Input], True),
    }


class DestinationSchema(AWSProperty):
    props = {
        'RecordFormatType': (str, False),
    }


class KinesisFirehoseOutput(AWSProperty):
    props = {
        'ResourceARN': (str, True),
        'RoleARN': (str, True),
    }


class KinesisStreamsOutput(AWSProperty):
    props = {
        'ResourceARN': (str, True),
        'RoleARN': (str, True),
    }


class LambdaOutput(AWSProperty):
    props = {
        'ResourceARN': (str, True),
        'RoleARN': (str, True),
    }


class Output(AWSProperty):
    props = {
        'DestinationSchema': (DestinationSchema, True),
        'KinesisFirehoseOutput': (KinesisFirehoseOutput, False),
        'KinesisStreamsOutput': (KinesisStreamsOutput, False),
        'LambdaOutput': (LambdaOutput, False),
        'Name': (str, True),
    }


class ApplicationOutput(AWSObject):
    resource_type = "AWS::KinesisAnalytics::ApplicationOutput"

    props = {
        'ApplicationName': (str, True),
        'Output': (Output, True),
    }


class ReferenceSchema(AWSProperty):
    props = {
        'RecordColumns': ([RecordColumn], True),
        'RecordEncoding': (str, False),
        'RecordFormat': (RecordFormat, True),
    }


class S3ReferenceDataSource(AWSProperty):
    props = {
        'BucketARN': (str, False),
        'FileKey': (str, False),
        'ReferenceRoleARN': (str, False),
    }


class ReferenceDataSource(AWSProperty):
    props = {
        'ReferenceSchema': (ReferenceSchema, True),
        'S3ReferenceDataSource': (S3ReferenceDataSource, False),
        'TableName': (str, False),
    }


class ApplicationReferenceDataSource(AWSObject):
    resource_type = "AWS::KinesisAnalytics::ApplicationReferenceDataSource"

    props = {
        'ApplicationName': (str, True),
        'ReferenceDataSource': (ReferenceDataSource, True),
    }
