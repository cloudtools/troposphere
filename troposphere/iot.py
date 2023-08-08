# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.iot import policytypes, validate_json_checker


class AuditCheckConfiguration(AWSProperty):
    """
    `AuditCheckConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfiguration.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
    }


class AuditCheckConfigurations(AWSProperty):
    """
    `AuditCheckConfigurations <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html>`__
    """

    props: PropsDictType = {
        "AuthenticatedCognitoRoleOverlyPermissiveCheck": (
            AuditCheckConfiguration,
            False,
        ),
        "CaCertificateExpiringCheck": (AuditCheckConfiguration, False),
        "CaCertificateKeyQualityCheck": (AuditCheckConfiguration, False),
        "ConflictingClientIdsCheck": (AuditCheckConfiguration, False),
        "DeviceCertificateExpiringCheck": (AuditCheckConfiguration, False),
        "DeviceCertificateKeyQualityCheck": (AuditCheckConfiguration, False),
        "DeviceCertificateSharedCheck": (AuditCheckConfiguration, False),
        "IntermediateCaRevokedForActiveDeviceCertificatesCheck": (
            AuditCheckConfiguration,
            False,
        ),
        "IoTPolicyPotentialMisConfigurationCheck": (AuditCheckConfiguration, False),
        "IotPolicyOverlyPermissiveCheck": (AuditCheckConfiguration, False),
        "IotRoleAliasAllowsAccessToUnusedServicesCheck": (
            AuditCheckConfiguration,
            False,
        ),
        "IotRoleAliasOverlyPermissiveCheck": (AuditCheckConfiguration, False),
        "LoggingDisabledCheck": (AuditCheckConfiguration, False),
        "RevokedCaCertificateStillActiveCheck": (AuditCheckConfiguration, False),
        "RevokedDeviceCertificateStillActiveCheck": (AuditCheckConfiguration, False),
        "UnauthenticatedCognitoRoleOverlyPermissiveCheck": (
            AuditCheckConfiguration,
            False,
        ),
    }


class AuditNotificationTarget(AWSProperty):
    """
    `AuditNotificationTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtarget.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "RoleArn": (str, False),
        "TargetArn": (str, False),
    }


class AuditNotificationTargetConfigurations(AWSProperty):
    """
    `AuditNotificationTargetConfigurations <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtargetconfigurations.html>`__
    """

    props: PropsDictType = {
        "Sns": (AuditNotificationTarget, False),
    }


class AccountAuditConfiguration(AWSObject):
    """
    `AccountAuditConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html>`__
    """

    resource_type = "AWS::IoT::AccountAuditConfiguration"

    props: PropsDictType = {
        "AccountId": (str, True),
        "AuditCheckConfigurations": (AuditCheckConfigurations, True),
        "AuditNotificationTargetConfigurations": (
            AuditNotificationTargetConfigurations,
            False,
        ),
        "RoleArn": (str, True),
    }


class Authorizer(AWSObject):
    """
    `Authorizer <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html>`__
    """

    resource_type = "AWS::IoT::Authorizer"

    props: PropsDictType = {
        "AuthorizerFunctionArn": (str, True),
        "AuthorizerName": (str, False),
        "EnableCachingForHttp": (boolean, False),
        "SigningDisabled": (boolean, False),
        "Status": (str, False),
        "Tags": (Tags, False),
        "TokenKeyName": (str, False),
        "TokenSigningPublicKeys": (dict, False),
    }


class RegistrationConfig(AWSProperty):
    """
    `RegistrationConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-cacertificate-registrationconfig.html>`__
    """

    props: PropsDictType = {
        "RoleArn": (str, False),
        "TemplateBody": (str, False),
        "TemplateName": (str, False),
    }


class CACertificate(AWSObject):
    """
    `CACertificate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html>`__
    """

    resource_type = "AWS::IoT::CACertificate"

    props: PropsDictType = {
        "AutoRegistrationStatus": (str, False),
        "CACertificatePem": (str, True),
        "CertificateMode": (str, False),
        "RegistrationConfig": (RegistrationConfig, False),
        "RemoveAutoRegistration": (boolean, False),
        "Status": (str, True),
        "Tags": (Tags, False),
        "VerificationCertificatePem": (str, False),
    }


class Certificate(AWSObject):
    """
    `Certificate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html>`__
    """

    resource_type = "AWS::IoT::Certificate"

    props: PropsDictType = {
        "CACertificatePem": (str, False),
        "CertificateMode": (str, False),
        "CertificatePem": (str, False),
        "CertificateSigningRequest": (str, False),
        "Status": (str, True),
    }


class CustomMetric(AWSObject):
    """
    `CustomMetric <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html>`__
    """

    resource_type = "AWS::IoT::CustomMetric"

    props: PropsDictType = {
        "DisplayName": (str, False),
        "MetricName": (str, False),
        "MetricType": (str, True),
        "Tags": (Tags, False),
    }


class Dimension(AWSObject):
    """
    `Dimension <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html>`__
    """

    resource_type = "AWS::IoT::Dimension"

    props: PropsDictType = {
        "Name": (str, False),
        "StringValues": ([str], True),
        "Tags": (Tags, False),
        "Type": (str, True),
    }


class AuthorizerConfig(AWSProperty):
    """
    `AuthorizerConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-authorizerconfig.html>`__
    """

    props: PropsDictType = {
        "AllowAuthorizerOverride": (boolean, False),
        "DefaultAuthorizerName": (str, False),
    }


class TlsConfig(AWSProperty):
    """
    `TlsConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-tlsconfig.html>`__
    """

    props: PropsDictType = {
        "SecurityPolicy": (str, False),
    }


class DomainConfiguration(AWSObject):
    """
    `DomainConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html>`__
    """

    resource_type = "AWS::IoT::DomainConfiguration"

    props: PropsDictType = {
        "AuthorizerConfig": (AuthorizerConfig, False),
        "DomainConfigurationName": (str, False),
        "DomainConfigurationStatus": (str, False),
        "DomainName": (str, False),
        "ServerCertificateArns": ([str], False),
        "ServiceType": (str, False),
        "Tags": (Tags, False),
        "TlsConfig": (TlsConfig, False),
        "ValidationCertificateArn": (str, False),
    }


class AggregationType(AWSProperty):
    """
    `AggregationType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-fleetmetric-aggregationtype.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Values": ([str], True),
    }


