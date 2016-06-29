import unittest
from troposphere.autoscaling import AutoScalingGroup
from troposphere.policies import AutoScalingRollingUpdate, UpdatePolicy
from troposphere import If


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

    def test_size_if(self):
        group = AutoScalingGroup(
            'mygroup',
            AvailabilityZones=['eu-west-1a', 'eu-west-1b'],
            LaunchConfigurationName="I'm a test",
            MaxSize=If("isstage", "1", "5"),
            MinSize="1",
            UpdatePolicy=UpdatePolicy(
                AutoScalingRollingUpdate=AutoScalingRollingUpdate(
                    PauseTime='PT5M',
                    MinInstancesInService="1",
                    MaxBatchSize='1',
                    WaitOnResourceSignals=True
                )
            )
        )
        self.assertTrue(group.validate())


if __name__ == '__main__':
    unittest.main()
