import unittest

from troposphere import Retain
from troposphere.logs import (
    Destination,
    LogGroup,
    ResourcePolicy,
    validate_resource_policy,
)


class TestLogs(unittest.TestCase):
    def test_loggroup_deletionpolicy_is_preserved(self):
        log_group = LogGroup("LogGroupWithDeletionPolicy", DeletionPolicy=Retain)
        self.assertIn("DeletionPolicy", log_group.to_dict())

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
            "MyLogDestination",
            DestinationName="destination-name",
            RoleArn="role-arn",
            TargetArn="target-arn",
            DestinationPolicy="destination-policy",
        )
        log_destination_json = log_destination.to_dict()
        self.assertIn("Type", log_destination_json)
        self.assertIn("Properties", log_destination_json)

    def test_validate_resource_policy(self):
        for s in [
            '{ "Version": "2012-10-17", "Statement": [ { "Sid": "Route53LogsToCloudWatchLogs", "Effect": "Allow", "Principal": { "Service": [ "route53.amazonaws.com" ] }, "Action":"logs:PutLogEvents", "Resource": "logArn" } ] }',
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "Route53LogsToCloudWatchLogs",
                        "Effect": "Allow",
                        "Principal": {"Service": ["route53.amazonaws.com"]},
                        "Action": "logs:PutLogEvents",
                        "Resource": "logArn",
                    }
                ],
            },
        ]:
            validate_resource_policy(s)
            log_policy = ResourcePolicy(
                "TestLogPolicy", PolicyName="TestLogPolicy", PolicyDocument=s
            )
            expected = log_policy.to_dict()
            properties = expected["Properties"]
            self.assertEqual(properties.get("PolicyDocument"), s)

        for s in ["", "H" * 5121, "TEXT", {}]:
            with self.assertRaises(ValueError):
                validate_resource_policy(s)


if __name__ == "__main__":
    unittest.main()
