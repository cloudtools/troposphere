from . import AWSObject


class FileSystem(AWSObject):
    resource_type = "AWS::EFS::FileSystem"

    props = {
        'FileSystemTags': (list, False),
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
