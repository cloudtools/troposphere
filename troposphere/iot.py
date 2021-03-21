from . import AWSObject, AWSProperty, Tags
from .compat import policytypes
from .validators import boolean, double, integer


class AuditCheckConfiguration(AWSProperty):
    props = {
        'Enabled': (boolean, False),
    }


class AuditCheckConfigurations(AWSProperty):
    props = {
        'AuthenticatedCognitoRoleOverlyPermissiveCheck':
            (AuditCheckConfiguration, False),
        'CaCertificateExpiringCheck': (AuditCheckConfiguration, False),
        'CaCertificateKeyQualityCheck': (AuditCheckConfiguration, False),
        'ConflictingClientIdsCheck': (AuditCheckConfiguration, False),
        'DeviceCertificateExpiringCheck': (AuditCheckConfiguration, False),
        'DeviceCertificateKeyQualityCheck':
            (AuditCheckConfiguration, False),
        'DeviceCertificateSharedCheck': (AuditCheckConfiguration, False),
        'IotPolicyOverlyPermissiveCheck': (AuditCheckConfiguration, False),
        'IotRoleAliasAllowsAccessToUnusedServicesCheck':
            (AuditCheckConfiguration, False),
        'IotRoleAliasOverlyPermissiveCheck':
            (AuditCheckConfiguration, False),
        'LoggingDisabledCheck': (AuditCheckConfiguration, False),
        'RevokedCaCertificateStillActiveCheck':
            (AuditCheckConfiguration, False),
        'RevokedDeviceCertificateStillActiveCheck':
            (AuditCheckConfiguration, False),
        'UnauthenticatedCognitoRoleOverlyPermissiveCheck':
            (AuditCheckConfiguration, False),
    }


class AuditNotificationTarget(AWSProperty):
    props = {
        'Enabled': (boolean, False),
        'RoleArn': (str, False),
        'TargetArn': (str, False),
    }


class AuditNotificationTargetConfigurations(AWSProperty):
    props = {
        'Sns': (AuditNotificationTarget, False),
    }


class AccountAuditConfiguration(AWSObject):
    resource_type = "AWS::IoT::AccountAuditConfiguration"

    props = {
        'AccountId': (str, True),
        'AuditCheckConfigurations': (AuditCheckConfigurations, True),
        'AuditNotificationTargetConfigurations':
            (AuditNotificationTargetConfigurations, False),
        'RoleArn': (str, True),
    }


class Authorizer(AWSObject):
    resource_type = "AWS::IoT::Authorizer"

    props = {
        'AuthorizerFunctionArn': (str, True),
        'AuthorizerName': (str, False),
        'SigningDisabled': (boolean, False),
        'Status': (str, False),
        'Tags': (dict, False),
        'TokenKeyName': (str, False),
        # 'TokenSigningPublicKeys': (TokenSigningPublicKeys, False),
    }


class Certificate(AWSObject):
    resource_type = "AWS::IoT::Certificate"

    props = {
        'CACertificatePem': (str, False),
        'CertificateMode': (str, False),
        'CertificatePem': (str, False),
        'CertificateSigningRequest': (str, False),
        'Status': (str, True),
    }


class CustomMetric(AWSObject):
    resource_type = "AWS::IoT::CustomMetric"

    props = {
        'DisplayName': (str, False),
        'MetricName': (str, False),
        'MetricType': (str, True),
        'Tags': (Tags, False),
    }


class Dimension(AWSObject):
    resource_type = "AWS::IoT::Dimension"

    props = {
        'Name': (str, False),
        'StringValues': ([str], True),
        'Tags': (Tags, False),
        'Type': (str, True),
    }


class AuthorizerConfig(AWSProperty):
    props = {
        'AllowAuthorizerOverride': (boolean, False),
        'DefaultAuthorizerName': (str, False),
    }


class DomainConfiguration(AWSObject):
    resource_type = "AWS::IoT::DomainConfiguration"

    props = {
        'AuthorizerConfig': (AuthorizerConfig, False),
        'DomainConfigurationName': (str, False),
        'DomainConfigurationStatus': (str, False),
        'DomainName': (str, False),
        'ServerCertificateArns': ([str], False),
        'ServiceType': (str, False),
        'Tags': (Tags, False),
        'ValidationCertificateArn': (str, False),
    }


