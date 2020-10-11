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
        'Description': (basestring, True),
        'Family': (basestring, True),
        'Name': (basestring, False),
        'Parameters': (dict, True),
        'Tags': (Tags, False),
    }


class DBCluster(AWSObject):
    resource_type = "AWS::Neptune::DBCluster"

    props = {
        'AvailabilityZones': ([basestring], False),
        'BackupRetentionPeriod': (integer, False),
        'DBClusterIdentifier': (basestring, False),
        'DBClusterParameterGroupName': (basestring, False),
        'DBSubnetGroupName': (basestring, False),
        'DeletionProtection': (boolean, False),
        'EnableCloudwatchLogsExports': ([basestring], False),
        'EngineVersion': (basestring, False),
        'IamAuthEnabled': (boolean, False),
        'KmsKeyId': (basestring, False),
        'Port': (integer, False),
        'PreferredBackupWindow': (basestring, False),
        'PreferredMaintenanceWindow': (basestring, False),
        'SnapshotIdentifier': (basestring, False),
        'StorageEncrypted': (boolean, False),
        'Tags': (Tags, False),
        'VpcSecurityGroupIds': ([basestring], False),
    }


class DBInstance(AWSObject):
    resource_type = "AWS::Neptune::DBInstance"

    props = {
        'AllowMajorVersionUpgrade': (boolean, False),
        'AutoMinorVersionUpgrade': (boolean, False),
        'AvailabilityZone': (basestring, False),
        'DBClusterIdentifier': (basestring, False),
        'DBInstanceClass': (basestring, True),
        'DBInstanceIdentifier': (basestring, False),
        'DBParameterGroupName': (basestring, False),
        'DBSnapshotIdentifier': (basestring, False),
        'DBSubnetGroupName': (basestring, False),
        'PreferredMaintenanceWindow': (basestring, False),
        'Tags': (Tags, False),
    }


class DBParameterGroup(AWSObject):
    resource_type = "AWS::Neptune::DBParameterGroup"

    props = {
        'Description': (basestring, True),
        'Family': (basestring, True),
        'Name': (basestring, False),
        'Parameters': (dict, True),
        'Tags': (Tags, False),
    }


class DBSubnetGroup(AWSObject):
    resource_type = "AWS::Neptune::DBSubnetGroup"

    props = {
        'DBSubnetGroupDescription': (basestring, True),
        'DBSubnetGroupName': (basestring, False),
        'SubnetIds': ([basestring], True),
        'Tags': (Tags, False),
    }
