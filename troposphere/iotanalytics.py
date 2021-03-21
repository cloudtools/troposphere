# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer, double


class RetentionPeriod(AWSProperty):
    props = {
        'NumberOfDays': (integer, False),
        'Unlimited': (boolean, False),
    }


class CustomerManagedS3(AWSProperty):
    props = {
        'Bucket': (str, True),
        'KeyPrefix': (str, False),
        'RoleArn': (str, True),
    }


class ServiceManagedS3(AWSProperty):
    props = {
    }


class ChannelStorage(AWSProperty):
    props = {
        'CustomerManagedS3': (CustomerManagedS3, False),
        'ServiceManagedS3': (ServiceManagedS3, False),
    }


class Channel(AWSObject):
    resource_type = "AWS::IoTAnalytics::Channel"

    props = {
        'ChannelName': (str, False),
        'ChannelStorage': (ChannelStorage, False),
        'RetentionPeriod': (RetentionPeriod, False),
        'Tags': ((Tags, list), False),
    }


class AddAttributes(AWSProperty):
    props = {
        'Attributes': (dict, False),
        'Name': (str, False),
        'Next': (str, False),
    }


class ActivityChannel(AWSProperty):
    props = {
        'ChannelName': (str, False),
        'Name': (str, False),
        'Next': (str, False),
    }


class ActivityDatastore(AWSProperty):
    props = {
        'DatastoreName': (str, False),
        'Name': (str, False),
    }


class DeviceRegistryEnrich(AWSProperty):
    props = {
        'Attribute': (str, False),
        'Name': (str, False),
        'Next': (str, False),
        'RoleArn': (str, False),
        'ThingName': (str, False),
    }


class DeviceShadowEnrich(AWSProperty):
    props = {
        'Attribute': (str, False),
        'Name': (str, False),
        'Next': (str, False),
        'RoleArn': (str, False),
        'ThingName': (str, False),
    }


class Filter(AWSProperty):
    props = {
        'Filter': (str, False),
        'Name': (str, False),
        'Next': (str, False),
    }


class Lambda(AWSProperty):
    props = {
        'BatchSize': (integer, False),
        'LambdaName': (str, False),
        'Name': (str, False),
        'Next': (str, False),
    }


class Math(AWSProperty):
    props = {
        'Attribute': (str, False),
        'Math': (str, False),
        'Name': (str, False),
        'Next': (str, False),
    }


class RemoveAttributes(AWSProperty):
    props = {
        'Attributes': ([str], False),
        'Name': (str, False),
        'Next': (str, False),
    }


class SelectAttributes(AWSProperty):
    props = {
        'Attributes': ([str], False),
        'Name': (str, False),
        'Next': (str, False),
    }


class Activity(AWSProperty):
    props = {
        'AddAttributes': (AddAttributes, False),
        'Channel': (ActivityChannel, False),
        'Datastore': (ActivityDatastore, False),
        'DeviceRegistryEnrich': (DeviceRegistryEnrich, False),
        'DeviceShadowEnrich': (DeviceShadowEnrich, False),
        'Filter': (Filter, False),
        'Lambda': (Lambda, False),
        'Math': (Math, False),
        'RemoveAttributes': (RemoveAttributes, False),
        'SelectAttributes': (SelectAttributes, False),
    }


class Pipeline(AWSObject):
    resource_type = "AWS::IoTAnalytics::Pipeline"

    props = {
        'PipelineActivities': ([Activity], True),
        'PipelineName': (str, False),
        'Tags': ((Tags, list), False),
    }


class ResourceConfiguration(AWSProperty):
    props = {
        'ComputeType': (str, True),
        'VolumeSizeInGB': (integer, True),
    }


class DatasetContentVersionValue(AWSProperty):
    props = {
        'DatasetName': (str, False),
    }


class OutputFileUriValue(AWSProperty):
    props = {
        'FileName': (str, False),
    }


class Variable(AWSProperty):
    props = {
        'DatasetContentVersionValue': (DatasetContentVersionValue, False),
        'DoubleValue': (double, False),
        'OutputFileUriValue': (OutputFileUriValue, False),
        'StringValue': (str, False),
        'VariableName': (str, False)
    }


