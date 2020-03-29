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
        'Bucket': (basestring, True),
        'KeyPrefix': (basestring, False),
        'RoleArn': (basestring, True),
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
        'ChannelName': (basestring, False),
        'ChannelStorage': (ChannelStorage, False),
        'RetentionPeriod': (RetentionPeriod, False),
        'Tags': ((Tags, list), False),
    }


class AddAttributes(AWSProperty):
    props = {
        'Attributes': (dict, False),
        'Name': (basestring, False),
        'Next': (basestring, False),
    }


class ActivityChannel(AWSProperty):
    props = {
        'ChannelName': (basestring, False),
        'Name': (basestring, False),
        'Next': (basestring, False),
    }


class ActivityDatastore(AWSProperty):
    props = {
        'DatastoreName': (basestring, False),
        'Name': (basestring, False),
    }


class DeviceRegistryEnrich(AWSProperty):
    props = {
        'Attribute': (basestring, False),
        'Name': (basestring, False),
        'Next': (basestring, False),
        'RoleArn': (basestring, False),
        'ThingName': (basestring, False),
    }


class DeviceShadowEnrich(AWSProperty):
    props = {
        'Attribute': (basestring, False),
        'Name': (basestring, False),
        'Next': (basestring, False),
        'RoleArn': (basestring, False),
        'ThingName': (basestring, False),
    }


class Filter(AWSProperty):
    props = {
        'Filter': (basestring, False),
        'Name': (basestring, False),
        'Next': (basestring, False),
    }


class Lambda(AWSProperty):
    props = {
        'BatchSize': (integer, False),
        'LambdaName': (basestring, False),
        'Name': (basestring, False),
        'Next': (basestring, False),
    }


class Math(AWSProperty):
    props = {
        'Attribute': (basestring, False),
        'Math': (basestring, False),
        'Name': (basestring, False),
        'Next': (basestring, False),
    }


class RemoveAttributes(AWSProperty):
    props = {
        'Attributes': ([basestring], False),
        'Name': (basestring, False),
        'Next': (basestring, False),
    }


class SelectAttributes(AWSProperty):
    props = {
        'Attributes': ([basestring], False),
        'Name': (basestring, False),
        'Next': (basestring, False),
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
        'PipelineName': (basestring, False),
        'Tags': ((Tags, list), False),
    }


class ResourceConfiguration(AWSProperty):
    props = {
        'ComputeType': (basestring, True),
        'VolumeSizeInGB': (integer, True),
    }


class DatasetContentVersionValue(AWSProperty):
    props = {
        'DatasetName': (basestring, False),
    }


class OutputFileUriValue(AWSProperty):
    props = {
        'FileName': (basestring, False),
    }


class Variable(AWSProperty):
    props = {
        'DatasetContentVersionValue': (DatasetContentVersionValue, False),
        'DoubleValue': (double, False),
        'OutputFileUriValue': (OutputFileUriValue, False),
        'StringValue': (basestring, False),
        'VariableName': (basestring, False)
    }


class ContainerAction(AWSProperty):
    props = {
        'ExecutionRoleArn': (basestring, True),
        'Image': (basestring, True),
        'ResourceConfiguration': (ResourceConfiguration, False),
        'Variables': ([Variable], False),
    }


class DeltaTime(AWSProperty):
    props = {
        'TimeExpression': (basestring, True),
        'OffsetSeconds': (integer, True),
    }


class QueryActionFilter(AWSProperty):
    props = {
        'DeltaTime': (DeltaTime, False),
    }


class QueryAction(AWSProperty):
    props = {
        'Filters': ([QueryActionFilter], False),
        'SqlQuery': (basestring, False),
    }


class Action(AWSProperty):
    props = {
        'ActionName': (basestring, True),
        'ContainerAction': (ContainerAction, False),
        'QueryAction': (QueryAction, False)
    }


class IotEventsDestinationConfiguration(AWSProperty):
    props = {
        'InputName': (basestring, True),
        'RoleArn': (basestring, True),
    }


class GlueConfiguration(AWSProperty):
    props = {
        'DatabaseName': (basestring, True),
        'TableName': (basestring, True),
    }


class S3DestinationConfiguration(AWSProperty):
    props = {
        'Bucket': (basestring, True),
        'GlueConfiguration': (GlueConfiguration, False),
        'Key': (basestring, True),
        'RoleArn': (basestring, True),
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
        'EntryName': (basestring, False),
    }


class Schedule(AWSProperty):
    props = {
        'ScheduleExpression': (basestring, True),
    }


class TriggeringDataset(AWSProperty):
    props = {
        'DatasetName': (basestring, True),
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
        'DatasetName': (basestring, False),
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


class Datastore(AWSObject):
    resource_type = "AWS::IoTAnalytics::Datastore"

    props = {
        'DatastoreName': (basestring, False),
        'DatastoreStorage': (DatastoreStorage, False),
        'RetentionPeriod': (RetentionPeriod, False),
        'Tags': ((Tags, list), False),
    }
