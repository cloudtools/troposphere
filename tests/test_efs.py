import unittest

from troposphere import Template, efs


class TestEfsTemplate(unittest.TestCase):
    def test_bucket_template(self):
        template = Template()
        title = "Efs"
        efs.FileSystem(title, template)
        self.assertIn(title, template.resources)


class TestEfs(unittest.TestCase):
    def test_validData(self):
        file_system = efs.FileSystem("Efs")
        file_system.to_dict()

    def test_validateThroughputMode(self):
        with self.assertRaises(ValueError):
            file_system = efs.FileSystem(
                "Efs", ThroughputMode="UndefinedThroughputMode"
            )
            file_system.to_dict()

        file_system = efs.FileSystem(
            "Efs", ThroughputMode=efs.Bursting
        )

        result = file_system.to_dict()
        self.assertEqual(result["Type"], "AWS::EFS::FileSystem")

    def test_validateProvisionedThroughputInMibps(self):
        with self.assertRaises(TypeError):
            file_system = efs.FileSystem(
                "Efs", ProvisionedThroughputInMibps="512"
            )
            file_system.to_dict()

        with self.assertRaises(TypeError):
            file_system = efs.FileSystem(
                "Efs", ProvisionedThroughputInMibps=512
            )
            file_system.to_dict()

        file_system = efs.FileSystem(
            "Efs", ProvisionedThroughputInMibps=512.0
        )

        result = file_system.to_dict()
        self.assertEqual(result["Type"], "AWS::EFS::FileSystem")

    def test_validateBackupPolicy(self):
        with self.assertRaises(ValueError):
            backup_policy = efs.BackupPolicy(
                "backupPolicy", Status="NOTOK"
            )
            backup_policy.to_dict()

        backup_policy = efs.BackupPolicy(
            "backupPolicy", Status="ENABLED"
        )

        result = backup_policy.to_dict()
        self.assertEqual(result["Status"], "ENABLED")


if __name__ == "__main__":
    unittest.main()
