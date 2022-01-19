import unittest

from troposphere import Template
from troposphere.opsworks import Stack


class TestOpsWorksStack(unittest.TestCase):
    def test_nosubnet(self):
        stack = Stack(
            "mystack",
            VpcId="myvpcid",
        )
        with self.assertRaises(ValueError):
            stack.validate()

    def test_stack(self):
        stack = Stack(
            "mystack",
            VpcId="myvpcid",
            DefaultSubnetId="subnetid",
        )
        self.assertIsNone(stack.validate())

    def test_no_required(self):
        stack = Stack(
            "mystack",
        )
        t = Template()
        t.add_resource(stack)
        with self.assertRaises(ValueError):
            t.to_json()

    def test_required(self):
        stack = Stack(
            "mystack",
            DefaultInstanceProfileArn="instancearn",
            Name="myopsworksname",
            ServiceRoleArn="arn",
        )
        t = Template()
        t.add_resource(stack)
        t.to_json()

    def test_custom_json(self):
        stack = Stack(
            "mystack",
            DefaultInstanceProfileArn="instancearn",
            Name="myopsworksname",
            ServiceRoleArn="arn",
        )

        # Test dict works
        t = Template()
        stack.CustomJson = {"foo": "bar"}
        t.add_resource(stack)
        t.to_json()

        # Test json string works
        t = Template()
        stack.CustomJson = '{"foo": "bar"}'
        t.add_resource(stack)
        t.to_json()

        # Test boolean fails
        with self.assertRaises(TypeError):
            stack.CustomJson = True


if __name__ == "__main__":
    unittest.main()
