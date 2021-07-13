# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 35.0.0


from troposphere import Tags

from . import AWSObject, AWSProperty
from .validators import boolean, integer


class CsvOptions(AWSProperty):
    props = {
        "Delimiter": (str, False),
        "HeaderRow": (boolean, False),
    }


class ExcelOptions(AWSProperty):
    props = {
        "HeaderRow": (boolean, False),
        "SheetIndexes": ([integer], False),
        "SheetNames": ([str], False),
    }


class JsonOptions(AWSProperty):
    props = {
        "MultiLine": (boolean, False),
    }


class FormatOptions(AWSProperty):
    props = {
        "Csv": (CsvOptions, False),
        "Excel": (ExcelOptions, False),
        "Json": (JsonOptions, False),
    }


class S3Location(AWSProperty):
    props = {
        "Bucket": (str, True),
        "Key": (str, False),
    }


class DataCatalogInputDefinition(AWSProperty):
    props = {
        "CatalogId": (str, False),
        "DatabaseName": (str, False),
        "TableName": (str, False),
        "TempDirectory": (S3Location, False),
    }


class DatabaseInputDefinition(AWSProperty):
    props = {
        "DatabaseTableName": (str, False),
        "GlueConnectionName": (str, False),
        "TempDirectory": (S3Location, False),
    }


class Input(AWSProperty):
    props = {
        "DataCatalogInputDefinition": (DataCatalogInputDefinition, False),
        "DatabaseInputDefinition": (DatabaseInputDefinition, False),
        "S3InputDefinition": (S3Location, False),
    }


class FilesLimit(AWSProperty):
    props = {
        "MaxFiles": (integer, True),
        "Order": (str, False),
        "OrderedBy": (str, False),
    }


class FilterValue(AWSProperty):
    props = {
        "Value": (str, True),
        "ValueReference": (str, True),
    }


class FilterExpression(AWSProperty):
    props = {
        "Expression": (str, True),
        "ValuesMap": ([FilterValue], True),
    }


class DatetimeOptions(AWSProperty):
    props = {
        "Format": (str, True),
        "LocaleCode": (str, False),
        "TimezoneOffset": (str, False),
    }


class DatasetParameter(AWSProperty):
    props = {
        "CreateColumn": (boolean, False),
        "DatetimeOptions": (DatetimeOptions, False),
        "Filter": (FilterExpression, False),
        "Name": (str, True),
        "Type": (str, True),
    }


class PathParameter(AWSProperty):
    props = {
        "DatasetParameter": (DatasetParameter, True),
        "PathParameterName": (str, True),
    }


class PathOptions(AWSProperty):
    props = {
        "FilesLimit": (FilesLimit, False),
        "LastModifiedDateCondition": (FilterExpression, False),
        "Parameters": ([PathParameter], False),
    }


class Dataset(AWSObject):
    resource_type = "AWS::DataBrew::Dataset"

    props = {
        "Format": (str, False),
        "FormatOptions": (FormatOptions, False),
        "Input": (Input, True),
        "Name": (str, True),
        "PathOptions": (PathOptions, False),
        "Tags": (Tags, False),
    }


class CsvOutputOptions(AWSProperty):
    props = {
        "Delimiter": (str, False),
    }


class OutputFormatOptions(AWSProperty):
    props = {
        "Csv": (CsvOutputOptions, False),
    }


class Output(AWSProperty):
    props = {
        "CompressionFormat": (str, False),
        "Format": (str, False),
        "FormatOptions": (OutputFormatOptions, False),
        "Location": (S3Location, True),
        "Overwrite": (boolean, False),
        "PartitionColumns": ([str], False),
    }


class Job(AWSObject):
    resource_type = "AWS::DataBrew::Job"

    props = {
        "DatasetName": (str, False),
        "EncryptionKeyArn": (str, False),
        "EncryptionMode": (str, False),
        "JobSample": (dict, False),
        "LogSubscription": (str, False),
        "MaxCapacity": (integer, False),
        "MaxRetries": (integer, False),
        "Name": (str, True),
        "OutputLocation": (dict, False),
        "Outputs": ([Output], False),
        "ProjectName": (str, False),
        "Recipe": (dict, False),
        "RoleArn": (str, True),
        "Tags": (Tags, False),
        "Timeout": (integer, False),
        "Type": (str, True),
    }


class Project(AWSObject):
    resource_type = "AWS::DataBrew::Project"

    props = {
        "DatasetName": (str, True),
        "Name": (str, True),
        "RecipeName": (str, True),
        "RoleArn": (str, True),
        "Sample": (dict, False),
        "Tags": (Tags, False),
    }


class Action(AWSProperty):
    props = {
        "Operation": (str, True),
        "Parameters": (dict, False),
    }


class ConditionExpression(AWSProperty):
    props = {
        "Condition": (str, True),
        "TargetColumn": (str, True),
        "Value": (str, False),
    }


class RecipeStep(AWSProperty):
    props = {
        "Action": (Action, True),
        "ConditionExpressions": ([ConditionExpression], False),
    }


class Recipe(AWSObject):
    resource_type = "AWS::DataBrew::Recipe"

    props = {
        "Description": (str, False),
        "Name": (str, True),
        "Steps": ([RecipeStep], True),
        "Tags": (Tags, False),
    }


class Schedule(AWSObject):
    resource_type = "AWS::DataBrew::Schedule"

    props = {
        "CronExpression": (str, True),
        "JobNames": ([str], False),
        "Name": (str, True),
        "Tags": (Tags, False),
    }