class AddThingsToThingGroupParams(AWSProperty):
    props = {
        'OverrideDynamicGroups': (boolean, False),
        'ThingGroupNames': ([str], True),
    }


class EnableIoTLoggingParams(AWSProperty):
    props = {
        'LogLevel': (str, True),
        'RoleArnForLogging': (str, True),
    }


class PublishFindingToSnsParams(AWSProperty):
    props = {
        'TopicArn': (str, True),
    }


class ReplaceDefaultPolicyVersionParams(AWSProperty):
    props = {
        'TemplateName': (str, True),
    }


class UpdateCACertificateParams(AWSProperty):
    props = {
        'Action': (str, True),
    }


class UpdateDeviceCertificateParams(AWSProperty):
    props = {
        'Action': (str, True),
    }


class ActionParams(AWSProperty):
    props = {
        'AddThingsToThingGroupParams': (AddThingsToThingGroupParams, False),
        'EnableIoTLoggingParams': (EnableIoTLoggingParams, False),
        'PublishFindingToSnsParams': (PublishFindingToSnsParams, False),
        'ReplaceDefaultPolicyVersionParams':
            (ReplaceDefaultPolicyVersionParams, False),
        'UpdateCACertificateParams': (UpdateCACertificateParams, False),
        'UpdateDeviceCertificateParams':
            (UpdateDeviceCertificateParams, False),
    }


class MitigationAction(AWSObject):
    resource_type = "AWS::IoT::MitigationAction"

    props = {
        'ActionName': (str, False),
        'ActionParams': (ActionParams, True),
        'RoleArn': (str, True),
        'Tags': (Tags, False),
    }


class CloudwatchAlarmAction(AWSProperty):
    props = {
        'AlarmName': (str, True),
        'RoleArn': (str, True),
        'StateReason': (str, True),
        'StateValue': (str, True),
    }


class CloudwatchMetricAction(AWSProperty):
    props = {
        'MetricName': (str, True),
        'MetricNamespace': (str, True),
        'MetricTimestamp': (str, False),
        'MetricUnit': (str, True),
        'MetricValue': (str, True),
        'RoleArn': (str, True),
    }


class DynamoDBAction(AWSProperty):
    props = {
        'HashKeyField': (str, True),
        'HashKeyType': (str, False),
        'HashKeyValue': (str, True),
        'PayloadField': (str, False),
        'RangeKeyField': (str, False),
        'RangeKeyType': (str, False),
        'RangeKeyValue': (str, False),
        'RoleArn': (str, True),
        'TableName': (str, True),
    }


class PutItemInput(AWSProperty):
    props = {
        'TableName': (str, True),
    }


class DynamoDBv2Action(AWSProperty):
    props = {
        'PutItem': (PutItemInput, False),
        'RoleArn': (str, False),
    }


class ElasticsearchAction(AWSProperty):
    props = {
        'Endpoint': (str, True),
        'Id': (str, True),
        'Index': (str, True),
        'RoleArn': (str, True),
        'Type': (str, True),
    }


class FirehoseAction(AWSProperty):
    props = {
        'DeliveryStreamName': (str, True),
        'RoleArn': (str, True),
        'Separator': (str, False),
    }


class IotAnalyticsAction(AWSProperty):
    props = {
        'ChannelName': (str, True),
        'RoleArn': (str, True),
    }


class KinesisAction(AWSProperty):
    props = {
        'PartitionKey': (str, False),
        'RoleArn': (str, True),
        'StreamName': (str, True),
    }


class LambdaAction(AWSProperty):
    props = {
        'FunctionArn': (str, True),
    }


class RepublishAction(AWSProperty):
    props = {
        'Qos': (integer, False),
        'RoleArn': (str, True),
        'Topic': (str, True),
    }


class S3Action(AWSProperty):
    props = {
        'BucketName': (str, True),
        'Key': (str, True),
        'RoleArn': (str, True),
    }


