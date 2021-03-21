# Copyright (c) 2014, Yuta Okamoto <okapies@gmail.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer, mutually_exclusive


class Source(AWSProperty):
    props = {
        'Password': (str, False),
        'Revision': (str, False),
        'SshKey': (str, False),
        'Type': (str, False),
        'Url': (str, False),
        'Username': (str, False),
    }


class SslConfiguration(AWSProperty):
    props = {
        'Certificate': (str, True),
        'Chain': (str, False),
        'PrivateKey': (str, True),
    }


class ChefConfiguration(AWSProperty):
    props = {
        'BerkshelfVersion': (str, False),
        'ManageBerkshelf': (boolean, False),
    }


class Recipes(AWSProperty):
    props = {
        'Configure': ([str], False),
        'Deploy': ([str], False),
        'Setup': ([str], False),
        'Shutdown': ([str], False),
        'Undeploy': ([str], False),
    }


def validate_volume_type(volume_type):
    volume_types = ('standard', 'io1', 'gp2')
    if volume_type not in volume_types:
        raise ValueError("VolumeType (given: %s) must be one of: %s" % (
            volume_type, ', '.join(volume_types)))
    return volume_type


class VolumeConfiguration(AWSProperty):
    props = {
        'Encrypted': (boolean, False),
        'Iops': (integer, False),
        'MountPoint': (str, True),
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
        'Name': (str, False),
        'Version': (str, False),
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
        'Key': (str, True),
        'Secure': (bool, False),
        'Value': (str, True),
    }


class LoadBasedAutoScaling(AWSProperty):
    props = {
        'DownScaling': (AutoScalingThresholds, False),
        'Enable': (bool, False),
        'UpScaling': (AutoScalingThresholds, False),
    }


def validate_data_source_type(data_source_type):
    data_source_types = (
        'AutoSelectOpsworksMysqlInstance',
        'OpsworksMysqlInstance',
        'RdsDbInstance'
    )
    if data_source_type not in data_source_types:
        raise ValueError("Type (given: %s) must be one of: %s" % (
            data_source_type, ', '.join(data_source_types)))
    return data_source_type


class DataSource(AWSProperty):
    props = {
        'Arn': (str, False),
        'DatabaseName': (str, False),
        'Type': (validate_data_source_type, False)
    }


class App(AWSObject):
    resource_type = "AWS::OpsWorks::App"

    props = {
        'AppSource': (Source, False),
        'Attributes': (dict, False),
        'DataSources': ([DataSource], False),
        'Description': (str, False),
        'Domains': ([str], False),
        'EnableSsl': (boolean, False),
        'Environment': ([Environment], False),
        'Name': (str, True),
        'Shortname': (str, False),
        'SslConfiguration': (SslConfiguration, False),
        'StackId': (str, True),
        'Type': (str, True),
    }


class ElasticLoadBalancerAttachment(AWSObject):
    resource_type = "AWS::OpsWorks::ElasticLoadBalancerAttachment"

    props = {
        'ElasticLoadBalancerName': (str, True),
        'LayerId': (str, True),
        'Tags': ((Tags, list), False),
    }


class EbsBlockDevice(AWSProperty):
    props = {
        'DeleteOnTermination': (boolean, False),
        'Iops': (integer, False),
        'SnapshotId': (str, False),
        'VolumeSize': (integer, False),
        'VolumeType': (str, False),
    }


class BlockDeviceMapping(AWSProperty):
    props = {
        'DeviceName': (str, False),
        'Ebs': (EbsBlockDevice, False),
        'NoDevice': (str, False),
        'VirtualName': (str, False),
    }

    def validate(self):
        conds = [
            'Ebs',
            'VirtualName',
        ]
        mutually_exclusive(self.__class__.__name__, self.properties, conds)


