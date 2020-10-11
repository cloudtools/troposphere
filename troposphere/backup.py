# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, If
from .validators import backup_vault_name, double, exactly_one, json_checker


class AdvancedBackupSettingResourceType(AWSProperty):
    props = {
        'BackupOptions': (dict, True),
        'ResourceType': (basestring, True),
    }


class LifecycleResourceType(AWSProperty):
    props = {
        'DeleteAfterDays': (double, False),
        'MoveToColdStorageAfterDays': (double, False),
    }


class BackupRuleResourceType(AWSProperty):
    props = {
        'CompletionWindowMinutes': (double, False),
        'Lifecycle': (LifecycleResourceType, False),
        'RecoveryPointTags': (dict, False),
        'RuleName': (basestring, True),
        'ScheduleExpression': (basestring, False),
        'StartWindowMinutes': (double, False),
        'TargetBackupVault': (basestring, True),
    }


class BackupPlanResourceType(AWSProperty):
    props = {
        'AdvancedBackupSettings':
            ([AdvancedBackupSettingResourceType], False),
        'BackupPlanName': (basestring, True),
        'BackupPlanRule': ([BackupRuleResourceType], True),
    }


class BackupPlan(AWSObject):
    resource_type = "AWS::Backup::BackupPlan"

    props = {
        'BackupPlan': (BackupPlanResourceType, True),
        'BackupPlanTags': (dict, False),
    }


class ConditionResourceType(AWSProperty):
    props = {
        'ConditionKey': (basestring, True),
        'ConditionType': (basestring, True),
        'ConditionValue': (basestring, True),
    }


class BackupSelectionResourceType(AWSProperty):
    props = {
        'IamRoleArn': (basestring, True),
        'ListOfTags': ([ConditionResourceType], False),
        'Resources': ([basestring], False),
        'SelectionName': (basestring, True),
    }

    def validate(self):
        conds = [
            'ListOfTags',
            'Resources',
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
        'BackupPlanId': (basestring, True),
        'BackupSelection': (BackupSelectionResourceType, True),
    }


class NotificationObjectType(AWSProperty):
    props = {
        'BackupVaultEvents': ([basestring], True),
        'SNSTopicArn': (basestring, True)
    }


class BackupVault(AWSObject):
    resource_type = "AWS::Backup::BackupVault"

    props = {
        'AccessPolicy': (json_checker, False),
        'BackupVaultName': (backup_vault_name, True),
        'BackupVaultTags': (dict, False),
        'EncryptionKeyArn': (basestring, False),
        'Notifications': (NotificationObjectType, False),
    }
