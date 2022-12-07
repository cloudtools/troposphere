import unittest

from troposphere.scheduler import EcsParameters, FlexibleTimeWindow


class TestSchedule(unittest.TestCase):
    def test_flexible_time_window_mode(self):
        for invalid_value in ("", "not-valid"):
            with self.assertRaises(ValueError):
                FlexibleTimeWindow(Mode=invalid_value).to_dict()

        for valid_value in ("OFF", "FLEXIBLE"):
            FlexibleTimeWindow(Mode=valid_value).to_dict()

    def test_ecsparameters_tags(self):
        with self.assertRaises(ValueError):
            EcsParameters(
                TaskDefinitionArn="some-arn",
                Tags={"tag1": "value1"},
            ).to_dict()

        EcsParameters(TaskDefinitionArn="some-arn").to_dict()


if __name__ == "__main__":
    unittest.main()
