# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer, network_port


class CacheCluster(AWSObject):
    resource_type = "AWS::ElastiCache::CacheCluster"

    props = {
        'AutoMinorVersionUpgrade': (boolean, False),
        'AZMode': (basestring, False),
        'CacheNodeType': (basestring, True),
        'CacheParameterGroupName': (basestring, False),
        'CacheSecurityGroupNames': ([basestring], False),
        'CacheSubnetGroupName': (basestring, False),
        'ClusterName': (basestring, False),
        'Engine': (basestring, True),
        'EngineVersion': (basestring, False),
        'NotificationTopicArn': (basestring, False),
        'NumCacheNodes': (integer, True),
        'Port': (integer, False),
        'PreferredAvailabilityZone': (basestring, False),
        'PreferredAvailabilityZones': ([basestring], False),
        'PreferredMaintenanceWindow': (basestring, False),
        'SnapshotArns': ([basestring], False),
        'SnapshotName': (basestring, False),
        'SnapshotRetentionLimit': (integer, False),
        'SnapshotWindow': (basestring, False),
        'Tags': (Tags, False),
        'VpcSecurityGroupIds': ([basestring], False),
    }

    def validate(self):
        # Check that AZMode is "cross-az" if more than one Availability zone
        # is specified in PreferredAvailabilityZones
        preferred_azs = self.properties.get('PreferredAvailabilityZones')
        if preferred_azs is not None and \
                isinstance(preferred_azs, list) and \
                len(preferred_azs) > 1:
            if self.properties.get('AZMode') != 'cross-az':
                raise ValueError('AZMode must be "cross-az" if more than one a'
                                 'vailability zone is specified in PreferredAv'
                                 'ailabilityZones: http://docs.aws.amazon.com/'
                                 'AWSCloudFormation/latest/UserGuide/aws-prope'
                                 'rties-elasticache-cache-cluster.html#cfn-ela'
                                 'sticache-cachecluster-azmode')

        return True


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
        'CacheSubnetGroupName': (basestring, False),
        'Description': (basestring, True),
        'SubnetIds': (list, True),
    }


class ReplicationGroup(AWSObject):
    resource_type = "AWS::ElastiCache::ReplicationGroup"

    props = {
        'AtRestEncryptionEnabled': (boolean, False),
        'AuthToken': (basestring, False),
        'AutoMinorVersionUpgrade': (boolean, False),
        'AutomaticFailoverEnabled': (boolean, False),
        'CacheNodeType': (basestring, True),
        'CacheParameterGroupName': (basestring, False),
        'CacheSecurityGroupNames': ([basestring], False),
        'CacheSubnetGroupName': (basestring, False),
        'Engine': (basestring, True),
        'EngineVersion': (basestring, False),
        'NodeGroupConfiguration': (list, False),
        'NotificationTopicArn': (basestring, False),
        'NumCacheClusters': (integer, False),
        'NumNodeGroups': (integer, False),
        'Port': (network_port, False),
        'PreferredCacheClusterAZs': ([basestring], False),
        'PreferredMaintenanceWindow': (basestring, False),
        'PrimaryClusterId': (basestring, False),
        'ReplicasPerNodeGroup': (integer, False),
        'ReplicationGroupDescription': (basestring, True),
        'ReplicationGroupId': (basestring, False),
        'SecurityGroupIds': ([basestring], False),
        'SnapshotArns': ([basestring], False),
        'SnapshotName': (basestring, False),
        'SnapshotRetentionLimit': (integer, False),
        'SnapshottingClusterId': (basestring, False),
        'SnapshotWindow': (basestring, False),
        'Tags': (Tags, False),
        'TransitEncryptionEnabled': (boolean, False),
    }

    def validate(self):
        if 'NumCacheClusters' not in self.properties and \
           'NumNodeGroups' not in self.properties and \
           'ReplicasPerNodeGroup' not in self.properties and \
           'PrimaryClusterId' not in self.properties:
            raise ValueError(
                'One of PrimaryClusterId, NumCacheClusters, '
                'NumNodeGroups or ReplicasPerNodeGroup are required'
                'in type AWS::ElastiCache::ReplicationGroup'
                )

        return True


class NodeGroupConfiguration(AWSProperty):
    props = {
        'PrimaryAvailabilityZone': (basestring, False),
        'ReplicaAvailabilityZones': (basestring, False),
        'ReplicaCount': (integer, False),
        'Slots': (basestring, False),
    }
