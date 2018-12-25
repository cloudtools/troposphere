# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer, json_checker, double
try:
    from awacs.aws import Policy
    policytypes = (dict, Policy)
except ImportError:
    policytypes = dict,


class RetentionPeriod(AWSProperty):
    props = {
        'NumberOfDays': (integer, False),
        'Unlimited': (boolean, False),
    }


class Channel(AWSObject):
    resource_type = "AWS::IoTAnalytics::Channel"

    props = {
        'ChannelName': (basestring, False),
        'RetentionPeriod': (RetentionPeriod, False),
        'Tags': ((Tags, list), False),
    }


class AddAttributes(AWSProperty):
    props = {
        'Attributes': (json_checker, False),
        'Name': (basestring, False),
        'Next': (basestring, False),
    }


class ActivityChannel(AWSProperty):
    props = {
        'ChannelName': (basestring, False),
        'Name': (basestring, False),
        'Next': (basestring, False),
    }


class Datastore(AWSProperty):
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
        'Datastore': (Datastore, False),
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


class RetentionPeriod(AWSProperty):
    props = {
        'NumberOfDays': (integer, False),
        'Unlimited': (boolean, False),
    }


class Datastore(AWSObject):
    resource_type = "AWS::IoTAnalytics::Datastore"

    props = {
        'DatastoreName': (basestring, False),
        'RetentionPeriod': (RetentionPeriod, False),
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


class Dataset(AWSObject):
    resource_type = "AWS::IoTAnalytics::Dataset"

    props = {
        'Actions': ([Action], True),
        'DatasetName': (basestring, False),
        'RetentionPeriod': (RetentionPeriod, False),
        'Tags': ((Tags, list), False),
        'Triggers': ([Trigger], False),
    }
