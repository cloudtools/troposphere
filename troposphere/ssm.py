# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import (integer, boolean, s3_bucket_name, notification_type,
                         notification_event, json_checker, task_type,
                         operating_system, compliance_level)


class NotificationConfig(AWSProperty):
    props = {
        'NotificationArn': (basestring, False),
        'NotificationEvents': (notification_event, False),
        'NotificationType': (notification_type, False),
    }


class LoggingInfo(AWSProperty):
    props = {
        'Region': (basestring, True),
        'S3Bucket': (s3_bucket_name, True),
        'S3Prefix': (basestring, False),
    }


class MaintenanceWindowAutomationParameters(AWSProperty):
    props = {
        'DocumentVersion': (basestring, False),
        'Parameters': (dict, False),
    }


class MaintenanceWindowLambdaParameters(AWSProperty):
    props = {
        'ClientContext': (basestring, False),
        'Payload': (json_checker, False),
        'Qualifier': (basestring, False),
    }


class MaintenanceWindowRunCommandParameters(AWSProperty):
    props = {
        'Comment': (basestring, False),
        'DocumentHash': (basestring, False),
        'DocumentHashType': (basestring, False),
        'NotificationConfig': (NotificationConfig, False),
        'OutputS3BucketName': (s3_bucket_name, False),
        'OutputS3KeyPrefix': (basestring, False),
        'Parameters': (dict, False),
        'ServiceRoleArn': (basestring, False),
        'TimeoutSeconds': (integer, False),
    }


class MaintenanceWindowStepFunctionsParameters(AWSProperty):
    props = {
        'Input': (basestring, False),
        'Name': (basestring, False),
    }


class PatchFilter(AWSProperty):
    props = {
        'Key': (basestring, True),
        'Values': ([basestring], True),
    }


class PatchFilterGroup(AWSProperty):
    props = {
        'PatchFilters': ([PatchFilter], False),
    }


class Rule(AWSProperty):
    props = {
        'ApproveAfterDays': (integer, False),
        'ComplianceLevel': (compliance_level, False),
        'PatchFilterGroup': (PatchFilterGroup, False),
    }


class RuleGroup(AWSProperty):
    props = {
        'PatchRules': ([Rule], False),
    }


class TaskInvocationParameters(AWSProperty):
    props = {
        'MaintenanceWindowAutomationParameters':
        (MaintenanceWindowAutomationParameters, False),
        'MaintenanceWindowLambdaParameters':
        (MaintenanceWindowLambdaParameters, False),
        'MaintenanceWindowRunCommandParameters':
        (MaintenanceWindowRunCommandParameters, False),
        'MaintenanceWindowStepFunctionsParameters':
        (MaintenanceWindowStepFunctionsParameters, False),
    }


class Targets(AWSProperty):
    props = {
        'Key': (basestring, True),
        'Values': ([basestring], True),
    }


class Association(AWSObject):
    resource_type = "AWS::SSM::Association"

    props = {
        'AssociationName': (basestring, False),
        'DocumentVersion': (basestring, False),
        'InstanceId': (basestring, False),
        'Name': (basestring, True),
        'Parameters': (dict, False),
        'ScheduleExpression': (basestring, False),
        'Targets': ([Targets], False),
    }


class Document(AWSObject):
    resource_type = "AWS::SSM::Document"

    props = {
        # Need a better implementation of the SSM Document
        'Content': (dict, True),
        'DocumentType': (basestring, False),
        'Tags': (Tags, False),
    }


class MaintenanceWindow(AWSObject):
    resource_type = "AWS::SSM::MaintenanceWindow"

    props = {
        'AllowUnassociatedTargets': (boolean, True),
        'Cutoff': (integer, True),
        'Description': (basestring, False),
        'Duration': (integer, True),
        'Name': (basestring, True),
        'Schedule': (basestring, True),
    }


class MaintenanceWindowTarget(AWSObject):
    resource_type = "AWS::SSM::MaintenanceWindowTarget"

    props = {
        'Description': (basestring, False),
        'Name': (basestring, False),
        'OwnerInformation': (basestring, False),
        'ResourceType': (basestring, True),
        'Targets': ([Targets], True),
        'WindowId': (basestring, True),
    }


class MaintenanceWindowTask(AWSObject):
    resource_type = "AWS::SSM::MaintenanceWindowTask"

    props = {
        'Description': (basestring, False),
        'LoggingInfo': (LoggingInfo, False),
        'MaxConcurrency': (integer, False),
        'MaxErrors': (integer, True),
        'Name': (basestring, False),
        'Priority': (integer, True),
        'ServiceRoleArn': (basestring, True),
        'Targets': ([Targets], True),
        'TaskArn': (basestring, True),
        'TaskInvocationParameters': (TaskInvocationParameters, False),
        'TaskParameters': (dict, False),
        'TaskType': (task_type, True),
        'WindowId': (basestring, False),
    }


class Parameter(AWSObject):
    resource_type = "AWS::SSM::Parameter"

    props = {
        'AllowedPattern': (basestring, False),
        'Description': (basestring, False),
        'Name': (basestring, False),
        'Type': (basestring, True),
        'Value': (basestring, True),
    }


class PatchBaseline(AWSObject):
    resource_type = "AWS::SSM::PatchBaseline"

    props = {
        'ApprovalRules': (RuleGroup, False),
        'ApprovedPatches': ([basestring], False),
        'ApprovedPatchesComplianceLevel': (compliance_level, False),
        'Description': (basestring, False),
        'GlobalFilters': (PatchFilterGroup, False),
        'Name': (basestring, True),
        'OperatingSystem': (operating_system, False),
        'PatchGroups': ([basestring], False),
        'RejectedPatches': ([basestring], False),
    }
