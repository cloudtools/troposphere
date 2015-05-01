import unittest
from troposphere.autoscaling import AutoScalingGroup


class TestAutoScalingGroup(unittest.TestCase):
    def test_exclusive(self):
        group = AutoScalingGroup(
            'mygroup',
            InstanceId="i-1234",
            LaunchConfigurationName="I'm a test",
            MaxSize="1",
            MinSize="1",
        )
        with self.assertRaises(ValueError):
            self.assertTrue(group.validate())

    def test_none(self):
        group = AutoScalingGroup(
            'mygroup',
            MaxSize="1",
            MinSize="1",
        )
        with self.assertRaises(ValueError):
            self.assertTrue(group.validate())

    def test_instanceid(self):
        group = AutoScalingGroup(
            'mygroup',
            AvailabilityZones=['eu-west-1a', 'eu-west-1b'],
            InstanceId="i-1234",
            MaxSize="1",
            MinSize="1",
        )
        self.assertTrue(group.validate())

    def test_launchconfigurationname(self):
        group = AutoScalingGroup(
            'mygroup',
            AvailabilityZones=['eu-west-1a', 'eu-west-1b'],
            LaunchConfigurationName="I'm a test",
            MaxSize="1",
            MinSize="1",
        )
        self.assertTrue(group.validate())


if __name__ == '__main__':
    unittest.main()
