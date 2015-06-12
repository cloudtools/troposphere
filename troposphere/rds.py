# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty, Ref
from .validators import boolean, network_port, integer, positive_integer


class DBInstance(AWSObject):
    resource_type = "AWS::RDS::DBInstance"

    props = {
        'AllocatedStorage': (positive_integer, True),
        'AllowMajorVersionUpgrade': (boolean, False),
        'AutoMinorVersionUpgrade': (boolean, False),
        'AvailabilityZone': (basestring, False),
        'BackupRetentionPeriod': (positive_integer, False),
        'CharacterSetName': (basestring, False),
        'DBInstanceClass': (basestring, True),
        'DBInstanceIdentifier': (basestring, False),
        'DBName': (basestring, False),
        'DBParameterGroupName': (basestring, False),
        'DBSecurityGroups': (list, False),
        'DBSnapshotIdentifier': (basestring, False),
        'DBSubnetGroupName': (basestring, False),
        'Engine': (basestring, True),
        'EngineVersion': (basestring, False),
        'Iops': (integer, False),
        'KmsKeyId': (basestring, False),
        'LicenseModel': (basestring, False),
        'MasterUsername': (basestring, False),
        'MasterUserPassword': (basestring, False),
        'MultiAZ': (boolean, False),
        'OptionGroupName': (basestring, False),
        'Port': (network_port, False),
        'PreferredBackupWindow': (basestring, False),
        'PreferredMaintenanceWindow': (basestring, False),
        'PubliclyAccessible': (boolean, False),
        'SourceDBInstanceIdentifier': (basestring, False),
        'StorageEncrypted': (boolean, False),
        'StorageType': (basestring, False),
        'Tags': (list, False),
        'VPCSecurityGroups': ([basestring, AWSHelperFn], False),
    }

    def validate(self):
        if 'SourceDBInstanceIdentifier' in self.properties:

            invalid_replica_properties = (
                'BackupRetentionPeriod', 'DBName', 'MasterUsername',
                'MasterUserPassword', 'PreferredBackupWindow', 'MultiAZ',
                'DBSnapshotIdentifier', 'DBSubnetGroupName',
            )

            invalid_properties = [s for s in self.properties.keys() if
                                  s in invalid_replica_properties]

            if invalid_properties:
                raise ValueError(
                    ('{0} properties can\'t be provided when '
                     'SourceDBInstanceIdentifier is present '
                     'AWS::RDS::DBInstance.'
                     ).format(', '.join(sorted(invalid_properties))))

        if ('DBSnapshotIdentifier' not in self.properties and
            'SourceDBInstanceIdentifier' not in self.properties) and \
            ('MasterUsername' not in self.properties or
             'MasterUserPassword' not in self.properties):
            raise ValueError(
                'Either (MasterUsername and MasterUserPassword) or'
                ' DBSnapshotIdentifier are required in type '
                'AWS::RDS::DBInstance.'
            )

        if 'KmsKeyId' in self.properties and \
           'StorageEncrypted' not in self.properties:
            raise ValueError(
                'If KmsKeyId is provided, StorageEncrypted is required '
                'AWS::RDS::DBInstance.'
            )

        return True


class DBParameterGroup(AWSObject):
    resource_type = "AWS::RDS::DBParameterGroup"

    props = {
        'Description': (basestring, False),
        'Family': (basestring, False),
        'Parameters': (dict, False),
        'Tags': (list, False),
    }


class DBSubnetGroup(AWSObject):
    resource_type = "AWS::RDS::DBSubnetGroup"

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
    resource_type = "AWS::RDS::DBSecurityGroup"

    props = {
        'EC2VpcId': (basestring, False),
        'DBSecurityGroupIngress': (list, True),
        'GroupDescription': (basestring, True),
        'Tags': (list, False),
    }


class DBSecurityGroupIngress(AWSObject):
    resource_type = "AWS::RDS::DBSecurityGroupIngress"

    props = {
        'CIDRIP': (basestring, False),
        'DBSecurityGroupName': (basestring, True),
        'EC2SecurityGroupId': (basestring, False),
        'EC2SecurityGroupName': (basestring, False),
        'EC2SecurityGroupOwnerId': (basestring, False),
    }


class EventSubscription(AWSObject):
    resource_type = "AWS::RDS::EventSubscription"

    props = {
        'Enabled': (boolean, False),
        'EventCategories': ([basestring], False),
        'SnsTopicArn': (basestring, True),
        'SourceIds': ([basestring, Ref], False),
        'SourceType': (basestring, False),
    }


class OptionSetting(AWSProperty):
    props = {
        'Name': (basestring, False),
        'Value': (basestring, False),
    }


class OptionGroupConfiguration(AWSProperty):
    props = {
        'DBSecurityGroupMemberships': ([basestring, Ref], False),
        'OptionName': (basestring, True),
        'OptionSettings': ([OptionSetting], False),
        'Port': (network_port, False),
        'VpcSecurityGroupMemberships': ([basestring, Ref], False),
    }


class OptionGroup(AWSObject):
    resource_type = "AWS::RDS::OptionGroup"

    props = {
        'EngineName': (basestring, True),
        'MajorEngineVersion': (basestring, True),
        'OptionGroupDescription': (basestring, True),
        'OptionGroupConfigurations': ([OptionGroupConfiguration], True),
        'Tags': (list, False),
    }
