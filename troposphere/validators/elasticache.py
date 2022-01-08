# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import re

from . import network_port


def validate_network_port(x):
    """
    Property: ReplicationGroup.Port
    """
    return network_port(x)


def validate_node_group_id(node_group_id):
    """
    Property: NodeGroupConfiguration.NodeGroupId
    """

    if re.match(r"\d{1,4}", node_group_id):
        return node_group_id
    raise ValueError("Invalid NodeGroupId: %s" % node_group_id)


def validate_cache_cluster(self):
    """
    Class: CacheCluster
    """

    # Check that AZMode is "cross-az" if more than one Availability zone
    # is specified in PreferredAvailabilityZones
    preferred_azs = self.properties.get("PreferredAvailabilityZones")
    if (
        preferred_azs is not None
        and isinstance(preferred_azs, list)
        and len(preferred_azs) > 1
    ):
        if self.properties.get("AZMode") != "cross-az":
            raise ValueError(
                'AZMode must be "cross-az" if more than one a'
                "vailability zone is specified in PreferredAv"
                "ailabilityZones: http://docs.aws.amazon.com/"
                "AWSCloudFormation/latest/UserGuide/aws-prope"
                "rties-elasticache-cache-cluster.html#cfn-ela"
                "sticache-cachecluster-azmode"
            )


def validate_replication_group(self):
    """
    Class: ReplicationGroup
    """

    if (
        "NumCacheClusters" not in self.properties
        and "NumNodeGroups" not in self.properties
        and "ReplicasPerNodeGroup" not in self.properties
        and "PrimaryClusterId" not in self.properties
    ):
        raise ValueError(
            "One of PrimaryClusterId, NumCacheClusters, "
            "NumNodeGroups or ReplicasPerNodeGroup are required"
            "in type AWS::ElastiCache::ReplicationGroup"
        )
