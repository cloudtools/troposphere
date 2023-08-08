# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.glue import (
    connection_type_validator,
    delete_behavior_validator,
    table_type_validator,
    trigger_type_validator,
    update_behavior_validator,
    validate_sortorder,
)


class CsvClassifier(AWSProperty):
    """
    `CsvClassifier <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html>`__
    """

    props: PropsDictType = {
        "AllowSingleColumn": (boolean, False),
        "ContainsHeader": (str, False),
        "Delimiter": (str, False),
        "DisableValueTrimming": (boolean, False),
        "Header": ([str], False),
        "Name": (str, False),
        "QuoteSymbol": (str, False),
    }


class GrokClassifier(AWSProperty):
    """
    `GrokClassifier <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-grokclassifier.html>`__
    """

    props: PropsDictType = {
        "Classification": (str, True),
        "CustomPatterns": (str, False),
        "GrokPattern": (str, True),
        "Name": (str, False),
    }


class JsonClassifier(AWSProperty):
    """
    `JsonClassifier <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-jsonclassifier.html>`__
    """

    props: PropsDictType = {
        "JsonPath": (str, True),
        "Name": (str, False),
    }


class XMLClassifier(AWSProperty):
    """
    `XMLClassifier <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-xmlclassifier.html>`__
    """

    props: PropsDictType = {
        "Classification": (str, True),
        "Name": (str, False),
        "RowTag": (str, True),
    }


class Classifier(AWSObject):
    """
    `Classifier <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-classifier.html>`__
    """

    resource_type = "AWS::Glue::Classifier"

    props: PropsDictType = {
        "CsvClassifier": (CsvClassifier, False),
        "GrokClassifier": (GrokClassifier, False),
        "JsonClassifier": (JsonClassifier, False),
        "XMLClassifier": (XMLClassifier, False),
    }


class PhysicalConnectionRequirements(AWSProperty):
    """
    `PhysicalConnectionRequirements <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-physicalconnectionrequirements.html>`__
    """

    props: PropsDictType = {
        "AvailabilityZone": (str, False),
        "SecurityGroupIdList": ([str], False),
        "SubnetId": (str, False),
    }


class ConnectionInput(AWSProperty):
    """
    `ConnectionInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-connectioninput.html>`__
    """

    props: PropsDictType = {
        "ConnectionProperties": (dict, False),
        "ConnectionType": (connection_type_validator, True),
        "Description": (str, False),
        "MatchCriteria": ([str], False),
        "Name": (str, False),
        "PhysicalConnectionRequirements": (PhysicalConnectionRequirements, False),
    }


class Connection(AWSObject):
    """
    `Connection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-connection.html>`__
    """

    resource_type = "AWS::Glue::Connection"

    props: PropsDictType = {
        "CatalogId": (str, True),
        "ConnectionInput": (ConnectionInput, True),
    }


class RecrawlPolicy(AWSProperty):
    """
    `RecrawlPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-recrawlpolicy.html>`__
    """

    props: PropsDictType = {
        "RecrawlBehavior": (str, False),
    }


class Schedule(AWSProperty):
    """
    `Schedule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-schedule.html>`__
    """

    props: PropsDictType = {
        "ScheduleExpression": (str, False),
    }


class SchemaChangePolicy(AWSProperty):
    """
    `SchemaChangePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-schemachangepolicy.html>`__
    """

    props: PropsDictType = {
        "DeleteBehavior": (delete_behavior_validator, False),
        "UpdateBehavior": (update_behavior_validator, False),
    }


class CatalogTarget(AWSProperty):
    """
    `CatalogTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-catalogtarget.html>`__
    """

    props: PropsDictType = {
        "ConnectionName": (str, False),
        "DatabaseName": (str, False),
        "DlqEventQueueArn": (str, False),
        "EventQueueArn": (str, False),
        "Tables": ([str], False),
    }