class FleetMetric(AWSObject):
    """
    `FleetMetric <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html>`__
    """

    resource_type = "AWS::IoT::FleetMetric"

    props: PropsDictType = {
        "AggregationField": (str, False),
        "AggregationType": (AggregationType, False),
        "Description": (str, False),
        "IndexName": (str, False),
        "MetricName": (str, True),
        "Period": (integer, False),
        "QueryString": (str, False),
        "QueryVersion": (str, False),
        "Tags": (Tags, False),
        "Unit": (str, False),
    }


class AbortCriteria(AWSProperty):
    """
    `AbortCriteria <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-abortcriteria.html>`__
    """

    props: PropsDictType = {
        "Action": (str, True),
        "FailureType": (str, True),
        "MinNumberOfExecutedThings": (integer, True),
        "ThresholdPercentage": (double, True),
    }


class AbortConfig(AWSProperty):
    """
    `AbortConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-abortconfig.html>`__
    """

    props: PropsDictType = {
        "CriteriaList": ([AbortCriteria], True),
    }


class RetryCriteria(AWSProperty):
    """
    `RetryCriteria <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-retrycriteria.html>`__
    """

    props: PropsDictType = {
        "FailureType": (str, False),
        "NumberOfRetries": (integer, False),
    }


class JobExecutionsRetryConfig(AWSProperty):
    """
    `JobExecutionsRetryConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-jobexecutionsretryconfig.html>`__
    """

    props: PropsDictType = {
        "RetryCriteriaList": ([RetryCriteria], False),
    }


