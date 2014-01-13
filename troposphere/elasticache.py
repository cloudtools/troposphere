# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, Ref
from .validators import boolean, integer


class CacheCluster(AWSObject):
    type = "AWS::ElastiCache::CacheCluster"

    props = {
        'AutoMinorVersionUpgrade': (boolean, False),
        'CacheNodeType': (basestring, True),
        'CacheParameterGroupName': (basestring, False),
        'CacheSecurityGroupNames': ([basestring, Ref], False),
        'CacheSubnetGroupName': (basestring, False),
        'ClusterName': (basestring, False),
        'Engine': (basestring, True),
        'EngineVersion': (basestring, False),
        'NotificationTopicArn': (basestring, False),
        'NumCacheNodes': (integer, False),
        'Port': (int, False),
        'PreferredAvailabilityZone': (basestring, False),
        'PreferredMaintenanceWindow': (basestring, False),
        'SnapshotArns': ([basestring, Ref], False),
        'VpcSecurityGroupIds': ([basestring, Ref], False),
    }


class ParameterGroup(AWSObject):
    type = "AWS::ElastiCache::ParameterGroup"

    props = {
        'CacheParameterGroupFamily': (basestring, True),
        'Description': (basestring, True),
        'Properties': (dict, True),
    }


class SecurityGroup(AWSObject):
    type = "AWS::ElastiCache::SecurityGroup"

    props = {
        'Description': (basestring, True),
    }


class SecurityGroupIngress(AWSObject):
    type = "AWS::ElastiCache::SecurityGroupIngress"

    props = {
        'CacheSecurityGroupName': (basestring, True),
        'EC2SecurityGroupName': (basestring, True),
        'EC2SecurityGroupOwnerId': (basestring, False),
    }


class SubnetGroup(AWSObject):
    type = "AWS::ElastiCache::SubnetGroup"

    props = {
        'Description': (basestring, True),
        'SubnetIds': (list, True),
    }
