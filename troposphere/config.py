# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean


ONE_HOUR = "One_Hour"
THREE_HOURS = "Three_Hours"
SIX_HOURS = "Six_Hours"
TWELVE_HOURS = "Twelve_Hours"
TWENTYFOUR_HOURS = "TwentyFour_Hours"


class Scope(AWSProperty):
    props = {
        'ComplianceResourceId': (basestring, False),
        'ComplianceResourceTypes': ([basestring], False),
        'TagKey': (basestring, False),
        'TagValue': (basestring, False),
    }


class SourceDetails(AWSProperty):
    props = {
        'EventSource': (basestring, True),
        'MaximumExecutionFrequency': (basestring, False),
        'MessageType': (basestring, True),
    }

    def validate(self):
        valid_freqs = [
            ONE_HOUR,
            THREE_HOURS,
            SIX_HOURS,
            TWELVE_HOURS,
            TWENTYFOUR_HOURS,
        ]
        freq = self.properties.get('MaximumExecutionFrequency')
        if freq and freq not in valid_freqs:
            raise ValueError(
                "MaximumExecutionFrequency (given: %s) must be one of: %s" % (
                    freq, ', '.join(valid_freqs)))


class Source(AWSProperty):
    props = {
        'Owner': (basestring, True),
        'SourceDetails': ([SourceDetails], False),
        'SourceIdentifier': (basestring, True),
    }


class ConfigRule(AWSObject):
    resource_type = "AWS::Config::ConfigRule"

    props = {
        'ConfigRuleName': (basestring, False),
        'Description': (basestring, False),
        'InputParameters': (dict, False),
        'MaximumExecutionFrequency': (basestring, False),
        'Scope': (Scope, False),
        'Source': (Source, True),
    }


class RecordingGroup(AWSProperty):
    props = {
        'AllSupported': (boolean, False),
        'IncludeGlobalResourceTypes': (boolean, False),
        'ResourceTypes': ([basestring], False),
    }


class ConfigurationRecorder(AWSObject):
    resource_type = "AWS::Config::ConfigurationRecorder"

    props = {
        'Name': (basestring, False),
        'RecordingGroup': (RecordingGroup, False),
        'RoleARN': (basestring, True),
    }


class ConfigSnapshotDeliveryProperties(AWSProperty):
    props = {
        'DeliveryFrequency': (basestring, False),
    }


class DeliveryChannel(AWSObject):
    resource_type = "AWS::Config::DeliveryChannel"

    props = {
        'ConfigSnapshotDeliveryProperties':
            (ConfigSnapshotDeliveryProperties, False),
        'Name': (basestring, False),
        'S3BucketName': (basestring, True),
        'S3KeyPrefix': (basestring, False),
        'SnsTopicARN': (basestring, False),
    }
