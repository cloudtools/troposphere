# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# Copyright (c) 2014, Andy Botting <andy.botting@theguardian.com>
# All rights reserved.
#
# See LICENSE file for full license.

from troposphere import AWSObject
from troposphere.validators import integer


# Due to the strange nature of the OpenStack compatability layer, some values
# that should be integers fail to validate and need to be represented as
# strings. For this reason, we duplicate the AWS::AutoScaling::AutoScalingGroup
# and change these types.
class AWSAutoScalingGroup(AWSObject):
    resource_type = "AWS::AutoScaling::AutoScalingGroup"

    props = {
        'AvailabilityZones': (list, True),
        'Cooldown': (integer, False),
        'DesiredCapacity': (basestring, False),
        'HealthCheckGracePeriod': (integer, False),
        'HealthCheckType': (basestring, False),
        'LaunchConfigurationName': (basestring, True),
        'LoadBalancerNames': (list, False),
        'MaxSize': (basestring, True),
        'MinSize': (basestring, True),
        'Tags': (list, False),
        'VPCZoneIdentifier': (list, False),
    }
