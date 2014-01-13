# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty
from .validators import boolean


class DBInstance(AWSObject):
    type = "AWS::RDS::DBInstance"

    props = {
        'AllocatedStorage': (basestring, True),
        'AutoMinorVersionUpgrade': (boolean, False),
        'AvailabilityZone': (basestring, False),
        'BackupRetentionPeriod': (basestring, False),
        'DBInstanceClass': (basestring, True),
        'DBInstanceIdentifier': (basestring, False),
        'DBName': (basestring, False),
        'DBParameterGroupName': (basestring, False),
        'DBSecurityGroups': (list, False),
        'DBSnapshotIdentifier': (basestring, False),
        'DBSubnetGroupName': (basestring, False),
        'Engine': (basestring, True),
        'EngineVersion': (basestring, False),
        'Iops': (int, False),
        'LicenseModel': (basestring, False),
        'MasterUsername': (basestring, True),
        'MasterUserPassword': (basestring, True),
        'MultiAZ': (boolean, False),
        'Port': (basestring, False),
        'PreferredBackupWindow': (basestring, False),
        'PreferredMaintenanceWindow': (basestring, False),
        'SourceDBInstanceIdentifier': (basestring, False),
        'Tags': (list, False),
        'VPCSecurityGroups': ([basestring, AWSHelperFn], False),
    }


class DBParameterGroup(AWSObject):
    type = "AWS::RDS::DBParameterGroup"

    props = {
        'Description': (basestring, False),
        'Family': (basestring, False),
        'Parameters': (dict, False),
        'Tags': (list, False),
    }


class DBSubnetGroup(AWSObject):
    type = "AWS::RDS::DBSubnetGroup"

    props = {
        'DBSubnetGroupDescription': (basestring, True),
        'SubnetIds': (list, True),
        'Tags': (list, False),
    }


class RDSSecurityGroup(AWSProperty):
    props = {
        'CIDRIP': (basestring, False),
        'EC2SecurityGroupId': (basestring, False),
        'EC2SecurityGroupName': (basestring, False),
        'EC2SecurityGroupOwnerId': (basestring, False),
    }


class DBSecurityGroup(AWSObject):
    type = "AWS::RDS::DBSecurityGroup"

    props = {
        'EC2VpcId': (basestring, False),
        'DBSecurityGroupIngress': (list, True),
        'GroupDescription': (basestring, True),
        'Tags': (list, False),
    }


class DBSecurityGroupIngress(AWSObject):
    type = "AWS::RDS::DBSecurityGroupIngress"

    props = {
        'CIDRIP': (basestring, False),
        'DBSecurityGroupName': (basestring, True),
        'EC2SecurityGroupId': (basestring, True),
        'EC2SecurityGroupName': (basestring, True),
        'EC2SecurityGroupOwnerId': (basestring, True),
    }
