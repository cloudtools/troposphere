from . import AWSObject, AWSProperty
from .constants import LOGS_ALLOWED_RETENTION_DAYS as RETENTION_DAYS
from .validators import integer_list_item


class Destination(AWSObject):
    resource_type = "AWS::Logs::Destination"

    props = {
        "DestinationName": (str, True),
        "DestinationPolicy": (str, True),
        "RoleArn": (str, True),
        "TargetArn": (str, True),
    }


class LogGroup(AWSObject):
    resource_type = "AWS::Logs::LogGroup"

    props = {
        "LogGroupName": (str, False),
        "RetentionInDays": (integer_list_item(RETENTION_DAYS), False),
    }


class LogStream(AWSObject):
    resource_type = "AWS::Logs::LogStream"

    props = {"LogGroupName": (str, True), "LogStreamName": (str, False)}


class MetricTransformation(AWSProperty):
    props = {
        "DefaultValue": (float, False),
        "MetricName": (str, True),
        "MetricNamespace": (str, True),
        "MetricValue": (str, True),
    }


class MetricFilter(AWSObject):
    resource_type = "AWS::Logs::MetricFilter"

    props = {
        "FilterPattern": (str, True),
        "LogGroupName": (str, True),
        "MetricTransformations": ([MetricTransformation], True),
    }


class QueryDefinition(AWSObject):
    resource_type = "AWS::Logs::QueryDefinition"

    props = {
        "LogGroupNames": ([str], False),
        "Name": (str, True),
        "QueryString": (str, True),
    }


class SubscriptionFilter(AWSObject):
    resource_type = "AWS::Logs::SubscriptionFilter"

    props = {
        "DestinationArn": (str, True),
        "FilterPattern": (str, True),
        "LogGroupName": (str, True),
        "RoleArn": (str, False),
    }
