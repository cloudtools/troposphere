# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer


ONE_HOUR = "One_Hour"
THREE_HOURS = "Three_Hours"
SIX_HOURS = "Six_Hours"
TWELVE_HOURS = "Twelve_Hours"
TWENTYFOUR_HOURS = "TwentyFour_Hours"


class Scope(AWSProperty):
    props = {
        'ComplianceResourceId': (str, False),
        'ComplianceResourceTypes': ([str], False),
        'TagKey': (str, False),
        'TagValue': (str, False),
    }


class SourceDetails(AWSProperty):
    props = {
        'EventSource': (str, True),
        'MaximumExecutionFrequency': (str, False),
        'MessageType': (str, True),
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
        'Owner': (str, True),
        'SourceDetails': ([SourceDetails], False),
        'SourceIdentifier': (str, True),
    }


class ConfigRule(AWSObject):
    resource_type = "AWS::Config::ConfigRule"

    props = {
        'ConfigRuleName': (str, False),
        'Description': (str, False),
        'InputParameters': (dict, False),
        'MaximumExecutionFrequency': (str, False),
        'Scope': (Scope, False),
        'Source': (Source, True),
    }


class AggregationAuthorization(AWSObject):
    resource_type = "AWS::Config::AggregationAuthorization"

    props = {
        'AuthorizedAccountId': (str, True),
        'AuthorizedAwsRegion': (str, True),
    }


class OrganizationAggregationSource(AWSProperty):
    props = {
        'AllAwsRegions': (boolean, False),
        'AwsRegions': ([str], False),
        'RoleArn': (str, True),
    }


class AccountAggregationSources(AWSProperty):
    props = {
        'AccountIds': ([str], True),
        'AllAwsRegions': (boolean, False),
        'AwsRegions': ([str], False),
    }


class ConfigurationAggregator(AWSObject):
    resource_type = "AWS::Config::ConfigurationAggregator"

    props = {
        'AccountAggregationSources': ([AccountAggregationSources], False),
        'ConfigurationAggregatorName': (str, True),
        'OrganizationAggregationSource':
            (OrganizationAggregationSource, False),
    }


class RecordingGroup(AWSProperty):
    props = {
        'AllSupported': (boolean, False),
        'IncludeGlobalResourceTypes': (boolean, False),
        'ResourceTypes': ([str], False),
    }


class ConfigurationRecorder(AWSObject):
    resource_type = "AWS::Config::ConfigurationRecorder"

    props = {
        'Name': (str, False),
        'RecordingGroup': (RecordingGroup, False),
        'RoleARN': (str, True),
    }


class ConfigSnapshotDeliveryProperties(AWSProperty):
    props = {
        'DeliveryFrequency': (str, False),
    }


class DeliveryChannel(AWSObject):
    resource_type = "AWS::Config::DeliveryChannel"

    props = {
        'ConfigSnapshotDeliveryProperties':
            (ConfigSnapshotDeliveryProperties, False),
        'Name': (str, False),
        'S3BucketName': (str, True),
        'S3KeyPrefix': (str, False),
        'SnsTopicARN': (str, False),
    }


class OrganizationCustomRuleMetadata(AWSProperty):
    props = {
        'Description': (str, False),
        'InputParameters': (str, False),
        'LambdaFunctionArn': (str, True),
        'MaximumExecutionFrequency': (str, False),
        'OrganizationConfigRuleTriggerTypes': ([str], True),
        'ResourceIdScope': (str, False),
        'ResourceTypesScope': ([str], False),
        'TagKeyScope': (str, False),
        'TagValueScope': (str, False),
    }


class OrganizationManagedRuleMetadata(AWSProperty):
    props = {
        'Description': (str, False),
        'InputParameters': (str, False),
        'MaximumExecutionFrequency': (str, False),
        'ResourceIdScope': (str, False),
        'ResourceTypesScope': ([str], False),
        'RuleIdentifier': (str, True),
        'TagKeyScope': (str, False),
        'TagValueScope': (str, False),
    }


class OrganizationConfigRule(AWSObject):
    resource_type = "AWS::Config::OrganizationConfigRule"

    props = {
        'ExcludedAccounts': ([str], False),
        'OrganizationConfigRuleName': (str, True),
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
        'ConfigRuleName': (str, True),
        'ExecutionControls': (ExecutionControls, False),
        'MaximumAutomaticAttempts': (integer, False),
        'Parameters': (dict, False),
        'ResourceType': (str, False),
        'RetryAttemptSeconds': (integer, False),
        'TargetId': (str, True),
        'TargetType': (str, True),
        'TargetVersion': (str, False),
    }


class ConformancePackInputParameter(AWSProperty):
    props = {
        'ParameterName': (str, True),
        'ParameterValue': (str, True),
    }


class ConformancePack(AWSObject):
    resource_type = "AWS::Config::ConformancePack"

    props = {
        'ConformancePackInputParameters': ([ConformancePackInputParameter], False),  # NOQA
        'ConformancePackName': (str, True),
        'DeliveryS3Bucket': (str, True),
        'DeliveryS3KeyPrefix': (str, False),
        'TemplateBody': (str, False),
        'TemplateS3Uri': (str, False),
    }


class OrganizationConformancePack(AWSObject):
    resource_type = "AWS::Config::OrganizationConformancePack"

    props = {
        'ConformancePackInputParameters': ([ConformancePackInputParameter], False),  # NOQA
        'DeliveryS3Bucket': (str, True),
        'DeliveryS3KeyPrefix': (str, False),
        'ExcludedAccounts': ([str], False),
        'OrganizationConformancePackName': (str, True),
        'TemplateBody': (str, False),
        'TemplateS3Uri': (str, False),
    }


class StoredQuery(AWSObject):
    resource_type = "AWS::Config::StoredQuery"

    props = {
        'QueryDescription': (str, False),
        'QueryExpression': (str, True),
        'QueryName': (str, True),
        'Tags': (Tags, False),
    }
