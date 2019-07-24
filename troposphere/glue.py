# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, double, integer_range, positive_integer


class CsvClassifier(AWSProperty):
    props = {
        'AllowSingleColumn': (boolean, False),
        'ContainsHeader': (basestring, False),
        'Delimiter': (basestring, False),
        'DisableValueTrimming': (boolean, False),
        'Header': ([basestring], False),
        'Name': (basestring, False),
        'QuoteSymbol': (basestring, False),
    }


class GrokClassifier(AWSProperty):
    props = {
        'Classification': (basestring, True),
        'CustomPatterns': (basestring, False),
        'GrokPattern': (basestring, True),
        'Name': (basestring, False),
    }


class JsonClassifier(AWSProperty):
    props = {
        'JsonPath': (basestring, True),
        'Name': (basestring, False),
    }


class XMLClassifier(AWSProperty):
    props = {
        'Classification': (basestring, True),
        'Name': (basestring, False),
        'RowTag': (basestring, True),
    }


class Classifier(AWSObject):
    resource_type = "AWS::Glue::Classifier"

    props = {
        'CsvClassifier': (CsvClassifier, False),
        'GrokClassifier': (GrokClassifier, False),
        'JsonClassifier': (JsonClassifier, False),
        'XMLClassifier': (XMLClassifier, False),
    }


class PhysicalConnectionRequirements(AWSProperty):
    props = {
        'AvailabilityZone': (basestring, False),
        'SecurityGroupIdList': ([basestring], False),
        'SubnetId': (basestring, False),
    }


def connection_type_validator(type):
    valid_types = [
        'JDBC',
        'SFTP',
    ]
    if type not in valid_types:
        raise ValueError('% is not a valid value for ConnectionType' % type)
    return type


class ConnectionInput(AWSProperty):
    props = {
        'ConnectionProperties': (dict, True),
        'ConnectionType': (connection_type_validator, True),
        'Description': (basestring, False),
        'MatchCriteria': ([basestring], False),
        'Name': (basestring, False),
        'PhysicalConnectionRequirements':
            (PhysicalConnectionRequirements, False),
    }


class Connection(AWSObject):
    resource_type = "AWS::Glue::Connection"

    props = {
        'CatalogId': (basestring, True),
        'ConnectionInput': (ConnectionInput, True),
    }


class Schedule(AWSProperty):
    props = {
        'ScheduleExpression': (basestring, False),
    }


def delete_behavior_validator(value):
    valid_values = [
        'LOG',
        'DELETE_FROM_DATABASE',
        'DEPRECATE_IN_DATABASE',
    ]
    if value not in valid_values:
        raise ValueError('% is not a valid value for DeleteBehavior' % value)
    return value


def update_behavior_validator(value):
    valid_values = [
        'LOG',
        'UPDATE_IN_DATABASE',
    ]
    if value not in valid_values:
        raise ValueError('% is not a valid value for UpdateBehavior' % value)
    return value


class SchemaChangePolicy(AWSProperty):
    props = {
        'DeleteBehavior': (delete_behavior_validator, False),
        'UpdateBehavior': (update_behavior_validator, False),
    }


class JdbcTarget(AWSProperty):
    props = {
        'ConnectionName': (basestring, False),
        'Exclusions': ([basestring], False),
        'Path': (basestring, False),
    }


class S3Target(AWSProperty):
    props = {
        'Exclusions': ([basestring], False),
        'Path': (basestring, False),
    }


class Targets(AWSProperty):
    props = {
        'JdbcTargets': ([JdbcTarget], False),
        'S3Targets': ([S3Target], False),
    }


class Crawler(AWSObject):
    resource_type = "AWS::Glue::Crawler"

    props = {
        'Classifiers': ([basestring], False),
        'Configuration': (basestring, False),
        'CrawlerSecurityConfiguration': (basestring, False),
        'DatabaseName': (basestring, True),
        'Description': (basestring, False),
        'Name': (basestring, False),
        'Role': (basestring, True),
        'Schedule': (Schedule, False),
        'SchemaChangePolicy': (SchemaChangePolicy, False),
        'TablePrefix': (basestring, False),
        'Tags': (Tags, False),
        'Targets': (Targets, True),
    }


