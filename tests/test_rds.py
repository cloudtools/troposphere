import unittest
import troposphere.rds as rds
from troposphere import If, Parameter, Ref


class TestRDS(unittest.TestCase):

    def test_it_allows_an_rds_instance_created_from_a_snapshot(self):
        rds_instance = rds.DBInstance(
            'SomeTitle',
            AllocatedStorage=100,
            DBInstanceClass='db.m1.small',
            Engine='MySQL',
            DBSnapshotIdentifier='SomeSnapshotIdentifier'
        )

        rds_instance.JSONrepr()

    def test_it_allows_an_rds_instance_with_master_username_and_password(self):
        rds_instance = rds.DBInstance(
            'SomeTitle',
            AllocatedStorage=1,
            DBInstanceClass='db.m1.small',
            Engine='MySQL',
            MasterUsername='SomeUsername',
            MasterUserPassword='SomePassword'
        )

        rds_instance.JSONrepr()

    def test_it_rds_instances_require_either_a_snapshot_or_credentials(self):
        rds_instance = rds.DBInstance(
            'SomeTitle',
            AllocatedStorage=1,
            DBInstanceClass='db.m1.small',
            Engine='MySQL'
        )

        with self.assertRaisesRegexp(
                ValueError,
                'Either \(MasterUsername and MasterUserPassword\) or'
                ' DBSnapshotIdentifier are required'
                ):
            rds_instance.JSONrepr()

    def test_it_allows_an_rds_replica(self):
        rds_instance = rds.DBInstance(
            'SomeTitle',
            AllocatedStorage=1,
            DBInstanceClass='db.m1.small',
            Engine='MySQL',
            SourceDBInstanceIdentifier='SomeSourceDBInstanceIdentifier'
        )

        rds_instance.JSONrepr()

    def test_replica_settings_are_inherited(self):
        rds_instance = rds.DBInstance(
            'SomeTitle',
            AllocatedStorage=1,
            DBInstanceClass='db.m1.small',
            Engine='MySQL',
            SourceDBInstanceIdentifier='SomeSourceDBInstanceIdentifier',
            BackupRetentionPeriod="1",
            DBName="SomeName",
            MasterUsername="SomeUsername",
            MasterUserPassword="SomePassword",
            PreferredBackupWindow="10:00-11:00",
            MultiAZ=True,
            DBSnapshotIdentifier="SomeDBSnapshotIdentifier",
            DBSubnetGroupName="SomeDBSubnetGroupName",
        )

        with self.assertRaisesRegexp(
                ValueError,
                'BackupRetentionPeriod, DBName, DBSnapshotIdentifier, '
                'DBSubnetGroupName, MasterUserPassword, MasterUsername, '
                'MultiAZ, PreferredBackupWindow '
                'properties can\'t be provided when '
                'SourceDBInstanceIdentifier is present '
                'AWS::RDS::DBInstance.'
                ):
            rds_instance.JSONrepr()

    def test_it_rds_instances_require_encryption_if_kms_key_provided(self):
        rds_instance = rds.DBInstance(
            'SomeTitle',
            AllocatedStorage=1,
            DBInstanceClass='db.m1.small',
            Engine='MySQL',
            MasterUsername='SomeUsername',
            MasterUserPassword='SomePassword',
            KmsKeyId='arn:aws:kms:us-east-1:123456789012:key/'
                     '12345678-1234-1234-1234-123456789012'
        )

        with self.assertRaisesRegexp(
                ValueError,
                'If KmsKeyId is provided, StorageEncrypted is required'
                ):
            rds_instance.JSONrepr()

    def test_it_allows_an_rds_instance_with_iops(self):
        # ensure troposphere works with longs and ints
        try:
            long_number = long(2000)
        except NameError:
            # Python 3 doesn't have 'long' anymore
            long_number = 2000
        rds_instance = rds.DBInstance(
            'SomeTitle',
            AllocatedStorage=200,
            DBInstanceClass='db.m1.small',
            Engine='MySQL',
            MasterUsername='SomeUsername',
            MasterUserPassword='SomePassword',
            StorageType='io1',
            Iops=long_number,
        )

        rds_instance.JSONrepr()

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
            ]
        )
        rds_optiongroup.JSONrepr()

    def test_fail_az_and_multiaz(self):
        i = rds.DBInstance(
            "NoAZAndMultiAZ",
            MasterUsername="myuser",
            MasterUserPassword="mypassword",
            AllocatedStorage=10,
            DBInstanceClass="db.m1.small",
            Engine="postgres",
            AvailabilityZone="us-east-1",
            MultiAZ=True)
        with self.assertRaisesRegexp(ValueError, "if MultiAZ is set to "):
            i.JSONrepr()

    def test_az_and_multiaz_funcs(self):
        AWS_NO_VALUE = "AWS::NoValue"
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

    def test_io1_storage_type_and_iops(self):
        i = rds.DBInstance(
            "NoAZAndMultiAZ",
            MasterUsername="myuser",
            MasterUserPassword="mypassword",
            AllocatedStorage=10,
            DBInstanceClass="db.m1.small",
            Engine="postgres",
            StorageType='io1')
        with self.assertRaisesRegexp(ValueError,
                                     "Must specify Iops if "):
            i.JSONrepr()

    def test_storage_to_iops_ratio(self):
        i = rds.DBInstance(
            "NoAZAndMultiAZ",
            MasterUsername="myuser",
            MasterUserPassword="mypassword",
            DBInstanceClass="db.m1.small",
            Engine="postgres",
            StorageType='io1',
            Iops=4000,
            AllocatedStorage=10)
        with self.assertRaisesRegexp(ValueError,
                                     " must be at least 100 "):
            i.JSONrepr()

        i.AllocatedStorage = 100
        with self.assertRaisesRegexp(ValueError,
                                     " must be no less than 1/10th "):
            i.JSONrepr()

        i.AllocatedStorage = 400
        i.JSONrepr()


