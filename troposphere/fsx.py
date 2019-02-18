# Copyright (c) 2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer


class LustreConfiguration(AWSProperty):
    props = {
        'ExportPath': (basestring, False),
        'ImportedFileChunkSize': (integer, False),
        'ImportPath': (basestring, False),
        'WeeklyMaintenanceStartTime': (basestring, False),

    }


class WindowsConfiguration(AWSProperty):
    props = {
        'ActiveDirectoryId': (basestring, False),
        'AutomaticBackupRetentionDays': (integer, False),
        'CopyTagsToBackups': (boolean, False),
        'DailyAutomaticBackupStartTime': (basestring, False),
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
        'SubnetIds': ([basestring], False),
        'Tags': (Tags, False),
        'WindowsConfiguration': (WindowsConfiguration, False),
    }
