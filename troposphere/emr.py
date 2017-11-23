# Copyright (c) 2012-2013, Antonio Alonso Dominguez <alonso.domin@gmail.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, AWSHelperFn, Tags
from .validators import (
    boolean, integer, positive_integer, floatingpoint, defer
)


CHANGE_IN_CAPACITY = 'CHANGE_IN_CAPACITY'
PERCENT_CHANGE_IN_CAPACITY = 'PERCENT_CHANGE_IN_CAPACITY'
EXACT_CAPACITY = 'EXACT_CAPACITY'


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


MetricDimension = KeyValue


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


class SecurityConfiguration(AWSObject):
    resource_type = "AWS::EMR::SecurityConfiguration"

    props = {
        'Name': (basestring, False),
        'SecurityConfiguration': (dict, True)
    }


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


class ScalingConstraints(AWSProperty):
    props = {
        'MinCapacity': (integer, True),
        'MaxCapacity': (integer, True)
    }


class CloudWatchAlarmDefinition(AWSProperty):
    props = {
        'ComparisonOperator': (basestring, True),
        'Dimensions': ([MetricDimension], False),
        'EvaluationPeriods': (positive_integer, False),
        'MetricName': (basestring, True),
        'Namespace': (basestring, False),
        'Period': (positive_integer, True),
        'Statistic': (basestring, False),
        'Threshold': (positive_integer, True),
        'Unit': (basestring, False),
    }


class ScalingTrigger(AWSProperty):
    props = {
        'CloudWatchAlarmDefinition': (CloudWatchAlarmDefinition, True),
    }


class SimpleScalingPolicyConfiguration(AWSProperty):
    props = {
        'AdjustmentType': (basestring, False),
        'CoolDown': (positive_integer, False),
        'ScalingAdjustment': (defer, True),
    }

    def validate(self):
        if 'AdjustmentType' in self.properties and \
           'ScalingAdjustment' in self.properties:

            valid_values = [
                CHANGE_IN_CAPACITY,
                PERCENT_CHANGE_IN_CAPACITY,
                EXACT_CAPACITY,
            ]

            adjustment_type = self.properties.get('AdjustmentType', None)
            scaling_adjustment = self.properties.get('ScalingAdjustment', None)

            if adjustment_type not in valid_values:
                raise ValueError(
                    'Only CHANGE_IN_CAPACITY, PERCENT_CHANGE_IN_CAPACITY, or'
                    ' EXACT_CAPACITY are valid AdjustmentTypes'
                )

            if adjustment_type == CHANGE_IN_CAPACITY:
                integer(scaling_adjustment)
            elif adjustment_type == PERCENT_CHANGE_IN_CAPACITY:
                floatingpoint(scaling_adjustment)
                f = float(scaling_adjustment)
                if f < 0.0 or f > 1.0:
                    raise ValueError(
                        'ScalingAdjustment value must be between 0.0 and 1.0'
                        ' value was %0.2f' % f
                    )
            elif adjustment_type == EXACT_CAPACITY:
                positive_integer(scaling_adjustment)
            else:
                raise ValueError('ScalingAdjustment value must be'
                                 ' an integer or a float')


class ScalingAction(AWSProperty):
    props = {
        'Market': (market_validator, False),
        'SimpleScalingPolicyConfiguration': (
            SimpleScalingPolicyConfiguration, True
        )
    }


class ScalingRule(AWSProperty):
    props = {
        'Action': (ScalingAction, True),
        'Description': (basestring, False),
        'Name': (basestring, True),
        'Trigger': (ScalingTrigger, True),
    }


class AutoScalingPolicy(AWSProperty):
    props = {
        'Constraints': (ScalingConstraints, True),
        'Rules': ([ScalingRule], False),
    }


class InstanceGroupConfigProperty(AWSProperty):
    props = {
        'AutoScalingPolicy': (AutoScalingPolicy, False),
        'BidPrice': (basestring, False),
        'Configurations': ([Configuration], False),
        'EbsConfiguration': (EbsConfiguration, False),
        'InstanceCount': (positive_integer, True),
        'InstanceType': (basestring, True),
        'Market': (market_validator, False),
        'Name': (basestring, False),
    }


