import unittest

from troposphere.appconfig import DeploymentStrategy, Validators


class TestAppconfigDeploymentStrategy(unittest.TestCase):
    def test_deploymentstrategy_growthtype_bad_value(self):
        with self.assertRaisesRegex(ValueError, "GrowthType must be one of"):
            DeploymentStrategy(
                "DeploymentStrategy",
                DeploymentDurationInMinutes=1,
                GrowthFactor=1,
                GrowthType="LINEA",
                Name="DeploymentStrategy",
                ReplicateTo="NONE",
            )

    def test_deploymentstrategy_replicateto_bad_value(self):
        with self.assertRaisesRegex(ValueError, "ReplicateTo must be one of"):
            DeploymentStrategy(
                "DeploymentStrategy",
                DeploymentDurationInMinutes=1,
                GrowthFactor=1,
                Name="DeploymentStrategy",
                ReplicateTo="none",
            )

    def test_deploymentstrategy(self):
        for replicate_to in ("NONE", "SSM_DOCUMENT"):
            DeploymentStrategy(
                "DeploymentStrategy",
                DeploymentDurationInMinutes=1,
                GrowthFactor=1,
                GrowthType="LINEAR",
                Name="DeploymentStrategy",
                ReplicateTo=replicate_to,
            )


class TestAppconfigValidators(unittest.TestCase):
    def test_validators_type_bad_value(self):
        with self.assertRaisesRegex(ValueError, "Validator Type must be one of"):
            Validators(Type="JSON_SCHEM")

    def test_validators_type(self):
        for validator_type in ("JSON_SCHEMA", "LAMBDA"):
            Validators(Type=validator_type)
