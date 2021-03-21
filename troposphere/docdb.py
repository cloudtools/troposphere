# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, Tags
from .validators import boolean, integer


class DBCluster(AWSObject):
    resource_type = "AWS::DocDB::DBCluster"

    props = {
        'AvailabilityZones': ([str], False),
        'BackupRetentionPeriod': (integer, False),
        'DBClusterIdentifier': (str, False),
        'DBClusterParameterGroupName': (str, False),
        'DBSubnetGroupName': (str, False),
        'DeletionProtection': (boolean, False),
        'EnableCloudwatchLogsExports': ([str], False),
        'EngineVersion': (str, False),
        'KmsKeyId': (str, False),
        'MasterUserPassword': (str, False),
        'MasterUsername': (str, False),
        'Port': (integer, False),
        'PreferredBackupWindow': (str, False),
        'PreferredMaintenanceWindow': (str, False),
        'SnapshotIdentifier': (str, False),
        'StorageEncrypted': (boolean, False),
        'Tags': (Tags, False),
        'VpcSecurityGroupIds': ([str], False),
    }


class DBClusterParameterGroup(AWSObject):
    resource_type = "AWS::DocDB::DBClusterParameterGroup"

    props = {
        'Description': (str, True),
        'Family': (str, True),
        'Name': (str, False),
        'Parameters': (dict, True),
        'Tags': (Tags, False),
    }


class DBInstance(AWSObject):
    resource_type = "AWS::DocDB::DBInstance"

    props = {
        'AutoMinorVersionUpgrade': (boolean, False),
        'AvailabilityZone': (str, False),
        'DBClusterIdentifier': (str, True),
        'DBInstanceClass': (str, True),
        'DBInstanceIdentifier': (str, False),
        'PreferredMaintenanceWindow': (str, False),
        'Tags': (Tags, False),
    }


class DBSubnetGroup(AWSObject):
    resource_type = "AWS::DocDB::DBSubnetGroup"

    props = {
        'DBSubnetGroupDescription': (str, True),
        'DBSubnetGroupName': (str, False),
        'SubnetIds': ([str], True),
        'Tags': (Tags, False),
    }
