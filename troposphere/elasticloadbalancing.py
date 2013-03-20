# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty


class AppCookieStickinessPolicy(AWSProperty):
    props = {
        'CookieName': (basestring, True),
        'PolicyName': (basestring, True),
    }


class HealthCheck(AWSProperty):
    props = {
        'HealthyThreshold': (basestring, True),
        'Interval': (basestring, True),
        'Target': (basestring, True),
        'Timeout': (basestring, True),
        'UnhealthyThreshold': (basestring, True),
    }


class LBCookieStickinessPolicy(AWSProperty):
    props = {
        'CookieExpirationPeriod': (basestring, False),
        'PolicyName': (basestring, False),
    }


class Listener(AWSProperty):
    props = {
        'InstancePort': (basestring, True),
        'InstanceProtocol': (basestring, False),
        'LoadBalancerPort': (basestring, True),
        'PolicyNames': (list, False),
        'Protocol': (basestring, True),
        'SSLCertificateId': (basestring, False),
    }


class Policy(AWSProperty):
    props = {
        'Attributes': (dict, False),
        'InstancePorts': (list, False),
        'LoadBalancerPorts': (list, True),
        'PolicyName': (basestring, True),
        'PolicyType': (basestring, True),
    }


class LoadBalancer(AWSObject):
    props = {
        'AppCookieStickinessPolicy': (list, False),
        'AvailabilityZones': (list, False),
        'HealthCheck': (HealthCheck, False),
        'Instances': (list, False),
        'LBCookieStickinessPolicy': (list, False),
        'Listeners': (list, True),
        'Policies': (list, False),
        'Scheme': (basestring, False),
        'SecurityGroups': (list, False),
        'Subnets': (list, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::ElasticLoadBalancing::LoadBalancer"
        sup = super(LoadBalancer, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)
