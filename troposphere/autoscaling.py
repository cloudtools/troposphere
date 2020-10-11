# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty, If, FindInMap, Ref
from .validators import boolean, integer, exactly_one, mutually_exclusive
from . import cloudformation


EC2_INSTANCE_LAUNCH = "autoscaling:EC2_INSTANCE_LAUNCH"
EC2_INSTANCE_LAUNCH_ERROR = "autoscaling:EC2_INSTANCE_LAUNCH_ERROR"
EC2_INSTANCE_TERMINATE = "autoscaling:EC2_INSTANCE_TERMINATE"
EC2_INSTANCE_TERMINATE_ERROR = "autoscaling:EC2_INSTANCE_TERMINATE_ERROR"
TEST_NOTIFICATION = "autoscaling:TEST_NOTIFICATION"

# Termination Policy constants
Default = 'Default'
OldestInstance = 'OldestInstance'
NewestInstance = 'NewestInstance'
OldestLaunchConfiguration = 'OldestLaunchConfiguration'
OldestLaunchTemplate = 'OldestLaunchTemplate'
ClosestToNextInstanceHour = 'ClosestToNextInstanceHour'
AllocationStrategy = 'AllocationStrategy'


class Tag(AWSHelperFn):
    def __init__(self, key, value, propogate):
        self.data = {
            'Key': key,
            'Value': value,
            'PropagateAtLaunch': propogate,
        }


class Tags(AWSHelperFn):
    defaultPropagateAtLaunch = True
    manyType = [type([]), type(())]

    def __init__(self, **kwargs):
        self.tags = []
        for k, v in sorted(kwargs.iteritems()):
            if type(v) in self.manyType:
                propagate = str(v[1]).lower()
                v = v[0]
            else:
                propagate = str(self.defaultPropagateAtLaunch).lower()
            self.tags.append({
                'Key': k,
                'Value': v,
                'PropagateAtLaunch': propagate,
            })

    # append tags to list
    def __add__(self, newtags):
        newtags.tags = self.tags + newtags.tags
        return newtags

    def to_dict(self):
        return self.tags


class LifecycleHookSpecification(AWSProperty):
    props = {
        'DefaultResult': (basestring, False),
        'HeartbeatTimeout': (integer, False),
        'LifecycleHookName': (basestring, True),
        'LifecycleTransition': (basestring, True),
        'NotificationMetadata': (basestring, False),
        'NotificationTargetARN': (basestring, False),
        'RoleARN': (basestring, False),
    }


class NotificationConfigurations(AWSProperty):
    props = {
        'TopicARN': (basestring, True),
        'NotificationTypes': (list, True),
    }


class MetricsCollection(AWSProperty):
    props = {
        'Granularity': (basestring, True),
        'Metrics': (list, False),
    }


class Metadata(AWSHelperFn):
    def __init__(self, init, authentication=None):
        self.validate(init, authentication)
        # get keys and values from init and authentication

        # if there's only one data point, then we know its the default
        # cfn-init; where the key is 'config'
        if len(init.data) == 1:
            initKey, initValue = init.data.popitem()
            self.data = {initKey: initValue}
        else:
            self.data = init.data

        if authentication:
            authKey, authValue = authentication.data.popitem()
            self.data[authKey] = authValue

    def validate(self, init, authentication):
        if not isinstance(init, cloudformation.Init):
            raise ValueError(
                'init must be of type cloudformation.Init'
            )

        is_instance = isinstance(authentication, cloudformation.Authentication)
        if authentication and not is_instance:
            raise ValueError(
                'authentication must be of type cloudformation.Authentication'
            )


class LaunchTemplateSpecification(AWSProperty):
    props = {
        'LaunchTemplateId': (basestring, False),
        'LaunchTemplateName': (basestring, False),
        'Version': (basestring, True)
    }

    def validate(self):
        template_ids = [
            'LaunchTemplateId',
            'LaunchTemplateName'
        ]
        exactly_one(self.__class__.__name__, self.properties, template_ids)


class InstancesDistribution(AWSProperty):
    props = {
        'OnDemandAllocationStrategy': (basestring, False),
        'OnDemandBaseCapacity': (integer, False),
        'OnDemandPercentageAboveBaseCapacity': (integer, False),
        'SpotAllocationStrategy': (basestring, False),
        'SpotInstancePools': (integer, False),
        'SpotMaxPrice': (basestring, False),
    }


