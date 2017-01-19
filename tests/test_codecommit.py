import unittest
import troposphere.codecommit as cc


class TestCodeCommit(unittest.TestCase):

    def test_trigger(self):
        trigger = cc.Trigger(
            Events=[
                'all',
            ]
        )
        trigger.JSONrepr()

        trigger = cc.Trigger(
            Events=[
                'updateReference',
                'createReference',
                'deleteReference',
            ]
        )
        trigger.JSONrepr()

        trigger = cc.Trigger(
            Events=[
                'all',
                'deleteReference',
            ]
        )
        with self.assertRaisesRegexp(ValueError, "Trigger events: all"):
            trigger.JSONrepr()

        trigger = cc.Trigger(
            Events=[
                'deleteReference',
                'foobar',
            ]
        )
        with self.assertRaisesRegexp(ValueError, "invalid event foobar"):
            trigger.JSONrepr()
