# Copyright (c) 2012-2013, Antonio Alonso Dominguez <alonso.domin@gmail.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, AWSHelperFn, Tags
from .validators import (
    boolean, integer, positive_integer, double, defer
)


CHANGE_IN_CAPACITY = 'CHANGE_IN_CAPACITY'
PERCENT_CHANGE_IN_CAPACITY = 'PERCENT_CHANGE_IN_CAPACITY'
EXACT_CAPACITY = 'EXACT_CAPACITY'
ACTIONS_ON_FAILURE = ('TERMINATE_CLUSTER', 'CANCEL_AND_WAIT', 'CONTINUE',
                      'TERMINATE_JOB_FLOW')


def validate_action_on_failure(action_on_failure):
    """Validate action on failure for EMR StepConfig """

    if action_on_failure not in ACTIONS_ON_FAILURE:
        raise ValueError("StepConfig ActionOnFailure  must be one of: %s" %
                         ", ".join(ACTIONS_ON_FAILURE))
    return action_on_failure


class KeyValue(AWSProperty):
    props = {
        'Key': (str, True),
        'Value': (str, True)
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
    for k, v in xs.items():
        if not isinstance(k, str):
            raise ValueError('AdditionalInfo keys must be strings')
        if not isinstance(v, str):
            raise ValueError('AdditionalInfo values must be strings')

    return xs


class SecurityConfiguration(AWSObject):
    resource_type = "AWS::EMR::SecurityConfiguration"

    props = {
        'Name': (str, False),
        'SecurityConfiguration': (dict, True)
    }


class Application(AWSProperty):
    props = {
        'AdditionalInfo': (additional_info_validator, False),
        'Args': ([str], False),
        'Name': (str, False),
        'Version': (str, False)
    }


class ScriptBootstrapActionConfig(AWSProperty):
    props = {
        'Args': ([str], False),
        'Path': (str, True)
    }


class BootstrapActionConfig(AWSProperty):
    props = {
        'Name': (str, True),
        'ScriptBootstrapAction': (ScriptBootstrapActionConfig, True)
    }


def properties_validator(xs):
    if not isinstance(xs, dict):
        raise ValueError("ConfigurationProperties must be a dict of "
                         "string to string pairs")
    for k, v in xs.items():
        if not isinstance(k, str):
            raise ValueError('ConfigurationProperties keys must be strings')
        if not isinstance(v, str) and not isinstance(v, AWSHelperFn):
            raise ValueError('ConfigurationProperties values must be strings'
                             ' or helper functions')

    return xs


class Configuration(AWSProperty):
    props = {
        'Classification': (str, False),
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
        'ComparisonOperator': (str, True),
        'Dimensions': ([MetricDimension], False),
        'EvaluationPeriods': (positive_integer, False),
        'MetricName': (str, True),
        'Namespace': (str, False),
        'Period': (positive_integer, True),
        'Statistic': (str, False),
        'Threshold': (positive_integer, True),
        'Unit': (str, False),
    }


class ScalingTrigger(AWSProperty):
    props = {
        'CloudWatchAlarmDefinition': (CloudWatchAlarmDefinition, True),
    }


class SimpleScalingPolicyConfiguration(AWSProperty):
    props = {
        'AdjustmentType': (str, False),
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
                double(scaling_adjustment)
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
        'Description': (str, False),
        'Name': (str, True),
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
        'BidPrice': (str, False),
        'Configurations': ([Configuration], False),
        'EbsConfiguration': (EbsConfiguration, False),
        'InstanceCount': (positive_integer, True),
        'InstanceType': (str, True),
        'Market': (market_validator, False),
        'Name': (str, False),
    }


class OnDemandProvisioningSpecification(AWSProperty):
    props = {
        'AllocationStrategy': (str, True),
    }

    def validate(self):
        valid_values = ['lowest-price']

        allocation_strategy = self.properties.get('AllocationStrategy', None)

        if allocation_strategy not in valid_values:
            raise ValueError(
                'AllocationStrategy %s is not valid. Valid options are %s' %
                (allocation_strategy, ', '.join(valid_values)))


class SpotProvisioningSpecification(AWSProperty):
    props = {
        'AllocationStrategy': (str, False),
        'BlockDurationMinutes': (positive_integer, False),
        'TimeoutAction': (str, True),
        'TimeoutDurationMinutes': (positive_integer, True),
    }

    def validate(self):
        if 'AllocationStrategy' in self.properties:
            valid_values = ['capacity-optimized']

            allocation_strategy = self.properties.get(
                'AllocationStrategy', None)

            if allocation_strategy not in valid_values:
                raise ValueError(
                    'AllocationStrategy %s is not valid. Valid options are %s'
                    % (allocation_strategy, ', '.join(valid_values)))


class InstanceFleetProvisioningSpecifications(AWSProperty):
    props = {
        'OnDemandSpecification': (OnDemandProvisioningSpecification, False),
        'SpotSpecification': (SpotProvisioningSpecification, False),
    }


class InstanceTypeConfig(AWSProperty):
    props = {
        'BidPrice': (str, False),
        'BidPriceAsPercentageOfOnDemandPrice': (str, False),
        'Configurations': ([Configuration], False),
        'EbsConfiguration': (EbsConfiguration, False),
        'InstanceType': (str, True),
        'WeightedCapacity': (positive_integer, False),
    }


class InstanceFleetConfigProperty(AWSProperty):
    props = {
        'InstanceTypeConfigs': ([InstanceTypeConfig], False),
        'LaunchSpecifications':
            (InstanceFleetProvisioningSpecifications, False),
        'Name': (str, False),
        'TargetOnDemandCapacity': (positive_integer, False),
        'TargetSpotCapacity': (positive_integer, False),
    }


class PlacementType(AWSProperty):
    props = {
        'AvailabilityZone': (str, True)
    }


class JobFlowInstancesConfig(AWSProperty):
    props = {
        'AdditionalMasterSecurityGroups': ([str], False),
        'AdditionalSlaveSecurityGroups': ([str], False),
        'CoreInstanceFleet': (InstanceFleetConfigProperty, False),
        'CoreInstanceGroup': (InstanceGroupConfigProperty, False),
        'Ec2KeyName': (str, False),
        'Ec2SubnetId': (str, False),
        'Ec2SubnetIds': ([str], False),
        'EmrManagedMasterSecurityGroup': (str, False),
        'EmrManagedSlaveSecurityGroup': (str, False),
        'HadoopVersion': (str, False),
        'KeepJobFlowAliveWhenNoSteps': (boolean, False),
        'MasterInstanceFleet': (InstanceFleetConfigProperty, False),
        'MasterInstanceGroup': (InstanceGroupConfigProperty, False),
        'Placement': (PlacementType, False),
        'ServiceAccessSecurityGroup': (str, False),
        'TerminationProtected': (boolean, False)
    }


class KerberosAttributes(AWSProperty):
    props = {
        'ADDomainJoinPassword': (str, False),
        'ADDomainJoinUser': (str, False),
        'CrossRealmTrustPrincipalPassword': (str, False),
        'KdcAdminPassword': (str, True),
        'Realm': (str, True),
    }


class ComputeLimits(AWSProperty):
    props = {
        'MaximumCapacityUnits': (integer, True),
        'MaximumCoreCapacityUnits': (integer, False),
        'MaximumOnDemandCapacityUnits': (integer, False),
        'MinimumCapacityUnits': (integer, True),
        'UnitType': (str, True),
    }


class ManagedScalingPolicy(AWSProperty):
    props = {
        'ComputeLimits': (ComputeLimits, False),
    }


class HadoopJarStepConfig(AWSProperty):
    props = {
        'Args': ([str], False),
        'Jar': (str, True),
        'MainClass': (str, False),
        'StepProperties': ([KeyValue], False)
    }


class StepConfig(AWSProperty):
    props = {
        'ActionOnFailure': (validate_action_on_failure, False),
        'HadoopJarStep': (HadoopJarStepConfig, True),
        'Name': (str, True),
    }


class Cluster(AWSObject):
    resource_type = "AWS::EMR::Cluster"

    props = {
        'AdditionalInfo': (dict, False),
        'Applications': ([Application], False),
        'AutoScalingRole': (str, False),
        'BootstrapActions': ([BootstrapActionConfig], False),
        'Configurations': ([Configuration], False),
        'CustomAmiId': (str, False),
        'EbsRootVolumeSize': (positive_integer, False),
        'Instances': (JobFlowInstancesConfig, True),
        'JobFlowRole': (str, True),
        'KerberosAttributes': (KerberosAttributes, False),
        'LogEncryptionKmsKeyId': (str, False),
        'LogUri': (str, False),
        'ManagedScalingPolicy': (ManagedScalingPolicy, False),
        'Name': (str, True),
        'ReleaseLabel': (str, False),
        'ScaleDownBehavior': (str, False),
        'SecurityConfiguration': (str, False),
        'ServiceRole': (str, True),
        'StepConcurrencyLevel': (integer, False),
        'Steps': ([StepConfig], False),
        'Tags': ((Tags, list), False),
        'VisibleToAllUsers': (boolean, False)
    }


class InstanceFleetConfig(AWSObject):
    resource_type = "AWS::EMR::InstanceFleetConfig"

    props = {
        'ClusterId': (str, True),
        'InstanceFleetType': (str, True),
        'InstanceTypeConfigs': ([InstanceTypeConfig], False),
        'LaunchSpecifications':
            (InstanceFleetProvisioningSpecifications, False),
        'Name': (str, False),
        'TargetOnDemandCapacity': (positive_integer, False),
        'TargetSpotCapacity': (positive_integer, False),
    }


class InstanceGroupConfig(AWSObject):
    resource_type = "AWS::EMR::InstanceGroupConfig"

    props = {
        'AutoScalingPolicy': (AutoScalingPolicy, False),
        'BidPrice': (str, False),
        'Configurations': ([Configuration], False),
        'EbsConfiguration': (EbsConfiguration, False),
        'InstanceCount': (integer, True),
        'InstanceRole': (str, True),
        'InstanceType': (str, True),
        'JobFlowId': (str, True),
        'Market': (market_validator, False),
        'Name': (str, False)
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
        'JobFlowId': (str, True),
        'Name': (str, True)
    }


class Studio(AWSObject):
    resource_type = "AWS::EMR::Studio"

    props = {
        'AuthMode': (str, True),
        'DefaultS3Location': (str, True),
        'Description': (str, False),
        'EngineSecurityGroupId': (str, True),
        'Name': (str, True),
        'ServiceRole': (str, True),
        'SubnetIds': ([str], True),
        'Tags': (Tags, False),
        'UserRole': (str, True),
        'VpcId': (str, True),
        'WorkspaceSecurityGroupId': (str, True),
    }


class StudioSessionMapping(AWSObject):
    resource_type = "AWS::EMR::StudioSessionMapping"

    props = {
        'IdentityName': (str, True),
        'IdentityType': (str, True),
        'SessionPolicyArn': (str, True),
        'StudioId': (str, True),
    }
