# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


import re

from .. import AWSHelperFn
from . import integer, integer_range, network_port, positive_integer, tags_or_list


def validate_network_port(x):
    """
    Property: DBCluster.Port
    Property: DBInstance.Port
    Property: OptionConfiguration.Port
    """
    return network_port(x)


def validate_str_or_int(x):
    """
    Property: DBInstance.AllocatedStorage
    """
    if isinstance(x, (AWSHelperFn, str, int)):
        return x
    raise ValueError(f"Value {x} of type {type(x)} must be either str or int")


def validate_tags_or_list(x):
    """
    Property: DBCluster.Tags
    Property: DBClusterParameterGroup.Tags
    Property: DBInstance.Tags
    Property: DBParameterGroup.Tags
    Property: DBSecurityGroup.Tags
    Property: DBSubnetGroup.Tags
    Property: OptionGroup.Tags
    """
    return tags_or_list(x)


def validate_backtrack_window(x):
    """
    Property: DBCluster.BacktrackWindow
    """
    return integer_range(0, 259200)(x)


def validate_iops(iops):
    """
    DBInstance Iops validation rules.
    Property: DBInstance.Iops
    """

    iops = integer(iops)
    if int(iops) == 0:
        return iops
    if int(iops) < 1000:
        raise ValueError("DBInstance Iops, if set, must be greater than 1000.")
    return iops


def validate_storage_type(storage_type):
    """
    Validate StorageType for DBInstance
    Property:
    """

    VALID_STORAGE_TYPES = ("standard", "gp2", "gp3", "io1")

    if storage_type not in VALID_STORAGE_TYPES:
        raise ValueError(
            "DBInstance StorageType must be one of: %s" % ", ".join(VALID_STORAGE_TYPES)
        )
    return storage_type


def validate_engine(engine):
    """
    Validate database Engine for DBInstance
    Property: DBInstance.Engine
    Property: DBCluster.Engine
    """

    VALID_DB_ENGINES = (
        "MySQL",
        "mysql",
        "oracle-se1",
        "oracle-se2",
        "oracle-se",
        "oracle-ee",
        "sqlserver-ee",
        "sqlserver-se",
        "sqlserver-ex",
        "sqlserver-web",
        "postgres",
        "aurora",
        "aurora-mysql",
        "aurora-postgresql",
        "mariadb",
    )

    if engine not in VALID_DB_ENGINES:
        raise ValueError(
            "DBInstance Engine must be one of: %s" % ", ".join(VALID_DB_ENGINES)
        )
    return engine


def validate_engine_mode(engine_mode):
    """
    Validate database EngineMode for DBCluster
    Property: DBCluster.EngineMode
    """

    VALID_DB_ENGINE_MODES = (
        "provisioned",
        "serverless",
        "parallelquery",
        "global",
        "multimaster",
    )

    if engine_mode not in VALID_DB_ENGINE_MODES:
        raise ValueError(
            "DBCluster EngineMode must be one of: %s" % ", ".join(VALID_DB_ENGINE_MODES)
        )
    return engine_mode


def validate_license_model(license_model):
    """
    Validate LicenseModel for DBInstance
    Property: DBInstance.LicenseModel
    """

    VALID_LICENSE_MODELS = (
        "license-included",
        "bring-your-own-license",
        "general-public-license",
        "postgresql-license",
    )

    if license_model not in VALID_LICENSE_MODELS:
        raise ValueError(
            "DBInstance LicenseModel must be one of: %s"
            % ", ".join(VALID_LICENSE_MODELS)
        )
    return license_model


