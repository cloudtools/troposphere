# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject
from .validators import boolean, integer
from troposphere import Tags


class DBClusterParameterGroup(AWSObject):
    resource_type = "AWS::Neptune::DBClusterParameterGroup"

    props = {
        'Description': (str, True),
        'Family': (str, True),
        'Name': (str, False),
        'Parameters': (dict, True),
        'Tags': (Tags, False),
    }


class DBCluster(AWSObject):
    resource_type = "AWS::Neptune::DBCluster"

    props = {
        'AvailabilityZones': ([str], False),
        'BackupRetentionPeriod': (integer, False),
        'DBClusterIdentifier': (str, False),
        'DBClusterParameterGroupName': (str, False),
        'DBSubnetGroupName': (str, False),
        'DeletionProtection': (boolean, False),
        'EnableCloudwatchLogsExports': ([str], False),
        'EngineVersion': (str, False),
        'IamAuthEnabled': (boolean, False),
        'KmsKeyId': (str, False),
        'Port': (integer, False),
        'PreferredBackupWindow': (str, False),
        'PreferredMaintenanceWindow': (str, False),
        'SnapshotIdentifier': (str, False),
        'StorageEncrypted': (boolean, False),
        'Tags': (Tags, False),
        'VpcSecurityGroupIds': ([str], False),
    }


class DBInstance(AWSObject):
    resource_type = "AWS::Neptune::DBInstance"

    props = {
        'AllowMajorVersionUpgrade': (boolean, False),
        'AutoMinorVersionUpgrade': (boolean, False),
        'AvailabilityZone': (str, False),
        'DBClusterIdentifier': (str, False),
        'DBInstanceClass': (str, True),
        'DBInstanceIdentifier': (str, False),
        'DBParameterGroupName': (str, False),
        'DBSnapshotIdentifier': (str, False),
        'DBSubnetGroupName': (str, False),
        'PreferredMaintenanceWindow': (str, False),
        'Tags': (Tags, False),
    }


class DBParameterGroup(AWSObject):
    resource_type = "AWS::Neptune::DBParameterGroup"

    props = {
        'Description': (str, True),
        'Family': (str, True),
        'Name': (str, False),
        'Parameters': (dict, True),
        'Tags': (Tags, False),
    }


class DBSubnetGroup(AWSObject):
    resource_type = "AWS::Neptune::DBSubnetGroup"

    props = {
        'DBSubnetGroupDescription': (str, True),
        'DBSubnetGroupName': (str, False),
        'SubnetIds': ([str], True),
        'Tags': (Tags, False),
    }