class RateIncreaseCriteria(AWSProperty):
    """
    `RateIncreaseCriteria <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-rateincreasecriteria.html>`__
    """

    props: PropsDictType = {
        "NumberOfNotifiedThings": (integer, False),
        "NumberOfSucceededThings": (integer, False),
    }


class ExponentialRolloutRate(AWSProperty):
    """
    `ExponentialRolloutRate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-exponentialrolloutrate.html>`__
    """

    props: PropsDictType = {
        "BaseRatePerMinute": (integer, True),
        "IncrementFactor": (double, True),
        "RateIncreaseCriteria": (RateIncreaseCriteria, True),
    }


class JobExecutionsRolloutConfig(AWSProperty):
    """
    `JobExecutionsRolloutConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-jobexecutionsrolloutconfig.html>`__
    """

    props: PropsDictType = {
        "ExponentialRolloutRate": (ExponentialRolloutRate, False),
        "MaximumPerMinute": (integer, False),
    }


class MaintenanceWindow(AWSProperty):
    """
    `MaintenanceWindow <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-maintenancewindow.html>`__
    """

    props: PropsDictType = {
        "DurationInMinutes": (integer, False),
        "StartTime": (str, False),
    }


class PresignedUrlConfig(AWSProperty):
    """
    `PresignedUrlConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-presignedurlconfig.html>`__
    """

    props: PropsDictType = {
        "ExpiresInSec": (integer, False),
        "RoleArn": (str, True),
    }


class TimeoutConfig(AWSProperty):
    """
    `TimeoutConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-timeoutconfig.html>`__
    """

    props: PropsDictType = {
        "InProgressTimeoutInMinutes": (integer, True),
    }


class JobTemplate(AWSObject):
    """
    `JobTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html>`__
    """

    resource_type = "AWS::IoT::JobTemplate"

    props: PropsDictType = {
        "AbortConfig": (validate_json_checker, False),
        "Description": (str, True),
        "Document": (str, False),
        "DocumentSource": (str, False),
        "JobArn": (str, False),
        "JobExecutionsRetryConfig": (JobExecutionsRetryConfig, False),
        "JobExecutionsRolloutConfig": (validate_json_checker, False),
        "JobTemplateId": (str, True),
        "MaintenanceWindows": ([MaintenanceWindow], False),
        "PresignedUrlConfig": (PresignedUrlConfig, False),
        "Tags": (Tags, False),
        "TimeoutConfig": (validate_json_checker, False),
    }


class Logging(AWSObject):
    """
    `Logging <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html>`__
    """

    resource_type = "AWS::IoT::Logging"

    props: PropsDictType = {
        "AccountId": (str, True),
        "DefaultLogLevel": (str, True),
        "RoleArn": (str, True),
    }


class AddThingsToThingGroupParams(AWSProperty):
    """
    `AddThingsToThingGroupParams <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-addthingstothinggroupparams.html>`__
    """

    props: PropsDictType = {
        "OverrideDynamicGroups": (boolean, False),
        "ThingGroupNames": ([str], True),
    }


class EnableIoTLoggingParams(AWSProperty):
    """
    `EnableIoTLoggingParams <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-enableiotloggingparams.html>`__
    """

    props: PropsDictType = {
        "LogLevel": (str, True),
        "RoleArnForLogging": (str, True),
    }


class PublishFindingToSnsParams(AWSProperty):
    """
    `PublishFindingToSnsParams <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-publishfindingtosnsparams.html>`__
    """

    props: PropsDictType = {
        "TopicArn": (str, True),
    }


class ReplaceDefaultPolicyVersionParams(AWSProperty):
    """
    `ReplaceDefaultPolicyVersionParams <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-replacedefaultpolicyversionparams.html>`__
    """

    props: PropsDictType = {
        "TemplateName": (str, True),
    }


class UpdateCACertificateParams(AWSProperty):
    """
    `UpdateCACertificateParams <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-updatecacertificateparams.html>`__
    """

    props: PropsDictType = {
        "Action": (str, True),
    }


