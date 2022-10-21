# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean


class DeliveryOptions(AWSProperty):
    """
    `DeliveryOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-deliveryoptions.html>`__
    """

    props: PropsDictType = {
        "SendingPoolName": (str, False),
        "TlsPolicy": (str, False),
    }


class ReputationOptions(AWSProperty):
    """
    `ReputationOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-reputationoptions.html>`__
    """

    props: PropsDictType = {
        "ReputationMetricsEnabled": (boolean, False),
    }


class SendingOptions(AWSProperty):
    """
    `SendingOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-sendingoptions.html>`__
    """

    props: PropsDictType = {
        "SendingEnabled": (boolean, False),
    }


class SuppressionOptions(AWSProperty):
    """
    `SuppressionOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-suppressionoptions.html>`__
    """

    props: PropsDictType = {
        "SuppressedReasons": ([str], False),
    }


class TrackingOptions(AWSProperty):
    """
    `TrackingOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-trackingoptions.html>`__
    """

    props: PropsDictType = {
        "CustomRedirectDomain": (str, False),
    }


class ConfigurationSet(AWSObject):
    """
    `ConfigurationSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html>`__
    """

    resource_type = "AWS::SES::ConfigurationSet"

    props: PropsDictType = {
        "DeliveryOptions": (DeliveryOptions, False),
        "Name": (str, False),
        "ReputationOptions": (ReputationOptions, False),
        "SendingOptions": (SendingOptions, False),
        "SuppressionOptions": (SuppressionOptions, False),
        "TrackingOptions": (TrackingOptions, False),
    }


class DimensionConfiguration(AWSProperty):
    """
    `DimensionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html>`__
    """

    props: PropsDictType = {
        "DefaultDimensionValue": (str, True),
        "DimensionName": (str, True),
        "DimensionValueSource": (str, True),
    }


class CloudWatchDestination(AWSProperty):
    """
    `CloudWatchDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-cloudwatchdestination.html>`__
    """

    props: PropsDictType = {
        "DimensionConfigurations": ([DimensionConfiguration], False),
    }


class KinesisFirehoseDestination(AWSProperty):
    """
    `KinesisFirehoseDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html>`__
    """

    props: PropsDictType = {
        "DeliveryStreamARN": (str, True),
        "IAMRoleARN": (str, True),
    }


class SnsDestination(AWSProperty):
    """
    `SnsDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-snsdestination.html>`__
    """

    props: PropsDictType = {
        "TopicARN": (str, True),
    }


class EventDestination(AWSProperty):
    """
    `EventDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html>`__
    """

    props: PropsDictType = {
        "CloudWatchDestination": (CloudWatchDestination, False),
        "Enabled": (boolean, False),
        "KinesisFirehoseDestination": (KinesisFirehoseDestination, False),
        "MatchingEventTypes": ([str], True),
        "Name": (str, False),
        "SnsDestination": (SnsDestination, False),
    }


class ConfigurationSetEventDestination(AWSObject):
    """
    `ConfigurationSetEventDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html>`__
    """

    resource_type = "AWS::SES::ConfigurationSetEventDestination"

    props: PropsDictType = {
        "ConfigurationSetName": (str, True),
        "EventDestination": (EventDestination, True),
    }


class Topic(AWSProperty):
    """
    `Topic <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html>`__
    """

    props: PropsDictType = {
        "DefaultSubscriptionStatus": (str, True),
        "Description": (str, False),
        "DisplayName": (str, True),
        "TopicName": (str, True),
    }


class ContactList(AWSObject):
    """
    `ContactList <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html>`__
    """

    resource_type = "AWS::SES::ContactList"

    props: PropsDictType = {
        "ContactListName": (str, False),
        "Description": (str, False),
        "Tags": (Tags, False),
        "Topics": ([Topic], False),
    }


class DedicatedIpPool(AWSObject):
    """
    `DedicatedIpPool <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-dedicatedippool.html>`__
    """

    resource_type = "AWS::SES::DedicatedIpPool"

    props: PropsDictType = {
        "PoolName": (str, False),
        "ScalingMode": (str, False),
    }


class ConfigurationSetAttributes(AWSProperty):
    """
    `ConfigurationSetAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-configurationsetattributes.html>`__
    """

    props: PropsDictType = {
        "ConfigurationSetName": (str, False),
    }


class DkimAttributes(AWSProperty):
    """
    `DkimAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimattributes.html>`__
    """

    props: PropsDictType = {
        "SigningEnabled": (boolean, False),
    }


class DkimSigningAttributes(AWSProperty):
    """
    `DkimSigningAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html>`__
    """

    props: PropsDictType = {
        "DomainSigningPrivateKey": (str, False),
        "DomainSigningSelector": (str, False),
        "NextSigningKeyLength": (str, False),
    }


