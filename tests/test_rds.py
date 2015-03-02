import unittest
import troposphere.rds as rds


class TestRDS(unittest.TestCase):

    def test_it_allows_an_rds_instance_created_from_a_snapshot(self):
        rds_instance = rds.DBInstance(
            'SomeTitle',
            AllocatedStorage=1,
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

    def test_rds_requires_engine(self):
        rds_no_engine = rds.DBInstance(
            'SomeTitle',
            AllocatedStorage=1,
            DBInstanceClass='db.m1.small',
        )

        with self.assertRaises(ValueError):
            rds_no_engine.JSONrepr()

    def test_rds_requires_allocated_storage(self):
        rds_no_allocated_storage = rds.DBInstance(
            'SomeTitle',
            DBInstanceClass='db.m1.small',
            Engine='MySQL'
        )

        with self.assertRaises(ValueError):
            rds_no_allocated_storage.JSONrepr()

    def test_rds_read_replica(self):
        rds_instance = rds.DBInstance(
            'SomeTitle',
            SourceDBInstanceIdentifier='masterdb',
            DBInstanceClass='db.m1.small',
            MultiAZ=False,
        )

        rds_instance.JSONrepr()

        rds_instance = rds.DBInstance(
            'SomeTitle',
            SourceDBInstanceIdentifier='masterdb',
            DBInstanceClass='db.m1.small',
            MultiAZ=True,
        )

        with self.assertRaises(ValueError):
            rds_instance.JSONrepr()

        rds_instance = rds.DBInstance(
            'SomeTitle',
            SourceDBInstanceIdentifier='masterdb',
            DBInstanceClass='db.m1.small',
            DBSnapshotIdentifier='dbident',
        )

        with self.assertRaises(ValueError):
            rds_instance.JSONrepr()

        rds_instance = rds.DBInstance(
            'SomeTitle',
            SourceDBInstanceIdentifier='masterdb',
            DBInstanceClass='db.m1.small',
            BackupRetentionPeriod='30',
        )

        with self.assertRaises(ValueError):
            rds_instance.JSONrepr()

        rds_instance = rds.DBInstance(
            'SomeTitle',
            SourceDBInstanceIdentifier='masterdb',
            DBInstanceClass='db.m1.small',
            DBName='dbname',
        )

        with self.assertRaises(ValueError):
            rds_instance.JSONrepr()

        rds_instance = rds.DBInstance(
            'SomeTitle',
            SourceDBInstanceIdentifier='masterdb',
            DBInstanceClass='db.m1.small',
            MasterUsername='username',
        )

        with self.assertRaises(ValueError):
            rds_instance.JSONrepr()

        rds_instance = rds.DBInstance(
            'SomeTitle',
            SourceDBInstanceIdentifier='masterdb',
            DBInstanceClass='db.m1.small',
            MasterUserPassword='password',
        )

        with self.assertRaises(ValueError):
            rds_instance.JSONrepr()

        rds_instance = rds.DBInstance(
            'SomeTitle',
            SourceDBInstanceIdentifier='masterdb',
            DBInstanceClass='db.m1.small',
            PreferredBackupWindow='backupwindow',
        )

        with self.assertRaises(ValueError):
            rds_instance.JSONrepr()
