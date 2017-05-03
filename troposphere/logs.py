from . import AWSObject, AWSProperty
from .validators import integer_list_item
from .constants import LOGS_ALLOWED_RETENTION_DAYS as RETENTION_DAYS


class Destination(AWSObject):
    resource_type = "AWS::Logs::Destination"

    props = {
        'DestinationName': (basestring, True),
        'DestinationPolicy': (basestring, True),
        'RoleArn': (basestring, True),
        'TargetArn': (basestring, True),
    }


class LogGroup(AWSObject):
    resource_type = "AWS::Logs::LogGroup"

    props = {
        'LogGroupName': (basestring, False),
        'RetentionInDays': (integer_list_item(RETENTION_DAYS), False),
    }


class LogStream(AWSObject):
    resource_type = "AWS::Logs::LogStream"

    props = {
        'LogGroupName': (basestring, True),
        'LogStreamName': (basestring, False)
    }


class MetricTransformation(AWSProperty):
    props = {
        'MetricName': (basestring, True),
        'MetricNamespace': (basestring, True),
        'MetricValue': (basestring, True),
    }


class MetricFilter(AWSObject):
    resource_type = "AWS::Logs::MetricFilter"

    props = {
        'FilterPattern': (basestring, True),
        'LogGroupName': (basestring, True),
        'MetricTransformations': ([MetricTransformation], True),
    }


class SubscriptionFilter(AWSObject):
    resource_type = "AWS::Logs::SubscriptionFilter"

    props = {
        'DestinationArn': (basestring, True),
        'FilterPattern': (basestring, True),
        'LogGroupName': (basestring, True),
        'RoleArn': (basestring, False),
    }
