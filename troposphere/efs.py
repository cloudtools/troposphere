from . import AWSObject, Tags


class FileSystem(AWSObject):
    resource_type = "AWS::EFS::FileSystem"

    props = {
        'FileSystemTags': (Tags, False),
    }


class MountTarget(AWSObject):
    resource_type = "AWS::EFS::MountTarget"

    props = {
        'FileSystemId': (basestring, True),
        'IpAddress': (basestring, False),
        'SecurityGroups': ([basestring], True),
        'SubnetId': (basestring, True),
    }