class UpdateDeviceCertificateParams(AWSProperty):
    """
    `UpdateDeviceCertificateParams <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-updatedevicecertificateparams.html>`__
    """

    props: PropsDictType = {
        "Action": (str, True),
    }


class ActionParams(AWSProperty):
    """
    `ActionParams <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html>`__
    """

    props: PropsDictType = {
        "AddThingsToThingGroupParams": (AddThingsToThingGroupParams, False),
        "EnableIoTLoggingParams": (EnableIoTLoggingParams, False),
        "PublishFindingToSnsParams": (PublishFindingToSnsParams, False),
        "ReplaceDefaultPolicyVersionParams": (ReplaceDefaultPolicyVersionParams, False),
        "UpdateCACertificateParams": (UpdateCACertificateParams, False),
        "UpdateDeviceCertificateParams": (UpdateDeviceCertificateParams, False),
    }


class MitigationAction(AWSObject):
    """
    `MitigationAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html>`__
    """

    resource_type = "AWS::IoT::MitigationAction"

    props: PropsDictType = {
        "ActionName": (str, False),
        "ActionParams": (ActionParams, True),
        "RoleArn": (str, True),
        "Tags": (Tags, False),
    }


class Policy(AWSObject):
    """
    `Policy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html>`__
    """

    resource_type = "AWS::IoT::Policy"

    props: PropsDictType = {
        "PolicyDocument": (policytypes, True),
        "PolicyName": (str, False),
    }


class PolicyPrincipalAttachment(AWSObject):
    """
    `PolicyPrincipalAttachment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policyprincipalattachment.html>`__
    """

    resource_type = "AWS::IoT::PolicyPrincipalAttachment"

    props: PropsDictType = {
        "PolicyName": (str, True),
        "Principal": (str, True),
    }


class ProvisioningHook(AWSProperty):
    """
    `ProvisioningHook <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-provisioningtemplate-provisioninghook.html>`__
    """

    props: PropsDictType = {
        "PayloadVersion": (str, False),
        "TargetArn": (str, False),
    }


class ProvisioningTemplate(AWSObject):
    """
    `ProvisioningTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html>`__
    """

    resource_type = "AWS::IoT::ProvisioningTemplate"

    props: PropsDictType = {
        "Description": (str, False),
        "Enabled": (boolean, False),
        "PreProvisioningHook": (ProvisioningHook, False),
        "ProvisioningRoleArn": (str, True),
        "Tags": (Tags, False),
        "TemplateBody": (str, True),
        "TemplateName": (str, False),
        "TemplateType": (str, False),
    }


class ResourceSpecificLogging(AWSObject):
    """
    `ResourceSpecificLogging <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html>`__
    """

    resource_type = "AWS::IoT::ResourceSpecificLogging"

    props: PropsDictType = {
        "LogLevel": (str, True),
        "TargetName": (str, True),
        "TargetType": (str, True),
    }


class RoleAlias(AWSObject):
    """
    `RoleAlias <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html>`__
    """

    resource_type = "AWS::IoT::RoleAlias"

    props: PropsDictType = {
        "CredentialDurationSeconds": (integer, False),
        "RoleAlias": (str, False),
        "RoleArn": (str, True),
        "Tags": (Tags, False),
    }


class ScheduledAudit(AWSObject):
    """
    `ScheduledAudit <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html>`__
    """

    resource_type = "AWS::IoT::ScheduledAudit"

    props: PropsDictType = {
        "DayOfMonth": (str, False),
        "DayOfWeek": (str, False),
        "Frequency": (str, True),
        "ScheduledAuditName": (str, False),
        "Tags": (Tags, False),
        "TargetCheckNames": ([str], True),
    }


class AlertTarget(AWSProperty):
    """
    `AlertTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-alerttarget.html>`__
    """

    props: PropsDictType = {
        "AlertTargetArn": (str, True),
        "RoleArn": (str, True),
    }


class MachineLearningDetectionConfig(AWSProperty):
    """
    `MachineLearningDetectionConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-machinelearningdetectionconfig.html>`__
    """

    props: PropsDictType = {
        "ConfidenceLevel": (str, False),
    }


