import unittest
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
        dashboard = Dashboard(
            "dashboard",
            DashboardBody=d
        )
        dashboard.validate()
        self.assertEqual(dashboard.properties['DashboardBody'], '{"c": "d"}')

        # Check invalid Dashboard type
        with self.assertRaises(TypeError):
            dashboard = Dashboard(
                "dashboard",
                DashboardBody=1
            )


if __name__ == '__main__':
    unittest.main()
