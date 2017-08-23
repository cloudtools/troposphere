from . import AWSObject, Tags
from .validators import boolean


class FileSystem(AWSObject):
    resource_type = "AWS::EFS::FileSystem"

    props = {
        'Encrypted': (boolean, False),
        'FileSystemTags': (Tags, False),
        'KmsKeyId': (basestring, False),
        'PerformanceMode': (basestring, False),
    }


class MountTarget(AWSObject):
    resource_type = "AWS::EFS::MountTarget"

    props = {
        'FileSystemId': (basestring, True),
        'IpAddress': (basestring, False),
        'SecurityGroups': ([basestring], True),
        'SubnetId': (basestring, True),
    }
