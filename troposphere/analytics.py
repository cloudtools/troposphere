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
        'Mapping': (basestring, False),
        'Name': (basestring, True),
        'SqlType': (basestring, True),
    }


class CSVMappingParameters(AWSProperty):
    props = {
        'RecordColumnDelimiter': (basestring, True),
        'RecordRowDelimiter': (basestring, True),
    }


class JSONMappingParameters(AWSProperty):
    props = {
        'RecordRowPath': (basestring, True),
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


class KinesisFirehoseInput(AWSProperty):
    props = {
        'ResourceARN': (basestring, True),
        'RoleARN': (basestring, True),
    }


class KinesisStreamsInput(AWSProperty):
    props = {
        'ResourceARN': (basestring, True),
        'RoleARN': (basestring, True),
    }


class InputLambdaProcessor(AWSProperty):
    props = {
        'ResourceARN': (basestring, True),
        'RoleARN': (basestring, True),
    }


class InputProcessingConfiguration(AWSProperty):
    props = {
        'InputLambdaProcessor': (InputLambdaProcessor, False),
    }


class Input(AWSProperty):
    props = {
        'NamePrefix': (basestring, True),
        'InputParallelism': (InputParallelism, False),
        'InputSchema': (InputSchema, True),
        'KinesisFirehoseInput': (KinesisFirehoseInput, False),
        'KinesisStreamsInput': (KinesisStreamsInput, False),
        'InputProcessingConfiguration': (InputProcessingConfiguration, False),
    }


class Application(AWSObject):
    resource_type = "AWS::KinesisAnalytics::Application"

    props = {
        'ApplicationName': (basestring, False),
        'ApplicationDescription': (basestring, False),
        'ApplicationCode': (basestring, False),
        'Inputs': ([Input], True),
    }


class DestinationSchema(AWSProperty):
    props = {
        'RecordFormatType': (basestring, False),
    }


class KinesisFirehoseOutput(AWSProperty):
    props = {
        'ResourceARN': (basestring, True),
        'RoleARN': (basestring, True),
    }


class KinesisStreamsOutput(AWSProperty):
    props = {
        'ResourceARN': (basestring, True),
        'RoleARN': (basestring, True),
    }


class LambdaOutput(AWSProperty):
    props = {
        'ResourceARN': (basestring, True),
        'RoleARN': (basestring, True),
    }


class Output(AWSProperty):
    props = {
        'DestinationSchema': (DestinationSchema, True),
        'KinesisFirehoseOutput': (KinesisFirehoseOutput, False),
        'KinesisStreamsOutput': (KinesisStreamsOutput, False),
        'LambdaOutput': (LambdaOutput, False),
        'Name': (basestring, True),
    }


class ApplicationOutput(AWSObject):
    resource_type = "AWS::KinesisAnalytics::ApplicationOutput"

    props = {
        'ApplicationName': (basestring, True),
        'Output': (Output, True),
    }


class ReferenceSchema(AWSProperty):
    props = {
        'RecordColumns': ([RecordColumn], True),
        'RecordEncoding': (basestring, False),
        'RecordFormat': (RecordFormat, True),
    }


class S3ReferenceDataSource(AWSProperty):
    props = {
        'BucketARN': (basestring, False),
        'FileKey': (basestring, False),
        'ReferenceRoleARN': (basestring, False),
    }


class ReferenceDataSource(AWSProperty):
    props = {
        'ReferenceSchema': (ReferenceSchema, True),
        'S3ReferenceDataSource': (S3ReferenceDataSource, False),
        'TableName': (basestring, False),
    }


class ApplicationReferenceDataSource(AWSObject):
    resource_type = "AWS::KinesisAnalytics::ApplicationReferenceDataSource"

    props = {
        'ApplicationName': (basestring, True),
        'ReferenceDataSource': (ReferenceDataSource, True),
    }
