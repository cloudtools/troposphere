# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty
from .validators import boolean, network_port, positive_integer


class DBInstance(AWSObject):
    type = "AWS::RDS::DBInstance"

    props = {
        'AllocatedStorage': (positive_integer, True),
        'AllowMajorVersionUpgrade': (boolean, False),
        'AutoMinorVersionUpgrade': (boolean, False),
        'AvailabilityZone': (basestring, False),
        'BackupRetentionPeriod': (positive_integer, False),
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
        'MasterUsername': (basestring, False),
        'MasterUserPassword': (basestring, False),
        'MultiAZ': (boolean, False),
        'Port': (network_port, False),
        'PreferredBackupWindow': (basestring, False),
        'PreferredMaintenanceWindow': (basestring, False),
        'PubliclyAccessible': (boolean, False),
        'SourceDBInstanceIdentifier': (basestring, False),
        'Tags': (list, False),
        'VPCSecurityGroups': ([basestring, AWSHelperFn], False),
    }

    def validate(self):
        if 'DBSnapshotIdentifier' not in self.properties and \
            ('MasterUsername' not in self.properties or
             'MasterUserPassword' not in self.properties):
            raise ValueError(
                'Either (MasterUsername and MasterUserPassword) or'
                ' DBSnapshotIdentifier are required in type '
                'AWS::RDS::DBInstance.'
            )

        return True


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
