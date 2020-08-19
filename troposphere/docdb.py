# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, Tags
from .validators import boolean, integer


class DBCluster(AWSObject):
    resource_type = "AWS::DocDB::DBCluster"

    props = {
        'AvailabilityZones': ([basestring], False),
        'BackupRetentionPeriod': (integer, False),
        'DBClusterIdentifier': (basestring, False),
        'DBClusterParameterGroupName': (basestring, False),
        'DBSubnetGroupName': (basestring, False),
        'DeletionProtection': (boolean, False),
        'EnableCloudwatchLogsExports': ([basestring], False),
        'EngineVersion': (basestring, False),
        'KmsKeyId': (basestring, False),
        'MasterUserPassword': (basestring, False),
        'MasterUsername': (basestring, False),
        'Port': (integer, False),
        'PreferredBackupWindow': (basestring, False),
        'PreferredMaintenanceWindow': (basestring, False),
        'SnapshotIdentifier': (basestring, False),
        'StorageEncrypted': (boolean, False),
        'Tags': (Tags, False),
        'VpcSecurityGroupIds': ([basestring], False),
    }


class DBClusterParameterGroup(AWSObject):
    resource_type = "AWS::DocDB::DBClusterParameterGroup"

    props = {
        'Description': (basestring, True),
        'Family': (basestring, True),
        'Name': (basestring, False),
        'Parameters': (dict, True),
        'Tags': (Tags, False),
    }


class DBInstance(AWSObject):
    resource_type = "AWS::DocDB::DBInstance"

    props = {
        'AutoMinorVersionUpgrade': (boolean, False),
        'AvailabilityZone': (basestring, False),
        'DBClusterIdentifier': (basestring, True),
        'DBInstanceClass': (basestring, True),
        'DBInstanceIdentifier': (basestring, False),
        'PreferredMaintenanceWindow': (basestring, False),
        'Tags': (Tags, False),
    }


class DBSubnetGroup(AWSObject):
    resource_type = "AWS::DocDB::DBSubnetGroup"

    props = {
        'DBSubnetGroupDescription': (basestring, True),
        'DBSubnetGroupName': (basestring, False),
        'SubnetIds': ([basestring], True),
        'Tags': (Tags, False),
    }
