# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import re

from . import AWSHelperFn, AWSObject, AWSProperty, Tags
from .validators import (boolean, network_port, integer, positive_integer,
                         integer_range)

# Taken from:
# http://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html

VALID_STORAGE_TYPES = ('standard', 'gp2', 'io1')
VALID_DB_ENGINES = ('MySQL', 'mysql', 'oracle-se1', 'oracle-se2', 'oracle-se',
                    'oracle-ee', 'sqlserver-ee', 'sqlserver-se',
                    'sqlserver-ex', 'sqlserver-web', 'postgres', 'aurora',
                    'aurora-mysql', 'aurora-postgresql', 'mariadb')
VALID_DB_ENGINE_MODES = ('provisioned', 'serverless', 'parallelquery',
                         'global', 'multimaster')
VALID_LICENSE_MODELS = ('license-included', 'bring-your-own-license',
                        'general-public-license', 'postgresql-license')
VALID_MYSQL_SCALING_CONFIGURATION_CAPACITIES = (1, 2, 4, 8, 16, 32, 64, 128,
                                                256)
VALID_POSTGRESL_SCALING_CONFIGURATION_CAPACITIES = (2, 4, 8, 16, 32, 64, 192,
                                                    384)


def validate_iops(iops):
    """DBInstance Iops validation rules."""

    iops = integer(iops)
    if int(iops) == 0:
        return iops
    if int(iops) < 1000:
        raise ValueError("DBInstance Iops, if set, must be greater than 1000.")
    return iops


def validate_storage_type(storage_type):
    """Validate StorageType for DBInstance"""

    if storage_type not in VALID_STORAGE_TYPES:
        raise ValueError("DBInstance StorageType must be one of: %s" %
                         ", ".join(VALID_STORAGE_TYPES))
    return storage_type


def validate_engine(engine):
    """Validate database Engine for DBInstance """

    if engine not in VALID_DB_ENGINES:
        raise ValueError("DBInstance Engine must be one of: %s" %
                         ", ".join(VALID_DB_ENGINES))
    return engine


def validate_engine_mode(engine_mode):
    """Validate database EngineMode for DBCluster"""

    if engine_mode not in VALID_DB_ENGINE_MODES:
        raise ValueError("DBCluster EngineMode must be one of: %s" %
                         ", ".join(VALID_DB_ENGINE_MODES))
    return engine_mode


def validate_license_model(license_model):
    """Validate LicenseModel for DBInstance"""

    if license_model not in VALID_LICENSE_MODELS:
        raise ValueError("DBInstance LicenseModel must be one of: %s" %
                         ", ".join(VALID_LICENSE_MODELS))
    return license_model


def validate_backup_window(window):
    """Validate PreferredBackupWindow for DBInstance"""

    hour = r'[01]?[0-9]|2[0-3]'
    minute = r'[0-5][0-9]'
    r = ("(?P<start_hour>%s):(?P<start_minute>%s)-"
         "(?P<end_hour>%s):(?P<end_minute>%s)") % (hour, minute, hour, minute)
    range_regex = re.compile(r)
    m = range_regex.match(window)
    if not m:
        raise ValueError("DBInstance PreferredBackupWindow must be in the "
                         "format: hh24:mi-hh24:mi")
    start_ts = (int(m.group('start_hour')) * 60) + int(m.group('start_minute'))
    end_ts = (int(m.group('end_hour')) * 60) + int(m.group('end_minute'))
    if abs(end_ts - start_ts) < 30:
        raise ValueError("DBInstance PreferredBackupWindow must be at least "
                         "30 minutes long.")
    return window


def validate_maintenance_window(window):
    """Validate PreferredMaintenanceWindow for DBInstance"""

    days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    day_re = r'[A-Z]{1}[a-z]{2}'
    hour = r'[01]?[0-9]|2[0-3]'
    minute = r'[0-5][0-9]'
    r = ("(?P<start_day>%s):(?P<start_hour>%s):(?P<start_minute>%s)-"
         "(?P<end_day>%s):(?P<end_hour>%s):(?P<end_minute>%s)") % (day_re,
                                                                   hour,
                                                                   minute,
                                                                   day_re,
                                                                   hour,
                                                                   minute)
    range_regex = re.compile(r)
    m = range_regex.match(window)
    if not m:
        raise ValueError("DBInstance PreferredMaintenanceWindow must be in "
                         "the format: ddd:hh24:mi-ddd:hh24:mi")
    if m.group('start_day') not in days or m.group('end_day') not in days:
        raise ValueError("DBInstance PreferredMaintenanceWindow day part of "
                         "ranges must be one of: %s" % ", ".join(days))
    start_ts = (days.index(m.group('start_day')) * 24 * 60) + \
        (int(m.group('start_hour')) * 60) + int(m.group('start_minute'))
    end_ts = (days.index(m.group('end_day')) * 24 * 60) + \
        (int(m.group('end_hour')) * 60) + int(m.group('end_minute'))
    if abs(end_ts - start_ts) < 30:
        raise ValueError("DBInstance PreferredMaintenanceWindow must be at "
                         "least 30 minutes long.")
    return window