class LaunchTemplateOverrides(AWSProperty):
    props = {
        'InstanceType': (basestring, False),
        'WeightedCapacity': (basestring, False),
    }


class LaunchTemplate(AWSProperty):
    props = {
        'LaunchTemplateSpecification': (LaunchTemplateSpecification, True),
        'Overrides': ([LaunchTemplateOverrides], True),
    }


class MixedInstancesPolicy(AWSProperty):
    props = {
        'InstancesDistribution': (InstancesDistribution, False),
        'LaunchTemplate': (LaunchTemplate, True),
    }


class AutoScalingGroup(AWSObject):
    resource_type = "AWS::AutoScaling::AutoScalingGroup"

    props = {
        'AutoScalingGroupName': (basestring, False),
        'AvailabilityZones': (list, False),
        'Cooldown': (integer, False),
        'DesiredCapacity': (integer, False),
        'HealthCheckGracePeriod': (integer, False),
        'HealthCheckType': (basestring, False),
        'InstanceId': (basestring, False),
        'LaunchConfigurationName': (basestring, False),
        'LaunchTemplate': (LaunchTemplateSpecification, False),
        'LifecycleHookSpecificationList':
            ([LifecycleHookSpecification], False),
        'LoadBalancerNames': (list, False),
        'MaxInstanceLifetime': (integer, False),
        'MaxSize': (integer, True),
        'MetricsCollection': ([MetricsCollection], False),
        'MinSize': (integer, True),
        'MixedInstancesPolicy': (MixedInstancesPolicy, False),
        'NewInstancesProtectedFromScaleIn': (boolean, False),
        'NotificationConfigurations': ([NotificationConfigurations], False),
        'PlacementGroup': (basestring, False),
        'ServiceLinkedRoleARN': (basestring, False),
        'Tags': ((Tags, list), False),
        'TargetGroupARNs': ([basestring], False),
        'TerminationPolicies': ([basestring], False),
        'VPCZoneIdentifier': (list, False),
    }

    def validate(self):
        if 'UpdatePolicy' in self.resource:
            update_policy = self.resource['UpdatePolicy']

            if (not isinstance(update_policy, AWSHelperFn) and
                    'AutoScalingRollingUpdate' in update_policy.properties):
                if not isinstance(
                        update_policy.AutoScalingRollingUpdate, AWSHelperFn):
                    rolling_update = update_policy.AutoScalingRollingUpdate

                    min_instances = rolling_update.properties.get(
                        "MinInstancesInService", "0")
                    is_min_no_check = isinstance(
                        min_instances, (If, FindInMap, Ref)
                    )
                    is_max_no_check = isinstance(self.MaxSize,
                                                 (If, FindInMap, Ref))

                    if not (is_min_no_check or is_max_no_check):
                        max_count = int(self.MaxSize)
                        min_count = int(min_instances)

                        if min_count >= max_count:
                            raise ValueError(
                                "The UpdatePolicy attribute "
                                "MinInstancesInService must be less than the "
                                "autoscaling group's MaxSize")

        instance_config_types = [
            'LaunchConfigurationName',
            'LaunchTemplate',
            'InstanceId'
        ]

        mutually_exclusive(self.__class__.__name__, self.properties,
                           instance_config_types)

        availability_zones = self.properties.get('AvailabilityZones')
        vpc_zone_identifier = self.properties.get('VPCZoneIdentifier')
        if not availability_zones and not vpc_zone_identifier:
            raise ValueError("Must specify AvailabilityZones and/or "
                             "VPCZoneIdentifier: http://docs.aws.amazon.com/A"
                             "WSCloudFormation/latest/UserGuide/aws-propertie"
                             "s-as-group.html#cfn-as-group-vpczoneidentifier")
        return True


class LaunchConfiguration(AWSObject):
    resource_type = "AWS::AutoScaling::LaunchConfiguration"

    props = {
        'AssociatePublicIpAddress': (boolean, False),
        'BlockDeviceMappings': (list, False),
        'ClassicLinkVPCId': (basestring, False),
        'ClassicLinkVPCSecurityGroups': ([basestring], False),
        'EbsOptimized': (boolean, False),
        'IamInstanceProfile': (basestring, False),
        'ImageId': (basestring, True),
        'InstanceId': (basestring, False),
        'InstanceMonitoring': (boolean, False),
        'InstanceType': (basestring, True),
        'KernelId': (basestring, False),
        'KeyName': (basestring, False),
        'LaunchConfigurationName': (basestring, False),
        'Metadata': (Metadata, False),
        'PlacementTenancy': (basestring, False),
        'RamDiskId': (basestring, False),
        'SecurityGroups': (list, False),
        'SpotPrice': (basestring, False),
        'UserData': (basestring, False),
    }