class SpotProvisioningSpecification(AWSProperty):
    props = {
        'BlockDurationMinutes': (positive_integer, False),
        'TimeoutAction': (basestring, True),
        'TimeoutDurationMinutes': (positive_integer, True),
    }


class InstanceFleetProvisioningSpecifications(AWSProperty):
    props = {
        'SpotSpecification': (SpotProvisioningSpecification, True),
    }


class InstanceTypeConfig(AWSProperty):
    props = {
        'BidPrice': (basestring, False),
        'BidPriceAsPercentageOfOnDemandPrice': (basestring, False),
        'Configurations': ([Configuration], False),
        'EbsConfiguration': (EbsConfiguration, False),
        'InstanceType': (basestring, True),
        'WeightedCapacity': (positive_integer, False),
    }


class InstanceFleetConfigProperty(AWSProperty):
    props = {
        'InstanceTypeConfigs': ([InstanceTypeConfig], False),
        'LaunchSpecifications':
            (InstanceFleetProvisioningSpecifications, False),
        'Name': (basestring, False),
        'TargetOnDemandCapacity': (positive_integer, False),
        'TargetSpotCapacity': (positive_integer, False),
    }


class PlacementType(AWSProperty):
    props = {
        'AvailabilityZone': (basestring, True)
    }


class JobFlowInstancesConfig(AWSProperty):
    props = {
        'AdditionalMasterSecurityGroups': ([basestring], False),
        'AdditionalSlaveSecurityGroups': ([basestring], False),
        'CoreInstanceFleet': (InstanceFleetConfigProperty, False),
        'CoreInstanceGroup': (InstanceGroupConfigProperty, False),
        'Ec2KeyName': (basestring, False),
        'Ec2SubnetId': (basestring, False),
        'EmrManagedMasterSecurityGroup': (basestring, False),
        'EmrManagedSlaveSecurityGroup': (basestring, False),
        'HadoopVersion': (basestring, False),
        'MasterInstanceFleet': (InstanceFleetConfigProperty, False),
        'MasterInstanceGroup': (InstanceGroupConfigProperty, False),
        'Placement': (PlacementType, False),
        'ServiceAccessSecurityGroup': (basestring, False),
        'TerminationProtected': (boolean, False)
    }


class Cluster(AWSObject):
    resource_type = "AWS::EMR::Cluster"

    props = {
        'AdditionalInfo': (dict, False),
        'Applications': ([Application], False),
        'AutoScalingRole': (basestring, False),
        'BootstrapActions': ([BootstrapActionConfig], False),
        'Configurations': ([Configuration], False),
        'CustomAmiId': (basestring, False),
        'EbsRootVolumeSize': (positive_integer, False),
        'Instances': (JobFlowInstancesConfig, True),
        'JobFlowRole': (basestring, True),
        'LogUri': (basestring, False),
        'Name': (basestring, True),
        'ReleaseLabel': (basestring, False),
        'ScaleDownBehavior': (basestring, False),
        'SecurityConfiguration': (basestring, False),
        'ServiceRole': (basestring, True),
        'Tags': ((Tags, list), False),
        'VisibleToAllUsers': (boolean, False)
    }


class InstanceFleetConfig(AWSObject):
    resource_type = "AWS::EMR::InstanceFleetConfig"

    props = {
        'ClusterId': (basestring, True),
        'InstanceFleetType': (basestring, True),
        'InstanceTypeConfigs': ([InstanceTypeConfig], False),
        'LaunchSpecifications':
            (InstanceFleetProvisioningSpecifications, False),
        'Name': (basestring, False),
        'TargetOnDemandCapacity': (positive_integer, False),
        'TargetSpotCapacity': (positive_integer, False),
    }


class InstanceGroupConfig(AWSObject):
    resource_type = "AWS::EMR::InstanceGroupConfig"

    props = {
        'AutoScalingPolicy': (AutoScalingPolicy, False),
        'BidPrice': (basestring, False),
        'Configurations': ([Configuration], False),
        'EbsConfiguration': (EbsConfiguration, False),
        'InstanceCount': (integer, True),
        'InstanceRole': (basestring, True),
        'InstanceType': (basestring, True),
        'JobFlowId': (basestring, True),
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