def validate_backup_retention_period(days):
    """Validate BackupRetentionPeriod for DBInstance"""

    days = positive_integer(days)
    if int(days) > 35:
        raise ValueError("DBInstance BackupRetentionPeriod cannot be larger "
                         "than 35 days.")
    return days


def validate_capacity(capacity):
    """Validate ScalingConfiguration capacity for serverless DBCluster"""

    if capacity not in VALID_POSTGRESL_SCALING_CONFIGURATION_CAPACITIES and \
            capacity not in VALID_MYSQL_SCALING_CONFIGURATION_CAPACITIES:
        raise ValueError(
            "ScalingConfiguration capacity must be one of: {}".format(
                ", ".join(map(
                    str,
                    VALID_MYSQL_SCALING_CONFIGURATION_CAPACITIES +
                    VALID_POSTGRESL_SCALING_CONFIGURATION_CAPACITIES
                ))
            )
        )
    return capacity


class DBInstanceRole(AWSProperty):
    props = {
        'FeatureName': (str, True),
        'RoleArn': (str, True),
        'Status': (str, False),
    }


class ProcessorFeature(AWSProperty):
    props = {
        'Name': (str, False),
        'Value': (str, False),
    }


class DBInstance(AWSObject):
    resource_type = "AWS::RDS::DBInstance"

    props = {
        'AllocatedStorage': (positive_integer, False),
        'AllowMajorVersionUpgrade': (boolean, False),
        'AssociatedRoles': ([DBInstanceRole], False),
        'AutoMinorVersionUpgrade': (boolean, False),
        'AvailabilityZone': (str, False),
        'BackupRetentionPeriod': (validate_backup_retention_period, False),
        'CACertificateIdentifier': (str, False),
        'CharacterSetName': (str, False),
        'CopyTagsToSnapshot': (boolean, False),
        'DBClusterIdentifier': (str, False),
        'DBInstanceClass': (str, True),
        'DBInstanceIdentifier': (str, False),
        'DBName': (str, False),
        'DBParameterGroupName': (str, False),
        'DBSecurityGroups': (list, False),
        'DBSnapshotIdentifier': (str, False),
        'DBSubnetGroupName': (str, False),
        'DeleteAutomatedBackups': (boolean, False),
        'DeletionProtection': (boolean, False),
        'Domain': (str, False),
        'DomainIAMRoleName': (str, False),
        'EnableCloudwatchLogsExports': ([str], False),
        'EnableIAMDatabaseAuthentication': (boolean, False),
        'EnablePerformanceInsights': (boolean, False),
        'Engine': (validate_engine, False),
        'EngineVersion': (str, False),
        'Iops': (validate_iops, False),
        'KmsKeyId': (str, False),
        'LicenseModel': (validate_license_model, False),
        'MasterUsername': (str, False),
        'MasterUserPassword': (str, False),
        'MaxAllocatedStorage': (integer, False),
        'MonitoringInterval': (positive_integer, False),
        'MonitoringRoleArn': (str, False),
        'MultiAZ': (boolean, False),
        'OptionGroupName': (str, False),
        'PerformanceInsightsKMSKeyId': (str, False),
        'PerformanceInsightsRetentionPeriod': (positive_integer, False),
        'Port': (network_port, False),
        'PreferredBackupWindow': (validate_backup_window, False),
        'PreferredMaintenanceWindow': (str, False),
        'ProcessorFeatures': ([ProcessorFeature], False),
        'PromotionTier': (positive_integer, False),
        'PubliclyAccessible': (boolean, False),
        'SourceDBInstanceIdentifier': (str, False),
        'SourceRegion': (str, False),
        'StorageEncrypted': (boolean, False),
        'StorageType': (str, False),
        'Tags': ((Tags, list), False),
        'UseDefaultProcessorFeatures': (boolean, False),
        'Timezone': (str, False),
        'VPCSecurityGroups': ([str], False),
    }

    def validate(self):
        if 'DBSnapshotIdentifier' not in self.properties:
            if 'Engine' not in self.properties:
                raise ValueError(
                    'Resource Engine is required in type %s'
                    % self.resource_type)

        if 'SourceDBInstanceIdentifier' in self.properties:

            invalid_replica_properties = (
                'BackupRetentionPeriod', 'DBName', 'MasterUsername',
                'MasterUserPassword', 'PreferredBackupWindow', 'MultiAZ',
                'DBSnapshotIdentifier',
            )

            invalid_properties = [s for s in list(self.properties.keys()) if
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
             'MasterUserPassword' not in self.properties) and \
                ('DBClusterIdentifier' not in self.properties):
            raise ValueError(
                r"Either (MasterUsername and MasterUserPassword) or"
                r" DBSnapshotIdentifier are required in type "
                r"AWS::RDS::DBInstance."
            )

        if 'KmsKeyId' in self.properties and \
           'StorageEncrypted' not in self.properties:
            raise ValueError(
                'If KmsKeyId is provided, StorageEncrypted is required '
                'AWS::RDS::DBInstance.'
            )

        nonetype = type(None)
        avail_zone = self.properties.get('AvailabilityZone', None)
        multi_az = self.properties.get('MultiAZ', None)
        if not (isinstance(avail_zone, (AWSHelperFn, nonetype)) and
                isinstance(multi_az, (AWSHelperFn, nonetype))):
            if avail_zone and multi_az in [True, 1, '1', 'true', 'True']:
                raise ValueError("AvailabiltyZone cannot be set on "
                                 "DBInstance if MultiAZ is set to true.")

        storage_type = self.properties.get('StorageType', None)
        if storage_type and storage_type == 'io1' and \
                'Iops' not in self.properties:
            raise ValueError("Must specify Iops if using StorageType io1")

        allocated_storage = self.properties.get('AllocatedStorage')
        iops = self.properties.get('Iops', None)
        if iops and not isinstance(iops, AWSHelperFn):
            if not isinstance(allocated_storage, AWSHelperFn) and \
                    int(allocated_storage) < 100:
                raise ValueError("AllocatedStorage must be at least 100 when "
                                 "Iops is set.")
            if not isinstance(allocated_storage, AWSHelperFn) and not \
                    isinstance(iops, AWSHelperFn) and \
                    float(iops) / float(allocated_storage) > 50.0:
                raise ValueError("AllocatedStorage must be no less than "
                                 "1/50th the provisioned Iops")

        return True


