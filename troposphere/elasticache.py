# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import re

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer, network_port


def validate_node_group_id(node_group_id):
    if re.match(r'\d{1,4}', node_group_id):
        return node_group_id
    raise ValueError("Invalid NodeGroupId: %s" % node_group_id)


class CacheCluster(AWSObject):
    resource_type = "AWS::ElastiCache::CacheCluster"

    props = {
        'AutoMinorVersionUpgrade': (boolean, False),
        'AZMode': (str, False),
        'CacheNodeType': (str, True),
        'CacheParameterGroupName': (str, False),
        'CacheSecurityGroupNames': ([str], False),
        'CacheSubnetGroupName': (str, False),
        'ClusterName': (str, False),
        'Engine': (str, True),
        'EngineVersion': (str, False),
        'NotificationTopicArn': (str, False),
        'NumCacheNodes': (integer, True),
        'Port': (integer, False),
        'PreferredAvailabilityZone': (str, False),
        'PreferredAvailabilityZones': ([str], False),
        'PreferredMaintenanceWindow': (str, False),
        'SnapshotArns': ([str], False),
        'SnapshotName': (str, False),
        'SnapshotRetentionLimit': (integer, False),
        'SnapshotWindow': (str, False),
        'Tags': (Tags, False),
        'VpcSecurityGroupIds': ([str], False),
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


class GlobalReplicationGroupMember(AWSProperty):
    props = {
        'ReplicationGroupId': (str, False),
        'ReplicationGroupRegion': (str, False),
        'Role': (str, False),
    }


class ReshardingConfiguration(AWSProperty):
    props = {
        'NodeGroupId': (str, False),
        'PreferredAvailabilityZones': ([str], False),
    }


class RegionalConfiguration(AWSProperty):
    props = {
        'ReplicationGroupId': (str, False),
        'ReplicationGroupRegion': (str, False),
        'ReshardingConfigurations': ([ReshardingConfiguration], False),
    }


class GlobalReplicationGroup(AWSObject):
    resource_type = "AWS::ElastiCache::GlobalReplicationGroup"

    props = {
        'AutomaticFailoverEnabled': (boolean, False),
        'CacheNodeType': (str, False),
        'CacheParameterGroupName': (str, False),
        'EngineVersion': (str, False),
        'GlobalNodeGroupCount': (integer, False),
        'GlobalReplicationGroupDescription': (str, False),
        'GlobalReplicationGroupIdSuffix': (str, False),
        'Members': ([GlobalReplicationGroupMember], True),
        'RegionalConfigurations': ([RegionalConfiguration], False),
    }


class ParameterGroup(AWSObject):
    resource_type = "AWS::ElastiCache::ParameterGroup"

    props = {
        'CacheParameterGroupFamily': (str, True),
        'Description': (str, True),
        'Properties': (dict, True),
    }


class SecurityGroup(AWSObject):
    resource_type = "AWS::ElastiCache::SecurityGroup"

    props = {
        'Description': (str, False),
    }


class SecurityGroupIngress(AWSObject):
    resource_type = "AWS::ElastiCache::SecurityGroupIngress"

    props = {
        'CacheSecurityGroupName': (str, True),
        'EC2SecurityGroupName': (str, True),
        'EC2SecurityGroupOwnerId': (str, False),
    }


class SubnetGroup(AWSObject):
    resource_type = "AWS::ElastiCache::SubnetGroup"

    props = {
        'CacheSubnetGroupName': (str, False),
        'Description': (str, True),
        'SubnetIds': (list, True),
    }


class NodeGroupConfiguration(AWSProperty):
    props = {
        'NodeGroupId': (validate_node_group_id, False),
        'PrimaryAvailabilityZone': (str, False),
        'ReplicaAvailabilityZones': ([str], False),
        'ReplicaCount': (integer, False),
        'Slots': (str, False),
    }


class ReplicationGroup(AWSObject):
    resource_type = "AWS::ElastiCache::ReplicationGroup"

    props = {
        'AtRestEncryptionEnabled': (boolean, False),
        'AuthToken': (str, False),
        'AutoMinorVersionUpgrade': (boolean, False),
        'AutomaticFailoverEnabled': (boolean, False),
        'CacheNodeType': (str, False),
        'CacheParameterGroupName': (str, False),
        'CacheSecurityGroupNames': ([str], False),
        'CacheSubnetGroupName': (str, False),
        'Engine': (str, False),
        'EngineVersion': (str, False),
        'KmsKeyId': (str, False),
        'MultiAZEnabled': (boolean, False),
        'NodeGroupConfiguration': ([NodeGroupConfiguration], False),
        'NotificationTopicArn': (str, False),
        'NumCacheClusters': (integer, False),
        'NumNodeGroups': (integer, False),
        'Port': (network_port, False),
        'PreferredCacheClusterAZs': ([str], False),
        'PreferredMaintenanceWindow': (str, False),
        'PrimaryClusterId': (str, False),
        'ReplicasPerNodeGroup': (integer, False),
        'ReplicationGroupDescription': (str, True),
        'ReplicationGroupId': (str, False),
        'SecurityGroupIds': ([str], False),
        'SnapshotArns': ([str], False),
        'SnapshotName': (str, False),
        'SnapshotRetentionLimit': (integer, False),
        'SnapshotWindow': (str, False),
        'SnapshottingClusterId': (str, False),
        'Tags': (Tags, False),
        'TransitEncryptionEnabled': (boolean, False),
        'UserGroupIds': ([str], False),
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
