import unittest

import troposphere.codecommit as cc


class TestCodeCommit(unittest.TestCase):
    def test_trigger(self):
        trigger = cc.Trigger(
            DestinationArn="arn:random",
            Events=[
                "all",
            ],
            Name="trigger name",
        )
        trigger.to_dict()

        trigger = cc.Trigger(
            DestinationArn="arn:random",
            Events=[
                "updateReference",
                "createReference",
                "deleteReference",
            ],
            Name="trigger name",
        )
        trigger.to_dict()

        trigger = cc.Trigger(
            DestinationArn="arn:random",
            Events=[
                "all",
                "deleteReference",
            ],
            Name="trigger name",
        )
        with self.assertRaisesRegex(ValueError, "Trigger events: all"):
            trigger.to_dict()

        trigger = cc.Trigger(
            DestinationArn="arn:random",
            Events=[
                "deleteReference",
                "foobar",
            ],
            Name="trigger name",
        )
        with self.assertRaisesRegex(ValueError, "invalid event foobar"):
            trigger.to_dict()