def validate_backup_window(window):
    """
    Validate PreferredBackupWindow for DBInstance
    Property: DBInstance.PreferredBackupWindow
    Property: DBCluster.PreferredBackupWindow
    """

    hour = r"[01]?[0-9]|2[0-3]"
    minute = r"[0-5][0-9]"
    r = (
        "(?P<start_hour>%s):(?P<start_minute>%s)-" "(?P<end_hour>%s):(?P<end_minute>%s)"
    ) % (hour, minute, hour, minute)
    range_regex = re.compile(r)
    m = range_regex.match(window)
    if not m:
        raise ValueError(
            "DBInstance PreferredBackupWindow must be in the " "format: hh24:mi-hh24:mi"
        )
    start_ts = (int(m.group("start_hour")) * 60) + int(m.group("start_minute"))
    end_ts = (int(m.group("end_hour")) * 60) + int(m.group("end_minute"))
    if abs(end_ts - start_ts) < 30:
        raise ValueError(
            "DBInstance PreferredBackupWindow must be at least " "30 minutes long."
        )
    return window


def validate_maintenance_window(window):
    """
    Validate PreferredMaintenanceWindow for DBInstance
    """

    days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    day_re = r"[A-Z]{1}[a-z]{2}"
    hour = r"[01]?[0-9]|2[0-3]"
    minute = r"[0-5][0-9]"
    r = (
        "(?P<start_day>%s):(?P<start_hour>%s):(?P<start_minute>%s)-"
        "(?P<end_day>%s):(?P<end_hour>%s):(?P<end_minute>%s)"
    ) % (day_re, hour, minute, day_re, hour, minute)
    range_regex = re.compile(r)
    m = range_regex.match(window)
    if not m:
        raise ValueError(
            "DBInstance PreferredMaintenanceWindow must be in "
            "the format: ddd:hh24:mi-ddd:hh24:mi"
        )
    if m.group("start_day") not in days or m.group("end_day") not in days:
        raise ValueError(
            "DBInstance PreferredMaintenanceWindow day part of "
            "ranges must be one of: %s" % ", ".join(days)
        )
    start_ts = (
        (days.index(m.group("start_day")) * 24 * 60)
        + (int(m.group("start_hour")) * 60)
        + int(m.group("start_minute"))
    )
    end_ts = (
        (days.index(m.group("end_day")) * 24 * 60)
        + (int(m.group("end_hour")) * 60)
        + int(m.group("end_minute"))
    )
    if abs(end_ts - start_ts) < 30:
        raise ValueError(
            "DBInstance PreferredMaintenanceWindow must be at " "least 30 minutes long."
        )
    return window


def validate_backup_retention_period(days):
    """
    Validate BackupRetentionPeriod for DBInstance
    Property: DBInstance.BackupRetentionPeriod
    Property: DBCluster.BackupRetentionPeriod
    """

    days = positive_integer(days)
    if int(days) > 35:
        raise ValueError(
            "DBInstance BackupRetentionPeriod cannot be larger " "than 35 days."
        )
    return days


def validate_capacity(capacity):
    """
    Validate ScalingConfiguration capacity for serverless DBCluster
    Property: ScalingConfiguration.MaxCapacity
    Property: ScalingConfiguration.MinCapacity
    """

    VALID_MYSQL_SCALING_CONFIGURATION_CAPACITIES = (1, 2, 4, 8, 16, 32, 64, 128, 256)
    VALID_POSTGRESL_SCALING_CONFIGURATION_CAPACITIES = (2, 4, 8, 16, 32, 64, 192, 384)
    if (
        capacity not in VALID_POSTGRESL_SCALING_CONFIGURATION_CAPACITIES
        and capacity not in VALID_MYSQL_SCALING_CONFIGURATION_CAPACITIES
    ):
        raise ValueError(
            "ScalingConfiguration capacity must be one of: {}".format(
                ", ".join(
                    map(
                        str,
                        VALID_MYSQL_SCALING_CONFIGURATION_CAPACITIES
                        + VALID_POSTGRESL_SCALING_CONFIGURATION_CAPACITIES,
                    )
                )
            )
        )
    return capacity


def validate_v2_capacity(capacity):
    """
    Validate ServerlessV2ScalingConfiguration capacity for serverless DBCluster
    Property: ServerlessV2ScalingConfiguration.MinCapacity
    """
    if capacity < 0.5:
        raise ValueError(
            "ServerlessV2ScalingConfiguration capacity {} cannot be smaller than 0.5.".format(
                capacity
            )
        )
    if capacity > 128:
        raise ValueError(
            "ServerlessV2ScalingConfiguration capacity {} cannot be larger than 128.".format(
                capacity
            )
        )

    if capacity * 10 % 5 != 0:
        raise ValueError(
            "ServerlessV2ScalingConfiguration capacity {} cannot be only specific in half-step increments.".format(
                capacity
            )
        )

    return capacity