class DBParameterGroup(AWSObject):
    resource_type = "AWS::RDS::DBParameterGroup"

    props = {
        'Description': (str, False),
        'Family': (str, False),
        'Parameters': (dict, False),
        'Tags': ((Tags, list), False),
    }


class AuthFormat(AWSProperty):
    props = {
        'AuthScheme': (str, False),
        'Description': (str, False),
        'IAMAuth': (str, False),
        'SecretArn': (str, False),
        'UserName': (str, False),
    }


class DBProxy(AWSObject):
    resource_type = "AWS::RDS::DBProxy"

    props = {
        'Auth': ([AuthFormat], True),
        'DBProxyName': (str, True),
        'DebugLogging': (boolean, False),
        'EngineFamily': (str, True),
        'IdleClientTimeout': (integer, False),
        'RequireTLS': (boolean, False),
        'RoleArn': (str, True),
        'Tags': (Tags, False),
        'VpcSecurityGroupIds': ([str], False),
        'VpcSubnetIds': ([str], True),
    }


class DBProxyEndpoint(AWSObject):
    resource_type = "AWS::RDS::DBProxyEndpoint"

    props = {
        'DBProxyEndpointName': (str, True),
        'DBProxyName': (str, True),
        'Tags': (Tags, False),
        'TargetRole': (str, False),
        'VpcSecurityGroupIds': ([str], False),
        'VpcSubnetIds': ([str], True),
    }


class ConnectionPoolConfigurationInfoFormat(AWSProperty):
    props = {
        'ConnectionBorrowTimeout': (integer, False),
        'InitQuery': (str, False),
        'MaxConnectionsPercent': (integer, False),
        'MaxIdleConnectionsPercent': (integer, False),
        'SessionPinningFilters': ([str], False),
    }


class DBProxyTargetGroup(AWSObject):
    resource_type = "AWS::RDS::DBProxyTargetGroup"

    props = {
        'ConnectionPoolConfigurationInfo':
            (ConnectionPoolConfigurationInfoFormat, False),
        'DBClusterIdentifiers': ([str], False),
        'DBInstanceIdentifiers': ([str], False),
        'DBProxyName': (str, True),
        'TargetGroupName': (str, True),
    }


class DBSubnetGroup(AWSObject):
    resource_type = "AWS::RDS::DBSubnetGroup"

    props = {
        'DBSubnetGroupDescription': (str, True),
        'DBSubnetGroupName': (str, False),
        'SubnetIds': (list, True),
        'Tags': ((Tags, list), False),
    }


