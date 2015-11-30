import unittest
from troposphere import Template, Retain
from troposphere.logs import LogGroup


class TestLogGroup(unittest.TestCase):
    def test_loggroup_deletionpolicy_is_preserved(self):
        log_group = LogGroup(
            "LogGroupWithDeletionPolicy",
            DeletionPolicy=Retain
        )
        self.assertIn('DeletionPolicy', log_group.JSONrepr())


if __name__ == '__main__':
    unittest.main()
