import unittest

import troposphere.rds as rds
import troposphere.validators.rds as vrds
from troposphere import If, Parameter, Ref

AWS_NO_VALUE = "AWS::NoValue"


class TestRDS(unittest.TestCase):
    def test_it_allows_an_rds_instance_created_from_a_snapshot(self):
        rds_instance = rds.DBInstance(
            "SomeTitle",
            AllocatedStorage=100,
            DBInstanceClass="db.m1.small",
            Engine="MySQL",
            DBSnapshotIdentifier="SomeSnapshotIdentifier",
        )

        rds_instance.to_dict()

    def test_it_allows_an_rds_instance_with_master_username_and_password(self):
        rds_instance = rds.DBInstance(
            "SomeTitle",
            AllocatedStorage=1,
            DBInstanceClass="db.m1.small",
            Engine="MySQL",
            MasterUsername="SomeUsername",
            MasterUserPassword="SomePassword",
        )

        rds_instance.to_dict()

    def test_it_rds_instances_require_either_a_snapshot_or_credentials(self):
        rds_instance = rds.DBInstance(
            "SomeTitle",
            AllocatedStorage=1,
            DBInstanceClass="db.m1.small",
            Engine="MySQL",
        )

        with self.assertRaisesRegex(
            ValueError,
            r"Either \(MasterUsername and either "
            r"MasterUserPassword or ManageMasterUserPassword\) or"
            r" DBSnapshotIdentifier are required",
        ):
            rds_instance.to_dict()

    def test_it_rds_credentials_using_masteruserpassword(self):
        rds_instance = rds.DBInstance(
            "SomeTitle",
            Engine="MySQL",
            MasterUsername="user",
            MasterUserPassword="password",
        )
        rds_instance.to_dict()

    def test_it_rds_credentials_using_managemasteruserpassword(self):
        rds_instance = rds.DBInstance(
            "SomeTitle",
            Engine="MySQL",
            MasterUsername="user",
            ManageMasterUserPassword=True,
        )
        rds_instance.to_dict()

    def test_it_rds_masteruserpassword_and_managemasteruserpassword_mutually_exclusive(
        self,
    ):
        rds_instance = rds.DBInstance(
            "SomeTitle",
            Engine="MySQL",
            MasterUsername="user",
            MasterUserPassword="password",
            ManageMasterUserPassword=True,
        )

        with self.assertRaisesRegex(
            ValueError,
            r"Both MasterUserPassword and ManageMasterUserPassword cannot be set simultaneously.",
        ):
            rds_instance.to_dict()

    def test_it_allows_an_rds_replica(self):
        rds_instance = rds.DBInstance(
            "SomeTitle",
            AllocatedStorage=1,
            DBInstanceClass="db.m1.small",
            Engine="MySQL",
            SourceDBInstanceIdentifier="SomeSourceDBInstanceIdentifier",
        )

        rds_instance.to_dict()

    def test_replica_settings_are_inherited(self):
        rds_instance = rds.DBInstance(
            "SomeTitle",
            AllocatedStorage=1,
            DBInstanceClass="db.m1.small",
            Engine="MySQL",
            SourceDBInstanceIdentifier="SomeSourceDBInstanceIdentifier",
            BackupRetentionPeriod="1",
            DBName="SomeName",
            MasterUsername="SomeUsername",
            MasterUserPassword="SomePassword",
            PreferredBackupWindow="10:00-11:00",
            MultiAZ=True,
            DBSnapshotIdentifier="SomeDBSnapshotIdentifier",
        )

        with self.assertRaisesRegex(
            ValueError,
            "DBName, DBSnapshotIdentifier, "
            "MasterUserPassword, MasterUsername, "
            "MultiAZ, PreferredBackupWindow "
            "properties can't be provided when "
            "SourceDBInstanceIdentifier is present "
            "AWS::RDS::DBInstance.",
        ):
            rds_instance.to_dict()

    def test_it_rds_instances_require_encryption_if_kms_key_provided(self):
        rds_instance = rds.DBInstance(
            "SomeTitle",
            AllocatedStorage=1,
            DBInstanceClass="db.m1.small",
            Engine="MySQL",
            MasterUsername="SomeUsername",
            MasterUserPassword="SomePassword",
            KmsKeyId="arn:aws:kms:us-east-1:123456789012:key/"
            "12345678-1234-1234-1234-123456789012",
        )

        with self.assertRaisesRegex(
            ValueError, "If KmsKeyId is provided, StorageEncrypted is required"
        ):
            rds_instance.to_dict()

    def test_it_allows_an_rds_instance_with_iops(self):
        rds_instance = rds.DBInstance(
            "SomeTitle",
            AllocatedStorage=200,
            DBInstanceClass="db.m1.small",
            Engine="MySQL",
            MasterUsername="SomeUsername",
            MasterUserPassword="SomePassword",
            StorageType="io1",
            Iops=2000,
        )

        rds_instance.to_dict()

    def test_optiongroup(self):
        rds_optiongroup = rds.OptionGroup(
            "OracleOptionGroup",
            EngineName="oracle-ee",
            MajorEngineVersion="12.1",
            OptionGroupDescription="A test option group",
            OptionConfigurations=[
                rds.OptionConfiguration(
                    DBSecurityGroupMemberships=["default"],
                    OptionName="OEM",
                    Port="5500",
                ),
                rds.OptionConfiguration(
                    OptionName="APEX",
                ),
            ],
        )
        rds_optiongroup.to_dict()

    def test_fail_az_and_multiaz(self):
        i = rds.DBInstance(
            "NoAZAndMultiAZ",
            MasterUsername="myuser",
            MasterUserPassword="mypassword",
            AllocatedStorage=10,
            DBInstanceClass="db.m1.small",
            Engine="postgres",
            AvailabilityZone="us-east-1",
            MultiAZ=True,
        )
        with self.assertRaisesRegex(ValueError, "if MultiAZ is set to "):
            i.to_dict()
        i.MultiAZ = "false"
        i.to_dict()
        i.MultiAZ = "true"
        with self.assertRaisesRegex(ValueError, "if MultiAZ is set to "):
            i.to_dict()

        i.MultiAZ = Ref(AWS_NO_VALUE)
        i.to_dict()

    def test_az_and_multiaz_funcs(self):
        db_az = "us-east-1"
        db_multi_az = Parameter("dbmultiaz", Type="String")
        i = rds.DBInstance(
            "NoAZAndMultiAZ",
            MasterUsername="myuser",
            MasterUserPassword="mypassword",
            AllocatedStorage=10,
            DBInstanceClass="db.m1.small",
            Engine="postgres",
            AvailabilityZone=If("db_az", Ref(db_az), Ref(AWS_NO_VALUE)),
            MultiAZ=Ref(db_multi_az),
        )
        i.validate()

    def test_allocated_storage_parameter_oracle(self):
        db_az = "us-east-1"
        allocated_storage = Parameter("allocatedstorage", Type="int")
        i = rds.DBInstance(
            "NoAZAndMultiAZ",
            MasterUsername="myuser",
            MasterUserPassword="mypassword",
            AllocatedStorage=Ref(allocated_storage),
            DBInstanceClass="db.m1.small",
            Engine="oracle-se1",
            StorageType="gp3",
            AvailabilityZone=If("db_az", Ref(db_az), Ref(AWS_NO_VALUE)),
        )
        i.validate()

    def test_allocated_storage_parameter_postgres(self):
        db_az = "us-east-1"
        allocated_storage = Parameter("allocatedstorage", Type="int")
        i = rds.DBInstance(
            "NoAZAndMultiAZ",
            MasterUsername="myuser",
            MasterUserPassword="mypassword",
            AllocatedStorage=Ref(allocated_storage),
            DBInstanceClass="db.m1.small",
            Engine="postgres",
            StorageType="gp3",
            AvailabilityZone=If("db_az", Ref(db_az), Ref(AWS_NO_VALUE)),
        )
        i.validate()

    def test_gp3_storage_performance(self):
        # Using a Ref() will disable the gp3 ratio check
        allocated_storage = Parameter("allocatedstorage", Type="int")
        i = rds.DBInstance(
            "Database1",
            Engine="postgres",
            EngineVersion="15.3",
            StorageType="gp3",
            AllocatedStorage=Ref(allocated_storage),
            Iops=12000,
            StorageThroughput=500,
            MasterUsername="test",
            MasterUserPassword="test",
        )
        i.validate()

        # Specify invalid ratio for iops/allocated_storage for gp3
        i = rds.DBInstance(
            "Database2",
            Engine="postgres",
            EngineVersion="15.3",
            StorageType="gp3",
            AllocatedStorage="400",
            Iops=200400,
            StorageThroughput=500,
            MasterUsername="test",
            MasterUserPassword="test",
        )
        with self.assertRaisesRegex(
            ValueError,
            r"Invalid ratio of Iops to AllocatedStorage",
        ):
            i.to_dict()

        # Check startswith match for oracle and sqlserver engines
        i = rds.DBInstance(
            "Database2",
            Engine="oracle-se2",
            EngineVersion="15.3",
            StorageType="gp3",
            Iops=10000,
            AllocatedStorage="10",
            MasterUsername="test",
            MasterUserPassword="test",
        )
        with self.assertRaisesRegex(
            ValueError,
            r"AllocatedStorage must be at least 200",
        ):
            i.to_dict()

        i.AllocatedStorage = "200"
        i.to_dict()

        i = rds.DBInstance(
            "Database2",
            Engine="sqlserver-se",
            EngineVersion="15.3",
            StorageType="gp3",
            Iops=1000,
            AllocatedStorage="10",
            MasterUsername="test",
            MasterUserPassword="test",
        )
        with self.assertRaisesRegex(
            ValueError,
            r"AllocatedStorage must be at least 20",
        ):
            i.to_dict()

        i.AllocatedStorage = "20"
        i.to_dict()

    def test_io1_storage_type_and_iops(self):
        i = rds.DBInstance(
            "NoAZAndMultiAZ",
            MasterUsername="myuser",
            MasterUserPassword="mypassword",
            AllocatedStorage=10,
            DBInstanceClass="db.m1.small",
            Engine="postgres",
            StorageType="io1",
        )
        with self.assertRaisesRegex(ValueError, "Must specify Iops if "):
            i.to_dict()

    def test_storage_to_iops_ratio(self):
        i = rds.DBInstance(
            "NoAZAndMultiAZ",
            MasterUsername="myuser",
            MasterUserPassword="mypassword",
            DBInstanceClass="db.m1.small",
            Engine="postgres",
            StorageType="io1",
            Iops=6000,
            AllocatedStorage=10,
        )
        with self.assertRaisesRegex(ValueError, " must be at least 100 "):
            i.to_dict()

        i.AllocatedStorage = 100
        with self.assertRaisesRegex(ValueError, " must be no less than 1/50th "):
            i.to_dict()

        i.Iops = 5000
        i.to_dict()

    def test_storage_sqlserver(self):
        i = rds.DBInstance(
            "NoAZAndMultiAZ",
            MasterUsername="myuser",
            MasterUserPassword="mypassword",
            DBInstanceClass="db.m1.small",
            Engine="sqlserver-ee",
            StorageType="io1",
            Iops=1000,
            AllocatedStorage=10,
        )
        with self.assertRaisesRegex(ValueError, " must be at least 20 "):
            i.to_dict()

        i.AllocatedStorage = 20
        i.to_dict()

    def test_snapshot(self):
        i = rds.DBInstance(
            "MyDB",
            DBName="test",
            AllocatedStorage=25,
            DBInstanceClass="db.m4.large",
            DBSubnetGroupName="default",
            DBSnapshotIdentifier="id",
        )
        i.to_dict()

    def test_snapshot_and_engine(self):
        i = rds.DBInstance(
            "MyDB",
            DBName="test",
            AllocatedStorage=25,
            DBInstanceClass="db.m4.large",
            DBSubnetGroupName="default",
            DBSnapshotIdentifier="id",
            Engine="postgres",
        )
        i.to_dict()

    def test_no_snapshot_or_engine(self):
        i = rds.DBInstance(
            "MyDB",
            DBName="test",
            AllocatedStorage=25,
            DBInstanceClass="db.m4.large",
            DBSubnetGroupName="default",
        )
        with self.assertRaisesRegex(ValueError, "Resource Engine is required"):
            i.to_dict()


