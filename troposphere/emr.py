# Copyright (c) 2012-2013, Antonio Alonso Dominguez <alonso.domin@gmail.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, AWSHelperFn
from .validators import (boolean, integer, positive_integer)


class KeyValue(AWSProperty):
    props = {
        'Key': (basestring, True),
        'Value': (basestring, True)
    }

    def __init__(self, key=None, value=None, **kwargs):
        # provided for backward compatibility
        if key is not None:
            kwargs['Key'] = key
        if value is not None:
            kwargs['Value'] = value
        super(KeyValue, self).__init__(**kwargs)


def additional_info_validator(xs):
    if not isinstance(xs, dict):
        raise ValueError("AdditionalInfo must be a dict of "
                         "string to string pairs")
    for k, v in xs.iteritems():
        if not isinstance(k, basestring):
            raise ValueError('AdditionalInfo keys must be strings')
        if not isinstance(v, basestring):
            raise ValueError('AdditionalInfo values must be strings')

    return xs


class Application(AWSProperty):
    props = {
        'AdditionalInfo': (additional_info_validator, False),
        'Args': ([basestring], False),
        'Name': (basestring, False),
        'Version': (basestring, False)
    }


class ScriptBootstrapActionConfig(AWSProperty):
    props = {
        'Args': ([basestring], False),
        'Path': (basestring, True)
    }


class BootstrapActionConfig(AWSProperty):
    props = {
        'Name': (basestring, True),
        'ScriptBootstrapAction': (ScriptBootstrapActionConfig, True)
    }


def properties_validator(xs):
    if not isinstance(xs, dict):
        raise ValueError("ConfigurationProperties must be a dict of "
                         "string to string pairs")
    for k, v in xs.iteritems():
        if not isinstance(k, basestring):
            raise ValueError('ConfigurationProperties keys must be strings')
        if not isinstance(v, basestring) and not isinstance(v, AWSHelperFn):
            raise ValueError('ConfigurationProperties values must be strings'
                             ' or helper functions')

    return xs


class Configuration(AWSProperty):
    props = {
        'Classification': (basestring, False),
        'ConfigurationProperties': (properties_validator, False)
    }
# we must define this one afterwards since Configuration does not exist
# before Configuration is done initializing
Configuration.props['Configurations'] = ([Configuration], False)


def market_validator(x):
    valid_values = ['ON_DEMAND', 'SPOT']
    if x not in valid_values:
        raise ValueError("Market must be one of: %s" %
                         ', '.join(valid_values))
    return x


def volume_type_validator(x):
    valid_values = ['standard', 'io1', 'gp2']
    if x not in valid_values:
        raise ValueError("VolumeType must be one of: %s" %
                         ', '.join(valid_values))
    return x


class VolumeSpecification(AWSProperty):
    props = {
        'Iops': (integer, False),
        'SizeInGB': (integer, True),
        'VolumeType': (volume_type_validator, True)
    }


class EbsBlockDeviceConfigs(AWSProperty):
    props = {
        'VolumeSpecification': (VolumeSpecification, True),
        'VolumesPerInstance': (integer, False)
    }


class EbsConfiguration(AWSProperty):
    props = {
        'EbsBlockDeviceConfigs': ([EbsBlockDeviceConfigs], False),
        'EbsOptimized': (boolean, False)
    }


class InstanceGroupConfigProperty(AWSProperty):
    props = {
        'BidPrice': (basestring, False),
        'Configurations': ([Configuration], False),
        'EbsConfiguration': (EbsConfiguration, False),
        'InstanceCount': (positive_integer, True),
        'InstanceType': (basestring, True),
        'Market': (market_validator, False),
        'Name': (basestring, False)
    }


class PlacementType(AWSProperty):
    props = {
        'AvailabilityZone': (basestring, True)
    }


class JobFlowInstancesConfig(AWSProperty):
    props = {
        'AdditionalMasterSecurityGroups': ([basestring], False),
        'AdditionalSlaveSecurityGroups': ([basestring], False),
        'CoreInstanceGroup': (InstanceGroupConfigProperty, True),
        'Ec2KeyName': (basestring, False),
        'Ec2SubnetId': (basestring, False),
        'EmrManagedMasterSecurityGroup': (basestring, False),
        'EmrManagedSlaveSecurityGroup': (basestring, False),
        'HadoopVersion': (basestring, False),
        'MasterInstanceGroup': (InstanceGroupConfigProperty, True),
        'Placement': (PlacementType, False),
        'ServiceAccessSecurityGroup': (basestring, False),
        'TerminationProtected': (boolean, False)
    }


class Cluster(AWSObject):
    resource_type = "AWS::EMR::Cluster"

    props = {
        'AdditionalInfo': (dict, False),
        'Applications': ([Application], False),
        'BootstrapActions': ([BootstrapActionConfig], False),
        'Configurations': ([Configuration], False),
        'Instances': (JobFlowInstancesConfig, True),
        'JobFlowRole': (basestring, True),
        'LogUri': (basestring, False),
        'Name': (basestring, True),
        'ReleaseLabel': (basestring, False),
        'ServiceRole': (basestring, True),
        'Tags': (list, False),
        'VisibleToAllUsers': (boolean, False)
    }


class InstanceGroupConfig(AWSObject):
    resource_type = "AWS::EMR::InstanceGroupConfig"

    props = {
        'BidPrice': (basestring, False),
        'Configurations': ([Configuration], False),
        'EbsConfiguration': (EbsConfiguration, False),
        'InstanceCount': (integer, True),
        'InstanceRole': (basestring, True),
        'InstanceType': (basestring, True),
        'Market': (market_validator, False),
        'Name': (basestring, False)
    }


class HadoopJarStepConfig(AWSProperty):
    props = {
        'Args': ([basestring], False),
        'Jar': (basestring, True),
        'MainClass': (basestring, False),
        'StepProperties': ([KeyValue], False)
    }


def action_on_failure_validator(x):
    valid_values = ['CONTINUE', 'CANCEL_AND_WAIT']
    if x not in valid_values:
        raise ValueError("ActionOnFailure must be one of: %s" %
                         ', '.join(valid_values))
    return x


class Step(AWSObject):
    resource_type = "AWS::EMR::Step"

    props = {
        'ActionOnFailure': (action_on_failure_validator, True),
        'HadoopJarStep': (HadoopJarStepConfig, True),
        'JobFlowId': (basestring, True),
        'Name': (basestring, True)
    }
