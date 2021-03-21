# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, double
from .validators import integer, integer_range, positive_integer


class CsvClassifier(AWSProperty):
    props = {
        'AllowSingleColumn': (boolean, False),
        'ContainsHeader': (str, False),
        'Delimiter': (str, False),
        'DisableValueTrimming': (boolean, False),
        'Header': ([str], False),
        'Name': (str, False),
        'QuoteSymbol': (str, False),
    }


class GrokClassifier(AWSProperty):
    props = {
        'Classification': (str, True),
        'CustomPatterns': (str, False),
        'GrokPattern': (str, True),
        'Name': (str, False),
    }


class JsonClassifier(AWSProperty):
    props = {
        'JsonPath': (str, True),
        'Name': (str, False),
    }


class XMLClassifier(AWSProperty):
    props = {
        'Classification': (str, True),
        'Name': (str, False),
        'RowTag': (str, True),
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
        'AvailabilityZone': (str, False),
        'SecurityGroupIdList': ([str], False),
        'SubnetId': (str, False),
    }


def connection_type_validator(type):
    valid_types = [
        'CUSTOM',
        'JDBC',
        'KAFKA',
        'MARKETPLACE',
        'MONGODB',
        'NETWORK',
        'SFTP',
    ]
    if type not in valid_types:
        raise ValueError('% is not a valid value for ConnectionType' % type)
    return type


class ConnectionInput(AWSProperty):
    props = {
        'ConnectionProperties': (dict, True),
        'ConnectionType': (connection_type_validator, True),
        'Description': (str, False),
        'MatchCriteria': ([str], False),
        'Name': (str, False),
        'PhysicalConnectionRequirements':
            (PhysicalConnectionRequirements, False),
    }


class Connection(AWSObject):
    resource_type = "AWS::Glue::Connection"

    props = {
        'CatalogId': (str, True),
        'ConnectionInput': (ConnectionInput, True),
    }


