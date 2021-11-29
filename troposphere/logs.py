import json

from . import AWSObject, AWSProperty, Tags
from .compat import policytypes
from .constants import LOGS_ALLOWED_RETENTION_DAYS as RETENTION_DAYS
from .validators import integer_list_item, json_checker

policytypes = policytypes + (str,)


def validate_resource_policy(policy_document):
    """validate policy_document. Between 1 to 5120"""

    if not isinstance(policy_document, policytypes):
        raise ValueError("PolicyDocument must be a valid policy document")

    if isinstance(policy_document, str) and not json_checker(policy_document):
        raise ValueError("PolicyDocument must be a valid JSON formated string")

    if isinstance(policy_document, dict):
        policy_document_text = json.dumps(policy_document)
    elif isinstance(policy_document, str):
        policy_document_text = policy_document
    else:
        policy_document_text = policy_document.to_json()

    # NB: {} empty dict is 2 length
    if len(policy_document_text) < 3:
        raise ValueError("PolicyDocument must not be empty")

    if len(policy_document_text) > 5120:
        raise ValueError("PolicyDocument maximum length must not exceed 5120")

    return policy_document


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
        "KmsKeyId": (str, False),
        "LogGroupName": (str, False),
        "RetentionInDays": (integer_list_item(RETENTION_DAYS), False),
        "Tags": (Tags, False),
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


class ResourcePolicy(AWSObject):
    resource_type = "AWS::Logs::ResourcePolicy"

    props = {
        "PolicyDocument": (validate_resource_policy, True),
        "PolicyName": (str, True),
    }


class SubscriptionFilter(AWSObject):
    resource_type = "AWS::Logs::SubscriptionFilter"

    props = {
        "DestinationArn": (str, True),
        "FilterPattern": (str, True),
        "LogGroupName": (str, True),
        "RoleArn": (str, False),
    }