class Instance(AWSObject):
    resource_type = "AWS::OpsWorks::Instance"

    props = {
        'AgentVersion': (str, False),
        'AmiId': (str, False),
        'Architecture': (str, False),
        'AutoScalingType': (str, False),
        'AvailabilityZone': (str, False),
        'BlockDeviceMappings': ([BlockDeviceMapping], False),
        'EbsOptimized': (boolean, False),
        'ElasticIps': ([str], False),
        'Hostname': (str, False),
        'InstallUpdatesOnBoot': (boolean, False),
        'InstanceType': (str, True),
        'LayerIds': ([str], True),
        'Os': (str, False),
        'RootDeviceType': (str, False),
        'SshKeyName': (str, False),
        'StackId': (str, True),
        'SubnetId': (str, False),
        'Tenancy': (str, False),
        'TimeBasedAutoScaling': (TimeBasedAutoScaling, False),
        'VirtualizationType': (str, False),
        'Volumes': ([str], False),
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
        'CustomInstanceProfileArn': (str, False),
        'CustomJson': ((str, dict), False),
        'CustomRecipes': (Recipes, False),
        'CustomSecurityGroupIds': ([str], False),
        'EnableAutoHealing': (boolean, True),
        'InstallUpdatesOnBoot': (boolean, False),
        'LifecycleEventConfiguration': (LifeCycleConfiguration, False),
        'LoadBasedAutoScaling': (LoadBasedAutoScaling, False),
        'Name': (str, True),
        'Packages': ([str], False),
        'Shortname': (str, True),
        'StackId': (str, True),
        'Type': (str, True),
        'VolumeConfigurations': ([VolumeConfiguration], False),
    }


class RdsDbInstance(AWSProperty):
    props = {
        'DbPassword': (str, True),
        'DbUser': (str, True),
        'RdsDbInstanceArn': (str, True)
    }


class ElasticIp(AWSProperty):
    props = {
        'Ip': (str, True),
        'Name': (str, False),
    }


class Stack(AWSObject):
    resource_type = "AWS::OpsWorks::Stack"

    props = {
        'AgentVersion': (str, False),
        'Attributes': (dict, False),
        'ChefConfiguration': (ChefConfiguration, False),
        'CloneAppIds': ([str], False),
        'ClonePermissions': (boolean, False),
        'ConfigurationManager': (StackConfigurationManager, False),
        'CustomCookbooksSource': (Source, False),
        'CustomJson': ((str, dict), False),
        'DefaultAvailabilityZone': (str, False),
        'DefaultInstanceProfileArn': (str, True),
        'DefaultOs': (str, False),
        'DefaultRootDeviceType': (str, False),
        'DefaultSshKeyName': (str, False),
        'DefaultSubnetId': (str, False),
        'EcsClusterArn': (str, False),
        'ElasticIps': ([ElasticIp], False),
        'HostnameTheme': (str, False),
        'Name': (str, True),
        'RdsDbInstances': ([RdsDbInstance], False),
        'ServiceRoleArn': (str, True),
        'SourceStackId': (str, False),
        'Tags': ((Tags, list), False),
        'UseCustomCookbooks': (boolean, False),
        'UseOpsworksSecurityGroups': (boolean, False),
        'VpcId': (str, False),
    }

    def validate(self):
        if 'VpcId' in self.properties and \
           'DefaultSubnetId' not in self.properties:
            raise ValueError('Using VpcId requires DefaultSubnetId to be'
                             'specified')
        return True


class UserProfile(AWSObject):
    resource_type = "AWS::OpsWorks::UserProfile"

    props = {
        'AllowSelfManagement': (boolean, False),
        'IamUserArn': (str, True),
        'SshPublicKey': (str, False),
        'SshUsername': (str, False),
    }


class Volume(AWSObject):
    resource_type = "AWS::OpsWorks::Volume"

    props = {
        'Ec2VolumeId': (str, True),
        'MountPoint': (str, False),
        'Name': (str, False),
        'StackId': (str, True),
    }


class EngineAttribute(AWSProperty):
    props = {
        'Name': (str, False),
        'Value': (str, False),
    }


class Server(AWSObject):
    resource_type = "AWS::OpsWorksCM::Server"

    props = {
        'AssociatePublicIpAddress': (boolean, False),
        'BackupId': (str, False),
        'BackupRetentionCount': (integer, False),
        'CustomCertificate': (str, False),
        'CustomDomain': (str, False),
        'CustomPrivateKey': (str, False),
        'DisableAutomatedBackup': (boolean, False),
        'Engine': (str, False),
        'EngineAttributes': ([EngineAttribute], False),
        'EngineModel': (str, False),
        'EngineVersion': (str, False),
        'InstanceProfileArn': (str, True),
        'InstanceType': (str, True),
        'KeyPair': (str, False),
        'PreferredBackupWindow': (str, False),
        'PreferredMaintenanceWindow': (str, False),
        'SecurityGroupIds': ([str], False),
        'ServerName': (str, False),
        'ServiceRoleArn': (str, True),
        'SubnetIds': ([str], False),
        'Tags': ((Tags, list), False),
    }
