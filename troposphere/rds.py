# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty
from .validators import boolean


class DBInstance(AWSObject):
    props = {
        'AllocatedStorage': (basestring, True),
        'AutoMinorVersionUpgrade': (bool, False),
        'AvailabilityZone': (basestring, False),
        'BackupRetentionPeriod': (basestring, False),
        'DBInstanceClass': (basestring, True),
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
        'Tags': (list, False),
        'VPCSecurityGroups': ([basestring, AWSHelperFn], False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::RDS::DBInstance"
        sup = super(DBInstance, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class DBParameterGroup(AWSObject):
    props = {
        'Description': (basestring, False),
        'Family': (basestring, False),
        'Parameters': (dict, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::RDS::DBParameterGroup"
        sup = super(DBParameterGroup, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class DBSubnetGroup(AWSObject):
    props = {
        'DBSubnetGroupDescription': (basestring, True),
        'SubnetIds': (list, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::RDS::DBSubnetGroup"
        sup = super(DBSubnetGroup, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class RDSSecurityGroup(AWSProperty):
    props = {
        'CIDRIP': (basestring, False),
        'EC2SecurityGroupId': (basestring, False),
        'EC2SecurityGroupName': (basestring, False),
        'EC2SecurityGroupOwnerId': (basestring, False),
    }


class DBSecurityGroup(AWSObject):
    props = {
        'EC2VpcId': (basestring, False),
        'DBSecurityGroupIngress': (list, True),
        'GroupDescription': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::RDS::DBSecurityGroup"
        sup = super(DBSecurityGroup, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class DBSecurityGroupIngress(AWSObject):
    props = {
        'CIDRIP': (basestring, False),
        'DBSecurityGroupName': (basestring, True),
        'EC2SecurityGroupId': (basestring, True),
        'EC2SecurityGroupName': (basestring, True),
        'EC2SecurityGroupOwnerId': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::RDS::DBSecurityGroupIngress"
        sup = super(DBSecurityGroupIngress, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)