class MetricValue(AWSProperty):
    """
    `MetricValue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html>`__
    """

    props: PropsDictType = {
        "Cidrs": ([str], False),
        "Count": (str, False),
        "Number": (double, False),
        "Numbers": ([double], False),
        "Ports": ([integer], False),
        "Strings": ([str], False),
    }


class StatisticalThreshold(AWSProperty):
    """
    `StatisticalThreshold <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-statisticalthreshold.html>`__
    """

    props: PropsDictType = {
        "Statistic": (str, False),
    }


class BehaviorCriteria(AWSProperty):
    """
    `BehaviorCriteria <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html>`__
    """

    props: PropsDictType = {
        "ComparisonOperator": (str, False),
        "ConsecutiveDatapointsToAlarm": (integer, False),
        "ConsecutiveDatapointsToClear": (integer, False),
        "DurationSeconds": (integer, False),
        "MlDetectionConfig": (MachineLearningDetectionConfig, False),
        "StatisticalThreshold": (StatisticalThreshold, False),
        "Value": (MetricValue, False),
    }


class MetricDimension(AWSProperty):
    """
    `MetricDimension <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricdimension.html>`__
    """

    props: PropsDictType = {
        "DimensionName": (str, True),
        "Operator": (str, False),
    }


class Behavior(AWSProperty):
    """
    `Behavior <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html>`__
    """

    props: PropsDictType = {
        "Criteria": (BehaviorCriteria, False),
        "Metric": (str, False),
        "MetricDimension": (MetricDimension, False),
        "Name": (str, True),
        "SuppressAlerts": (boolean, False),
    }


class MetricToRetain(AWSProperty):
    """
    `MetricToRetain <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metrictoretain.html>`__
    """

    props: PropsDictType = {
        "Metric": (str, True),
        "MetricDimension": (MetricDimension, False),
    }


class SecurityProfile(AWSObject):
    """
    `SecurityProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html>`__
    """

    resource_type = "AWS::IoT::SecurityProfile"

    props: PropsDictType = {
        "AdditionalMetricsToRetainV2": ([MetricToRetain], False),
        "AlertTargets": (dict, False),
        "Behaviors": ([Behavior], False),
        "SecurityProfileDescription": (str, False),
        "SecurityProfileName": (str, False),
        "Tags": (Tags, False),
        "TargetArns": ([str], False),
    }


class AttributePayload(AWSProperty):
    """
    `AttributePayload <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-thing-attributepayload.html>`__
    """

    props: PropsDictType = {
        "Attributes": (dict, False),
    }


class Thing(AWSObject):
    """
    `Thing <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html>`__
    """

    resource_type = "AWS::IoT::Thing"

    props: PropsDictType = {
        "AttributePayload": (AttributePayload, False),
        "ThingName": (str, False),
    }


class ThingPrincipalAttachment(AWSObject):
    """
    `ThingPrincipalAttachment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingprincipalattachment.html>`__
    """

    resource_type = "AWS::IoT::ThingPrincipalAttachment"

    props: PropsDictType = {
        "Principal": (str, True),
        "ThingName": (str, True),
    }


class CloudwatchAlarmAction(AWSProperty):
    """
    `CloudwatchAlarmAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchalarmaction.html>`__
    """

    props: PropsDictType = {
        "AlarmName": (str, True),
        "RoleArn": (str, True),
        "StateReason": (str, True),
        "StateValue": (str, True),
    }


class CloudwatchLogsAction(AWSProperty):
    """
    `CloudwatchLogsAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchlogsaction.html>`__
    """

    props: PropsDictType = {
        "BatchMode": (boolean, False),
        "LogGroupName": (str, True),
        "RoleArn": (str, True),
    }


class CloudwatchMetricAction(AWSProperty):
    """
    `CloudwatchMetricAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html>`__
    """

    props: PropsDictType = {
        "MetricName": (str, True),
        "MetricNamespace": (str, True),
        "MetricTimestamp": (str, False),
        "MetricUnit": (str, True),
        "MetricValue": (str, True),
        "RoleArn": (str, True),
    }


