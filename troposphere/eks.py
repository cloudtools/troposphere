# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import (boolean, double)


class LogSetup(AWSProperty):
    props = {
        'Enable': (bool, False),
        'Types': ([basestring], False)
        }

    def validate(self):
        types = set(self.properties.get('Types'))
        conditionals = ['api', 'audit', 'authenticator', 'controllerManager',
                        'scheduler']
        if not (types.issubset(conditionals)):
            raise ValueError(
                '%s must be one of: %s' % (', '.join(types),
                                           ', '.join(conditionals)))


class Logging(AWSProperty):
    props = {
        'ClusterLogging': ([LogSetup], False)
    }


class ResourcesVpcConfig(AWSProperty):
    props = {
        'SecurityGroupIds': ([basestring], False),
        'SubnetIds': ([basestring], True),
    }


class Provider(AWSProperty):
    props = {
        'KeyArn': (basestring, False),
    }


class EncryptionConfig(AWSProperty):
    props = {
        'Provider': (Provider, False),
        'Resources': ([basestring], False),
    }


class Cluster(AWSObject):
    resource_type = "AWS::EKS::Cluster"

    props = {
        'EncryptionConfig': ([EncryptionConfig], False),
        'Name': (basestring, False),
        'Logging': (Logging, False),
        'ResourcesVpcConfig': (ResourcesVpcConfig, True),
        'RoleArn': (basestring, True),
        'Version': (basestring, False),
    }


class RemoteAccess(AWSProperty):
    props = {
        'Ec2SshKey': (basestring, True),
        'SourceSecurityGroups': ([basestring], False),
    }


class ScalingConfig(AWSProperty):
    props = {
        'DesiredSize': (double, False),
        'MaxSize': (double, False),
        'MinSize': (double, False),
    }


class Nodegroup(AWSObject):
    resource_type = "AWS::EKS::Nodegroup"

    props = {
        'AmiType': (basestring, False),
        'ClusterName': (basestring, True),
        'DiskSize': (double, False),
        'ForceUpdateEnabled': (boolean, False),
        'InstanceTypes': ([basestring], False),
        'Labels': (dict, False),
        'NodegroupName': (basestring, False),
        'NodeRole': (basestring, True),
        'ReleaseVersion': (basestring, False),
        'RemoteAccess': (RemoteAccess, False),
        'ScalingConfig': (ScalingConfig, False),
        'Subnets': ([basestring], False),
        'Tags': (dict, False),
        'Version': (basestring, False),
    }
