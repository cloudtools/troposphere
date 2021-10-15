# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, If, Tags
from .validators import backup_vault_name, double, exactly_one, json_checker


class AdvancedBackupSettingResourceType(AWSProperty):
    props = {
        "BackupOptions": (dict, True),
        "ResourceType": (str, True),
    }


class LifecycleResourceType(AWSProperty):
    props = {
        "DeleteAfterDays": (double, False),
        "MoveToColdStorageAfterDays": (double, False),
    }


class CopyActionResourceType(AWSProperty):
    props = {
        "DestinationBackupVaultArn": (str, True),
        "Lifecycle": (LifecycleResourceType, False),
    }


class BackupRuleResourceType(AWSProperty):
    props = {
        "CompletionWindowMinutes": (double, False),
        "CopyActions": ([CopyActionResourceType], False),
        "EnableContinuousBackup": (bool, False),
        "Lifecycle": (LifecycleResourceType, False),
        "RecoveryPointTags": (dict, False),
        "RuleName": (str, True),
        "ScheduleExpression": (str, False),
        "StartWindowMinutes": (double, False),
        "TargetBackupVault": (str, True),
    }


class BackupPlanResourceType(AWSProperty):
    props = {
        "AdvancedBackupSettings": ([AdvancedBackupSettingResourceType], False),
        "BackupPlanName": (str, True),
        "BackupPlanRule": ([BackupRuleResourceType], True),
    }


class BackupPlan(AWSObject):
    resource_type = "AWS::Backup::BackupPlan"

    props = {
        "BackupPlan": (BackupPlanResourceType, True),
        "BackupPlanTags": (dict, False),
    }


class ConditionResourceType(AWSProperty):
    props = {
        "ConditionKey": (str, True),
        "ConditionType": (str, True),
        "ConditionValue": (str, True),
    }


class BackupSelectionResourceType(AWSProperty):
    props = {
        "IamRoleArn": (str, True),
        "ListOfTags": ([ConditionResourceType], False),
        "Resources": ([str], False),
        "SelectionName": (str, True),
    }

    def validate(self):
        conds = [
            "ListOfTags",
            "Resources",
        ]

        def check_if(names, props):
            validated = []
            for name in names:
                validated.append(name in props and isinstance(props[name], If))
            return all(validated)

        if check_if(conds, self.properties):
            return

        exactly_one(self.__class__.__name__, self.properties, conds)


class BackupSelection(AWSObject):
    resource_type = "AWS::Backup::BackupSelection"

    props = {
        "BackupPlanId": (str, True),
        "BackupSelection": (BackupSelectionResourceType, True),
    }


class LockConfigurationType(AWSProperty):
    props = {
        "ChangeableForDays": (double, False),
        "MaxRetentionDays": (double, False),
        "MinRetentionDays": (double, True),
    }


class NotificationObjectType(AWSProperty):
    props = {"BackupVaultEvents": ([str], True), "SNSTopicArn": (str, True)}


class BackupVault(AWSObject):
    resource_type = "AWS::Backup::BackupVault"

    props = {
        "AccessPolicy": (json_checker, False),
        "BackupVaultName": (backup_vault_name, True),
        "BackupVaultTags": (dict, False),
        "EncryptionKeyArn": (str, False),
        "LockConfiguration": (LockConfigurationType, False),
        "Notifications": (NotificationObjectType, False),
    }


class ControlInputParameter(AWSProperty):
    props = {
        "ParameterName": (str, True),
        "ParameterValue": (str, True),
    }


class FrameworkControl(AWSProperty):
    props = {
        "ControlInputParameters": ([ControlInputParameter], False),
        "ControlName": (str, True),
        "ControlScope": (dict, False),
    }


class Framework(AWSObject):
    resource_type = "AWS::Backup::Framework"

    props = {
        "FrameworkControls": ([FrameworkControl], True),
        "FrameworkDescription": (str, False),
        "FrameworkName": (str, False),
        "FrameworkTags": (Tags, False),
    }


class ReportPlan(AWSObject):
    resource_type = "AWS::Backup::ReportPlan"

    props = {
        "ReportDeliveryChannel": (dict, True),
        "ReportPlanDescription": (str, False),
        "ReportPlanName": (str, False),
        "ReportPlanTags": (Tags, False),
        "ReportSetting": (dict, True),
    }
