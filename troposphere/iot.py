from . import AWSObject, AWSProperty
from .compat import policytypes
from .validators import boolean, integer


class Authorizer(AWSObject):
    resource_type = "AWS::IoT::Authorizer"

    props = {
        'AuthorizerFunctionArn': (basestring, True),
        'AuthorizerName': (basestring, False),
        'SigningDisabled': (boolean, False),
        'Status': (basestring, False),
        'Tags': (dict, False),
        'TokenKeyName': (basestring, False),
        # 'TokenSigningPublicKeys': (TokenSigningPublicKeys, False),
    }


class CloudwatchAlarmAction(AWSProperty):
    props = {
        'AlarmName': (basestring, True),
        'RoleArn': (basestring, True),
        'StateReason': (basestring, True),
        'StateValue': (basestring, True),
    }


class CloudwatchMetricAction(AWSProperty):
    props = {
        'MetricName': (basestring, True),
        'MetricNamespace': (basestring, True),
        'MetricTimestamp': (basestring, False),
        'MetricUnit': (basestring, True),
        'MetricValue': (basestring, True),
        'RoleArn': (basestring, True),
    }


class DynamoDBAction(AWSProperty):
    props = {
        'HashKeyField': (basestring, True),
        'HashKeyType': (basestring, False),
        'HashKeyValue': (basestring, True),
        'PayloadField': (basestring, False),
        'RangeKeyField': (basestring, False),
        'RangeKeyType': (basestring, False),
        'RangeKeyValue': (basestring, False),
        'RoleArn': (basestring, True),
        'TableName': (basestring, True),
    }


class PutItemInput(AWSProperty):
    props = {
        'TableName': (basestring, True),
    }


class DynamoDBv2Action(AWSProperty):
    props = {
        'PutItem': (PutItemInput, False),
        'RoleArn': (basestring, False),
    }


class ElasticsearchAction(AWSProperty):
    props = {
        'Endpoint': (basestring, True),
        'Id': (basestring, True),
        'Index': (basestring, True),
        'RoleArn': (basestring, True),
        'Type': (basestring, True),
    }


class FirehoseAction(AWSProperty):
    props = {
        'DeliveryStreamName': (basestring, True),
        'RoleArn': (basestring, True),
        'Separator': (basestring, False),
    }


class IotAnalyticsAction(AWSProperty):
    props = {
        'ChannelName': (basestring, True),
        'RoleArn': (basestring, True),
    }


class KinesisAction(AWSProperty):
    props = {
        'PartitionKey': (basestring, False),
        'RoleArn': (basestring, True),
        'StreamName': (basestring, True),
    }


class LambdaAction(AWSProperty):
    props = {
        'FunctionArn': (basestring, True),
    }


class RepublishAction(AWSProperty):
    props = {
        'Qos': (integer, False),
        'RoleArn': (basestring, True),
        'Topic': (basestring, True),
    }


class S3Action(AWSProperty):
    props = {
        'BucketName': (basestring, True),
        'Key': (basestring, True),
        'RoleArn': (basestring, True),
    }


class SnsAction(AWSProperty):
    props = {
        'MessageFormat': (basestring, False),
        'RoleArn': (basestring, True),
        'TargetArn': (basestring, True),
    }


class SqsAction(AWSProperty):
    props = {
        'QueueUrl': (basestring, True),
        'RoleArn': (basestring, True),
        'UseBase64': (basestring, False),
    }


class SigV4Authorization(AWSProperty):
    props = {
        'RoleArn': (basestring, True),
        'ServiceName': (basestring, True),
        'SigningRegion': (basestring, True),
    }


class HttpActionHeader(AWSProperty):
    props = {
        'Key': (basestring, True),
        'Value': (basestring, True),
    }


class HttpAuthorization(AWSProperty):
    props = {
        'Sigv4': (SigV4Authorization, False),
    }


class HttpAction(AWSProperty):
    props = {
        'Auth': (HttpAuthorization, False),
        'ConfirmationUrl': (basestring, False),
        'Headers': ([HttpActionHeader], False),
        'Url': (basestring, True),
    }


class IotEventsAction(AWSProperty):
    props = {
        'InputName': (basestring, True),
        'MessageId': (basestring, False),
        'RoleArn': (basestring, True),
    }


class AssetPropertyVariant(AWSProperty):
    props = {
        'BooleanValue': (basestring, False),
        'DoubleValue': (basestring, False),
        'IntegerValue': (basestring, False),
        'StringValue': (basestring, False),
    }


class AssetPropertyTimestamp(AWSProperty):
    props = {
        'OffsetInNanos': (basestring, False),
        'TimeInSeconds': (basestring, True),
    }


class AssetPropertyValue(AWSProperty):
    props = {
        'Quality': (basestring, False),
        'Timestamp': (AssetPropertyTimestamp, True),
        'Value': (AssetPropertyVariant, True),
    }


class PutAssetPropertyValueEntry(AWSProperty):
    props = {
        'AssetId': (basestring, False),
        'EntryId': (basestring, False),
        'PropertyAlias': (basestring, False),
        'PropertyId': (basestring, False),
        'PropertyValues': ([AssetPropertyValue], True),
    }


class IotSiteWiseAction(AWSProperty):
    props = {
        'PutAssetPropertyValueEntries': ([PutAssetPropertyValueEntry], True),
        'RoleArn': (basestring, True),
    }


class StepFunctionsAction(AWSProperty):
    props = {
        'ExecutionNamePrefix': (basestring, False),
        'RoleArn': (basestring, True),
        'StateMachineName': (basestring, True),
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
        'AwsIotSqlVersion': (basestring, False),
        'Description': (basestring, False),
        'RuleDisabled': (boolean, True),
        'Sql': (basestring, True),
    }


class TopicRule(AWSObject):
    resource_type = "AWS::IoT::TopicRule"

    props = {
        'RuleName': (basestring, False),
        'TopicRulePayload': (TopicRulePayload, True),
    }


class ThingPrincipalAttachment(AWSObject):
    resource_type = "AWS::IoT::ThingPrincipalAttachment"

    props = {
        'Principal': (basestring, True),
        'ThingName': (basestring, True),
    }


class Thing(AWSObject):
    resource_type = "AWS::IoT::Thing"

    props = {
        'AttributePayload': (dict, False),
        'ThingName': (basestring, False),
    }


class PolicyPrincipalAttachment(AWSObject):
    resource_type = "AWS::IoT::PolicyPrincipalAttachment"

    props = {
        'PolicyName': (basestring, True),
        'Principal': (basestring, True),
    }


class Policy(AWSObject):
    resource_type = "AWS::IoT::Policy"

    props = {
        'PolicyDocument': (policytypes, True),
        'PolicyName': (basestring, False),
    }


class Certificate(AWSObject):
    resource_type = "AWS::IoT::Certificate"

    props = {
        'CertificateSigningRequest': (basestring, True),
        'Status': (basestring, True),
    }


class ProvisioningHook(AWSProperty):
    props = {
        'PayloadVersion': (basestring, False),
        'TargetArn': (basestring, False),
    }


class ProvisioningTemplate(AWSObject):
    resource_type = "AWS::IoT::ProvisioningTemplate"

    props = {
        'Description': (basestring, False),
        'Enabled': (boolean, False),
        'PreProvisioningHook': (ProvisioningHook, False),
        'ProvisioningRoleArn': (basestring, True),
        'Tags': (dict, False),
        'TemplateBody': (basestring, True),
        'TemplateName': (basestring, False),
    }
