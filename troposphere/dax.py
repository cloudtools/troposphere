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
        'AvailabilityZones': (basestring, False),
        'ClusterName': (basestring, False),
        'Description': (basestring, False),
        'IAMRoleARN': (basestring, True),
        'NodeType': (basestring, True),
        'NotificationTopicARN': (basestring, False),
        'ParameterGroupName': (basestring, False),
        'PreferredMaintenanceWindow': (basestring, False),
        'ReplicationFactor': (basestring, True),
        'SSESpecification': (SSESpecification, False),
        'SecurityGroupIds': ([basestring], False),
        'SubnetGroupName': (basestring, True),
        'Tags': (dict, False),
    }


class ParameterGroup(AWSObject):
    resource_type = "AWS::DAX::ParameterGroup"

    props = {
        'Description': (basestring, False),
        'ParameterGroupName': (basestring, False),
        'ParameterNameValues': (dict, False),
    }


class SubnetGroup(AWSObject):
    resource_type = "AWS::DAX::SubnetGroup"

    props = {
        'Description': (basestring, False),
        'SubnetGroupName': (basestring, False),
        'SubnetIds': ([basestring], False),
    }