class DeltaTarget(AWSProperty):
    """
    `DeltaTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-deltatarget.html>`__
    """

    props: PropsDictType = {
        "ConnectionName": (str, False),
        "CreateNativeDeltaTable": (boolean, False),
        "DeltaTables": ([str], False),
        "WriteManifest": (boolean, False),
    }


class DynamoDBTarget(AWSProperty):
    """
    `DynamoDBTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-dynamodbtarget.html>`__
    """

    props: PropsDictType = {
        "Path": (str, False),
    }


class JdbcTarget(AWSProperty):
    """
    `JdbcTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-jdbctarget.html>`__
    """

    props: PropsDictType = {
        "ConnectionName": (str, False),
        "Exclusions": ([str], False),
        "Path": (str, False),
    }


class MongoDBTarget(AWSProperty):
    """
    `MongoDBTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-mongodbtarget.html>`__
    """

    props: PropsDictType = {
        "ConnectionName": (str, False),
        "Path": (str, False),
    }


class S3Target(AWSProperty):
    """
    `S3Target <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-s3target.html>`__
    """

    props: PropsDictType = {
        "ConnectionName": (str, False),
        "DlqEventQueueArn": (str, False),
        "EventQueueArn": (str, False),
        "Exclusions": ([str], False),
        "Path": (str, False),
        "SampleSize": (integer, False),
    }


class Targets(AWSProperty):
    """
    `Targets <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html>`__
    """

    props: PropsDictType = {
        "CatalogTargets": ([CatalogTarget], False),
        "DeltaTargets": ([DeltaTarget], False),
        "DynamoDBTargets": ([DynamoDBTarget], False),
        "JdbcTargets": ([JdbcTarget], False),
        "MongoDBTargets": ([MongoDBTarget], False),
        "S3Targets": ([S3Target], False),
    }


class Crawler(AWSObject):
    """
    `Crawler <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html>`__
    """

    resource_type = "AWS::Glue::Crawler"

    props: PropsDictType = {
        "Classifiers": ([str], False),
        "Configuration": (str, False),
        "CrawlerSecurityConfiguration": (str, False),
        "DatabaseName": (str, False),
        "Description": (str, False),
        "Name": (str, False),
        "RecrawlPolicy": (RecrawlPolicy, False),
        "Role": (str, True),
        "Schedule": (Schedule, False),
        "SchemaChangePolicy": (SchemaChangePolicy, False),
        "TablePrefix": (str, False),
        "Tags": (dict, False),
        "Targets": (Targets, True),
    }


class ConnectionPasswordEncryption(AWSProperty):
    """
    `ConnectionPasswordEncryption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-connectionpasswordencryption.html>`__
    """

    props: PropsDictType = {
        "KmsKeyId": (str, False),
        "ReturnConnectionPasswordEncrypted": (boolean, False),
    }


class EncryptionAtRest(AWSProperty):
    """
    `EncryptionAtRest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-encryptionatrest.html>`__
    """

    props: PropsDictType = {
        "CatalogEncryptionMode": (str, False),
        "SseAwsKmsKeyId": (str, False),
    }


class DataCatalogEncryptionSettingsProperty(AWSProperty):
    """
    `DataCatalogEncryptionSettingsProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-datacatalogencryptionsettings.html>`__
    """

    props: PropsDictType = {
        "ConnectionPasswordEncryption": (ConnectionPasswordEncryption, False),
        "EncryptionAtRest": (EncryptionAtRest, False),
    }


class DataCatalogEncryptionSettings(AWSObject):
    """
    `DataCatalogEncryptionSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-datacatalogencryptionsettings.html>`__
    """

    resource_type = "AWS::Glue::DataCatalogEncryptionSettings"

    props: PropsDictType = {
        "CatalogId": (str, True),
        "DataCatalogEncryptionSettings": (DataCatalogEncryptionSettingsProperty, True),
    }


