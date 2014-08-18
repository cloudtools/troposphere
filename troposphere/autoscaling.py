# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty, Ref
from .validators import boolean, integer
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
ClosestToNextInstanceHour = 'ClosestToNextInstanceHour'


class Tag(AWSHelperFn):
    def __init__(self, key, value, propogate):
        self.data = {
            'Key': key,
            'Value': value,
            'PropagateAtLaunch': propogate,
        }

    def JSONrepr(self):
        return self.data


class NotificationConfiguration(AWSProperty):
    props = {
        'TopicARN': (basestring, True),
        'NotificationTypes': (list, True),
    }


class MetricsCollection(AWSProperty):
    props = {
        'Granularity': (basestring, True),
        'Metrics': (list, False),
    }


class AutoScalingGroup(AWSObject):
    type = "AWS::AutoScaling::AutoScalingGroup"

    props = {
        'AvailabilityZones': (list, True),
        'Cooldown': (integer, False),
        'DesiredCapacity': (integer, False),
        'HealthCheckGracePeriod': (int, False),
        'HealthCheckType': (basestring, False),
        'InstanceId': (basestring, False),
        'LaunchConfigurationName': (basestring, True),
        'LoadBalancerNames': (list, False),
        'MaxSize': (integer, True),
        'MetricsCollection': ([MetricsCollection], False),
        'MinSize': (integer, True),
        'NotificationConfiguration': (NotificationConfiguration, False),
        'PlacementGroup': (basestring, False),
        'Tags': (list, False),  # Although docs say these are required
        'TerminationPolicies': ([basestring], False),
        'VPCZoneIdentifier': (list, False),
    }

    def validate(self):
        if 'UpdatePolicy' in self.resource:
            update_policy = self.resource['UpdatePolicy']

            isMinRef = isinstance(update_policy.MinInstancesInService, Ref)
            isMaxRef = isinstance(self.MaxSize, Ref)

            if not (isMinRef or isMaxRef):
                minCount = int(update_policy.MinInstancesInService)
                maxCount = int(self.MaxSize)

                if minCount >= maxCount:
                    raise ValueError(
                        "The UpdatePolicy attribute "
                        "MinInstancesInService must be less than the "
                        "autoscaling group's MaxSize")
        return True


class LaunchConfiguration(AWSObject):
    type = "AWS::AutoScaling::LaunchConfiguration"

    props = {
        'AssociatePublicIpAddress': (boolean, False),
        'BlockDeviceMappings': (list, False),
        'EbsOptimized': (boolean, False),
        'IamInstanceProfile': (basestring, False),
        'ImageId': (basestring, True),
        'InstanceId': (basestring, False),
        'InstanceMonitoring': (boolean, False),
        'InstanceType': (basestring, True),
        'KernelId': (basestring, False),
        'KeyName': (basestring, False),
        'Metadata': (cloudformation.Init, False),
        'RamDiskId': (basestring, False),
        'SecurityGroups': (list, False),
        'SpotPrice': (basestring, False),
        'UserData': (basestring, False),
    }


class ScalingPolicy(AWSObject):
    type = "AWS::AutoScaling::ScalingPolicy"

    props = {
        'AdjustmentType': (basestring, True),
        'AutoScalingGroupName': (basestring, True),
        'Cooldown': (integer, False),
        'ScalingAdjustment': (basestring, True),
    }


class ScheduledAction(AWSObject):
    type = "AWS::AutoScaling::ScheduledAction"

    props = {
        'AutoScalingGroupName': (basestring, True),
        'DesiredCapacity': (integer, False),
        'EndTime': (basestring, True),
        'MaxSize': (integer, False),
        'MinSize': (integer, False),
        'Recurrence': (basestring, True),
        'StartTime': (basestring, True),
    }


class Trigger(AWSObject):
    type = "AWS::AutoScaling::Trigger"

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