class FeedbackAttributes(AWSProperty):
    """
    `FeedbackAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-feedbackattributes.html>`__
    """

    props: PropsDictType = {
        "EmailForwardingEnabled": (boolean, False),
    }


class MailFromAttributes(AWSProperty):
    """
    `MailFromAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-mailfromattributes.html>`__
    """

    props: PropsDictType = {
        "BehaviorOnMxFailure": (str, False),
        "MailFromDomain": (str, False),
    }


class EmailIdentity(AWSObject):
    """
    `EmailIdentity <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html>`__
    """

    resource_type = "AWS::SES::EmailIdentity"

    props: PropsDictType = {
        "ConfigurationSetAttributes": (ConfigurationSetAttributes, False),
        "DkimAttributes": (DkimAttributes, False),
        "DkimSigningAttributes": (DkimSigningAttributes, False),
        "EmailIdentity": (str, True),
        "FeedbackAttributes": (FeedbackAttributes, False),
        "MailFromAttributes": (MailFromAttributes, False),
    }


class IpFilter(AWSProperty):
    """
    `IpFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html>`__
    """

    props: PropsDictType = {
        "Cidr": (str, True),
        "Policy": (str, True),
    }


class Filter(AWSProperty):
    """
    `Filter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html>`__
    """

    props: PropsDictType = {
        "IpFilter": (IpFilter, True),
        "Name": (str, False),
    }


class ReceiptFilter(AWSObject):
    """
    `ReceiptFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html>`__
    """

    resource_type = "AWS::SES::ReceiptFilter"

    props: PropsDictType = {
        "Filter": (Filter, True),
    }


class AddHeaderAction(AWSProperty):
    """
    `AddHeaderAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html>`__
    """

    props: PropsDictType = {
        "HeaderName": (str, True),
        "HeaderValue": (str, True),
    }


class BounceAction(AWSProperty):
    """
    `BounceAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html>`__
    """

    props: PropsDictType = {
        "Message": (str, True),
        "Sender": (str, True),
        "SmtpReplyCode": (str, True),
        "StatusCode": (str, False),
        "TopicArn": (str, False),
    }


class LambdaAction(AWSProperty):
    """
    `LambdaAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html>`__
    """

    props: PropsDictType = {
        "FunctionArn": (str, True),
        "InvocationType": (str, False),
        "TopicArn": (str, False),
    }


class S3Action(AWSProperty):
    """
    `S3Action <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html>`__
    """

    props: PropsDictType = {
        "BucketName": (str, True),
        "KmsKeyArn": (str, False),
        "ObjectKeyPrefix": (str, False),
        "TopicArn": (str, False),
    }


class SNSAction(AWSProperty):
    """
    `SNSAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html>`__
    """

    props: PropsDictType = {
        "Encoding": (str, False),
        "TopicArn": (str, False),
    }


class StopAction(AWSProperty):
    """
    `StopAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html>`__
    """

    props: PropsDictType = {
        "Scope": (str, True),
        "TopicArn": (str, False),
    }


class WorkmailAction(AWSProperty):
    """
    `WorkmailAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html>`__
    """

    props: PropsDictType = {
        "OrganizationArn": (str, True),
        "TopicArn": (str, False),
    }


class Action(AWSProperty):
    """
    `Action <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html>`__
    """

    props: PropsDictType = {
        "AddHeaderAction": (AddHeaderAction, False),
        "BounceAction": (BounceAction, False),
        "LambdaAction": (LambdaAction, False),
        "S3Action": (S3Action, False),
        "SNSAction": (SNSAction, False),
        "StopAction": (StopAction, False),
        "WorkmailAction": (WorkmailAction, False),
    }


class Rule(AWSProperty):
    """
    `Rule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html>`__
    """

    props: PropsDictType = {
        "Actions": ([Action], False),
        "Enabled": (boolean, False),
        "Name": (str, False),
        "Recipients": ([str], False),
        "ScanEnabled": (boolean, False),
        "TlsPolicy": (str, False),
    }


class ReceiptRule(AWSObject):
    """
    `ReceiptRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html>`__
    """

    resource_type = "AWS::SES::ReceiptRule"

    props: PropsDictType = {
        "After": (str, False),
        "Rule": (Rule, True),
        "RuleSetName": (str, True),
    }


class ReceiptRuleSet(AWSObject):
    """
    `ReceiptRuleSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html>`__
    """

    resource_type = "AWS::SES::ReceiptRuleSet"

    props: PropsDictType = {
        "RuleSetName": (str, False),
    }


class EmailTemplate(AWSProperty):
    """
    `EmailTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html>`__
    """

    props: PropsDictType = {
        "HtmlPart": (str, False),
        "SubjectPart": (str, True),
        "TemplateName": (str, False),
        "TextPart": (str, False),
    }


class Template(AWSObject):
    """
    `Template <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html>`__
    """

    resource_type = "AWS::SES::Template"

    props: PropsDictType = {
        "Template": (EmailTemplate, False),
    }
