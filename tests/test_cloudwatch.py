import unittest

import troposphere.cloudwatch as cloudwatch
from troposphere.cloudwatch import Dashboard


class TestModel(unittest.TestCase):
    def test_dashboard(self):
        # Check valid json dashboard string
        dashboard = Dashboard(
            "dashboard",
            DashboardBody='{"a": "b"}',
        )
        dashboard.validate()

        # Check invalid json dashboard string
        dashboard = Dashboard(
            "dashboard",
            DashboardBody='{"a: "b"}',
        )
        with self.assertRaises(ValueError):
            dashboard.validate()

        # Check accepting dict and converting to string in validate
        d = {"c": "d"}
        dashboard = Dashboard("dashboard", DashboardBody=d)
        dashboard.validate()
        self.assertEqual(dashboard.properties["DashboardBody"], '{"c": "d"}')

        # Check invalid Dashboard type
        with self.assertRaises(TypeError):
            dashboard = Dashboard("dashboard", DashboardBody=1)


class TestCloudWatchValidators(unittest.TestCase):
    def test_validate_units(self):
        cloudwatch.validate_unit("Bytes/Second")
        for bad_unit in ["Minutes", "Bytes/Minute", "Bits/Hour", ""]:
            with self.assertRaisesRegex(ValueError, "must be one of"):
                cloudwatch.validate_unit(bad_unit)

    def test_validate_treat_missing_data(self):
        cloudwatch.validate_treat_missing_data("missing")
        for bad_value in ["exists", "notMissing", ""]:
            with self.assertRaisesRegex(ValueError, "must be one of"):
                cloudwatch.validate_treat_missing_data(bad_value)


if __name__ == "__main__":
    unittest.main()
