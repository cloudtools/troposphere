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
        'NotificationArn': (str, False),
        'NotificationEvents': (notification_event, False),
        'NotificationType': (notification_type, False),
    }


class LoggingInfo(AWSProperty):
    props = {
        'Region': (str, True),
        'S3Bucket': (s3_bucket_name, True),
        'S3Prefix': (str, False),
    }


class MaintenanceWindowAutomationParameters(AWSProperty):
    props = {
        'DocumentVersion': (str, False),
        'Parameters': (dict, False),
    }


class MaintenanceWindowLambdaParameters(AWSProperty):
    props = {
        'ClientContext': (str, False),
        'Payload': (json_checker, False),
        'Qualifier': (str, False),
    }


class MaintenanceWindowRunCommandParameters(AWSProperty):
    props = {
        'Comment': (str, False),
        'DocumentHash': (str, False),
        'DocumentHashType': (str, False),
        'NotificationConfig': (NotificationConfig, False),
        'OutputS3BucketName': (s3_bucket_name, False),
        'OutputS3KeyPrefix': (str, False),
        'Parameters': (dict, False),
        'ServiceRoleArn': (str, False),
        'TimeoutSeconds': (integer, False),
    }


class MaintenanceWindowStepFunctionsParameters(AWSProperty):
    props = {
        'Input': (str, False),
        'Name': (str, False),
    }


class PatchFilter(AWSProperty):
    props = {
        'Key': (str, True),
        'Values': ([str], True),
    }


class PatchFilterGroup(AWSProperty):
    props = {
        'PatchFilters': ([PatchFilter], False),
    }


class Rule(AWSProperty):
    props = {
        'ApproveAfterDays': (integer, False),
        'ComplianceLevel': (compliance_level, False),
        'EnableNonSecurity': (boolean, False),
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
        'Key': (str, True),
        'Values': ([str], True),
    }


class S3OutputLocation(AWSProperty):
    props = {
        'OutputS3BucketName': (str, False),
        'OutputS3KeyPrefix': (str, False),
    }


class InstanceAssociationOutputLocation(AWSProperty):
    props = {
        'S3Location': (S3OutputLocation, False),
    }


class Association(AWSObject):
    resource_type = "AWS::SSM::Association"

    props = {
        'AssociationName': (str, False),
        'DocumentVersion': (str, False),
        'InstanceId': (str, False),
        'Name': (str, True),
        'OutputLocation': (InstanceAssociationOutputLocation, False),
        'Parameters': (dict, False),
        'ScheduleExpression': (str, False),
        'Targets': ([Targets], False),
        'WaitForSuccessTimeoutSeconds': (integer, False),
    }


class Document(AWSObject):
    resource_type = "AWS::SSM::Document"

    props = {
        # Need a better implementation of the SSM Document
        'Content': (dict, True),
        'DocumentType': (str, False),
        'Name': (str, False),
        'Tags': (Tags, False),
    }


class MaintenanceWindow(AWSObject):
    resource_type = "AWS::SSM::MaintenanceWindow"

    props = {
        'AllowUnassociatedTargets': (boolean, True),
        'Cutoff': (integer, True),
        'Description': (str, False),
        'Duration': (integer, True),
        'EndDate': (str, False),
        'Name': (str, True),
        'Schedule': (str, True),
        'ScheduleTimezone': (str, False),
        'StartDate': (str, False),
        'Tags': (Tags, False),
    }


class MaintenanceWindowTarget(AWSObject):
    resource_type = "AWS::SSM::MaintenanceWindowTarget"

    props = {
        'Description': (str, False),
        'Name': (str, False),
        'OwnerInformation': (str, False),
        'ResourceType': (str, True),
        'Targets': ([Targets], True),
        'WindowId': (str, True),
    }


class MaintenanceWindowTask(AWSObject):
    resource_type = "AWS::SSM::MaintenanceWindowTask"

    props = {
        'Description': (str, False),
        'LoggingInfo': (LoggingInfo, False),
        'MaxConcurrency': (str, False),
        'MaxErrors': (str, True),
        'Name': (str, False),
        'Priority': (integer, True),
        'ServiceRoleArn': (str, True),
        'Targets': ([Targets], True),
        'TaskArn': (str, True),
        'TaskInvocationParameters': (TaskInvocationParameters, False),
        'TaskParameters': (dict, False),
        'TaskType': (task_type, True),
        'WindowId': (str, False),
    }


class Parameter(AWSObject):
    resource_type = "AWS::SSM::Parameter"

    props = {
        'AllowedPattern': (str, False),
        'DataType': (str, False),
        'Description': (str, False),
        'Name': (str, False),
        'Policies': (str, False),
        'Tags': (dict, False),
        'Tier': (str, False),
        'Type': (str, True),
        'Value': (str, True),
    }


class PatchSource(AWSProperty):
    props = {
        'Configuration': (str, False),
        'Name': (str, False),
        'Products': ([str], False),
    }


class PatchBaseline(AWSObject):
    resource_type = "AWS::SSM::PatchBaseline"

    props = {
        'ApprovalRules': (RuleGroup, False),
        'ApprovedPatches': ([str], False),
        'ApprovedPatchesComplianceLevel': (compliance_level, False),
        'ApprovedPatchesEnableNonSecurity': (boolean, False),
        'Description': (str, False),
        'GlobalFilters': (PatchFilterGroup, False),
        'Name': (str, True),
        'OperatingSystem': (operating_system, False),
        'PatchGroups': ([str], False),
        'RejectedPatches': ([str], False),
        'RejectedPatchesAction': (str, False),
        'Sources': ([PatchSource], False),
        'Tags': (Tags, False),
    }


class AwsOrganizationsSource(AWSProperty):
    props = {
        'OrganizationalUnits': ([str], False),
        'OrganizationSourceType': (str, True),
    }


class SyncSource(AWSProperty):
    props = {
        'AwsOrganizationsSource': (AwsOrganizationsSource, False),
        'IncludeFutureRegions': (boolean, False),
        'SourceRegions': ([str], True),
        'SourceType': (str, True),

    }


class ResourceDataSync(AWSObject):
    resource_type = "AWS::SSM::ResourceDataSync"

    props = {
        'BucketName': (str, True),
        'BucketPrefix': (str, False),
        'BucketRegion': (str, True),
        'KMSKeyArn': (str, False),
        'SyncFormat': (str, True),
        'SyncName': (str, True),
        'SyncSource': (SyncSource, False),
        'SyncType': (str, False),
    }
