# Copyright (c) 2012-2013, Antonio Alonso Dominguez <alonso.domin@gmail.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, AWSHelperFn
from .validators import (boolean, integer, positive_integer)


class KeyValue(AWSHelperFn):
    def __init__(self, key, value):
        self.data = {'Key': key, 'Value': value}

    def JSONrepr(self):
        return self.data


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
        'Args': (list, False),
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
        if not isinstance(v, basestring):
            raise ValueError('ConfigurationProperties values must be strings')

    return xs


def configurations_validator(xs):
    if not isinstance(xs, list):
        raise ValueError("Configurations must be a list of "
                         "Configuration objects.")
    for x in xs:
        if not isinstance(x, Configuration):
            raise ValueError("Configuration '%s' must be of "
                             "Configuration type" % x)
    return xs


class Configuration(AWSProperty):
    props = {
        'Classification': (basestring, False),
        'ConfigurationProperties': (properties_validator, False),
        'Configurations': (configurations_validator, False)
    }


def market_validator(x):
    valid_values = ['ON_DEMAND', 'SPOT']
    if x not in valid_values:
        raise ValueError("Market must be one of: %s" %
                         ', '.join(valid_values))
    return x


class InstanceGroupConfigProperty(AWSProperty):
    props = {
        'BidPrice': (basestring, False),
        'Configurations': (configurations_validator, False),
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
        'Configurations': (configurations_validator, False),
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
        'Configurations': (configurations_validator, False),
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
    valid_values = ['CONTINUE', 'CONTINUE_AND_WAIT']
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
