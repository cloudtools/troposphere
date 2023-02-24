import unittest

from troposphere.dlm import CreateRule


class TestDlmCreateRule(unittest.TestCase):
    def test_createrule_interval_bad_value(self):
        with self.assertRaisesRegex(ValueError, "Interval must be one of"):
            CreateRule("CreateRule", Interval=25)

    def test_createrule_intervalunit_bad_value(self):
        with self.assertRaisesRegex(ValueError, "Interval unit must be one of"):
            CreateRule("CreateRule", Interval=24, IntervalUnit="HOUR")

    def test_createrule(self):
        CreateRule("CreateRule", Interval=24, IntervalUnit="HOURS")
