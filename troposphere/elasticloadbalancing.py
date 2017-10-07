# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import (
    boolean, elb_name, integer_range, positive_integer, network_port, integer)


class AppCookieStickinessPolicy(AWSProperty):
    props = {
        'CookieName': (basestring, True),
        'PolicyName': (basestring, True),
    }


class HealthCheck(AWSProperty):
    props = {
        'HealthyThreshold': (integer_range(2, 10), True),
        'Interval': (positive_integer, True),
        'Target': (basestring, True),
        'Timeout': (positive_integer, True),
        'UnhealthyThreshold': (integer_range(2, 10), True),
    }


class LBCookieStickinessPolicy(AWSProperty):
    props = {
        'CookieExpirationPeriod': (basestring, False),
        'PolicyName': (basestring, False),
    }


class Listener(AWSProperty):
    props = {
        'InstancePort': (network_port, True),
        'InstanceProtocol': (basestring, False),
        'LoadBalancerPort': (network_port, True),
        'PolicyNames': (list, False),
        'Protocol': (basestring, True),
        'SSLCertificateId': (basestring, False),
    }


class Policy(AWSProperty):
    props = {
        'Attributes': ([dict], False),
        'InstancePorts': (list, False),
        'LoadBalancerPorts': (list, False),
        'PolicyName': (basestring, True),
        'PolicyType': (basestring, True),
    }


class ConnectionDrainingPolicy(AWSProperty):
    props = {
        'Enabled': (bool, True),
        'Timeout': (integer, False)
    }


class ConnectionSettings(AWSProperty):
    props = {
        'IdleTimeout': (integer, True),
    }


class AccessLoggingPolicy(AWSProperty):
    props = {
        'EmitInterval': (integer, False),
        'Enabled': (bool, True),
        'S3BucketName': (basestring, False),
        'S3BucketPrefix': (basestring, False),
    }


class LoadBalancer(AWSObject):
    resource_type = "AWS::ElasticLoadBalancing::LoadBalancer"

    props = {
        'AccessLoggingPolicy': (AccessLoggingPolicy, False),
        'AppCookieStickinessPolicy': (list, False),
        'AvailabilityZones': (list, False),
        'ConnectionDrainingPolicy': (ConnectionDrainingPolicy, False),
        'ConnectionSettings': (ConnectionSettings, False),
        'CrossZone': (boolean, False),
        'HealthCheck': (HealthCheck, False),
        'Instances': (list, False),
        'LBCookieStickinessPolicy': (list, False),
        'LoadBalancerName': (elb_name, False),
        'Listeners': (list, True),
        'Policies': (list, False),
        'Scheme': (basestring, False),
        'SecurityGroups': (list, False),
        'Subnets': (list, False),
        'Tags': ((Tags, list), False),
    }
