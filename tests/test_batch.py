import unittest
from troposphere.batch import ComputeEnvironment


class TestModel(unittest.TestCase):
    def test_ComputeEnvironmentState(self):
        ce = ComputeEnvironment(
            "Compute",
            ServiceRole="test",
            State="DISABLED",
            Type="test",
        )
        ce.validate()

        ce = ComputeEnvironment(
            "Compute",
            ServiceRole="test",
            State="ENABLED",
            Type="test",
        )
        ce.validate()

        with self.assertRaises(ValueError):
            ce = ComputeEnvironment(
                "Compute",
                ServiceRole="test",
                State="test",
                Type="test",
            )


if __name__ == '__main__':
    unittest.main()
