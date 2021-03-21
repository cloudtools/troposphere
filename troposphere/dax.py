# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean


class SSESpecification(AWSProperty):
    props = {
        'SSEEnabled': (boolean, False),
    }


class Cluster(AWSObject):
    resource_type = "AWS::DAX::Cluster"

    props = {
        'AvailabilityZones': (str, False),
        'ClusterName': (str, False),
        'Description': (str, False),
        'IAMRoleARN': (str, True),
        'NodeType': (str, True),
        'NotificationTopicARN': (str, False),
        'ParameterGroupName': (str, False),
        'PreferredMaintenanceWindow': (str, False),
        'ReplicationFactor': (str, True),
        'SSESpecification': (SSESpecification, False),
        'SecurityGroupIds': ([str], False),
        'SubnetGroupName': (str, True),
        'Tags': (dict, False),
    }


class ParameterGroup(AWSObject):
    resource_type = "AWS::DAX::ParameterGroup"

    props = {
        'Description': (str, False),
        'ParameterGroupName': (str, False),
        'ParameterNameValues': (dict, False),
    }


class SubnetGroup(AWSObject):
    resource_type = "AWS::DAX::SubnetGroup"

    props = {
        'Description': (str, False),
        'SubnetGroupName': (str, False),
        'SubnetIds': ([str], False),
    }