class Schedule(AWSProperty):
    props = {
        'ScheduleExpression': (str, False),
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


class CatalogTarget(AWSProperty):
    props = {
        'DatabaseName': (str, False),
        'Tables': ([str], False),
    }


class DynamoDBTarget(AWSProperty):
    props = {
        'Path': (str, False),
    }


class JdbcTarget(AWSProperty):
    props = {
        'ConnectionName': (str, False),
        'Exclusions': ([str], False),
        'Path': (str, False),
    }


class S3Target(AWSProperty):
    props = {
        'Exclusions': ([str], False),
        'Path': (str, False),
    }


class Targets(AWSProperty):
    props = {
        'CatalogTargets': ([CatalogTarget], False),
        'DynamoDBTargets': ([DynamoDBTarget], False),
        'JdbcTargets': ([JdbcTarget], False),
        'S3Targets': ([S3Target], False),
    }


class Crawler(AWSObject):
    resource_type = "AWS::Glue::Crawler"

    props = {
        'Classifiers': ([str], False),
        'Configuration': (str, False),
        'CrawlerSecurityConfiguration': (str, False),
        'DatabaseName': (str, True),
        'Description': (str, False),
        'Name': (str, False),
        'Role': (str, True),
        'Schedule': (Schedule, False),
        'SchemaChangePolicy': (SchemaChangePolicy, False),
        'TablePrefix': (str, False),
        'Tags': (dict, False),
        'Targets': (Targets, True),
    }


class ConnectionPasswordEncryption(AWSProperty):
    props = {
        'KmsKeyId': (str, False),
        'ReturnConnectionPasswordEncrypted': (boolean, False),
    }


class EncryptionAtRest(AWSProperty):
    props = {
        'CatalogEncryptionMode': (str, False),
        'SseAwsKmsKeyId': (str, False),
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
        'CatalogId': (str, True),
        'DataCatalogEncryptionSettings':
            (DataCatalogEncryptionSettingsProperty, True),
    }


class DatabaseInput(AWSProperty):
    props = {
        'Description': (str, False),
        'LocationUri': (str, False),
        'Name': (str, False),
        'Parameters': (dict, False),
    }


class Database(AWSObject):
    resource_type = "AWS::Glue::Database"

    props = {
        'CatalogId': (str, True),
        'DatabaseInput': (DatabaseInput, True),
    }


class DevEndpoint(AWSObject):
    resource_type = "AWS::Glue::DevEndpoint"

    props = {
        'Arguments': (dict, False),
        'EndpointName': (str, False),
        'ExtraJarsS3Path': (str, False),
        'ExtraPythonLibsS3Path': (str, False),
        'GlueVersion': (str, False),
        'NumberOfNodes': (integer, False),
        'NumberOfWorkers': (integer, False),
        'PublicKey': (str, False),
        'PublicKeys': ([str], False),
        'RoleArn': (str, True),
        'SecurityConfiguration': (str, False),
        'SecurityGroupIds': ([str], False),
        'SubnetId': (str, False),
        'Tags': (dict, False),
        'WorkerType': (str, False),
    }


class ConnectionsList(AWSProperty):
    props = {
        'Connections': ([str], False),
    }


class ExecutionProperty(AWSProperty):
    props = {
        'MaxConcurrentRuns': (positive_integer, False),
    }


class JobCommand(AWSProperty):
    props = {
        'Name': (str, False),
        'PythonVersion': (str, False),
        'ScriptLocation': (str, False),
    }


class NotificationProperty(AWSProperty):
    props = {
        'NotifyDelayAfter': (integer, False),
    }


class Job(AWSObject):
    resource_type = "AWS::Glue::Job"

    props = {
        'AllocatedCapacity': (double, False),
        'Command': (JobCommand, True),
        'Connections': (ConnectionsList, False),
        'DefaultArguments': (dict, False),
        'Description': (str, False),
        'ExecutionProperty': (ExecutionProperty, False),
        'GlueVersion': (str, False),
        'LogUri': (str, False),
        'MaxCapacity': (double, False),
        'MaxRetries': (double, False),
        'Name': (str, False),
        'NotificationProperty': (NotificationProperty, False),
        'NumberOfWorkers': (integer, False),
        'Role': (str, True),
        'SecurityConfiguration': (str, False),
        'Tags': (dict, False),
        'Timeout': (integer, False),
        'WorkerType': (str, False),
    }


class GlueTables(AWSProperty):
    props = {
        'CatalogId': (str, False),
        'ConnectionName': (str, False),
        'DatabaseName': (str, True),
        'TableName': (str, True),
    }


class InputRecordTables(AWSProperty):
    props = {
        'GlueTables': ([GlueTables], False),
    }


class FindMatchesParameters(AWSProperty):
    props = {
        'AccuracyCostTradeoff': (float, False),
        'EnforceProvidedLabels': (boolean, False),
        'PrecisionRecallTradeoff': (float, False),
        'PrimaryKeyColumnName': (str, True),
    }


class TransformParameters(AWSProperty):
    props = {
        'FindMatchesParameters': (FindMatchesParameters, False),
        'TransformType': (str, True),
    }


class MLTransform(AWSObject):
    resource_type = "AWS::Glue::MLTransform"

    props = {
        'Description': (str, False),
        'GlueVersion': (str, False),
        'InputRecordTables': (InputRecordTables, True),
        'MaxCapacity': (double, False),
        'MaxRetries': (integer, False),
        'Name': (str, False),
        'NumberOfWorkers': (integer, False),
        'Role': (str, True),
        'Tags': (dict, False),
        'Timeout': (integer, False),
        'TransformParameters': (TransformParameters, True),
        'WorkerType': (str, False),
    }


class Column(AWSProperty):
    props = {
        'Comment': (str, False),
        'Name': (str, True),
        'Type': (str, False),
    }


class Order(AWSProperty):
    props = {
        'Column': (str, True),
        'SortOrder': (integer_range(0, 1), False),
    }


class SerdeInfo(AWSProperty):
    props = {
        'Name': (str, False),
        'Parameters': (dict, False),
        'SerializationLibrary': (str, False),
    }


class SkewedInfo(AWSProperty):
    props = {
        'SkewedColumnNames': ([str], False),
        'SkewedColumnValues': ([str], False),
        'SkewedColumnValueLocationMaps': (dict, False),
    }


class StorageDescriptor(AWSProperty):
    props = {
        'BucketColumns': ([str], False),
        'Columns': ([Column], False),
        'Compressed': (boolean, False),
        'InputFormat': (str, False),
        'Location': (str, False),
        'NumberOfBuckets': (positive_integer, False),
        'OutputFormat': (str, False),
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
        'Values': ([str], True),
    }


class Partition(AWSObject):
    resource_type = "AWS::Glue::Partition"

    props = {
        'CatalogId': (str, True),
        'DatabaseName': (str, True),
        'PartitionInput': (PartitionInput, True),
        'TableName': (str, True),
    }


class Registry(AWSObject):
    resource_type = "AWS::Glue::Registry"

    props = {
        'Description': (str, False),
        'Name': (str, True),
        'Tags': (Tags, False),
    }


class SchemaVersion(AWSProperty):
    props = {
        'IsLatest': (boolean, False),
        'VersionNumber': (integer, False),
    }


class Schema(AWSObject):
    resource_type = "AWS::Glue::Schema"

    props = {
        'CheckpointVersion': (SchemaVersion, False),
        'Compatibility': (str, True),
        'DataFormat': (str, True),
        'Description': (str, False),
        'Name': (str, True),
        'Registry': (Registry, False),
        'SchemaDefinition': (str, True),
        'Tags': (Tags, False),
    }


class SchemaVersionMetadata(AWSObject):
    resource_type = "AWS::Glue::SchemaVersionMetadata"

    props = {
        'Key': (str, True),
        'SchemaVersionId': (str, True),
        'Value': (str, True),
    }


class CloudWatchEncryption(AWSProperty):
    props = {
        'CloudWatchEncryptionMode': (str, False),
        'KmsKeyArn': (str, False),
    }


class JobBookmarksEncryption(AWSProperty):
    props = {
        'JobBookmarksEncryptionMode': (str, False),
        'KmsKeyArn': (str, False),
    }


class S3Encryption(AWSProperty):
    props = {
        'KmsKeyArn': (str, False),
        'S3EncryptionMode': (str, False),
    }


class EncryptionConfiguration(AWSProperty):
    props = {
        'CloudWatchEncryption': (CloudWatchEncryption, False),
        'JobBookmarksEncryption': (JobBookmarksEncryption, False),
        'S3Encryptions': ([S3Encryption], False),
    }


class SecurityConfiguration(AWSObject):
    resource_type = "AWS::Glue::SecurityConfiguration"

    props = {
        'EncryptionConfiguration': (EncryptionConfiguration, True),
        'Name': (str, True),
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
        'Description': (str, False),
        'Name': (str, False),
        'Owner': (str, False),
        'Parameters': (dict, False),
        'PartitionKeys': ([Column], False),
        'Retention': (positive_integer, False),
        'StorageDescriptor': (StorageDescriptor, False),
        'TableType': (table_type_validator, False),
        'ViewExpandedText': (str, False),
        'ViewOriginalText': (str, False),
    }


class Table(AWSObject):
    resource_type = "AWS::Glue::Table"

    props = {
        'CatalogId': (str, True),
        'DatabaseName': (str, True),
        'TableInput': (TableInput, True),
    }


class Action(AWSProperty):
    props = {
        'Arguments': (dict, False),
        'CrawlerName': (str, False),
        'JobName': (str, False),
        'SecurityConfiguration': (str, False),
    }


class Condition(AWSProperty):
    props = {
        'CrawlerName': (str, False),
        'CrawlState': (str, False),
        'JobName': (str, False),
        'LogicalOperator': (str, False),
        'State': (str, False),
    }


class Predicate(AWSProperty):
    props = {
        'Conditions': ([Condition], False),
        'Logical': (str, False),
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
        'Description': (str, False),
        'Name': (str, False),
        'Predicate': (Predicate, False),
        'Schedule': (str, False),
        'StartOnCreation': (boolean, False),
        'Tags': (dict, False),
        'Type': (str, True),
        'WorkflowName': (str, False),
    }


class Workflow(AWSObject):
    resource_type = "AWS::Glue::Workflow"

    props = {
        'DefaultRunProperties': (dict, False),
        'Description': (str, False),
        'Name': (str, False),
        'Tags': (dict, False),
    }