class DatabaseIdentifier(AWSProperty):
    """
    `DatabaseIdentifier <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseidentifier.html>`__
    """

    props: PropsDictType = {
        "CatalogId": (str, False),
        "DatabaseName": (str, False),
    }


class FederatedDatabase(AWSProperty):
    """
    `FederatedDatabase <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput-federateddatabase.html>`__
    """

    props: PropsDictType = {
        "ConnectionName": (str, False),
        "Identifier": (str, False),
    }


class DataLakePrincipal(AWSProperty):
    """
    `DataLakePrincipal <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-datalakeprincipal.html>`__
    """

    props: PropsDictType = {
        "DataLakePrincipalIdentifier": (str, False),
    }


class PrincipalPrivileges(AWSProperty):
    """
    `PrincipalPrivileges <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-principalprivileges.html>`__
    """

    props: PropsDictType = {
        "Permissions": ([str], False),
        "Principal": (DataLakePrincipal, False),
    }


class DatabaseInput(AWSProperty):
    """
    `DatabaseInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html>`__
    """

    props: PropsDictType = {
        "CreateTableDefaultPermissions": ([PrincipalPrivileges], False),
        "Description": (str, False),
        "FederatedDatabase": (FederatedDatabase, False),
        "LocationUri": (str, False),
        "Name": (str, False),
        "Parameters": (dict, False),
        "TargetDatabase": (DatabaseIdentifier, False),
    }


class Database(AWSObject):
    """
    `Database <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-database.html>`__
    """

    resource_type = "AWS::Glue::Database"

    props: PropsDictType = {
        "CatalogId": (str, True),
        "DatabaseInput": (DatabaseInput, True),
    }


class DevEndpoint(AWSObject):
    """
    `DevEndpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html>`__
    """

    resource_type = "AWS::Glue::DevEndpoint"

    props: PropsDictType = {
        "Arguments": (dict, False),
        "EndpointName": (str, False),
        "ExtraJarsS3Path": (str, False),
        "ExtraPythonLibsS3Path": (str, False),
        "GlueVersion": (str, False),
        "NumberOfNodes": (integer, False),
        "NumberOfWorkers": (integer, False),
        "PublicKey": (str, False),
        "PublicKeys": ([str], False),
        "RoleArn": (str, True),
        "SecurityConfiguration": (str, False),
        "SecurityGroupIds": ([str], False),
        "SubnetId": (str, False),
        "Tags": (dict, False),
        "WorkerType": (str, False),
    }


class ConnectionsList(AWSProperty):
    """
    `ConnectionsList <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-connectionslist.html>`__
    """

    props: PropsDictType = {
        "Connections": ([str], False),
    }


class ExecutionProperty(AWSProperty):
    """
    `ExecutionProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-executionproperty.html>`__
    """

    props: PropsDictType = {
        "MaxConcurrentRuns": (double, False),
    }


