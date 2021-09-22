import unittest

from troposphere import If, Ref
from troposphere.autoscaling import AutoScalingGroup, EBSBlockDevice
from troposphere.policies import AutoScalingRollingUpdate, UpdatePolicy


class TestAutoScalingGroup(unittest.TestCase):
    def test_exclusive(self):
        group = AutoScalingGroup(
            "mygroup",
            InstanceId="i-1234",
            LaunchConfigurationName="I'm a test",
            MaxSize="1",
            MinSize="1",
        )
        with self.assertRaises(ValueError):
            self.assertTrue(group.validate())

    def test_none(self):
        group = AutoScalingGroup(
            "mygroup",
            MaxSize="1",
            MinSize="1",
        )
        with self.assertRaises(ValueError):
            self.assertTrue(group.validate())

    def test_instanceid(self):
        group = AutoScalingGroup(
            "mygroup",
            AvailabilityZones=["eu-west-1a", "eu-west-1b"],
            InstanceId="i-1234",
            MaxSize="1",
            MinSize="1",
        )
        self.assertTrue(group.validate())

    def test_launchconfigurationname(self):
        group = AutoScalingGroup(
            "mygroup",
            AvailabilityZones=["eu-west-1a", "eu-west-1b"],
            LaunchConfigurationName="I'm a test",
            MaxSize="1",
            MinSize="1",
        )
        self.assertTrue(group.validate())

    def test_size_if(self):
        group = AutoScalingGroup(
            "mygroup",
            AvailabilityZones=["eu-west-1a", "eu-west-1b"],
            LaunchConfigurationName="I'm a test",
            MaxSize=If("isstage", "1", "5"),
            MinSize="1",
            UpdatePolicy=UpdatePolicy(
                AutoScalingRollingUpdate=AutoScalingRollingUpdate(
                    PauseTime="PT5M",
                    MinInstancesInService="1",
                    MaxBatchSize="1",
                    WaitOnResourceSignals=True,
                )
            ),
        )
        self.assertTrue(group.validate())

    def test_helperfn_as_updatepolicy(self):
        update_policy = UpdatePolicy(
            AutoScalingRollingUpdate=AutoScalingRollingUpdate(
                PauseTime="PT5M",
                MinInstancesInService="1",
                MaxBatchSize="1",
                WaitOnResourceSignals=True,
            )
        )
        group = AutoScalingGroup(
            "mygroup",
            AvailabilityZones=["eu-west-1a", "eu-west-1b"],
            LaunchConfigurationName="I'm a test",
            MaxSize=If("isstage", "1", "5"),
            MinSize="1",
            UpdatePolicy=If("UseUpdatePolicy", update_policy, Ref("AWS::NoValue")),
        )
        self.assertTrue(group.validate())

    def test_helperfn_as_AutoScalingRollingUpdate(self):
        update_policy = UpdatePolicy(
            AutoScalingRollingUpdate=If(
                "RollingUpdate",
                AutoScalingRollingUpdate(
                    PauseTime="PT5M",
                    MinInstancesInService="1",
                    MaxBatchSize="1",
                    WaitOnResourceSignals=True,
                ),
                Ref("AWS::NoValue"),
            ),
        )
        group = AutoScalingGroup(
            "mygroup",
            AvailabilityZones=["eu-west-1a", "eu-west-1b"],
            LaunchConfigurationName="I'm a test",
            MaxSize=If("isstage", "1", "5"),
            MinSize="1",
            UpdatePolicy=If("UseUpdatePolicy", update_policy, Ref("AWS::NoValue")),
        )
        self.assertTrue(group.validate())

    def test_AutoScalingRollingUpdate_all_defaults(self):
        group = AutoScalingGroup(
            "mygroup",
            AvailabilityZones=["eu-west-1a", "eu-west-1b"],
            LaunchConfigurationName="I'm a test",
            MaxSize="1",
            MinSize="1",
            UpdatePolicy=UpdatePolicy(
                AutoScalingRollingUpdate=AutoScalingRollingUpdate()
            ),
        )
        self.assertTrue(group.validate())

    def test_AutoScalingRollingUpdate_validation(self):
        update_policy = UpdatePolicy(
            AutoScalingRollingUpdate=AutoScalingRollingUpdate(
                MinInstancesInService="2", MaxBatchSize="1"
            )
        )
        group = AutoScalingGroup(
            "mygroup",
            AvailabilityZones=["eu-west-1a", "eu-west-1b"],
            LaunchConfigurationName="I'm a test",
            MaxSize="2",
            MinSize="1",
            UpdatePolicy=update_policy,
        )

        with self.assertRaises(ValueError):
            self.assertTrue(group.validate())

    def test_can_define_gp3_ebsblockdevice(self):
        ebs = EBSBlockDevice(
            DeleteOnTermination=True,
            Encrypted=True,
            Iops=3000,
            Throughput=500,
            VolumeSize=100,
            VolumeType="gp3"
        )

        self.assertEquals(ebs.properties["VolumeType"], "gp3")
        self.assertIn("Throughput", ebs.properties,
                      "gp3 volumes require an additional Throughput param")


if __name__ == "__main__":
    unittest.main()
