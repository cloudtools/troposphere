# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty


EC2_INSTANCE_LAUNCH = "autoscaling:EC2_INSTANCE_LAUNCH"
EC2_INSTANCE_LAUNCH_ERROR = "autoscaling:EC2_INSTANCE_LAUNCH_ERROR"
EC2_INSTANCE_TERMINATE = "autoscaling:EC2_INSTANCE_TERMINATE"
EC2_INSTANCE_TERMINATE_ERROR = "autoscaling:EC2_INSTANCE_TERMINATE_ERROR"
TEST_NOTIFICATION = "autoscaling:TEST_NOTIFICATION"


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


class AutoScalingGroup(AWSObject):
    props = {
        'AvailabilityZones': (list, True),
        'Cooldown': (int, False),
        'DesiredCapacity': (int, False),
        'HealthCheckGracePeriod': (int, False),
        'HealthCheckType': (basestring, False),
        'LaunchConfigurationName': (basestring, True),
        'LoadBalancerNames': (list, False),
        'MaxSize': (int, True),
        'MinSize': (int, True),
        'NotificationConfiguration': (NotificationConfiguration, False),
        'Tags': (list, False),  # Although docs say these are required
        'VPCZoneIdentifier': (list, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::AutoScaling::AutoScalingGroup"
        sup = super(AutoScalingGroup, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class LaunchConfiguration(AWSObject):
    props = {
        'BlockDeviceMappings': (list, False),
        'EbsOptimized': (bool, False),
        'IamInstanceProfile': (basestring, False),
        'ImageId': (basestring, True),
        'InstanceMonitoring': (bool, False),
        'InstanceType': (basestring, True),
        'KernelId': (basestring, False),
        'KeyName': (basestring, False),
        'RamDiskId': (basestring, False),
        'SecurityGroups': (list, False),
        'SpotPrice': (basestring, False),
        'UserData': (basestring, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::AutoScaling::LaunchConfiguration"
        sup = super(LaunchConfiguration, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class ScalingPolicy(AWSObject):
    props = {
        'AdjustmentType': (basestring, True),
        'AutoScalingGroupName': (basestring, True),
        'Cooldown': (int, False),
        'ScalingAdjustment': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::AutoScaling::ScalingPolicy"
        sup = super(ScalingPolicy, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class Trigger(AWSObject):
    props = {
        'AutoScalingGroupName': (basestring, True),
        'BreachDuration': (int, True),
        'Dimensions': (list, True),
        'LowerBreachScaleIncrement': (int, False),
        'LowerThreshold': (int, True),
        'MetricName': (basestring, True),
        'Namespace': (basestring, True),
        'Period': (int, True),
        'Statistic': (basestring, True),
        'Unit': (basestring, False),
        'UpperBreachScaleIncrement': (int, False),
        'UpperThreshold': (int, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::AutoScaling::Trigger"
        sup = super(Trigger, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class EBSBlockDevice(AWSProperty):
    props = {
        'SnapshotId': (basestring, False),
        'VolumeSize': (int, False),
    }


class BlockDeviceMapping(AWSProperty):
    props = {
        'DeviceName': (basestring, True),
        'Ebs': (EBSBlockDevice, False),
        'VirtualName': (basestring, False),
    }
