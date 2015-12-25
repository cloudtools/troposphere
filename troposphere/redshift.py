# Copyright (c) 2014, Guillem Anguera <ganguera@gmail.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, integer


class Cluster(AWSObject):
    resource_type = "AWS::Redshift::Cluster"

    props = {
        'AllowVersionUpgrade': (boolean, False),
        'AutomatedSnapshotRetentionPeriod': (integer, False),
        'AvailabilityZone': (basestring, False),
        'ClusterParameterGroupName': (basestring, False),
        'ClusterSecurityGroups': (list, False),
        'ClusterSubnetGroupName': (basestring, False),
        'ClusterType': (basestring, True),
        'ClusterVersion': (basestring, False),
        'DBName': (basestring, True),
        'ElasticIp': (basestring, False),
        'Encrypted': (boolean, False),
        'HsmClientCertificateIdentifier': (basestring, False),
        'HsmConfigurationIdentifier': (basestring, False),
        'KmsKeyId': (basestring, False),
        'MasterUsername': (basestring, True),
        'MasterUserPassword': (basestring, True),
        'NodeType': (basestring, True),
        'NumberOfNodes': (integer, False),  # Conditional
        'OwnerAccount': (basestring, False),
        'Port': (integer, False),
        'PreferredMaintenanceWindow': (basestring, False),
        'PubliclyAccessible': (boolean, False),
        'SnapshotClusterIdentifier': (basestring, False),
        'SnapshotIdentifier': (basestring, False),
        'VpcSecurityGroupIds': (list, False),
    }


class AmazonRedshiftParameter(AWSProperty):
    props = {
        'ParameterName': (basestring, True),
        'ParameterValue': (basestring, True),
    }


class ClusterParameterGroup(AWSObject):
    resource_type = "AWS::Redshift::ClusterParameterGroup"

    props = {
        'Description': (basestring, True),
        'ParameterGroupFamily': (basestring, True),
        'Parameters': ([AmazonRedshiftParameter], False),
    }


class ClusterSecurityGroup(AWSObject):
    resource_type = "AWS::Redshift::ClusterSecurityGroup"

    props = {
        'Description': (basestring, True),
    }


class ClusterSecurityGroupIngress(AWSObject):
    resource_type = "AWS::Redshift::ClusterSecurityGroupIngress"

    props = {
        'ClusterSecurityGroupName': (basestring, True),
        'CIDRIP': (basestring, False),
        'EC2SecurityGroupName': (basestring, False),
        'EC2SecurityGroupOwnerId': (basestring, False),
    }


class ClusterSubnetGroup(AWSObject):
    resource_type = "AWS::Redshift::ClusterSubnetGroup"

    props = {
        'Description': (basestring, True),
        'SubnetIds': (list, True),
    }
