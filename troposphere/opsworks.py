# Copyright (c) 2014, Yuta Okamoto <okapies@gmail.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Ref
from .validators import boolean, integer


class Source(AWSProperty):
    props = {
        'Password': (basestring, False),
        'Revision': (basestring, False),
        'SshKey': (basestring, False),
        'Type': (basestring, False),
        'Url': (basestring, False),
        'Username': (basestring, False),
    }


class SslConfiguration(AWSProperty):
    props = {
        'Certificate': (basestring, True),
        'Chain': (basestring, False),
        'PrivateKey': (basestring, True),
    }


class ChefConfiguration(AWSProperty):
    props = {
        'BerkshelfVersion': (basestring, False),
        'ManageBerkshelf': (boolean, False),
    }


class Recipes(AWSProperty):
    props = {
        'Configure': ([basestring], False),
        'Deploy': ([basestring], False),
        'Setup': ([basestring], False),
        'Shutdown': ([basestring], False),
        'Undeploy': ([basestring], False),
    }


def validate_volume_type(volume_type):
    volume_types = ('standard', 'io1', 'gp2')
    if volume_type not in volume_types:
        raise ValueError("VolumeType (given: %s) must be one of: %s" % (
            volume_type, ', '.join(volume_types)))
    return volume_type


class VolumeConfiguration(AWSProperty):
    props = {
        'Iops': (integer, False),
        'MountPoint': (basestring, True),
        'NumberOfDisks': (integer, True),
        'RaidLevel': (integer, False),
        'Size': (integer, True),
        'VolumeType': (validate_volume_type, False)
    }

    def validate(self):
        volume_type = self.properties.get('VolumeType')
        iops = self.properties.get('Iops')
        if volume_type == 'io1' and not iops:
            raise ValueError("Must specify Iops if VolumeType is 'io1'.")
        if volume_type != 'io1' and iops:
            raise ValueError("Cannot specify Iops if VolumeType is not 'io1'.")


class StackConfigurationManager(AWSProperty):
    props = {
        'Name': (basestring, False),
        'Version': (basestring, False),
    }


class TimeBasedAutoScaling(AWSProperty):
    props = {
        'Monday': (dict, False),
        'Tuesday': (dict, False),
        'Wednesday': (dict, False),
        'Thursday': (dict, False),
        'Friday': (dict, False),
        'Saturday': (dict, False),
        'Sunday': (dict, False),
    }


class AutoScalingThresholds(AWSProperty):
    props = {
        'CpuThreshold': (float, False),
        'IgnoreMetricsTime': (integer, False),
        'InstanceCount': (integer, False),
        'LoadThreshold': (float, False),
        'MemoryThreshold': (float, False),
        'ThresholdsWaitTime': (integer, False),
    }


class Environment(AWSProperty):
    props = {
        'Key': (basestring, True),
        'Secure': (bool, False),
        'Value': (basestring, True),
    }


class LoadBasedAutoScaling(AWSProperty):
    props = {
        'DownScaling': (AutoScalingThresholds, False),
        'Enable': (bool, False),
        'UpScaling': (AutoScalingThresholds, False),
    }


class App(AWSObject):
    resource_type = "AWS::OpsWorks::App"

    props = {
        'AppSource': (Source, False),
        'Attributes': (dict, False),
        'Description': (basestring, False),
        'Domains': ([basestring], False),
        'EnableSsl': (boolean, False),
        'Environment': ([Environment], False),
        'Name': (basestring, True),
        'Shortname': (basestring, False),
        'SslConfiguration': (SslConfiguration, False),
        'StackId': (basestring, True),
        'Type': (basestring, True),
    }


class ElasticLoadBalancerAttachment(AWSObject):
    resource_type = "AWS::OpsWorks::ElasticLoadBalancerAttachment"

    props = {
        'ElasticLoadBalancerName': (basestring, True),
        'LayerId': (basestring, True),
    }


class Instance(AWSObject):
    resource_type = "AWS::OpsWorks::Instance"

    props = {
        'AmiId': (basestring, False),
        'Architecture': (basestring, False),
        'AutoScalingType': (basestring, False),
        'AvailabilityZone': (basestring, False),
        'InstallUpdatesOnBoot': (boolean, False),
        'InstanceType': (basestring, True),
        'LayerIds': ([basestring, Ref], True),
        'Os': (basestring, False),
        'RootDeviceType': (basestring, False),
        'SshKeyName': (basestring, False),
        'StackId': (basestring, True),
        'SubnetId': (basestring, False),
        'TimeBasedAutoScaling': (TimeBasedAutoScaling, False),
    }


class ShutdownEventConfiguration(AWSProperty):
    props = {
        'DelayUntilElbConnectionsDrained': (boolean, False),
        'ExecutionTimeout': (integer, False),
    }


class LifeCycleConfiguration(AWSProperty):
    props = {
        'ShutdownEventConfiguration': (ShutdownEventConfiguration, False),
    }


class Layer(AWSObject):
    resource_type = "AWS::OpsWorks::Layer"

    props = {
        'Attributes': (dict, False),
        'AutoAssignElasticIps': (boolean, True),
        'AutoAssignPublicIps': (boolean, True),
        'CustomInstanceProfileArn': (basestring, False),
        'CustomRecipes': (Recipes, False),
        'CustomSecurityGroupIds': ([basestring, Ref], False),
        'EnableAutoHealing': (boolean, True),
        'InstallUpdatesOnBoot': (boolean, False),
        'LifecycleEventConfiguration': (LifeCycleConfiguration, False),
        'LoadBasedAutoScaling': (LoadBasedAutoScaling, False),
        'Name': (basestring, True),
        'Packages': ([basestring], False),
        'Shortname': (basestring, True),
        'StackId': (basestring, True),
        'Type': (basestring, True),
        'VolumeConfigurations': ([VolumeConfiguration], False),
    }


class Stack(AWSObject):
    resource_type = "AWS::OpsWorks::Stack"

    props = {
        'AgentVersion': (basestring, False),
        'Attributes': (dict, False),
        'ChefConfiguration': (ChefConfiguration, False),
        'ConfigurationManager': (StackConfigurationManager, False),
        'CustomCookbooksSource': (Source, False),
        'CustomJson': (dict, False),
        'DefaultAvailabilityZone': (basestring, False),
        'DefaultInstanceProfileArn': (basestring, True),
        'DefaultOs': (basestring, False),
        'DefaultRootDeviceType': (basestring, False),
        'DefaultSshKeyName': (basestring, False),
        'DefaultSubnetId': (basestring, False),
        'HostnameTheme': (basestring, False),
        'Name': (basestring, True),
        'ServiceRoleArn': (basestring, True),
        'UseCustomCookbooks': (boolean, False),
        'UseOpsworksSecurityGroups': (boolean, False),
        'VpcId': (basestring, False),
    }

    def validate(self):
        if 'VpcId' in self.properties and \
           'DefaultSubnetId' not in self.properties:
            raise ValueError('Using VpcId requires DefaultSubnetId to be'
                             'specified')
        return True