class JobCommand(AWSProperty):
    """
    `JobCommand <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-jobcommand.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "PythonVersion": (str, False),
        "ScriptLocation": (str, False),
    }


class NotificationProperty(AWSProperty):
    """
    `NotificationProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-notificationproperty.html>`__
    """

    props: PropsDictType = {
        "NotifyDelayAfter": (integer, False),
    }


class Job(AWSObject):
    """
    `Job <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html>`__
    """

    resource_type = "AWS::Glue::Job"

    props: PropsDictType = {
        "AllocatedCapacity": (double, False),
        "Command": (JobCommand, True),
        "Connections": (ConnectionsList, False),
        "DefaultArguments": (dict, False),
        "Description": (str, False),
        "ExecutionClass": (str, False),
        "ExecutionProperty": (ExecutionProperty, False),
        "GlueVersion": (str, False),
        "LogUri": (str, False),
        "MaxCapacity": (double, False),
        "MaxRetries": (double, False),
        "Name": (str, False),
        "NonOverridableArguments": (dict, False),
        "NotificationProperty": (NotificationProperty, False),
        "NumberOfWorkers": (integer, False),
        "Role": (str, True),
        "SecurityConfiguration": (str, False),
        "Tags": (dict, False),
        "Timeout": (integer, False),
        "WorkerType": (str, False),
    }


class GlueTables(AWSProperty):
    """
    `GlueTables <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables-gluetables.html>`__
    """

    props: PropsDictType = {
        "CatalogId": (str, False),
        "ConnectionName": (str, False),
        "DatabaseName": (str, True),
        "TableName": (str, True),
    }


class InputRecordTables(AWSProperty):
    """
    `InputRecordTables <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables.html>`__
    """

    props: PropsDictType = {
        "GlueTables": ([GlueTables], False),
    }


class MLUserDataEncryption(AWSProperty):
    """
    `MLUserDataEncryption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption-mluserdataencryption.html>`__
    """

    props: PropsDictType = {
        "KmsKeyId": (str, False),
        "MLUserDataEncryptionMode": (str, True),
    }


class TransformEncryption(AWSProperty):
    """
    `TransformEncryption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption.html>`__
    """

    props: PropsDictType = {
        "MLUserDataEncryption": (MLUserDataEncryption, False),
        "TaskRunSecurityConfigurationName": (str, False),
    }


class FindMatchesParameters(AWSProperty):
    """
    `FindMatchesParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters-findmatchesparameters.html>`__
    """

    props: PropsDictType = {
        "AccuracyCostTradeoff": (double, False),
        "EnforceProvidedLabels": (boolean, False),
        "PrecisionRecallTradeoff": (double, False),
        "PrimaryKeyColumnName": (str, True),
    }


class TransformParameters(AWSProperty):
    """
    `TransformParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters.html>`__
    """

    props: PropsDictType = {
        "FindMatchesParameters": (FindMatchesParameters, False),
        "TransformType": (str, True),
    }


class MLTransform(AWSObject):
    """
    `MLTransform <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html>`__
    """

    resource_type = "AWS::Glue::MLTransform"

    props: PropsDictType = {
        "Description": (str, False),
        "GlueVersion": (str, False),
        "InputRecordTables": (InputRecordTables, True),
        "MaxCapacity": (double, False),
        "MaxRetries": (integer, False),
        "Name": (str, False),
        "NumberOfWorkers": (integer, False),
        "Role": (str, True),
        "Tags": (dict, False),
        "Timeout": (integer, False),
        "TransformEncryption": (TransformEncryption, False),
        "TransformParameters": (TransformParameters, True),
        "WorkerType": (str, False),
    }


class Column(AWSProperty):
    """
    `Column <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-column.html>`__
    """

    props: PropsDictType = {
        "Comment": (str, False),
        "Name": (str, True),
        "Type": (str, False),
    }


class Order(AWSProperty):
    """
    `Order <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-order.html>`__
    """

    props: PropsDictType = {
        "Column": (str, True),
        "SortOrder": (validate_sortorder, True),
    }


class SchemaId(AWSProperty):
    """
    `SchemaId <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemaid.html>`__
    """

    props: PropsDictType = {
        "RegistryName": (str, False),
        "SchemaArn": (str, False),
        "SchemaName": (str, False),
    }


class SchemaReference(AWSProperty):
    """
    `SchemaReference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemareference.html>`__
    """

    props: PropsDictType = {
        "SchemaId": (SchemaId, False),
        "SchemaVersionId": (str, False),
        "SchemaVersionNumber": (integer, False),
    }


class SerdeInfo(AWSProperty):
    """
    `SerdeInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-serdeinfo.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Parameters": (dict, False),
        "SerializationLibrary": (str, False),
    }


class SkewedInfo(AWSProperty):
    """
    `SkewedInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-skewedinfo.html>`__
    """

    props: PropsDictType = {
        "SkewedColumnNames": ([str], False),
        "SkewedColumnValueLocationMaps": (dict, False),
        "SkewedColumnValues": ([str], False),
    }


class StorageDescriptor(AWSProperty):
    """
    `StorageDescriptor <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html>`__
    """

    props: PropsDictType = {
        "BucketColumns": ([str], False),
        "Columns": ([Column], False),
        "Compressed": (boolean, False),
        "InputFormat": (str, False),
        "Location": (str, False),
        "NumberOfBuckets": (integer, False),
        "OutputFormat": (str, False),
        "Parameters": (dict, False),
        "SchemaReference": (SchemaReference, False),
        "SerdeInfo": (SerdeInfo, False),
        "SkewedInfo": (SkewedInfo, False),
        "SortColumns": ([Order], False),
        "StoredAsSubDirectories": (boolean, False),
    }


class PartitionInput(AWSProperty):
    """
    `PartitionInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-partitioninput.html>`__
    """

    props: PropsDictType = {
        "Parameters": (dict, False),
        "StorageDescriptor": (StorageDescriptor, False),
        "Values": ([str], True),
    }


class Partition(AWSObject):
    """
    `Partition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-partition.html>`__
    """

    resource_type = "AWS::Glue::Partition"

    props: PropsDictType = {
        "CatalogId": (str, True),
        "DatabaseName": (str, True),
        "PartitionInput": (PartitionInput, True),
        "TableName": (str, True),
    }


class Registry(AWSObject):
    """
    `Registry <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-registry.html>`__
    """

    resource_type = "AWS::Glue::Registry"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class RegistryProperty(AWSProperty):
    """
    `RegistryProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schema-registry.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, False),
        "Name": (str, False),
    }