class StepAdjustments(AWSProperty):
    props = {
        'MetricIntervalLowerBound': (integer, False),
        'MetricIntervalUpperBound': (integer, False),
        'ScalingAdjustment': (integer, True),
    }


class MetricDimension(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Value': (basestring, True),
    }


class CustomizedMetricSpecification(AWSProperty):
    props = {
        'Dimensions': ([MetricDimension], False),
        'MetricName': (basestring, True),
        'Namespace': (basestring, True),
        'Statistic': (basestring, True),
        'Unit': (basestring, False),
    }


class PredefinedMetricSpecification(AWSProperty):
    props = {
        'PredefinedMetricType': (basestring, True),
        'ResourceLabel': (basestring, False),
    }


class TargetTrackingConfiguration(AWSProperty):
    props = {
        'CustomizedMetricSpecification':
            (CustomizedMetricSpecification, False),
        'DisableScaleIn': (boolean, False),
        'PredefinedMetricSpecification':
            (PredefinedMetricSpecification, False),
        'TargetValue': (float, True),
    }


class ScalingPolicy(AWSObject):
    resource_type = "AWS::AutoScaling::ScalingPolicy"

    props = {
        'AdjustmentType': (basestring, False),
        'AutoScalingGroupName': (basestring, True),
        'Cooldown': (integer, False),
        'EstimatedInstanceWarmup': (integer, False),
        'MetricAggregationType': (basestring, False),
        'MinAdjustmentMagnitude': (integer, False),
        'PolicyType': (basestring, False),
        'ScalingAdjustment': (integer, False),
        'StepAdjustments': ([StepAdjustments], False),
        'TargetTrackingConfiguration': (TargetTrackingConfiguration, False),
    }


class ScheduledAction(AWSObject):
    resource_type = "AWS::AutoScaling::ScheduledAction"

    props = {
        'AutoScalingGroupName': (basestring, True),
        'DesiredCapacity': (integer, False),
        'EndTime': (basestring, False),
        'MaxSize': (integer, False),
        'MinSize': (integer, False),
        'Recurrence': (basestring, False),
        'StartTime': (basestring, False),
    }


class LifecycleHook(AWSObject):
    resource_type = "AWS::AutoScaling::LifecycleHook"

    props = {
        'AutoScalingGroupName': (basestring, True),
        'DefaultResult': (basestring, False),
        'HeartbeatTimeout': (integer, False),
        'LifecycleHookName': (basestring, False),
        'LifecycleTransition': (basestring, True),
        'NotificationMetadata': (basestring, False),
        'NotificationTargetARN': (basestring, False),
        'RoleARN': (basestring, False),
    }


class Trigger(AWSObject):
    resource_type = "AWS::AutoScaling::Trigger"

    props = {
        'AutoScalingGroupName': (basestring, True),
        'BreachDuration': (integer, True),
        'Dimensions': (list, True),
        'LowerBreachScaleIncrement': (integer, False),
        'LowerThreshold': (integer, True),
        'MetricName': (basestring, True),
        'Namespace': (basestring, True),
        'Period': (integer, True),
        'Statistic': (basestring, True),
        'Unit': (basestring, False),
        'UpperBreachScaleIncrement': (integer, False),
        'UpperThreshold': (integer, True),
    }


class EBSBlockDevice(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig-blockdev-template.html
    props = {
        'DeleteOnTermination': (boolean, False),
        'Encrypted': (boolean, False),
        'Iops': (integer, False),
        'SnapshotId': (basestring, False),
        'VolumeSize': (integer, False),
        'VolumeType': (basestring, False),
    }


class BlockDeviceMapping(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig-blockdev-mapping.html
    props = {
        'DeviceName': (basestring, True),
        'Ebs': (EBSBlockDevice, False),
        'NoDevice': (boolean, False),
        'VirtualName': (basestring, False),
    }
