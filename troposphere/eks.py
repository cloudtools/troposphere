# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
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


class Provider(AWSProperty):
    props = {
        'KeyArn': (basestring, False),
    }


class EncryptionConfig(AWSProperty):
    props = {
        'Provider': (Provider, False),
        'Resources': ([basestring], False),
    }


class KubernetesNetworkConfig(AWSProperty):
    props = {
        'ServiceIpv4Cidr': (basestring, False),
    }


class ResourcesVpcConfig(AWSProperty):
    props = {
        'SecurityGroupIds': ([basestring], False),
        'SubnetIds': ([basestring], True),
    }


class Cluster(AWSObject):
    resource_type = "AWS::EKS::Cluster"

    props = {
        'EncryptionConfig': ([EncryptionConfig], False),
        'KubernetesNetworkConfig': (KubernetesNetworkConfig, False),
        'Name': (basestring, False),
        'Logging': (Logging, False),
        'ResourcesVpcConfig': (ResourcesVpcConfig, True),
        'RoleArn': (basestring, True),
        'Version': (basestring, False),
    }


class Label(AWSProperty):
    props = {
        'Key': (basestring, True),
        'Value': (basestring, True),
    }


class Selector(AWSProperty):
    props = {
        'Labels': ([Label], False),
        'Namespace': (basestring, True),
    }


class FargateProfile(AWSObject):
    resource_type = "AWS::EKS::FargateProfile"

    props = {
        'ClusterName': (basestring, True),
        'FargateProfileName': (basestring, False),
        'PodExecutionRoleArn': (basestring, True),
        'Selectors': ([Selector], True),
        'Subnets': ([basestring], False),
        'Tags': (Tags, False),
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


class LaunchTemplateSpecification(AWSProperty):
    props = {
        'Id': (basestring, False),
        'Name': (basestring, False),
        'Version': (basestring, False),
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
        'LaunchTemplate': (LaunchTemplateSpecification, False),
        'NodegroupName': (basestring, False),
        'NodeRole': (basestring, True),
        'ReleaseVersion': (basestring, False),
        'RemoteAccess': (RemoteAccess, False),
        'ScalingConfig': (ScalingConfig, False),
        'Subnets': ([basestring], False),
        'Tags': (dict, False),
        'Version': (basestring, False),
    }
