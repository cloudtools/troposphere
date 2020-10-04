# Copyright (c) 2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer, storage_type


VALID_LUSTRECONFIGURATION_DEPLOYMENTTYPE = ('PERSISTENT_1', 'SCRATCH_1',
                                            'SCRATCH_2')


VALID_LUSTRECONFIGURATION_PERUNITSTORAGETHROUGHPUT = (50, 100, 200)


def validate_lustreconfiguration_deploymenttype(lustreconfiguration_deploymenttype):  # NOQA
    """Validate DeploymentType for LustreConfiguration"""

    if lustreconfiguration_deploymenttype not in VALID_LUSTRECONFIGURATION_DEPLOYMENTTYPE:  # NOQA
        raise ValueError("LustreConfiguration DeploymentType must be one of: %s" %  # NOQA
                         ", ".join(VALID_LUSTRECONFIGURATION_DEPLOYMENTTYPE))
    return lustreconfiguration_deploymenttype


def validate_lustreconfiguration_perunitstoragethroughput(lustreconfiguration_perunitstoragethroughput):  # NOQA
    """Validate PerUnitStorageThroughput for LustreConfiguration"""

    if lustreconfiguration_perunitstoragethroughput not in VALID_LUSTRECONFIGURATION_PERUNITSTORAGETHROUGHPUT:  # NOQA
        raise ValueError("LustreConfiguration PerUnitStorageThroughput must be one of: %s" %  # NOQA
                         ", ".join(VALID_LUSTRECONFIGURATION_PERUNITSTORAGETHROUGHPUT))  # NOQA
    return lustreconfiguration_perunitstoragethroughput


class LustreConfiguration(AWSProperty):
    props = {
        'AutoImportPolicy': (basestring, False),
        'AutomaticBackupRetentionDays': (integer, False),
        'CopyTagsToBackups': (boolean, False),
        'DailyAutomaticBackupStartTime': (basestring, False),
        'DeploymentType': (validate_lustreconfiguration_deploymenttype, False),
        'DriveCacheType': (basestring, False),
        'ExportPath': (basestring, False),
        'ImportedFileChunkSize': (integer, False),
        'ImportPath': (basestring, False),
        'PerUnitStorageThroughput': (validate_lustreconfiguration_perunitstoragethroughput, False),  # NOQA
        'WeeklyMaintenanceStartTime': (basestring, False),
    }


class SelfManagedActiveDirectoryConfiguration(AWSProperty):
    props = {
        'DnsIps': ([basestring], False),
        'DomainName': (basestring, False),
        'FileSystemAdministratorsGroup': (basestring, False),
        'OrganizationalUnitDistinguishedName': (basestring, False),
        'Password': (basestring, False),
        'UserName': (basestring, False),
    }


class WindowsConfiguration(AWSProperty):
    props = {
        'ActiveDirectoryId': (basestring, False),
        'AutomaticBackupRetentionDays': (integer, False),
        'CopyTagsToBackups': (boolean, False),
        'DailyAutomaticBackupStartTime': (basestring, False),
        'DeploymentType': (basestring, False),
        'PreferredSubnetId': (basestring, False),
        'SelfManagedActiveDirectoryConfiguration':
            (SelfManagedActiveDirectoryConfiguration, False),
        'ThroughputCapacity': (integer, False),
        'WeeklyMaintenanceStartTime': (basestring, False),
    }


class FileSystem(AWSObject):
    resource_type = 'AWS::FSx::FileSystem'

    props = {
        'BackupId': (basestring, False),
        'FileSystemType': (basestring, False),
        'KmsKeyId': (basestring, False),
        'LustreConfiguration': (LustreConfiguration, False),
        'SecurityGroupIds': ([basestring], False),
        'StorageCapacity': (integer, False),
        'StorageType': (storage_type, False),
        'SubnetIds': ([basestring], False),
        'Tags': (Tags, False),
        'WindowsConfiguration': (WindowsConfiguration, False),
    }
