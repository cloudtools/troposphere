# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean


class DimensionConfiguration(AWSProperty):
    props = {
        'DefaultDimensionValue': (basestring, True),
        'DimensionName': (basestring, True),
        'DimensionValueSource': (basestring, True),
    }


class CloudWatchDestination(AWSProperty):
    props = {
        'DimensionConfigurations': ([DimensionConfiguration], False),
    }


class KinesisFirehoseDestination(AWSProperty):
    props = {
        'DeliveryStreamARN': (basestring, True),
        'IAMRoleARN': (basestring, True),
    }


class EventDestination(AWSProperty):
    props = {
        'CloudWatchDestination': (CloudWatchDestination, False),
        'Enabled': (boolean, False),
        'KinesisFirehoseDestination': (KinesisFirehoseDestination, False),
        'MatchingEventTypes': ([basestring], True),
        'Name': (basestring, False),
    }


class ConfigurationSetEventDestination(AWSObject):
    resource_type = "AWS::SES::ConfigurationSetEventDestination"

    props = {
        'ConfigurationSetName': (basestring, True),
        'EventDestination': (EventDestination, True),
    }


class ConfigurationSet(AWSObject):
    resource_type = "AWS::SES::ConfigurationSet"

    props = {
        'Name': (basestring, False),
    }


class IpFilter(AWSProperty):
    props = {
        'Cidr': (basestring, True),
        'Policy': (basestring, True),
    }


class Filter(AWSProperty):
    props = {
        'IpFilter': (IpFilter, True),
        'Name': (basestring, False),
    }


class ReceiptFilter(AWSObject):
    resource_type = "AWS::SES::ReceiptFilter"

    props = {
        'Filter': (Filter, True),
    }


class ReceiptRuleSet(AWSObject):
    resource_type = "AWS::SES::ReceiptRuleSet"

    props = {
        'RuleSetName': (basestring, False),
    }


class AddHeaderAction(AWSProperty):
    props = {
        'HeaderName': (basestring, True),
        'HeaderValue': (basestring, True),
    }


class BounceAction(AWSProperty):
    props = {
        'Message': (basestring, True),
        'Sender': (basestring, True),
        'SmtpReplyCode': (basestring, True),
        'StatusCode': (basestring, False),
        'TopicArn': (basestring, False),
    }


class LambdaAction(AWSProperty):
    props = {
        'FunctionArn': (basestring, True),
        'InvocationType': (basestring, False),
        'TopicArn': (basestring, False),
    }


class S3Action(AWSProperty):
    props = {
        'BucketName': (basestring, True),
        'KmsKeyArn': (basestring, False),
        'ObjectKeyPrefix': (basestring, False),
        'TopicArn': (basestring, False),
    }


class SNSAction(AWSProperty):
    props = {
        'Encoding': (basestring, False),
        'TopicArn': (basestring, False),
    }


class StopAction(AWSProperty):
    props = {
        'Scope': (basestring, True),
        'TopicArn': (basestring, False),
    }


class WorkmailAction(AWSProperty):
    props = {
        'OrganizationArn': (basestring, True),
        'TopicArn': (basestring, False),
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
        'Name': (basestring, False),
        'Recipients': ([basestring], False),
        'ScanEnabled': (boolean, False),
        'TlsPolicy': (basestring, False),
    }


class ReceiptRule(AWSObject):
    resource_type = "AWS::SES::ReceiptRule"

    props = {
        'After': (basestring, False),
        'Rule': (Rule, True),
        'RuleSetName': (basestring, True),
    }


class EmailTemplate(AWSProperty):
    props = {
        'HtmlPart': (basestring, False),
        'SubjectPart': (basestring, False),
        'TemplateName': (basestring, False),
        'TextPart': (basestring, False),
    }


class Template(AWSObject):
    resource_type = "AWS::SES::Template"

    props = {
        'Template': (EmailTemplate, False),
    }