class TestRDSValidators(unittest.TestCase):
    def test_validate_iops(self):
        with self.assertRaises(ValueError):
            rds.validate_iops(500)
        rds.validate_iops(2000)
        rds.validate_iops(0)

    def test_validate_storage_type(self):
        for t in rds.VALID_STORAGE_TYPES:
            rds.validate_storage_type(t)

        with self.assertRaises(ValueError):
            rds.validate_storage_type("bad_storage_type")

    def test_validate_engine(self):
        for e in rds.VALID_DB_ENGINES:
            rds.validate_engine(e)

        with self.assertRaises(ValueError):
            rds.validate_engine("bad_engine")

    def test_validate_license_model(self):
        for lm in rds.VALID_LICENSE_MODELS:
            rds.validate_license_model(lm)

        with self.assertRaises(ValueError):
            rds.validate_license_model("bad_license_model")

    def test_validate_backup_window(self):
        good_windows = ("10:00-11:00", "22:00-06:00")
        for w in good_windows:
            rds.validate_backup_window(w)

        bad_format = ("bad_backup_window", "28:11-10:00", "10:00-28:11")
        for w in bad_format:
            with self.assertRaisesRegexp(ValueError, "must be in the format"):
                rds.validate_backup_window(w)

        with self.assertRaisesRegexp(ValueError, "must be at least 30 "):
            rds.validate_backup_window("10:00-10:10")

    def test_validate_maintenance_window(self):
        good_windows = ("Mon:10:00-Mon:16:30", "Mon:10:00-Wed:10:00",
                        "Sun:16:00-Mon:11:00")

        for w in good_windows:
            rds.validate_maintenance_window(w)

        bad_format = ("bad_mainteance", "Mon:10:00-Tue:28:00", "10:00-22:00")
        for w in bad_format:
            with self.assertRaisesRegexp(ValueError, "must be in the format"):
                rds.validate_maintenance_window(w)

        bad_days = ("Boo:10:00-Woo:10:30", "Boo:10:00-Tue:10:30",
                    "Mon:10:00-Boo:10:30")
        for w in bad_days:
            with self.assertRaisesRegexp(ValueError, " day part of ranges "):
                rds.validate_maintenance_window(w)

        with self.assertRaisesRegexp(ValueError, "must be at least 30 "):
            rds.validate_maintenance_window("Mon:10:00-Mon:10:10")

    def test_validate_backup_retention_period(self):
        for d in (1, 10, 15, 35):
            rds.validate_backup_retention_period(d)

        with self.assertRaisesRegexp(ValueError,
                                     " cannot be larger than 35 "):
            rds.validate_backup_retention_period(40)

        rds.validate_backup_retention_period(10)