class SchemaVersionProperty(AWSProperty):
    """
    `SchemaVersionProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schema-schemaversion.html>`__
    """

    props: PropsDictType = {
        "IsLatest": (boolean, False),
        "VersionNumber": (integer, False),
    }


class Schema(AWSObject):
    """
    `Schema <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html>`__
    """

    resource_type = "AWS::Glue::Schema"

    props: PropsDictType = {
        "CheckpointVersion": (SchemaVersionProperty, False),
        "Compatibility": (str, True),
        "DataFormat": (str, True),
        "Description": (str, False),
        "Name": (str, True),
        "Registry": (RegistryProperty, False),
        "SchemaDefinition": (str, True),
        "Tags": (Tags, False),
    }


class SchemaProperty(AWSProperty):
    """
    `SchemaProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schemaversion-schema.html>`__
    """

    props: PropsDictType = {
        "RegistryName": (str, False),
        "SchemaArn": (str, False),
        "SchemaName": (str, False),
    }


class SchemaVersion(AWSObject):
    """
    `SchemaVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.html>`__
    """

    resource_type = "AWS::Glue::SchemaVersion"

    props: PropsDictType = {
        "Schema": (SchemaProperty, True),
        "SchemaDefinition": (str, True),
    }


class SchemaVersionMetadata(AWSObject):
    """
    `SchemaVersionMetadata <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversionmetadata.html>`__
    """

    resource_type = "AWS::Glue::SchemaVersionMetadata"

    props: PropsDictType = {
        "Key": (str, True),
        "SchemaVersionId": (str, True),
        "Value": (str, True),
    }


class CloudWatchEncryption(AWSProperty):
    """
    `CloudWatchEncryption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-cloudwatchencryption.html>`__
    """

    props: PropsDictType = {
        "CloudWatchEncryptionMode": (str, False),
        "KmsKeyArn": (str, False),
    }


class JobBookmarksEncryption(AWSProperty):
    """
    `JobBookmarksEncryption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-jobbookmarksencryption.html>`__
    """

    props: PropsDictType = {
        "JobBookmarksEncryptionMode": (str, False),
        "KmsKeyArn": (str, False),
    }


