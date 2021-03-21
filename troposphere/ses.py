# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean


class DimensionConfiguration(AWSProperty):
    props = {
        'DefaultDimensionValue': (str, True),
        'DimensionName': (str, True),
        'DimensionValueSource': (str, True),
    }


class CloudWatchDestination(AWSProperty):
    props = {
        'DimensionConfigurations': ([DimensionConfiguration], False),
    }


class KinesisFirehoseDestination(AWSProperty):
    props = {
        'DeliveryStreamARN': (str, True),
        'IAMRoleARN': (str, True),
    }


class EventDestination(AWSProperty):
    props = {
        'CloudWatchDestination': (CloudWatchDestination, False),
        'Enabled': (boolean, False),
        'KinesisFirehoseDestination': (KinesisFirehoseDestination, False),
        'MatchingEventTypes': ([str], True),
        'Name': (str, False),
    }


class ConfigurationSetEventDestination(AWSObject):
    resource_type = "AWS::SES::ConfigurationSetEventDestination"

    props = {
        'ConfigurationSetName': (str, True),
        'EventDestination': (EventDestination, True),
    }


class ConfigurationSet(AWSObject):
    resource_type = "AWS::SES::ConfigurationSet"

    props = {
        'Name': (str, False),
    }


class IpFilter(AWSProperty):
    props = {
        'Cidr': (str, True),
        'Policy': (str, True),
    }


class Filter(AWSProperty):
    props = {
        'IpFilter': (IpFilter, True),
        'Name': (str, False),
    }


class ReceiptFilter(AWSObject):
    resource_type = "AWS::SES::ReceiptFilter"

    props = {
        'Filter': (Filter, True),
    }


class ReceiptRuleSet(AWSObject):
    resource_type = "AWS::SES::ReceiptRuleSet"

    props = {
        'RuleSetName': (str, False),
    }


class AddHeaderAction(AWSProperty):
    props = {
        'HeaderName': (str, True),
        'HeaderValue': (str, True),
    }


class BounceAction(AWSProperty):
    props = {
        'Message': (str, True),
        'Sender': (str, True),
        'SmtpReplyCode': (str, True),
        'StatusCode': (str, False),
        'TopicArn': (str, False),
    }


class LambdaAction(AWSProperty):
    props = {
        'FunctionArn': (str, True),
        'InvocationType': (str, False),
        'TopicArn': (str, False),
    }


class S3Action(AWSProperty):
    props = {
        'BucketName': (str, True),
        'KmsKeyArn': (str, False),
        'ObjectKeyPrefix': (str, False),
        'TopicArn': (str, False),
    }


class SNSAction(AWSProperty):
    props = {
        'Encoding': (str, False),
        'TopicArn': (str, False),
    }


class StopAction(AWSProperty):
    props = {
        'Scope': (str, True),
        'TopicArn': (str, False),
    }


class WorkmailAction(AWSProperty):
    props = {
        'OrganizationArn': (str, True),
        'TopicArn': (str, False),
    }


class Action(AWSProperty):
    props = {
        'AddHeaderAction': (AddHeaderAction, False),
        'BounceAction': (BounceAction, False),
        'LambdaAction': (LambdaAction, False),
        'S3Action': (S3Action, False),
        'SNSAction': (SNSAction, False),
        'StopAction': (StopAction, False),
        'WorkmailAction': (WorkmailAction, False),
    }


class Rule(AWSProperty):
    props = {
        'Actions': ([Action], False),
        'Enabled': (boolean, False),
        'Name': (str, False),
        'Recipients': ([str], False),
        'ScanEnabled': (boolean, False),
        'TlsPolicy': (str, False),
    }


class ReceiptRule(AWSObject):
    resource_type = "AWS::SES::ReceiptRule"

    props = {
        'After': (str, False),
        'Rule': (Rule, True),
        'RuleSetName': (str, True),
    }


class EmailTemplate(AWSProperty):
    props = {
        'HtmlPart': (str, False),
        'SubjectPart': (str, False),
        'TemplateName': (str, False),
        'TextPart': (str, False),
    }


class Template(AWSObject):
    resource_type = "AWS::SES::Template"

    props = {
        'Template': (EmailTemplate, False),
    }