def validate_v2_max_capacity(capacity):
    """
    Validate ServerlessV2ScalingConfiguration max capacity for serverless DBCluster
    Property: ServerlessV2ScalingConfiguration.MaxCapacity
    """
    if capacity < 1:
        raise ValueError(
            "ServerlessV2ScalingConfiguration max capacity {} cannot be smaller than 1.".format(
                capacity
            )
        )

    return validate_v2_capacity(capacity)


def validate_dbinstance(self) -> None:
    """
    Class: DBInstance
    """
    if "DBSnapshotIdentifier" not in self.properties:
        if "Engine" not in self.properties:
            raise ValueError(
                "Resource Engine is required in type %s" % self.resource_type
            )

    if "SourceDBInstanceIdentifier" in self.properties:

        invalid_replica_properties = (
            "DBName",
            "MasterUsername",
            "MasterUserPassword",
            "PreferredBackupWindow",
            "MultiAZ",
            "DBSnapshotIdentifier",
        )

        invalid_properties = [
            s for s in self.properties.keys() if s in invalid_replica_properties
        ]

        if invalid_properties:
            raise ValueError(
                (
                    "{0} properties can't be provided when "
                    "SourceDBInstanceIdentifier is present "
                    "AWS::RDS::DBInstance."
                ).format(", ".join(sorted(invalid_properties)))
            )

    if (
        (
            "DBSnapshotIdentifier" not in self.properties
            and "SourceDBInstanceIdentifier" not in self.properties
        )
        and (
            "MasterUsername" not in self.properties
            or "MasterUserPassword" not in self.properties
        )
        and ("DBClusterIdentifier" not in self.properties)
    ):
        raise ValueError(
            r"Either (MasterUsername and MasterUserPassword) or"
            r" DBSnapshotIdentifier are required in type "
            r"AWS::RDS::DBInstance."
        )

    if "KmsKeyId" in self.properties and "StorageEncrypted" not in self.properties:
        raise ValueError(
            "If KmsKeyId is provided, StorageEncrypted is required "
            "AWS::RDS::DBInstance."
        )

    nonetype = type(None)
    avail_zone = self.properties.get("AvailabilityZone", None)
    multi_az = self.properties.get("MultiAZ", None)
    if not (
        isinstance(avail_zone, (AWSHelperFn, nonetype))
        and isinstance(multi_az, (AWSHelperFn, nonetype))
    ):
        if avail_zone and multi_az in [True, 1, "1", "true", "True"]:
            raise ValueError(
                "AvailabiltyZone cannot be set on "
                "DBInstance if MultiAZ is set to true."
            )

    storage_type = self.properties.get("StorageType", None)
    if (
        storage_type
        and storage_type in ["io1", "gp3"]
        and "Iops" not in self.properties
    ):
        raise ValueError("Must specify Iops if using StorageType io1 or gp3")

    allocated_storage = self.properties.get("AllocatedStorage")
    iops = self.properties.get("Iops", None)
    if iops and not isinstance(iops, AWSHelperFn):
        min_storage_size = 100
        engine = self.properties.get("Engine")
        if not isinstance(engine, AWSHelperFn) and engine.startswith("sqlserver"):
            min_storage_size = 20

        if (
            not isinstance(allocated_storage, AWSHelperFn)
            and int(allocated_storage) < min_storage_size
        ):
            raise ValueError(
                f"AllocatedStorage must be at least {min_storage_size} when "
                "Iops is set."
            )
        if (
            not isinstance(allocated_storage, AWSHelperFn)
            and not isinstance(iops, AWSHelperFn)
            and float(iops) / float(allocated_storage) > 50.0
        ):
            raise ValueError(
                "AllocatedStorage must be no less than " "1/50th the provisioned Iops"
            )