class S3Encryption(AWSProperty):
    """
    `S3Encryption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-s3encryption.html>`__
    """

    props: PropsDictType = {
        "KmsKeyArn": (str, False),
        "S3EncryptionMode": (str, False),
    }


class EncryptionConfiguration(AWSProperty):
    """
    `EncryptionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-encryptionconfiguration.html>`__
    """

    props: PropsDictType = {
        "CloudWatchEncryption": (CloudWatchEncryption, False),
        "JobBookmarksEncryption": (JobBookmarksEncryption, False),
        "S3Encryptions": ([S3Encryption], False),
    }


class SecurityConfiguration(AWSObject):
    """
    `SecurityConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-securityconfiguration.html>`__
    """

    resource_type = "AWS::Glue::SecurityConfiguration"

    props: PropsDictType = {
        "EncryptionConfiguration": (EncryptionConfiguration, True),
        "Name": (str, True),
    }


class TableIdentifier(AWSProperty):
    """
    `TableIdentifier <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableidentifier.html>`__
    """

    props: PropsDictType = {
        "CatalogId": (str, False),
        "DatabaseName": (str, False),
        "Name": (str, False),
    }


class TableInput(AWSProperty):
    """
    `TableInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html>`__
    """

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, False),
        "Owner": (str, False),
        "Parameters": (dict, False),
        "PartitionKeys": ([Column], False),
        "Retention": (integer, False),
        "StorageDescriptor": (StorageDescriptor, False),
        "TableType": (table_type_validator, False),
        "TargetTable": (TableIdentifier, False),
        "ViewExpandedText": (str, False),
        "ViewOriginalText": (str, False),
    }


class Table(AWSObject):
    """
    `Table <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.html>`__
    """

    resource_type = "AWS::Glue::Table"

    props: PropsDictType = {
        "CatalogId": (str, True),
        "DatabaseName": (str, True),
        "TableInput": (TableInput, True),
    }


class Action(AWSProperty):
    """
    `Action <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-action.html>`__
    """

    props: PropsDictType = {
        "Arguments": (dict, False),
        "CrawlerName": (str, False),
        "JobName": (str, False),
        "NotificationProperty": (NotificationProperty, False),
        "SecurityConfiguration": (str, False),
        "Timeout": (integer, False),
    }


class EventBatchingCondition(AWSProperty):
    """
    `EventBatchingCondition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-eventbatchingcondition.html>`__
    """

    props: PropsDictType = {
        "BatchSize": (integer, True),
        "BatchWindow": (integer, False),
    }


class Condition(AWSProperty):
    """
    `Condition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-condition.html>`__
    """

    props: PropsDictType = {
        "CrawlState": (str, False),
        "CrawlerName": (str, False),
        "JobName": (str, False),
        "LogicalOperator": (str, False),
        "State": (str, False),
    }


class Predicate(AWSProperty):
    """
    `Predicate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-predicate.html>`__
    """

    props: PropsDictType = {
        "Conditions": ([Condition], False),
        "Logical": (str, False),
    }


class Trigger(AWSObject):
    """
    `Trigger <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html>`__
    """

    resource_type = "AWS::Glue::Trigger"

    props: PropsDictType = {
        "Actions": ([Action], True),
        "Description": (str, False),
        "EventBatchingCondition": (EventBatchingCondition, False),
        "Name": (str, False),
        "Predicate": (Predicate, False),
        "Schedule": (str, False),
        "StartOnCreation": (boolean, False),
        "Tags": (dict, False),
        "Type": (trigger_type_validator, True),
        "WorkflowName": (str, False),
    }


class Workflow(AWSObject):
    """
    `Workflow <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html>`__
    """

    resource_type = "AWS::Glue::Workflow"

    props: PropsDictType = {
        "DefaultRunProperties": (dict, False),
        "Description": (str, False),
        "MaxConcurrentRuns": (integer, False),
        "Name": (str, False),
        "Tags": (dict, False),
    }
