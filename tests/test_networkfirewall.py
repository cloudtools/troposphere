import unittest

from troposphere.networkfirewall import RuleGroup


class TestNetworkFirewall(unittest.TestCase):
    def test_RuleGroup(self):
        RuleGroup(
            "rulegroup",
            Capacity="10",
            RuleGroupName="foobar",
            Type="STATEFUL",
        ).to_dict()

    def test_invalid_RuleGroup(self):
        with self.assertRaises(ValueError):
            RuleGroup(
                "rulegroup",
                Capacity="10",
                RuleGroupName="foobar",
                Type="NOSTATE",
            ).to_dict()


if __name__ == "__main__":
    unittest.main()
