# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, integer


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


class AggregationAuthorization(AWSObject):
    resource_type = "AWS::Config::AggregationAuthorization"

    props = {
        'AuthorizedAccountId': (basestring, True),
        'AuthorizedAwsRegion': (basestring, True),
    }


class OrganizationAggregationSource(AWSProperty):
    props = {
        'AllAwsRegions': (boolean, False),
        'AwsRegions': ([basestring], False),
        'RoleArn': (basestring, True),
    }


class AccountAggregationSources(AWSProperty):
    props = {
        'AccountIds': ([basestring], True),
        'AllAwsRegions': (boolean, False),
        'AwsRegions': ([basestring], False),
    }


class ConfigurationAggregator(AWSObject):
    resource_type = "AWS::Config::ConfigurationAggregator"

    props = {
        'AccountAggregationSources': ([AccountAggregationSources], False),
        'ConfigurationAggregatorName': (basestring, True),
        'OrganizationAggregationSource':
            (OrganizationAggregationSource, False),
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


class OrganizationCustomRuleMetadata(AWSProperty):
    props = {
        'Description': (basestring, False),
        'InputParameters': (basestring, False),
        'LambdaFunctionArn': (basestring, True),
        'MaximumExecutionFrequency': (basestring, False),
        'OrganizationConfigRuleTriggerTypes': ([basestring], True),
        'ResourceIdScope': (basestring, False),
        'ResourceTypesScope': ([basestring], False),
        'TagKeyScope': (basestring, False),
        'TagValueScope': (basestring, False),
    }


class OrganizationManagedRuleMetadata(AWSProperty):
    props = {
        'Description': (basestring, False),
        'InputParameters': (basestring, False),
        'MaximumExecutionFrequency': (basestring, False),
        'ResourceIdScope': (basestring, False),
        'ResourceTypesScope': ([basestring], False),
        'RuleIdentifier': (basestring, True),
        'TagKeyScope': (basestring, False),
        'TagValueScope': (basestring, False),
    }


class OrganizationConfigRule(AWSObject):
    resource_type = "AWS::Config::OrganizationConfigRule"

    props = {
        'ExcludedAccounts': ([basestring], False),
        'OrganizationConfigRuleName': (basestring, True),
        'OrganizationCustomRuleMetadata':
            (OrganizationCustomRuleMetadata, False),
        'OrganizationManagedRuleMetadata':
            (OrganizationManagedRuleMetadata, False),
    }


class SsmControls(AWSProperty):
    props = {
        'ConcurrentExecutionRatePercentage': (integer, False),
        'ErrorPercentage': (integer, False),
    }


class ExecutionControls(AWSProperty):
    props = {
        'SsmControls': (SsmControls, False),
    }


class RemediationConfiguration(AWSObject):
    resource_type = "AWS::Config::RemediationConfiguration"

    props = {
        'Automatic': (boolean, False),
        'ConfigRuleName': (basestring, True),
        'ExecutionControls': (ExecutionControls, False),
        'MaximumAutomaticAttempts': (integer, False),
        'Parameters': (dict, False),
        'ResourceType': (basestring, False),
        'RetryAttemptSeconds': (integer, False),
        'TargetId': (basestring, True),
        'TargetType': (basestring, True),
        'TargetVersion': (basestring, False),
    }


class ConformancePackInputParameter(AWSProperty):
    props = {
        'ParameterName': (basestring, True),
        'ParameterValue': (basestring, True),
    }


class ConformancePack(AWSObject):
    resource_type = "AWS::Config::ConformancePack"

    props = {
        'ConformancePackInputParameters': ([ConformancePackInputParameter], False),  # NOQA
        'ConformancePackName': (basestring, True),
        'DeliveryS3Bucket': (basestring, True),
        'DeliveryS3KeyPrefix': (basestring, False),
        'TemplateBody': (basestring, False),
        'TemplateS3Uri': (basestring, False),
    }


class OrganizationConformancePack(AWSObject):
    resource_type = "AWS::Config::OrganizationConformancePack"

    props = {
        'ConformancePackInputParameters': ([ConformancePackInputParameter], False),  # NOQA
        'DeliveryS3Bucket': (basestring, True),
        'DeliveryS3KeyPrefix': (basestring, False),
        'ExcludedAccounts': ([basestring], False),
        'OrganizationConformancePackName': (basestring, True),
        'TemplateBody': (basestring, False),
        'TemplateS3Uri': (basestring, False),
    }
