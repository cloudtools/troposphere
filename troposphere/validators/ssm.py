# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import json_checker, s3_bucket_name


def validate_document_content(x):
    """
    Property: Document.Content
    """

    def check_json(x):
        import json

        try:
            json.loads(x)
            return True
        except json.decoder.JSONDecodeError:
            return False

    def check_yaml(x):
        import yaml

        try:
            yaml.safe_load(x)
            return True
        except yaml.composer.ComposerError:
            return False

    if isinstance(x, dict):
        return x

    if check_json(x) or check_yaml(x):
        return x

    raise ValueError("Content must be one of dict or json/yaml string")


def validate_json_checker(x):
    """
    Property: MaintenanceWindowLambdaParameters.Payload
    """
    return json_checker(x)


def compliance_level(level):
    """
    Property: PatchBaseline.ApprovedPatchesComplianceLevel
    Property: Rule.ComplianceLevel
    """

    valid_levels = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"]
    if level not in valid_levels:
        raise ValueError(
            'ApprovedPatchesComplianceLevel must be one of: "%s"'
            % (", ".join(valid_levels))
        )
    return level


def notification_event(events):
    """
    Property: NotificationConfig.NotificationEvents
    """

    valid_events = ["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
    for event in events:
        if event not in valid_events:
            raise ValueError(
                'NotificationEvents must be at least one of: "%s"'
                % (", ".join(valid_events))
            )
    return events


def notification_type(notification):
    """
    Property: NotificationConfig.NotificationType
    """

    valid_notifications = ["Command", "Invocation"]
    if notification not in valid_notifications:
        raise ValueError(
            'NotificationType must be one of: "%s"' % (", ".join(valid_notifications))
        )
    return notification


def operating_system(os):
    """
    Property: PatchBaseline.OperatingSystem
    """

    valid_os = [
        "AMAZON_LINUX",
        "AMAZON_LINUX_2",
        "CENTOS",
        "DEBIAN",
        "MACOS",
        "ORACLE_LINUX",
        "RASPBIAN",
        "REDHAT_ENTERPRISE_LINUX",
        "ROCKY_LINUX",
        "SUSE",
        "UBUNTU",
        "WINDOWS",
    ]
    if os not in valid_os:
        raise ValueError('OperatingSystem must be one of: "%s"' % (", ".join(valid_os)))
    return os


def validate_s3_bucket_name(b):
    """
    Property: LoggingInfo.S3Bucket
    Property: MaintenanceWindowRunCommandParameters.OutputS3BucketName
    """

    return s3_bucket_name(b)


def task_type(task):
    """
    Property: MaintenanceWindowTask.TaskType
    """

    valid_tasks = ["RUN_COMMAND", "AUTOMATION", "LAMBDA", "STEP_FUNCTION"]
    if task not in valid_tasks:
        raise ValueError('TaskType must be one of: "%s"' % (", ".join(valid_tasks)))
    return task