class DynamoDBAction(AWSProperty):
    """
    `DynamoDBAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html>`__
    """

    props: PropsDictType = {
        "HashKeyField": (str, True),
        "HashKeyType": (str, False),
        "HashKeyValue": (str, True),
        "PayloadField": (str, False),
        "RangeKeyField": (str, False),
        "RangeKeyType": (str, False),
        "RangeKeyValue": (str, False),
        "RoleArn": (str, True),
        "TableName": (str, True),
    }


class PutItemInput(AWSProperty):
    """
    `PutItemInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putiteminput.html>`__
    """

    props: PropsDictType = {
        "TableName": (str, True),
    }


class DynamoDBv2Action(AWSProperty):
    """
    `DynamoDBv2Action <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbv2action.html>`__
    """

    props: PropsDictType = {
        "PutItem": (PutItemInput, False),
        "RoleArn": (str, False),
    }


class ElasticsearchAction(AWSProperty):
    """
    `ElasticsearchAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html>`__
    """

    props: PropsDictType = {
        "Endpoint": (str, True),
        "Id": (str, True),
        "Index": (str, True),
        "RoleArn": (str, True),
        "Type": (str, True),
    }


class FirehoseAction(AWSProperty):
    """
    `FirehoseAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-firehoseaction.html>`__
    """

    props: PropsDictType = {
        "BatchMode": (boolean, False),
        "DeliveryStreamName": (str, True),
        "RoleArn": (str, True),
        "Separator": (str, False),
    }


