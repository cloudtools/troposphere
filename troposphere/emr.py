# Copyright (c) 2012-2013, Antonio Alonso Dominguez <alonso.domin@gmail.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, AWSHelperFn
from .validators import (boolean, integer)


class KeyValue(AWSHelperFn):
    def __init__(self, key, value):
        self.data = {'Key': key, 'Value': value}

    def JSONrepr(self):
        return self.data


class Application(AWSProperty):
    props = {
        'AdditionalInfo': (dict, False),
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


class ClusterConfiguration(AWSProperty):
    props = {
        'Classification': (basestring, False),
        'ConfigurationProperties': (dict, False),
        'Configurations': (list, False)
    }


class InstanceGroupConfigProperty(AWSProperty):
    props = {
        'BidPrice': (basestring, False),
        'Configurations': (list, False),
        'InstanceCount': (integer, True),
        'InstanceType': (basestring, True),
        'Market': (basestring, False),
        'Name': (basestring, False)
    }


class PlacementType(AWSProperty):
    props = {
        'AvailabilityZone': (basestring, True)
    }


class JobFlowInstancesConfig(AWSProperty):
    props = {
        'AdditionalMasterSecurityGroups': (list, False),
        'AdditionalSlaveSecurityGroups': (list, False),
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
        'Configurations': ([ClusterConfiguration], False),
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
        'Configurations': (list, False),
        'InstanceCount': (integer, True),
        'InstanceRole': (basestring, True),
        'InstanceType': (basestring, True),
        'Market': (basestring, False),
        'Name': (basestring, False)
    }


class HadoopJarStepConfig(AWSProperty):
    props = {
        'Args': (basestring, False),
        'Jar': (basestring, True),
        'MainClass': (basestring, False)
    }


class Step(AWSObject):
    resource_type = "AWS::EMR::Step"

    props = {
        'ActionOnFailure': (basestring, True),
        'HadoopJarStep': (HadoopJarStepConfig, True),
        'JobFlowId': (basestring, True),
        'Name': (basestring, True),
        'StepProperties': (list, False)
    }
