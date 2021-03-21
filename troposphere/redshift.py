# Copyright (c) 2014, Guillem Anguera <ganguera@gmail.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer


class LoggingProperties(AWSProperty):
    props = {
        'BucketName': (str, True),
        'S3KeyPrefix': (str, False),
    }


class Cluster(AWSObject):
    resource_type = "AWS::Redshift::Cluster"

    props = {
        'AllowVersionUpgrade': (boolean, False),
        'AutomatedSnapshotRetentionPeriod': (integer, False),
        'AvailabilityZone': (str, False),
        'ClusterIdentifier': (str, False),
        'ClusterParameterGroupName': (str, False),
        'ClusterSecurityGroups': (list, False),
        'ClusterSubnetGroupName': (str, False),
        'ClusterType': (str, True),
        'ClusterVersion': (str, False),
        'DBName': (str, True),
        'ElasticIp': (str, False),
        'Encrypted': (boolean, False),
        'HsmClientCertificateIdentifier': (str, False),
        'HsmConfigurationIdentifier': (str, False),
        'IamRoles': ([str], False),
        'KmsKeyId': (str, False),
        'LoggingProperties': (LoggingProperties, False),
        'MasterUsername': (str, True),
        'MasterUserPassword': (str, True),
        'NodeType': (str, True),
        'NumberOfNodes': (integer, False),  # Conditional
        'OwnerAccount': (str, False),
        'Port': (integer, False),
        'PreferredMaintenanceWindow': (str, False),
        'PubliclyAccessible': (boolean, False),
        'SnapshotClusterIdentifier': (str, False),
        'SnapshotIdentifier': (str, False),
        'Tags': (Tags, False),
        'VpcSecurityGroupIds': (list, False),
    }


class AmazonRedshiftParameter(AWSProperty):
    props = {
        'ParameterName': (str, True),
        'ParameterValue': (str, True),
    }


class ClusterParameterGroup(AWSObject):
    resource_type = "AWS::Redshift::ClusterParameterGroup"

    props = {
        'Description': (str, True),
        'ParameterGroupFamily': (str, True),
        'Parameters': ([AmazonRedshiftParameter], False),
        'Tags': (Tags, False),
    }


class ClusterSecurityGroup(AWSObject):
    resource_type = "AWS::Redshift::ClusterSecurityGroup"

    props = {
        'Description': (str, True),
        'Tags': (Tags, False),
    }


class ClusterSecurityGroupIngress(AWSObject):
    resource_type = "AWS::Redshift::ClusterSecurityGroupIngress"

    props = {
        'ClusterSecurityGroupName': (str, True),
        'CIDRIP': (str, False),
        'EC2SecurityGroupName': (str, False),
        'EC2SecurityGroupOwnerId': (str, False),
    }


class ClusterSubnetGroup(AWSObject):
    resource_type = "AWS::Redshift::ClusterSubnetGroup"

    props = {
        'Description': (str, True),
        'SubnetIds': (list, True),
        'Tags': (Tags, False),
    }