class ConnectionPasswordEncryption(AWSProperty):
    props = {
        'KmsKeyId': (basestring, False),
        'ReturnConnectionPasswordEncrypted': (boolean, False),
    }


class EncryptionAtRest(AWSProperty):
    props = {
        'CatalogEncryptionMode': (basestring, False),
        'SseAwsKmsKeyId': (basestring, False),
    }


class DataCatalogEncryptionSettingsProperty(AWSProperty):
    props = {
        'ConnectionPasswordEncryption':
            (ConnectionPasswordEncryption, False),
        'EncryptionAtRest': (EncryptionAtRest, False),
    }


class DataCatalogEncryptionSettings(AWSObject):
    resource_type = "AWS::Glue::DataCatalogEncryptionSettings"

    props = {
        'CatalogId': (basestring, True),
        'DataCatalogEncryptionSettings':
            (DataCatalogEncryptionSettingsProperty, True),
    }


class DatabaseInput(AWSProperty):
    props = {
        'Description': (basestring, False),
        'LocationUri': (basestring, False),
        'Name': (basestring, False),
        'Parameters': (dict, False),
    }


class Database(AWSObject):
    resource_type = "AWS::Glue::Database"

    props = {
        'CatalogId': (basestring, True),
        'DatabaseInput': (DatabaseInput, True),
    }


class DevEndpoint(AWSObject):
    resource_type = "AWS::Glue::DevEndpoint"

    props = {
        'EndpointName': (basestring, False),
        'ExtraJarsS3Path': (basestring, False),
        'ExtraPythonLibsS3Path': (basestring, False),
        'NumberOfNodes': (positive_integer, False),
        'PublicKey': (basestring, True),
        'RoleArn': (basestring, True),
        'SecurityConfiguration': (basestring, False),
        'SecurityGroupIds': ([basestring], False),
        'SubnetId': (basestring, False),
        'Tags': (Tags, False),
    }


class ConnectionsList(AWSProperty):
    props = {
        'Connections': ([basestring], False),
    }


class ExecutionProperty(AWSProperty):
    props = {
        'MaxConcurrentRuns': (positive_integer, False),
    }


class JobCommand(AWSProperty):
    props = {
        'Name': (basestring, False),
        'ScriptLocation': (basestring, False),
    }


class Job(AWSObject):
    resource_type = "AWS::Glue::Job"

    props = {
        'AllocatedCapacity': (double, False),
        'Command': (JobCommand, True),
        'Connections': (ConnectionsList, False),
        'DefaultArguments': (dict, False),
        'Description': (basestring, False),
        'ExecutionProperty': (ExecutionProperty, False),
        'LogUri': (basestring, False),
        'MaxRetries': (double, False),
        'Name': (basestring, False),
        'Role': (basestring, True),
        'SecurityConfiguration': (basestring, False),
        'Tags': (Tags, False),
    }


class Column(AWSProperty):
    props = {
        'Comment': (basestring, False),
        'Name': (basestring, True),
        'Type': (basestring, False),
    }


class Order(AWSProperty):
    props = {
        'Column': (basestring, True),
        'SortOrder': (integer_range(0, 1), False),
    }


class SerdeInfo(AWSProperty):
    props = {
        'Name': (basestring, False),
        'Parameters': (dict, False),
        'SerializationLibrary': (basestring, False),
    }


class SkewedInfo(AWSProperty):
    props = {
        'SkewedColumnNames': ([basestring], False),
        'SkewedColumnValues': ([basestring], False),
        'SkewedColumnValueLocationMaps': (dict, False),
    }


