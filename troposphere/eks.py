# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import (boolean, double)


class Addon(AWSObject):
    resource_type = "AWS::EKS::Addon"

    props = {
        'AddonName': (str, True),
        'AddonVersion': (str, False),
        'ClusterName': (str, True),
        'ResolveConflicts': (str, False),
        'ServiceAccountRoleArn': (str, False),
        'Tags': (Tags, False),
    }


class LogSetup(AWSProperty):
    props = {
        'Enable': (bool, False),
        'Types': ([str], False)
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
        'KeyArn': (str, False),
    }


class EncryptionConfig(AWSProperty):
    props = {
        'Provider': (Provider, False),
        'Resources': ([str], False),
    }


class KubernetesNetworkConfig(AWSProperty):
    props = {
        'ServiceIpv4Cidr': (str, False),
    }


class ResourcesVpcConfig(AWSProperty):
    props = {
        'SecurityGroupIds': ([str], False),
        'SubnetIds': ([str], True),
    }


class Cluster(AWSObject):
    resource_type = "AWS::EKS::Cluster"

    props = {
        'EncryptionConfig': ([EncryptionConfig], False),
        'KubernetesNetworkConfig': (KubernetesNetworkConfig, False),
        'Name': (str, False),
        'Logging': (Logging, False),
        'ResourcesVpcConfig': (ResourcesVpcConfig, True),
        'RoleArn': (str, True),
        'Version': (str, False),
    }


class Label(AWSProperty):
    props = {
        'Key': (str, True),
        'Value': (str, True),
    }


class Selector(AWSProperty):
    props = {
        'Labels': ([Label], False),
        'Namespace': (str, True),
    }


class FargateProfile(AWSObject):
    resource_type = "AWS::EKS::FargateProfile"

    props = {
        'ClusterName': (str, True),
        'FargateProfileName': (str, False),
        'PodExecutionRoleArn': (str, True),
        'Selectors': ([Selector], True),
        'Subnets': ([str], False),
        'Tags': (Tags, False),
    }


class RemoteAccess(AWSProperty):
    props = {
        'Ec2SshKey': (str, True),
        'SourceSecurityGroups': ([str], False),
    }


class ScalingConfig(AWSProperty):
    props = {
        'DesiredSize': (double, False),
        'MaxSize': (double, False),
        'MinSize': (double, False),
    }


class LaunchTemplateSpecification(AWSProperty):
    props = {
        'Id': (str, False),
        'Name': (str, False),
        'Version': (str, False),
    }


class Nodegroup(AWSObject):
    resource_type = "AWS::EKS::Nodegroup"

    props = {
        'AmiType': (str, False),
        'CapacityType': (str, False),
        'ClusterName': (str, True),
        'DiskSize': (double, False),
        'ForceUpdateEnabled': (boolean, False),
        'InstanceTypes': ([str], False),
        'Labels': (dict, False),
        'LaunchTemplate': (LaunchTemplateSpecification, False),
        'NodegroupName': (str, False),
        'NodeRole': (str, True),
        'ReleaseVersion': (str, False),
        'RemoteAccess': (RemoteAccess, False),
        'ScalingConfig': (ScalingConfig, False),
        'Subnets': ([str], False),
        'Tags': (dict, False),
        'Version': (str, False),
    }
