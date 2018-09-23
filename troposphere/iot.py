from . import AWSObject, AWSProperty
from .validators import boolean
try:
    from awacs.aws import Policy
    policytypes = (dict, Policy)
except ImportError:
    policytypes = dict,


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


class Action(AWSProperty):
    props = {
        'CloudwatchAlarm': (CloudwatchAlarmAction, False),
        'CloudwatchMetric': (CloudwatchMetricAction, False),
        'DynamoDB': (DynamoDBAction, False),
        'DynamoDBv2': (DynamoDBv2Action, False),
        'Elasticsearch': (ElasticsearchAction, False),
        'Firehose': (FirehoseAction, False),
        'Kinesis': (KinesisAction, False),
        'Lambda': (LambdaAction, False),
        'Republish': (RepublishAction, False),
        'S3': (S3Action, False),
        'Sns': (SnsAction, False),
        'Sqs': (SqsAction, False),
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
