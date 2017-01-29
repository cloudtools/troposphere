import unittest
from troposphere import autoscaling, policies, Ref


class TestAutoScalingGroup(unittest.TestCase):
    def test_validate_allow_helper_fn_in_update_policy(self):
        asg = autoscaling.AutoScalingGroup(
            "AutoScalingGroup",
            LaunchConfigurationName="FakeLaunchName",
            AvailabilityZones=["us-east-1a", ],
            MinSize=1,
            MaxSize=10,
            UpdatePolicy=policies.UpdatePolicy(
                AutoScalingRollingUpdate=Ref("AWS::NoValue")
            )
        )

        asg.validate()