class RDSSecurityGroup(AWSProperty):
    props = {
        'CIDRIP': (str, False),
        'EC2SecurityGroupId': (str, False),
        'EC2SecurityGroupName': (str, False),
        'EC2SecurityGroupOwnerId': (str, False),
    }


class DBSecurityGroup(AWSObject):
    resource_type = "AWS::RDS::DBSecurityGroup"

    props = {
        'EC2VpcId': (str, False),
        'DBSecurityGroupIngress': (list, True),
        'GroupDescription': (str, True),
        'Tags': ((Tags, list), False),
    }


class DBSecurityGroupIngress(AWSObject):
    resource_type = "AWS::RDS::DBSecurityGroupIngress"

    props = {
        'CIDRIP': (str, False),
        'DBSecurityGroupName': (str, True),
        'EC2SecurityGroupId': (str, False),
        'EC2SecurityGroupName': (str, False),
        'EC2SecurityGroupOwnerId': (str, False),
    }


class EventSubscription(AWSObject):
    resource_type = "AWS::RDS::EventSubscription"

    props = {
        'Enabled': (boolean, False),
        'EventCategories': ([str], False),
        'SnsTopicArn': (str, True),
        'SourceIds': ([str], False),
        'SourceType': (str, False),
    }


class GlobalCluster(AWSObject):
    resource_type = "AWS::RDS::GlobalCluster"

    props = {
        'DeletionProtection': (boolean, False),
        'Engine': (str, False),
        'EngineVersion': (str, False),
        'GlobalClusterIdentifier': (str, False),
        'SourceDBClusterIdentifier': (str, False),
        'StorageEncrypted': (boolean, False),
    }


class OptionSetting(AWSProperty):
    props = {
        'Name': (str, False),
        'Value': (str, False),
    }


class OptionConfiguration(AWSProperty):
    props = {
        'DBSecurityGroupMemberships': ([str], False),
        'OptionName': (str, True),
        'OptionSettings': ([OptionSetting], False),
        'OptionVersion': (str, False),
        'Port': (network_port, False),
        'VpcSecurityGroupMemberships': ([str], False),
    }


class OptionGroup(AWSObject):
    resource_type = "AWS::RDS::OptionGroup"

    props = {
        'EngineName': (str, True),
        'MajorEngineVersion': (str, True),
        'OptionGroupDescription': (str, True),
        'OptionConfigurations': ([OptionConfiguration], True),
        'Tags': ((Tags, list), False),
    }


class DBClusterParameterGroup(AWSObject):
    resource_type = "AWS::RDS::DBClusterParameterGroup"

    props = {
        'Description': (str, True),
        'Family': (str, True),
        'Parameters': (dict, False),
        'Tags': ((Tags, list), False),
    }


class DBClusterRole(AWSProperty):
    props = {
        'FeatureName': (str, False),
        'RoleArn': (str, True),
        'Status': (str, False),
    }


class ScalingConfiguration(AWSProperty):
    props = {
        'AutoPause': (boolean, False),
        'MaxCapacity': (validate_capacity, False),
        'MinCapacity': (validate_capacity, False),
        'SecondsUntilAutoPause': (positive_integer, False),
    }


class DBCluster(AWSObject):
    resource_type = "AWS::RDS::DBCluster"

    props = {
        'AssociatedRoles': ([DBClusterRole], False),
        'AvailabilityZones': ([str], False),
        'BacktrackWindow': (integer_range(0, 259200), False),
        'BackupRetentionPeriod': (validate_backup_retention_period, False),
        'DatabaseName': (str, False),
        'DBClusterIdentifier': (str, False),
        'DBClusterParameterGroupName': (str, False),
        'DBSubnetGroupName': (str, False),
        'DeletionProtection': (boolean, False),
        'EnableCloudwatchLogsExports': ([str], False),
        'EnableHttpEndpoint': (boolean, False),
        'EnableIAMDatabaseAuthentication': (boolean, False),
        'Engine': (validate_engine, True),
        'EngineMode': (validate_engine_mode, False),
        'EngineVersion': (str, False),
        'KmsKeyId': (str, False),
        'MasterUsername': (str, False),
        'MasterUserPassword': (str, False),
        'Port': (network_port, False),
        'PreferredBackupWindow': (validate_backup_window, False),
        'PreferredMaintenanceWindow': (str, False),
        'ReplicationSourceIdentifier': (str, False),
        'RestoreType': (str, False),
        'ScalingConfiguration': (ScalingConfiguration, False),
        'SnapshotIdentifier': (str, False),
        'SourceDBClusterIdentifier': (str, False),
        'SourceRegion': (str, False),
        'StorageEncrypted': (boolean, False),
        'Tags': ((Tags, list), False),
        'UseLatestRestorableTime': (boolean, False),
        'VpcSecurityGroupIds': ([str], False),
    }