class StorageDescriptor(AWSProperty):
    props = {
        'BucketColumns': ([basestring], False),
        'Columns': ([Column], False),
        'Compressed': (boolean, False),
        'InputFormat': (basestring, False),
        'Location': (basestring, False),
        'NumberOfBuckets': (positive_integer, False),
        'OutputFormat': (basestring, False),
        'Parameters': (dict, False),
        'SerdeInfo': (SerdeInfo, False),
        'SkewedInfo': (SkewedInfo, False),
        'SortColumns': ([Order], False),
        'StoredAsSubDirectories': (boolean, False),
    }


class PartitionInput(AWSProperty):
    props = {
        'Parameters': (dict, False),
        'StorageDescriptor': (StorageDescriptor, False),
        'Values': ([basestring], True),
    }


class Partition(AWSObject):
    resource_type = "AWS::Glue::Partition"

    props = {
        'CatalogId': (basestring, True),
        'DatabaseName': (basestring, True),
        'PartitionInput': (PartitionInput, True),
        'TableName': (basestring, True),
    }


class CloudWatchEncryption(AWSProperty):
    props = {
        'CloudWatchEncryptionMode': (basestring, False),
        'KmsKeyArn': (basestring, False),
    }


class JobBookmarksEncryption(AWSProperty):
    props = {
        'JobBookmarksEncryptionMode': (basestring, False),
        'KmsKeyArn': (basestring, False),
    }


class S3Encryptions(AWSProperty):
    props = {
    }


class EncryptionConfiguration(AWSProperty):
    props = {
        'CloudWatchEncryption': (CloudWatchEncryption, False),
        'JobBookmarksEncryption': (JobBookmarksEncryption, False),
        'S3Encryptions': (S3Encryptions, False),
    }


class SecurityConfiguration(AWSObject):
    resource_type = "AWS::Glue::SecurityConfiguration"

    props = {
        'EncryptionConfiguration': (EncryptionConfiguration, True),
        'Name': (basestring, True),
    }


def table_type_validator(type):
    valid_types = [
        'EXTERNAL_TABLE',
        'VIRTUAL_VIEW',
    ]
    if type not in valid_types:
        raise ValueError('% is not a valid value for TableType' % type)
    return type


class TableInput(AWSProperty):
    props = {
        'Description': (basestring, False),
        'Name': (basestring, False),
        'Owner': (basestring, False),
        'Parameters': (dict, False),
        'PartitionKeys': ([Column], False),
        'Retention': (positive_integer, False),
        'StorageDescriptor': (StorageDescriptor, False),
        'TableType': (table_type_validator, False),
        'ViewExpandedText': (basestring, False),
        'ViewOriginalText': (basestring, False),
    }


class Table(AWSObject):
    resource_type = "AWS::Glue::Table"

    props = {
        'CatalogId': (basestring, True),
        'DatabaseName': (basestring, True),
        'TableInput': (TableInput, True),
    }


class Action(AWSProperty):
    props = {
        'Arguments': (dict, False),
        'JobName': (basestring, False),
        'SecurityConfiguration': (basestring, False),
    }


class Condition(AWSProperty):
    props = {
        'JobName': (basestring, False),
        'LogicalOperator': (basestring, False),
        'State': (basestring, False),
    }


class Predicate(AWSProperty):
    props = {
        'Conditions': ([Condition], False),
        'Logical': (basestring, False),
    }


def trigger_type_validator(type):
    valid_types = [
        'SCHEDULED',
        'CONDITIONAL',
        'ON_DEMAND',
    ]
    if type not in valid_types:
        raise ValueError('% is not a valid value for Type' % type)
    return type


class Trigger(AWSObject):
    resource_type = "AWS::Glue::Trigger"

    props = {
        'Actions': ([Action], True),
        'Description': (basestring, False),
        'Name': (basestring, False),
        'Predicate': (Predicate, False),
        'Schedule': (basestring, False),
        'Tags': (Tags, False),
        'Type': (trigger_type_validator, True),
    }