class HttpActionHeader(AWSProperty):
    """
    `HttpActionHeader <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpactionheader.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Value": (str, True),
    }


class SigV4Authorization(AWSProperty):
    """
    `SigV4Authorization <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sigv4authorization.html>`__
    """

    props: PropsDictType = {
        "RoleArn": (str, True),
        "ServiceName": (str, True),
        "SigningRegion": (str, True),
    }


class HttpAuthorization(AWSProperty):
    """
    `HttpAuthorization <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpauthorization.html>`__
    """

    props: PropsDictType = {
        "Sigv4": (SigV4Authorization, False),
    }


class HttpAction(AWSProperty):
    """
    `HttpAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpaction.html>`__
    """

    props: PropsDictType = {
        "Auth": (HttpAuthorization, False),
        "ConfirmationUrl": (str, False),
        "Headers": ([HttpActionHeader], False),
        "Url": (str, True),
    }


class IotAnalyticsAction(AWSProperty):
    """
    `IotAnalyticsAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotanalyticsaction.html>`__
    """

    props: PropsDictType = {
        "BatchMode": (boolean, False),
        "ChannelName": (str, True),
        "RoleArn": (str, True),
    }


class IotEventsAction(AWSProperty):
    """
    `IotEventsAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-ioteventsaction.html>`__
    """

    props: PropsDictType = {
        "BatchMode": (boolean, False),
        "InputName": (str, True),
        "MessageId": (str, False),
        "RoleArn": (str, True),
    }


class AssetPropertyTimestamp(AWSProperty):
    """
    `AssetPropertyTimestamp <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertytimestamp.html>`__
    """

    props: PropsDictType = {
        "OffsetInNanos": (str, False),
        "TimeInSeconds": (str, True),
    }


class AssetPropertyVariant(AWSProperty):
    """
    `AssetPropertyVariant <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvariant.html>`__
    """

    props: PropsDictType = {
        "BooleanValue": (str, False),
        "DoubleValue": (str, False),
        "IntegerValue": (str, False),
        "StringValue": (str, False),
    }


class AssetPropertyValue(AWSProperty):
    """
    `AssetPropertyValue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvalue.html>`__
    """

    props: PropsDictType = {
        "Quality": (str, False),
        "Timestamp": (AssetPropertyTimestamp, True),
        "Value": (AssetPropertyVariant, True),
    }


class PutAssetPropertyValueEntry(AWSProperty):
    """
    `PutAssetPropertyValueEntry <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html>`__
    """

    props: PropsDictType = {
        "AssetId": (str, False),
        "EntryId": (str, False),
        "PropertyAlias": (str, False),
        "PropertyId": (str, False),
        "PropertyValues": ([AssetPropertyValue], True),
    }


class IotSiteWiseAction(AWSProperty):
    """
    `IotSiteWiseAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotsitewiseaction.html>`__
    """

    props: PropsDictType = {
        "PutAssetPropertyValueEntries": ([PutAssetPropertyValueEntry], True),
        "RoleArn": (str, True),
    }


class KafkaAction(AWSProperty):
    """
    `KafkaAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html>`__
    """

    props: PropsDictType = {
        "ClientProperties": (dict, True),
        "DestinationArn": (str, True),
        "Key": (str, False),
        "Partition": (str, False),
        "Topic": (str, True),
    }


class KinesisAction(AWSProperty):
    """
    `KinesisAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kinesisaction.html>`__
    """

    props: PropsDictType = {
        "PartitionKey": (str, False),
        "RoleArn": (str, True),
        "StreamName": (str, True),
    }


class LambdaAction(AWSProperty):
    """
    `LambdaAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-lambdaaction.html>`__
    """

    props: PropsDictType = {
        "FunctionArn": (str, False),
    }


class Timestamp(AWSProperty):
    """
    `Timestamp <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestamp.html>`__
    """

    props: PropsDictType = {
        "Unit": (str, False),
        "Value": (str, True),
    }


class LocationAction(AWSProperty):
    """
    `LocationAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html>`__
    """

    props: PropsDictType = {
        "DeviceId": (str, True),
        "Latitude": (str, True),
        "Longitude": (str, True),
        "RoleArn": (str, True),
        "Timestamp": (Timestamp, False),
        "TrackerName": (str, True),
    }


class OpenSearchAction(AWSProperty):
    """
    `OpenSearchAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html>`__
    """

    props: PropsDictType = {
        "Endpoint": (str, True),
        "Id": (str, True),
        "Index": (str, True),
        "RoleArn": (str, True),
        "Type": (str, True),
    }


class UserProperty(AWSProperty):
    """
    `UserProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-userproperty.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Value": (str, True),
    }


class RepublishActionHeaders(AWSProperty):
    """
    `RepublishActionHeaders <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishactionheaders.html>`__
    """

    props: PropsDictType = {
        "ContentType": (str, False),
        "CorrelationData": (str, False),
        "MessageExpiry": (str, False),
        "PayloadFormatIndicator": (str, False),
        "ResponseTopic": (str, False),
        "UserProperties": ([UserProperty], False),
    }


class RepublishAction(AWSProperty):
    """
    `RepublishAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishaction.html>`__
    """

    props: PropsDictType = {
        "Headers": (RepublishActionHeaders, False),
        "Qos": (integer, False),
        "RoleArn": (str, True),
        "Topic": (str, True),
    }


class S3Action(AWSProperty):
    """
    `S3Action <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-s3action.html>`__
    """

    props: PropsDictType = {
        "BucketName": (str, True),
        "CannedAcl": (str, False),
        "Key": (str, True),
        "RoleArn": (str, True),
    }


class SnsAction(AWSProperty):
    """
    `SnsAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-snsaction.html>`__
    """

    props: PropsDictType = {
        "MessageFormat": (str, False),
        "RoleArn": (str, True),
        "TargetArn": (str, True),
    }


class SqsAction(AWSProperty):
    """
    `SqsAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sqsaction.html>`__
    """

    props: PropsDictType = {
        "QueueUrl": (str, True),
        "RoleArn": (str, True),
        "UseBase64": (boolean, False),
    }


class StepFunctionsAction(AWSProperty):
    """
    `StepFunctionsAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-stepfunctionsaction.html>`__
    """

    props: PropsDictType = {
        "ExecutionNamePrefix": (str, False),
        "RoleArn": (str, True),
        "StateMachineName": (str, True),
    }


class TimestreamDimension(AWSProperty):
    """
    `TimestreamDimension <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamdimension.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Value": (str, True),
    }


