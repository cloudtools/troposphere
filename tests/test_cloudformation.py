import unittest

from troposphere import Ref
from troposphere.cloudformation import WaitCondition, WaitConditionHandle
from troposphere.policies import CreationPolicy, ResourceSignal


class TestWaitCondition(unittest.TestCase):
    def test_CreationPolicy(self):
        w = WaitCondition(
            "mycondition",
            CreationPolicy=CreationPolicy(
                ResourceSignal=ResourceSignal(Timeout="PT15M")
            ),
        )
        w.validate()

    def test_CreationPolicyWithProps(self):
        w = WaitCondition(
            "mycondition",
            Count=10,
            CreationPolicy=CreationPolicy(
                ResourceSignal=ResourceSignal(Timeout="PT15M")
            ),
        )
        with self.assertRaises(ValueError):
            w.validate()

    def test_RequiredProps(self):
        handle = WaitConditionHandle("myWaitHandle")
        w = WaitCondition(
            "mycondition",
            Handle=Ref(handle),
            Timeout="300",
        )
        w.validate()


if __name__ == "__main__":
    unittest.main()