class SnsAction(AWSProperty):
    props = {
        'MessageFormat': (str, False),
        'RoleArn': (str, True),
        'TargetArn': (str, True),
    }


class SqsAction(AWSProperty):
    props = {
        'QueueUrl': (str, True),
        'RoleArn': (str, True),
        'UseBase64': (str, False),
    }


class SigV4Authorization(AWSProperty):
    props = {
        'RoleArn': (str, True),
        'ServiceName': (str, True),
        'SigningRegion': (str, True),
    }


class HttpActionHeader(AWSProperty):
    props = {
        'Key': (str, True),
        'Value': (str, True),
    }


class HttpAuthorization(AWSProperty):
    props = {
        'Sigv4': (SigV4Authorization, False),
    }


class HttpAction(AWSProperty):
    props = {
        'Auth': (HttpAuthorization, False),
        'ConfirmationUrl': (str, False),
        'Headers': ([HttpActionHeader], False),
        'Url': (str, True),
    }


class IotEventsAction(AWSProperty):
    props = {
        'InputName': (str, True),
        'MessageId': (str, False),
        'RoleArn': (str, True),
    }


class AssetPropertyVariant(AWSProperty):
    props = {
        'BooleanValue': (str, False),
        'DoubleValue': (str, False),
        'IntegerValue': (str, False),
        'StringValue': (str, False),
    }


class AssetPropertyTimestamp(AWSProperty):
    props = {
        'OffsetInNanos': (str, False),
        'TimeInSeconds': (str, True),
    }


class AssetPropertyValue(AWSProperty):
    props = {
        'Quality': (str, False),
        'Timestamp': (AssetPropertyTimestamp, True),
        'Value': (AssetPropertyVariant, True),
    }


class PutAssetPropertyValueEntry(AWSProperty):
    props = {
        'AssetId': (str, False),
        'EntryId': (str, False),
        'PropertyAlias': (str, False),
        'PropertyId': (str, False),
        'PropertyValues': ([AssetPropertyValue], True),
    }


class IotSiteWiseAction(AWSProperty):
    props = {
        'PutAssetPropertyValueEntries': ([PutAssetPropertyValueEntry], True),
        'RoleArn': (str, True),
    }


class StepFunctionsAction(AWSProperty):
    props = {
        'ExecutionNamePrefix': (str, False),
        'RoleArn': (str, True),
        'StateMachineName': (str, True),
    }


class Action(AWSProperty):
    props = {
        'CloudwatchAlarm': (CloudwatchAlarmAction, False),
        'CloudwatchMetric': (CloudwatchMetricAction, False),
        'DynamoDB': (DynamoDBAction, False),
        'DynamoDBv2': (DynamoDBv2Action, False),
        'Elasticsearch': (ElasticsearchAction, False),
        'Firehose': (FirehoseAction, False),
        'Http': (HttpAction, False),
        'IotAnalytics': (IotAnalyticsAction, False),
        'IotEvents': (IotEventsAction, False),
        'IotSiteWise': (IotSiteWiseAction, False),
        'Kinesis': (KinesisAction, False),
        'Lambda': (LambdaAction, False),
        'Republish': (RepublishAction, False),
        'S3': (S3Action, False),
        'Sns': (SnsAction, False),
        'Sqs': (SqsAction, False),
        'StepFunctions': (StepFunctionsAction, False)
    }


class TopicRulePayload(AWSProperty):
    props = {
        'Actions': ([Action], True),
        'AwsIotSqlVersion': (str, False),
        'Description': (str, False),
        'RuleDisabled': (boolean, True),
        'Sql': (str, True),
    }


class TopicRule(AWSObject):
    resource_type = "AWS::IoT::TopicRule"

    props = {
        'RuleName': (str, False),
        'TopicRulePayload': (TopicRulePayload, True),
    }


class ThingPrincipalAttachment(AWSObject):
    resource_type = "AWS::IoT::ThingPrincipalAttachment"

    props = {
        'Principal': (str, True),
        'ThingName': (str, True),
    }


