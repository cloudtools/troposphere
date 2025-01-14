# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double


class DeliveryOptions(AWSProperty):
    """
    `DeliveryOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-deliveryoptions.html>`__
    """

    props: PropsDictType = {
        "MaxDeliverySeconds": (double, False),
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


class DashboardOptions(AWSProperty):
    """
    `DashboardOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-dashboardoptions.html>`__
    """

    props: PropsDictType = {
        "EngagementMetrics": (str, True),
    }


class GuardianOptions(AWSProperty):
    """
    `GuardianOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-guardianoptions.html>`__
    """

    props: PropsDictType = {
        "OptimizedSharedDelivery": (str, True),
    }


class VdmOptions(AWSProperty):
    """
    `VdmOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-vdmoptions.html>`__
    """

    props: PropsDictType = {
        "DashboardOptions": (DashboardOptions, False),
        "GuardianOptions": (GuardianOptions, False),
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
        "VdmOptions": (VdmOptions, False),
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


class EventBridgeDestination(AWSProperty):
    """
    `EventBridgeDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventbridgedestination.html>`__
    """

    props: PropsDictType = {
        "EventBusArn": (str, True),
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
        "EventBridgeDestination": (EventBridgeDestination, False),
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


class MailManagerAddonInstance(AWSObject):
    """
    `MailManagerAddonInstance <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-mailmanageraddoninstance.html>`__
    """

    resource_type = "AWS::SES::MailManagerAddonInstance"

    props: PropsDictType = {
        "AddonSubscriptionId": (str, True),
        "Tags": (Tags, False),
    }


class MailManagerAddonSubscription(AWSObject):
    """
    `MailManagerAddonSubscription <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-mailmanageraddonsubscription.html>`__
    """

    resource_type = "AWS::SES::MailManagerAddonSubscription"

    props: PropsDictType = {
        "AddonName": (str, True),
        "Tags": (Tags, False),
    }


class ArchiveRetention(AWSProperty):
    """
    `ArchiveRetention <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerarchive-archiveretention.html>`__
    """

    props: PropsDictType = {
        "RetentionPeriod": (str, True),
    }


class MailManagerArchive(AWSObject):
    """
    `MailManagerArchive <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-mailmanagerarchive.html>`__
    """

    resource_type = "AWS::SES::MailManagerArchive"

    props: PropsDictType = {
        "ArchiveName": (str, False),
        "KmsKeyArn": (str, False),
        "Retention": (ArchiveRetention, False),
        "Tags": (Tags, False),
    }


class IngressPointConfiguration(AWSProperty):
    """
    `IngressPointConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanageringresspoint-ingresspointconfiguration.html>`__
    """

    props: PropsDictType = {
        "SecretArn": (str, False),
        "SmtpPassword": (str, False),
    }


class MailManagerIngressPoint(AWSObject):
    """
    `MailManagerIngressPoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-mailmanageringresspoint.html>`__
    """

    resource_type = "AWS::SES::MailManagerIngressPoint"

    props: PropsDictType = {
        "IngressPointConfiguration": (IngressPointConfiguration, False),
        "IngressPointName": (str, False),
        "RuleSetId": (str, True),
        "StatusToUpdate": (str, False),
        "Tags": (Tags, False),
        "TrafficPolicyId": (str, True),
        "Type": (str, True),
    }


class RelayAuthentication(AWSProperty):
    """
    `RelayAuthentication <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerrelay-relayauthentication.html>`__
    """

    props: PropsDictType = {
        "NoAuthentication": (dict, False),
        "SecretArn": (str, False),
    }


class MailManagerRelay(AWSObject):
    """
    `MailManagerRelay <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-mailmanagerrelay.html>`__
    """

    resource_type = "AWS::SES::MailManagerRelay"

    props: PropsDictType = {
        "Authentication": (RelayAuthentication, True),
        "RelayName": (str, False),
        "ServerName": (str, True),
        "ServerPort": (double, True),
        "Tags": (Tags, False),
    }


class AddHeaderAction(AWSProperty):
    """
    `AddHeaderAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html>`__
    """

    props: PropsDictType = {
        "HeaderName": (str, True),
        "HeaderValue": (str, True),
    }


class ArchiveAction(AWSProperty):
    """
    `ArchiveAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-archiveaction.html>`__
    """

    props: PropsDictType = {
        "ActionFailurePolicy": (str, False),
        "TargetArchive": (str, True),
    }


class DeliverToMailboxAction(AWSProperty):
    """
    `DeliverToMailboxAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-delivertomailboxaction.html>`__
    """

    props: PropsDictType = {
        "ActionFailurePolicy": (str, False),
        "MailboxArn": (str, True),
        "RoleArn": (str, True),
    }


class DeliverToQBusinessAction(AWSProperty):
    """
    `DeliverToQBusinessAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-delivertoqbusinessaction.html>`__
    """

    props: PropsDictType = {
        "ActionFailurePolicy": (str, False),
        "ApplicationId": (str, True),
        "IndexId": (str, True),
        "RoleArn": (str, True),
    }


class MailManagerS3Action(AWSProperty):
    """
    `MailManagerS3Action <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-s3action.html>`__
    """

    props: PropsDictType = {
        "ActionFailurePolicy": (str, False),
        "RoleArn": (str, True),
        "S3Bucket": (str, True),
        "S3Prefix": (str, False),
        "S3SseKmsKeyId": (str, False),
    }


class RelayAction(AWSProperty):
    """
    `RelayAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-relayaction.html>`__
    """

    props: PropsDictType = {
        "ActionFailurePolicy": (str, False),
        "MailFrom": (str, False),
        "Relay": (str, True),
    }


class ReplaceRecipientAction(AWSProperty):
    """
    `ReplaceRecipientAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-replacerecipientaction.html>`__
    """

    props: PropsDictType = {
        "ReplaceWith": ([str], False),
    }


class SendAction(AWSProperty):
    """
    `SendAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-sendaction.html>`__
    """

    props: PropsDictType = {
        "ActionFailurePolicy": (str, False),
        "RoleArn": (str, True),
    }


class RuleAction(AWSProperty):
    """
    `RuleAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-ruleaction.html>`__
    """

    props: PropsDictType = {
        "AddHeader": (AddHeaderAction, False),
        "Archive": (ArchiveAction, False),
        "DeliverToMailbox": (DeliverToMailboxAction, False),
        "DeliverToQBusiness": (DeliverToQBusinessAction, False),
        "Drop": (dict, False),
        "Relay": (RelayAction, False),
        "ReplaceRecipient": (ReplaceRecipientAction, False),
        "Send": (SendAction, False),
        "WriteToS3": (MailManagerS3Action, False),
    }


class RuleBooleanToEvaluate(AWSProperty):
    """
    `RuleBooleanToEvaluate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-rulebooleantoevaluate.html>`__
    """

    props: PropsDictType = {
        "Attribute": (str, True),
    }


class RuleBooleanExpression(AWSProperty):
    """
    `RuleBooleanExpression <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-rulebooleanexpression.html>`__
    """

    props: PropsDictType = {
        "Evaluate": (RuleBooleanToEvaluate, True),
        "Operator": (str, True),
    }


class RuleDmarcExpression(AWSProperty):
    """
    `RuleDmarcExpression <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-ruledmarcexpression.html>`__
    """

    props: PropsDictType = {
        "Operator": (str, True),
        "Values": ([str], True),
    }


class RuleIpToEvaluate(AWSProperty):
    """
    `RuleIpToEvaluate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-ruleiptoevaluate.html>`__
    """

    props: PropsDictType = {
        "Attribute": (str, True),
    }


class RuleIpExpression(AWSProperty):
    """
    `RuleIpExpression <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-ruleipexpression.html>`__
    """

    props: PropsDictType = {
        "Evaluate": (RuleIpToEvaluate, True),
        "Operator": (str, True),
        "Values": ([str], True),
    }


class RuleNumberToEvaluate(AWSProperty):
    """
    `RuleNumberToEvaluate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-rulenumbertoevaluate.html>`__
    """

    props: PropsDictType = {
        "Attribute": (str, True),
    }


class RuleNumberExpression(AWSProperty):
    """
    `RuleNumberExpression <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-rulenumberexpression.html>`__
    """

    props: PropsDictType = {
        "Evaluate": (RuleNumberToEvaluate, True),
        "Operator": (str, True),
        "Value": (double, True),
    }


class RuleStringToEvaluate(AWSProperty):
    """
    `RuleStringToEvaluate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-rulestringtoevaluate.html>`__
    """

    props: PropsDictType = {
        "Attribute": (str, False),
        "MimeHeaderAttribute": (str, False),
    }


class RuleStringExpression(AWSProperty):
    """
    `RuleStringExpression <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-rulestringexpression.html>`__
    """

    props: PropsDictType = {
        "Evaluate": (RuleStringToEvaluate, True),
        "Operator": (str, True),
        "Values": ([str], True),
    }


class Analysis(AWSProperty):
    """
    `Analysis <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-analysis.html>`__
    """

    props: PropsDictType = {
        "Analyzer": (str, True),
        "ResultField": (str, True),
    }


class RuleVerdictToEvaluate(AWSProperty):
    """
    `RuleVerdictToEvaluate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-ruleverdicttoevaluate.html>`__
    """

    props: PropsDictType = {
        "Analysis": (Analysis, False),
        "Attribute": (str, False),
    }


class RuleVerdictExpression(AWSProperty):
    """
    `RuleVerdictExpression <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-ruleverdictexpression.html>`__
    """

    props: PropsDictType = {
        "Evaluate": (RuleVerdictToEvaluate, True),
        "Operator": (str, True),
        "Values": ([str], True),
    }


class RuleCondition(AWSProperty):
    """
    `RuleCondition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-rulecondition.html>`__
    """

    props: PropsDictType = {
        "BooleanExpression": (RuleBooleanExpression, False),
        "DmarcExpression": (RuleDmarcExpression, False),
        "IpExpression": (RuleIpExpression, False),
        "NumberExpression": (RuleNumberExpression, False),
        "StringExpression": (RuleStringExpression, False),
        "VerdictExpression": (RuleVerdictExpression, False),
    }


class MailManagerRule(AWSProperty):
    """
    `MailManagerRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagerruleset-rule.html>`__
    """

    props: PropsDictType = {
        "Actions": ([RuleAction], True),
        "Conditions": ([RuleCondition], False),
        "Name": (str, False),
        "Unless": ([RuleCondition], False),
    }


class MailManagerRuleSet(AWSObject):
    """
    `MailManagerRuleSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-mailmanagerruleset.html>`__
    """

    resource_type = "AWS::SES::MailManagerRuleSet"

    props: PropsDictType = {
        "RuleSetName": (str, False),
        "Rules": ([MailManagerRule], True),
        "Tags": (Tags, False),
    }


class IngressAnalysis(AWSProperty):
    """
    `IngressAnalysis <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagertrafficpolicy-ingressanalysis.html>`__
    """

    props: PropsDictType = {
        "Analyzer": (str, True),
        "ResultField": (str, True),
    }


class IngressBooleanToEvaluate(AWSProperty):
    """
    `IngressBooleanToEvaluate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagertrafficpolicy-ingressbooleantoevaluate.html>`__
    """

    props: PropsDictType = {
        "Analysis": (IngressAnalysis, True),
    }


class IngressBooleanExpression(AWSProperty):
    """
    `IngressBooleanExpression <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagertrafficpolicy-ingressbooleanexpression.html>`__
    """

    props: PropsDictType = {
        "Evaluate": (IngressBooleanToEvaluate, True),
        "Operator": (str, True),
    }


class IngressIpToEvaluate(AWSProperty):
    """
    `IngressIpToEvaluate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagertrafficpolicy-ingressiptoevaluate.html>`__
    """

    props: PropsDictType = {
        "Attribute": (str, True),
    }


class IngressIpv4Expression(AWSProperty):
    """
    `IngressIpv4Expression <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagertrafficpolicy-ingressipv4expression.html>`__
    """

    props: PropsDictType = {
        "Evaluate": (IngressIpToEvaluate, True),
        "Operator": (str, True),
        "Values": ([str], True),
    }


class IngressStringToEvaluate(AWSProperty):
    """
    `IngressStringToEvaluate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagertrafficpolicy-ingressstringtoevaluate.html>`__
    """

    props: PropsDictType = {
        "Attribute": (str, True),
    }


class IngressStringExpression(AWSProperty):
    """
    `IngressStringExpression <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagertrafficpolicy-ingressstringexpression.html>`__
    """

    props: PropsDictType = {
        "Evaluate": (IngressStringToEvaluate, True),
        "Operator": (str, True),
        "Values": ([str], True),
    }


class IngressTlsProtocolToEvaluate(AWSProperty):
    """
    `IngressTlsProtocolToEvaluate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate.html>`__
    """

    props: PropsDictType = {
        "Attribute": (str, True),
    }


class IngressTlsProtocolExpression(AWSProperty):
    """
    `IngressTlsProtocolExpression <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocolexpression.html>`__
    """

    props: PropsDictType = {
        "Evaluate": (IngressTlsProtocolToEvaluate, True),
        "Operator": (str, True),
        "Value": (str, True),
    }


class PolicyCondition(AWSProperty):
    """
    `PolicyCondition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagertrafficpolicy-policycondition.html>`__
    """

    props: PropsDictType = {
        "BooleanExpression": (IngressBooleanExpression, False),
        "IpExpression": (IngressIpv4Expression, False),
        "StringExpression": (IngressStringExpression, False),
        "TlsExpression": (IngressTlsProtocolExpression, False),
    }


class PolicyStatement(AWSProperty):
    """
    `PolicyStatement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-mailmanagertrafficpolicy-policystatement.html>`__
    """

    props: PropsDictType = {
        "Action": (str, True),
        "Conditions": ([PolicyCondition], True),
    }


class MailManagerTrafficPolicy(AWSObject):
    """
    `MailManagerTrafficPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-mailmanagertrafficpolicy.html>`__
    """

    resource_type = "AWS::SES::MailManagerTrafficPolicy"

    props: PropsDictType = {
        "DefaultAction": (str, True),
        "MaxMessageSizeBytes": (double, False),
        "PolicyStatements": ([PolicyStatement], True),
        "Tags": (Tags, False),
        "TrafficPolicyName": (str, False),
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


class ConnectAction(AWSProperty):
    """
    `ConnectAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-connectaction.html>`__
    """

    props: PropsDictType = {
        "IAMRoleARN": (str, True),
        "InstanceARN": (str, True),
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
        "IamRoleArn": (str, False),
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
        "ConnectAction": (ConnectAction, False),
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


class DashboardAttributes(AWSProperty):
    """
    `DashboardAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-vdmattributes-dashboardattributes.html>`__
    """

    props: PropsDictType = {
        "EngagementMetrics": (str, False),
    }


class GuardianAttributes(AWSProperty):
    """
    `GuardianAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-vdmattributes-guardianattributes.html>`__
    """

    props: PropsDictType = {
        "OptimizedSharedDelivery": (str, False),
    }


class VdmAttributes(AWSObject):
    """
    `VdmAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-vdmattributes.html>`__
    """

    resource_type = "AWS::SES::VdmAttributes"

    props: PropsDictType = {
        "DashboardAttributes": (DashboardAttributes, False),
        "GuardianAttributes": (GuardianAttributes, False),
    }
