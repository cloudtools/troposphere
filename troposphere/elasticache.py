# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, Ref, GetAtt
from .validators import boolean, integer


class CacheCluster(AWSObject):
    resource_type = "AWS::ElastiCache::CacheCluster"

    props = {
        'AutoMinorVersionUpgrade': (boolean, False),
        'AZMode': (basestring, False),
        'CacheNodeType': (basestring, True),
        'CacheParameterGroupName': (basestring, False),
        'CacheSecurityGroupNames': ([basestring, Ref], False),
        'CacheSubnetGroupName': (basestring, False),
        'ClusterName': (basestring, False),
        'Engine': (basestring, True),
        'EngineVersion': (basestring, False),
        'NotificationTopicArn': (basestring, False),
        'NumCacheNodes': (integer, True),
        'Port': (int, False),
        'PreferredAvailabilityZone': (basestring, False),
        'PreferredAvailabilityZones': ([basestring], False),
        'PreferredMaintenanceWindow': (basestring, False),
        'SnapshotArns': ([basestring, Ref], False),
        'SnapshotRetentionLimit': (int, False),
        'SnapshotWindow': (basestring, False),
        'VpcSecurityGroupIds': ([basestring, Ref, GetAtt], False),
    }


class ParameterGroup(AWSObject):
    resource_type = "AWS::ElastiCache::ParameterGroup"

    props = {
        'CacheParameterGroupFamily': (basestring, True),
        'Description': (basestring, True),
        'Properties': (dict, True),
    }


class SecurityGroup(AWSObject):
    resource_type = "AWS::ElastiCache::SecurityGroup"

    props = {
        'Description': (basestring, False),
    }


class SecurityGroupIngress(AWSObject):
    resource_type = "AWS::ElastiCache::SecurityGroupIngress"

    props = {
        'CacheSecurityGroupName': (basestring, True),
        'EC2SecurityGroupName': (basestring, True),
        'EC2SecurityGroupOwnerId': (basestring, False),
    }


class SubnetGroup(AWSObject):
    resource_type = "AWS::ElastiCache::SubnetGroup"

    props = {
        'Description': (basestring, True),
        'SubnetIds': (list, True),
    }
