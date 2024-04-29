"""
Openstack Heat
--------------

Due to the strange nature of the OpenStack compatability layer, some values
that should be integers fail to validate and need to be represented as
strings. For this reason, we duplicate the AWS::AutoScaling::AutoScalingGroup
and change these types.
"""

# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# Copyright (c) 2014, Andy Botting <andy.botting@theguardian.com>
# All rights reserved.
#
# See LICENSE file for full license.
# ----------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------


from troposphere import AWSObject
from troposphere.validators import integer

# ----------------------------------------------------------------------------
# Class:  AWSAutoScalingGroup
# ----------------------------------------------------------------------------


class AWSAutoScalingGroup(AWSObject):
    """Fix issues with OpenStack compatability layer.

    Due to the strange nature of the OpenStack compatability layer, some
    values that should be integers fail to validate and need to be
    represented as strings. For this reason, we duplicate the
    AWS::AutoScaling::AutoScalingGroup and change these types.
    """

    resource_type = "AWS::AutoScaling::AutoScalingGroup"

    props = {
        "AvailabilityZones": (list, True),
        "Cooldown": (integer, False),
        "DesiredCapacity": (str, False),
        "HealthCheckGracePeriod": (integer, False),
        "HealthCheckType": (str, False),
        "LaunchConfigurationName": (str, True),
        "LoadBalancerNames": (list, False),
        "MaxSize": (str, True),
        "MinSize": (str, True),
        "Tags": (list, False),
        "VPCZoneIdentifier": (list, False),
    }
