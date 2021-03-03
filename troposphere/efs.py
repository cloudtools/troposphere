from . import AWSObject, AWSProperty, Tags
from .validators import boolean, one_of

Bursting = 'bursting'
Provisioned = 'provisioned'


def throughput_mode_validator(mode):
    valid_modes = [Bursting, Provisioned]
    if mode not in valid_modes:
        raise ValueError(
            'ThroughputMode must be one of: "%s"' % (', '.join(valid_modes))
        )
    return mode


def provisioned_throughput_validator(throughput):
    if throughput < 0.0:
        raise ValueError(
            'ProvisionedThroughputInMibps must be greater than or equal to 0.0'
        )
    return throughput


class PosixUser(AWSProperty):
    props = {
        'Gid': (basestring, True),
        'SecondaryGids': ([basestring], False),
        'Uid': (basestring, True),
    }


class CreationInfo(AWSProperty):
    props = {
        'OwnerGid': (basestring, True),
        'OwnerUid': (basestring, True),
        'Permissions': (basestring, True),
    }


class RootDirectory(AWSProperty):
    props = {
        'CreationInfo': (CreationInfo, False),
        'Path': (basestring, False),
    }


class AccessPoint(AWSObject):
    resource_type = "AWS::EFS::AccessPoint"

    props = {
        'AccessPointTags': (Tags, False),
        'ClientToken': (basestring, False),
        'FileSystemId': (basestring, True),
        'PosixUser': (PosixUser, False),
        'RootDirectory': (RootDirectory, False),
    }


class LifecyclePolicy(AWSProperty):
    props = {
        'TransitionToIA': (basestring, True),
    }


class BackupPolicy(AWSProperty):
    props = {
        'Status': (basestring, True),
    }

    def validate(self):
        conds = [
            'DISABLED',
            'DISABLING',
            'ENABLED',
            'ENABLING'
        ]
        one_of(self.__class__.__name__, self.properties, 'Status', conds)


class FileSystem(AWSObject):
    resource_type = "AWS::EFS::FileSystem"

    props = {
        'BackupPolicy': (BackupPolicy, False),
        'Encrypted': (boolean, False),
        'FileSystemPolicy': (dict, False),
        'FileSystemTags': (Tags, False),
        'KmsKeyId': (basestring, False),
        'LifecyclePolicies': ([LifecyclePolicy], False),
        'PerformanceMode': (basestring, False),
        'ProvisionedThroughputInMibps': (float, False),
        'ThroughputMode': (throughput_mode_validator, False),
    }


class MountTarget(AWSObject):
    resource_type = "AWS::EFS::MountTarget"

    props = {
        'FileSystemId': (basestring, True),
        'IpAddress': (basestring, False),
        'SecurityGroups': ([basestring], True),
        'SubnetId': (basestring, True),
    }
