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
        for k, v in sorted(kwargs.items()):
            if type(v) in self.manyType:
                propagate = boolean(v[1])
                v = v[0]
            else:
                propagate = boolean(self.defaultPropagateAtLaunch)
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


class MetadataOptions(AWSProperty):
    props = {
        'HttpEndpoint': (str, False),
        'HttpPutResponseHopLimit': (integer, False),
        'HttpTokens': (str, False),
    }


class LifecycleHookSpecification(AWSProperty):
    props = {
        'DefaultResult': (str, False),
        'HeartbeatTimeout': (integer, False),
        'LifecycleHookName': (str, True),
        'LifecycleTransition': (str, True),
        'NotificationMetadata': (str, False),
        'NotificationTargetARN': (str, False),
        'RoleARN': (str, False),
    }


class NotificationConfigurations(AWSProperty):
    props = {
        'TopicARN': (str, True),
        'NotificationTypes': (list, True),
    }


class MetricsCollection(AWSProperty):
    props = {
        'Granularity': (str, True),
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
        'LaunchTemplateId': (str, False),
        'LaunchTemplateName': (str, False),
        'Version': (str, True)
    }

    def validate(self):
        template_ids = [
            'LaunchTemplateId',
            'LaunchTemplateName'
        ]
        exactly_one(self.__class__.__name__, self.properties, template_ids)


class InstancesDistribution(AWSProperty):
    props = {
        'OnDemandAllocationStrategy': (str, False),
        'OnDemandBaseCapacity': (integer, False),
        'OnDemandPercentageAboveBaseCapacity': (integer, False),
        'SpotAllocationStrategy': (str, False),
        'SpotInstancePools': (integer, False),
        'SpotMaxPrice': (str, False),
    }


class LaunchTemplateOverrides(AWSProperty):
    props = {
        'InstanceType': (str, False),
        'WeightedCapacity': (str, False),
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
        'AutoScalingGroupName': (str, False),
        'AvailabilityZones': (list, False),
        'CapacityRebalance': (boolean, False),
        'Cooldown': (integer, False),
        'DesiredCapacity': (integer, False),
        'HealthCheckGracePeriod': (integer, False),
        'HealthCheckType': (str, False),
        'InstanceId': (str, False),
        'LaunchConfigurationName': (str, False),
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
        'PlacementGroup': (str, False),
        'ServiceLinkedRoleARN': (str, False),
        'Tags': ((Tags, list), False),
        'TargetGroupARNs': ([str], False),
        'TerminationPolicies': ([str], False),
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
        'ClassicLinkVPCId': (str, False),
        'ClassicLinkVPCSecurityGroups': ([str], False),
        'EbsOptimized': (boolean, False),
        'IamInstanceProfile': (str, False),
        'ImageId': (str, True),
        'InstanceId': (str, False),
        'InstanceMonitoring': (boolean, False),
        'InstanceType': (str, True),
        'KernelId': (str, False),
        'KeyName': (str, False),
        'LaunchConfigurationName': (str, False),
        'Metadata': (Metadata, False),
        'MetadataOptions': (MetadataOptions, False),
        'PlacementTenancy': (str, False),
        'RamDiskId': (str, False),
        'SecurityGroups': (list, False),
        'SpotPrice': (str, False),
        'UserData': (str, False),
    }


class StepAdjustments(AWSProperty):
    props = {
        'MetricIntervalLowerBound': (integer, False),
        'MetricIntervalUpperBound': (integer, False),
        'ScalingAdjustment': (integer, True),
    }


class MetricDimension(AWSProperty):
    props = {
        'Name': (str, True),
        'Value': (str, True),
    }


class CustomizedMetricSpecification(AWSProperty):
    props = {
        'Dimensions': ([MetricDimension], False),
        'MetricName': (str, True),
        'Namespace': (str, True),
        'Statistic': (str, True),
        'Unit': (str, False),
    }


class PredefinedMetricSpecification(AWSProperty):
    props = {
        'PredefinedMetricType': (str, True),
        'ResourceLabel': (str, False),
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
        'AdjustmentType': (str, False),
        'AutoScalingGroupName': (str, True),
        'Cooldown': (integer, False),
        'EstimatedInstanceWarmup': (integer, False),
        'MetricAggregationType': (str, False),
        'MinAdjustmentMagnitude': (integer, False),
        'PolicyType': (str, False),
        'ScalingAdjustment': (integer, False),
        'StepAdjustments': ([StepAdjustments], False),
        'TargetTrackingConfiguration': (TargetTrackingConfiguration, False),
    }


class ScheduledAction(AWSObject):
    resource_type = "AWS::AutoScaling::ScheduledAction"

    props = {
        'AutoScalingGroupName': (str, True),
        'DesiredCapacity': (integer, False),
        'EndTime': (str, False),
        'MaxSize': (integer, False),
        'MinSize': (integer, False),
        'Recurrence': (str, False),
        'StartTime': (str, False),
    }


class LifecycleHook(AWSObject):
    resource_type = "AWS::AutoScaling::LifecycleHook"

    props = {
        'AutoScalingGroupName': (str, True),
        'DefaultResult': (str, False),
        'HeartbeatTimeout': (integer, False),
        'LifecycleHookName': (str, False),
        'LifecycleTransition': (str, True),
        'NotificationMetadata': (str, False),
        'NotificationTargetARN': (str, False),
        'RoleARN': (str, False),
    }


class Trigger(AWSObject):
    resource_type = "AWS::AutoScaling::Trigger"

    props = {
        'AutoScalingGroupName': (str, True),
        'BreachDuration': (integer, True),
        'Dimensions': (list, True),
        'LowerBreachScaleIncrement': (integer, False),
        'LowerThreshold': (integer, True),
        'MetricName': (str, True),
        'Namespace': (str, True),
        'Period': (integer, True),
        'Statistic': (str, True),
        'Unit': (str, False),
        'UpperBreachScaleIncrement': (integer, False),
        'UpperThreshold': (integer, True),
    }


class EBSBlockDevice(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig-blockdev-template.html
    props = {
        'DeleteOnTermination': (boolean, False),
        'Encrypted': (boolean, False),
        'Iops': (integer, False),
        'SnapshotId': (str, False),
        'VolumeSize': (integer, False),
        'VolumeType': (str, False),
    }


class BlockDeviceMapping(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig-blockdev-mapping.html
    props = {
        'DeviceName': (str, True),
        'Ebs': (EBSBlockDevice, False),
        'NoDevice': (boolean, False),
        'VirtualName': (str, False),
    }
