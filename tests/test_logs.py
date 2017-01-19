import unittest
from troposphere import Retain
from troposphere.logs import LogGroup, Destination


class TestLogs(unittest.TestCase):
    def test_loggroup_deletionpolicy_is_preserved(self):
        log_group = LogGroup(
            "LogGroupWithDeletionPolicy",
            DeletionPolicy=Retain
        )
        self.assertIn('DeletionPolicy', log_group.JSONrepr())

    def test_log_destination(self):
        log_destination = Destination(
            'MyLogDestination',
            DestinationName='destination-name',
            RoleArn='role-arn',
            TargetArn='target-arn',
            DestinationPolicy='destination-policy'
        )
        log_destination_json = log_destination.JSONrepr()
        self.assertIn('Type', log_destination_json)
        self.assertIn('Properties', log_destination_json)


if __name__ == '__main__':
    unittest.main()