class TestRDSValidators(unittest.TestCase):
    def test_validate_iops(self):
        with self.assertRaises(ValueError):
            vrds.validate_iops(500)
        vrds.validate_iops(2000)
        vrds.validate_iops(0)

    def test_validate_storage_type(self):
        vrds.validate_storage_type("standard")

        with self.assertRaises(ValueError):
            vrds.validate_storage_type("bad_storage_type")

    def test_validate_engine(self):
        vrds.validate_engine("postgres")

        with self.assertRaises(ValueError):
            vrds.validate_engine("bad_engine")

    def test_validate_engine_mode(self):
        vrds.validate_engine_mode("provisioned")

        with self.assertRaises(ValueError):
            vrds.validate_engine_mode("bad_engine")

    def test_validate_license_model(self):
        vrds.validate_license_model("postgresql-license")

        with self.assertRaises(ValueError):
            vrds.validate_license_model("bad_license_model")

    def test_validate_backup_window(self):
        good_windows = ("10:00-11:00", "22:00-06:00")
        for w in good_windows:
            vrds.validate_backup_window(w)

        bad_format = ("bad_backup_window", "28:11-10:00", "10:00-28:11")
        for w in bad_format:
            with self.assertRaisesRegex(ValueError, "must be in the format"):
                vrds.validate_backup_window(w)

        with self.assertRaisesRegex(ValueError, "must be at least 30 "):
            vrds.validate_backup_window("10:00-10:10")

    def test_validate_maintenance_window(self):
        good_windows = (
            "Mon:10:00-Mon:16:30",
            "Mon:10:00-Wed:10:00",
            "Sun:16:00-Mon:11:00",
        )

        for w in good_windows:
            vrds.validate_maintenance_window(w)

        bad_format = ("bad_mainteance", "Mon:10:00-Tue:28:00", "10:00-22:00")
        for w in bad_format:
            with self.assertRaisesRegex(ValueError, "must be in the format"):
                vrds.validate_maintenance_window(w)

        bad_days = ("Boo:10:00-Woo:10:30", "Boo:10:00-Tue:10:30", "Mon:10:00-Boo:10:30")
        for w in bad_days:
            with self.assertRaisesRegex(ValueError, " day part of ranges "):
                vrds.validate_maintenance_window(w)

        with self.assertRaisesRegex(ValueError, "must be at least 30 "):
            vrds.validate_maintenance_window("Mon:10:00-Mon:10:10")

    def test_validate_backup_retention_period(self):
        for d in (1, 10, 15, 35):
            vrds.validate_backup_retention_period(d)

        with self.assertRaisesRegex(ValueError, " cannot be larger than 35 "):
            vrds.validate_backup_retention_period(40)

        vrds.validate_backup_retention_period(10)

    def test_validate_capacity(self):
        vrds.validate_capacity(64)

        with self.assertRaises(ValueError):
            vrds.validate_capacity(3)

        with self.assertRaises(ValueError):
            vrds.validate_capacity(100001)

    def test_v2_validate_capacity(self):
        vrds.validate_v2_capacity(64)
        vrds.validate_v2_capacity(0.5)

        with self.assertRaises(ValueError):
            vrds.validate_v2_capacity(129)

        with self.assertRaises(ValueError):
            vrds.validate_v2_capacity(1.1)

        with self.assertRaises(ValueError):
            vrds.validate_v2_max_capacity(0.5)