class ContainerAction(AWSProperty):
    props = {
        'ExecutionRoleArn': (str, True),
        'Image': (str, True),
        'ResourceConfiguration': (ResourceConfiguration, False),
        'Variables': ([Variable], False),
    }


class DeltaTime(AWSProperty):
    props = {
        'TimeExpression': (str, True),
        'OffsetSeconds': (integer, True),
    }


class QueryActionFilter(AWSProperty):
    props = {
        'DeltaTime': (DeltaTime, False),
    }


class QueryAction(AWSProperty):
    props = {
        'Filters': ([QueryActionFilter], False),
        'SqlQuery': (str, False),
    }


class Action(AWSProperty):
    props = {
        'ActionName': (str, True),
        'ContainerAction': (ContainerAction, False),
        'QueryAction': (QueryAction, False)
    }


class IotEventsDestinationConfiguration(AWSProperty):
    props = {
        'InputName': (str, True),
        'RoleArn': (str, True),
    }


class GlueConfiguration(AWSProperty):
    props = {
        'DatabaseName': (str, True),
        'TableName': (str, True),
    }


class S3DestinationConfiguration(AWSProperty):
    props = {
        'Bucket': (str, True),
        'GlueConfiguration': (GlueConfiguration, False),
        'Key': (str, True),
        'RoleArn': (str, True),
    }


class DatasetContentDeliveryRuleDestination(AWSProperty):
    props = {
        'IotEventsDestinationConfiguration':
            (IotEventsDestinationConfiguration, False),
        'S3DestinationConfiguration': (S3DestinationConfiguration, False),
    }


class DatasetContentDeliveryRule(AWSProperty):
    props = {
        'Destination': (DatasetContentDeliveryRuleDestination, True),
        'EntryName': (str, False),
    }


class DeltaTimeSessionWindowConfiguration(AWSProperty):
    props = {
        'TimeoutInMinutes': (integer, True),
    }


class LateDataRuleConfiguration(AWSProperty):
    props = {
        'DeltaTimeSessionWindowConfiguration':
            (DeltaTimeSessionWindowConfiguration, False),
    }


class LateDataRule(AWSProperty):
    props = {
        'RuleConfiguration': (LateDataRuleConfiguration, True),
        'RuleName': (str, False),
    }


class Schedule(AWSProperty):
    props = {
        'ScheduleExpression': (str, True),
    }


class TriggeringDataset(AWSProperty):
    props = {
        'DatasetName': (str, True),
    }


class Trigger(AWSProperty):
    props = {
        'Schedule': (Schedule, False),
        'TriggeringDataset': (TriggeringDataset, False),
    }


class VersioningConfiguration(AWSProperty):
    props = {
        'MaxVersions': (integer, False),
        'Unlimited': (boolean, False),
    }


class Dataset(AWSObject):
    resource_type = "AWS::IoTAnalytics::Dataset"

    props = {
        'Actions': ([Action], True),
        'ContentDeliveryRules': ([DatasetContentDeliveryRule], False),
        'DatasetName': (str, False),
        'LateDataRules': ([LateDataRule], False),
        'RetentionPeriod': (RetentionPeriod, False),
        'Tags': (Tags, False),
        'Triggers': ([Trigger], False),
        'VersioningConfiguration': (VersioningConfiguration, False),
    }


class DatastoreStorage(AWSProperty):
    props = {
        'CustomerManagedS3': (CustomerManagedS3, False),
        'ServiceManagedS3': (ServiceManagedS3, False),
    }


class Column(AWSProperty):
    props = {
        'Name': (str, True),
        'Type': (str, True),
    }


class SchemaDefinition(AWSProperty):
    props = {
        'Columns': ([Column], False),
    }


class ParquetConfiguration(AWSProperty):
    props = {
        'SchemaDefinition': (SchemaDefinition, False),
    }


class FileFormatConfiguration(AWSProperty):
    props = {
        'JsonConfiguration': (dict, False),
        'ParquetConfiguration': (ParquetConfiguration, False),
    }


class Datastore(AWSObject):
    resource_type = "AWS::IoTAnalytics::Datastore"

    props = {
        'DatastoreName': (str, False),
        'DatastoreStorage': (DatastoreStorage, False),
        'FileFormatConfiguration': (FileFormatConfiguration, False),
        'RetentionPeriod': (RetentionPeriod, False),
        'Tags': ((Tags, list), False),
    }
