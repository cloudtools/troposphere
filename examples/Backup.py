from troposphere import Template, backup
from troposphere.iam import Role

template = Template("AWS Backup")
template.set_version()

backup_vault = template.add_resource(
    backup.BackupVault(
        "Vault",
        BackupVaultName="my-backup-vault",
        BackupVaultTags=dict(
            Project="Project",
            Environment="Environment",
            Classifier="Classifier",
        ),
        # EncryptionKeyArn="KmsKeyId",
    )
)

backup_plan = template.add_resource(
    backup.BackupPlan(
        "Backup",
        BackupPlan=backup.BackupPlanResourceType(
            BackupPlanName="BackupPlan",
            BackupPlanRule=[
                backup.BackupRuleResourceType(
                    TargetBackupVault=backup_vault.ref(),
                    Lifecycle=backup.LifecycleResourceType(DeleteAfterDays=31),
                    RecoveryPointTags=dict(
                        Project="Project",
                        Environment="Environment",
                        Classifier="Classifier",
                    ),
                    RuleName="Rule 1",
                    ScheduleExpression="cron(0 0/12 * * ? *)",
                )
            ],
        ),
        BackupPlanTags=dict(
            Project="Project",
            Environment="Environment",
            Classifier="Classifier",
        ),
    )
)

service_role = template.add_resource(
    Role(
        "BackupServiceRole",
        AssumeRolePolicyDocument={
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"Service": ["backup.amazonaws.com"]},
                    "Action": ["sts:AssumeRole"],
                }
            ]
        },
        ManagedPolicyArns=[
            (
                "arn:aws:iam::aws:policy/service-role/"
                "AWSBackupServiceRolePolicyForBackup"
            ),
            (
                "arn:aws:iam::aws:policy/service-role/"
                "AWSBackupServiceRolePolicyForRestores"
            ),
        ],
    )
)

template.add_resource(
    backup.BackupSelection(
        "StorageBackupSelectionByTags",
        BackupSelection=backup.BackupSelectionResourceType(
            IamRoleArn=service_role.get_att("Arn"),
            ListOfTags=[
                backup.ConditionResourceType(
                    ConditionKey="Backup",
                    ConditionType="STRINGEQUALS",
                    ConditionValue="True",
                )
            ],
            SelectionName="MySelection",
        ),
        BackupPlanId=backup_plan.ref(),
    )
)

print(template.to_json())
