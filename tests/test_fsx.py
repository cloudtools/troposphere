import unittest

from troposphere.fsx import FileSystem


class TestFSx(unittest.TestCase):
    def test_FileSystem(self):
        FileSystem(
            "filesystem",
            FileSystemType="type",
            StorageType="HDD",
            SubnetIds=["subnet"],
        ).to_dict()

    def test_invalid_storagetype(self):
        with self.assertRaises(ValueError):
            FileSystem(
                "filesystem",
                FileSystemType="type",
                StorageType="floppy",
                SubnetIds=["subnet"],
            ).to_dict()


if __name__ == "__main__":
    unittest.main()
