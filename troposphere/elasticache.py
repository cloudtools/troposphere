# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject
from .validators import integer


class CacheCluster(AWSObject):
    props = {
        'AutoMinorVersionUpgrade': (bool, False),
        'CacheNodeType': (basestring, True),
        'CacheParameterGroupName': (basestring, False),
        'CacheSecurityGroupNames': (list, True),
        'Engine': (basestring, True),
        'EngineVersion': (basestring, False),
        'NotificationTopicArn': (basestring, False),
        'NumCacheNodes': (integer, False),
        'Port': (int, False),
        'PreferredAvailabilityZone': (basestring, False),
        'PreferredMaintenanceWindow': (basestring, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::ElastiCache::CacheCluster"
        sup = super(CacheCluster, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class ParameterGroup(AWSObject):
    props = {
        'CacheParameterGroupFamily': (basestring, True),
        'Description': (basestring, True),
        'Properties': (dict, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::ElastiCache::ParameterGroup"
        sup = super(ParameterGroup, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class SecurityGroup(AWSObject):
    props = {
        'Description': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::ElastiCache::SecurityGroup"
        sup = super(SecurityGroup, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class SecurityGroupIngress(AWSObject):
    props = {
        'CacheSecurityGroupName': (basestring, True),
        'EC2SecurityGroupName': (basestring, True),
        'EC2SecurityGroupOwnerId': (basestring, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::ElastiCache::SecurityGroupIngress"
        sup = super(SecurityGroupIngress, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)