class Thing(AWSObject):
    resource_type = "AWS::IoT::Thing"

    props = {
        'AttributePayload': (dict, False),
        'ThingName': (str, False),
    }


class PolicyPrincipalAttachment(AWSObject):
    resource_type = "AWS::IoT::PolicyPrincipalAttachment"

    props = {
        'PolicyName': (str, True),
        'Principal': (str, True),
    }


class Policy(AWSObject):
    resource_type = "AWS::IoT::Policy"

    props = {
        'PolicyDocument': (policytypes, True),
        'PolicyName': (str, False),
    }


class ProvisioningHook(AWSProperty):
    props = {
        'PayloadVersion': (str, False),
        'TargetArn': (str, False),
    }


class ProvisioningTemplate(AWSObject):
    resource_type = "AWS::IoT::ProvisioningTemplate"

    props = {
        'Description': (str, False),
        'Enabled': (boolean, False),
        'PreProvisioningHook': (ProvisioningHook, False),
        'ProvisioningRoleArn': (str, True),
        'Tags': (dict, False),
        'TemplateBody': (str, True),
        'TemplateName': (str, False),
    }


class ScheduledAudit(AWSObject):
    resource_type = "AWS::IoT::ScheduledAudit"

    props = {
        'DayOfMonth': (str, False),
        'DayOfWeek': (str, False),
        'Frequency': (str, True),
        'ScheduledAuditName': (str, False),
        'Tags': (Tags, False),
        'TargetCheckNames': ([str], True),
    }


class MachineLearningDetectionConfig(AWSProperty):
    props = {
        'ConfidenceLevel': (str, False),
    }


class MetricValue(AWSProperty):
    props = {
        'Cidrs': ([str], False),
        'Count': (str, False),
        'Number': (double, False),
        'Numbers': ([double], False),
        'Ports': ([integer], False),
        'Strings': ([str], False),
    }


class StatisticalThreshold(AWSProperty):
    props = {
        'Statistic': (str, False),
    }


class BehaviorCriteria(AWSProperty):
    props = {
        'ComparisonOperator': (str, False),
        'ConsecutiveDatapointsToAlarm': (integer, False),
        'ConsecutiveDatapointsToClear': (integer, False),
        'DurationSeconds': (integer, False),
        'MlDetectionConfig': (MachineLearningDetectionConfig, False),
        'StatisticalThreshold': (StatisticalThreshold, False),
        'Value': (MetricValue, False),
    }


class MetricDimension(AWSProperty):
    props = {
        'DimensionName': (str, True),
        'Operator': (str, False),
    }


class Behavior(AWSProperty):
    props = {
        'Criteria': (BehaviorCriteria, False),
        'Metric': (str, False),
        'MetricDimension': (MetricDimension, False),
        'Name': (str, True),
        'SuppressAlerts': (boolean, False),
    }


class MetricToRetain(AWSProperty):
    props = {
        'Metric': (str, True),
        'MetricDimension': (MetricDimension, False),
    }


class SecurityProfile(AWSObject):
    resource_type = "AWS::IoT::SecurityProfile"

    props = {
        'AdditionalMetricsToRetainV2': ([MetricToRetain], False),
        'AlertTargets': (dict, False),
        'Behaviors': ([Behavior], False),
        'SecurityProfileDescription': (str, False),
        'SecurityProfileName': (str, False),
        'Tags': (Tags, False),
        'TargetArns': ([str], False),
    }


class HttpUrlDestinationSummary(AWSProperty):
    props = {
        'ConfirmationUrl': (str, False),
    }


class VpcDestinationProperties(AWSProperty):
    props = {
        'RoleArn': (str, False),
        'SecurityGroups': ([str], False),
        'SubnetIds': ([str], False),
        'VpcId': (str, False),
    }


class TopicRuleDestination(AWSObject):
    resource_type = "AWS::IoT::TopicRuleDestination"

    props = {
        'HttpUrlProperties': (HttpUrlDestinationSummary, False),
        'Status': (str, False),
        'VpcProperties': (VpcDestinationProperties, False),
    }
