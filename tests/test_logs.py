import unittest
from troposphere import Retain
from troposphere.logs import LogGroup, Destination


class TestLogs(unittest.TestCase):
    def test_loggroup_deletionpolicy_is_preserved(self):
        log_group = LogGroup(
            "LogGroupWithDeletionPolicy",
            DeletionPolicy=Retain
        )
        self.assertIn('DeletionPolicy', log_group.to_dict())

    def test_loggroup_retention(self):
        for days in [7, "7"]:
            LogGroup(
                "LogGroupWithDeletionPolicy",
                RetentionInDays=days,
            )

        for days in [6, "6"]:
            with self.assertRaises(ValueError):
                LogGroup(
                    "LogGroupWithDeletionPolicy",
                    RetentionInDays=days,
                )

    def test_log_destination(self):
        log_destination = Destination(
            'MyLogDestination',
            DestinationName='destination-name',
            RoleArn='role-arn',
            TargetArn='target-arn',
            DestinationPolicy='destination-policy'
        )
        log_destination_json = log_destination.to_dict()
        self.assertIn('Type', log_destination_json)
        self.assertIn('Properties', log_destination_json)


if __name__ == '__main__':
    unittest.main()