class TimestreamTimestamp(AWSProperty):
    """
    `TimestreamTimestamp <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamtimestamp.html>`__
    """

    props: PropsDictType = {
        "Unit": (str, True),
        "Value": (str, True),
    }


class TimestreamAction(AWSProperty):
    """
    `TimestreamAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html>`__
    """

    props: PropsDictType = {
        "DatabaseName": (str, True),
        "Dimensions": ([TimestreamDimension], True),
        "RoleArn": (str, True),
        "TableName": (str, True),
        "Timestamp": (TimestreamTimestamp, False),
    }


class Action(AWSProperty):
    """
    `Action <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html>`__
    """

    props: PropsDictType = {
        "CloudwatchAlarm": (CloudwatchAlarmAction, False),
        "CloudwatchLogs": (CloudwatchLogsAction, False),
        "CloudwatchMetric": (CloudwatchMetricAction, False),
        "DynamoDB": (DynamoDBAction, False),
        "DynamoDBv2": (DynamoDBv2Action, False),
        "Elasticsearch": (ElasticsearchAction, False),
        "Firehose": (FirehoseAction, False),
        "Http": (HttpAction, False),
        "IotAnalytics": (IotAnalyticsAction, False),
        "IotEvents": (IotEventsAction, False),
        "IotSiteWise": (IotSiteWiseAction, False),
        "Kafka": (KafkaAction, False),
        "Kinesis": (KinesisAction, False),
        "Lambda": (LambdaAction, False),
        "Location": (LocationAction, False),
        "OpenSearch": (OpenSearchAction, False),
        "Republish": (RepublishAction, False),
        "S3": (S3Action, False),
        "Sns": (SnsAction, False),
        "Sqs": (SqsAction, False),
        "StepFunctions": (StepFunctionsAction, False),
        "Timestream": (TimestreamAction, False),
    }


class TopicRulePayload(AWSProperty):
    """
    `TopicRulePayload <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html>`__
    """

    props: PropsDictType = {
        "Actions": ([Action], True),
        "AwsIotSqlVersion": (str, False),
        "Description": (str, False),
        "ErrorAction": (Action, False),
        "RuleDisabled": (boolean, False),
        "Sql": (str, True),
    }


class TopicRule(AWSObject):
    """
    `TopicRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html>`__
    """

    resource_type = "AWS::IoT::TopicRule"

    props: PropsDictType = {
        "RuleName": (str, False),
        "Tags": (Tags, False),
        "TopicRulePayload": (TopicRulePayload, True),
    }


class HttpUrlDestinationSummary(AWSProperty):
    """
    `HttpUrlDestinationSummary <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-httpurldestinationsummary.html>`__
    """

    props: PropsDictType = {
        "ConfirmationUrl": (str, False),
    }


class VpcDestinationProperties(AWSProperty):
    """
    `VpcDestinationProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-vpcdestinationproperties.html>`__
    """

    props: PropsDictType = {
        "RoleArn": (str, False),
        "SecurityGroups": ([str], False),
        "SubnetIds": ([str], False),
        "VpcId": (str, False),
    }


class TopicRuleDestination(AWSObject):
    """
    `TopicRuleDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html>`__
    """

    resource_type = "AWS::IoT::TopicRuleDestination"

    props: PropsDictType = {
        "HttpUrlProperties": (HttpUrlDestinationSummary, False),
        "Status": (str, False),
        "VpcProperties": (VpcDestinationProperties, False),
    }


class ServerCertificateSummary(AWSProperty):
    """
    `ServerCertificateSummary <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-servercertificatesummary.html>`__
    """

    props: PropsDictType = {
        "ServerCertificateArn": (str, False),
        "ServerCertificateStatus": (str, False),
        "ServerCertificateStatusDetail": (str, False),
    }
