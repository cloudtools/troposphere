# Copyright (c) 2011-2012, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import json

from . import AWSObject


class AppCookieStickinessPolicy(AWSObject):
    props = {
        'CookieName': (basestring, True),
        'PolicyName': (basestring, True),
    }

    def __init__(self, **kwargs):
        sup = super(AppCookieStickinessPolicy, self)
        sup.__init__(None, props=self.props, **kwargs)


class HealthCheck(AWSObject):
    props = {
        'HealthyThreshold': (basestring, True),
        'Interval': (basestring, True),
        'Target': (basestring, True),
        'Timeout': (basestring, True),
        'UnhealthyThreshold': (basestring, True),
    }

    def __init__(self, **kwargs):
        sup = super(HealthCheck, self)
        sup.__init__(None, props=self.props, **kwargs)


class LBCookieStickinessPolicy(AWSObject):
    props = {
        'CookieExpirationPeriod': (basestring, False),
        'PolicyName': (basestring, False),
    }

    def __init__(self, **kwargs):
        sup = super(LBCookieStickinessPolicy, self)
        sup.__init__(None, props=self.props, **kwargs)


class Listener(AWSObject):
    props = {
        'InstancePort': (basestring, True),
        'InstanceProtocol': (basestring, False),
        'LoadBalancerPort': (basestring, True),
        'PolicyNames': (list, False),
        'Protocol': (basestring, True),
        'SSLCertificateId': (basestring, False),
    }

    def __init__(self, **kwargs):
        sup = super(Listener, self)
        sup.__init__(None, props=self.props, **kwargs)


class Policy(AWSObject):
    props = {
        'Attributes': (dict, False),
        'InstancePorts': (list, False),
        'LoadBalancerPorts': (list, True),
        'PolicyName': (basestring, True),
        'PolicyType': (basestring, True),
    }

    def __init__(self, **kwargs):
        sup = super(Policy, self)
        sup.__init__(None, props=self.props, **kwargs)


class LoadBalancer(AWSObject):
    props = {
        'AppCookieStickinessPolicy': (list, False),
        'AvailabilityZones': (basestring, False),
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
