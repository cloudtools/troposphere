import unittest

from troposphere.intrinsic_functions import *


class TestIntrinsicFunctions(unittest.TestCase):
    def test_to_dict(self):
        """Test all three modes of to_dict"""
        # Function with primitive parameter
        expected = {
            "Ref": "foo"
        }
        self.assertDictEqual(expected, Ref("foo").to_dict())

        # Nested functions
        expected = {
            "Fn::ImportValue": {"Fn::Join": [" ", ["join", "me"]]}
        }
        self.assertDictEqual(expected, FnImportValue(FnJoin(" ", ["join", "me"])).to_dict())

        # List with nested function
        expected = {
            "Fn::Base64": {"Ref": "foo"}
        }
        self.assertDictEqual(expected, FnBase64(Ref("foo")).to_dict())

        # List with mixed nested and primitive arguments and sublists
        expected = {
            "Fn::Base64": {"Fn::Join": [" ", [{"Ref": "foo"}, "bar", {"Ref": {"Ref": "baz"}}]]}
        }
        self.assertDictEqual(expected, FnBase64(FnJoin(" ", [Ref("foo"), "bar", Ref(Ref("baz"))])).to_dict())

    def test_fn_base64(self):
        expected = {
            "Fn::Base64": "SomeString"
        }
        self.assertDictEqual(expected, FnBase64("SomeString").to_dict())

    def test_fn_cidr(self):
        expected = {
            "Fn::Cidr": [
                "10.10.0.0/16",
                123,
                16
            ]
        }
        self.assertDictEqual(expected, FnCidr("10.10.0.0/16", 123, 16).to_dict())
        with self.assertRaises(ValueError):
            FnCidr("10.10.0.0/16", 99999, 16)

    def test_fn_findinmap(self):
        expected = {
            "Fn::FindInMap": [
                "foo",
                "bar",
                "baz"
            ]
        }
        self.assertDictEqual(expected, FnFindInMap("foo", "bar", "baz").to_dict())

    def test_fn_getatt(self):
        expected = {
            "Fn::GetAtt": [
                "foo",
                "bar"
            ]
        }
        self.assertDictEqual(expected, FnGetAtt("foo", "bar").to_dict())

    def test_fn_getazs(self):
        expected = {
            "Fn::GetAZs": "foo"
        }
        self.assertDictEqual(expected, FnGetAZs("foo").to_dict())

    def test_fn_importvalue(self):
        expected = {
            "Fn::ImportValue": "foo"
        }
        self.assertDictEqual(expected, FnImportValue("foo").to_dict())

    def test_fn_join(self):
        expected = {
            "Fn::Join": [
                " ",
                ["Join", "this", "please"]
            ]
        }
        self.assertDictEqual(expected, FnJoin(" ", ["Join", "this", "please"]).to_dict())

    def test_fn_select(self):
        expected = {
            "Fn::Select": [
                1,
                ["val0", "val1", "val2"]
            ]
        }
        self.assertDictEqual(expected, FnSelect(1, ["val0", "val1", "val2"]).to_dict())

    def test_ref(self):
        expected = {
            "Ref": "foo"
        }
        self.assertDictEqual(expected, Ref("foo").to_dict())

    def test_fn_if(self):
        expected = {
            "Fn::If": [
                "foo",
                "bar",
                "baz"
            ]
        }
        self.assertDictEqual(expected, FnIf("foo", "bar", "baz").to_dict())

    def test_fn_sub(self):
        expected = {
            "Fn::Sub": "foo"
        }
        self.assertDictEqual(expected, FnSub("foo").to_dict())
        expected = {
            "Fn::Sub": [
                "foo",
                {
                    "foo1", "bar1",
                    "foo2", "bar2"
                }
            ]
        }
        self.assertDictEqual(expected, FnSub("foo", {"foo1", "bar1", "foo2", "bar2"}).to_dict())

    def test_fn_split(self):
        expected = {
            "Fn::Split": [
                "foo",
                "bar"
            ]
        }
        self.assertDictEqual(expected, FnSplit("foo", "bar").to_dict())

    def test_fn_transform(self):
        expected = {
            "Fn::Transform": {
                "Name": "foo",
                "Parameters": {
                    "param1": "foo",
                    "param2": "bar"
                }
            }
        }
        self.assertDictEqual(expected, FnTransform("foo", {"param1": "foo", "param2": "bar"}).to_dict())

    def test_fn_and(self):
        expected = {
            "Fn::And": [
                {"Ref": "foo"},
                {"Ref": "bar"}
            ]
        }
        self.assertDictEqual(expected, FnAnd([Ref("foo"), Ref("bar")]).to_dict())

    def test_fn_equals(self):
        expected = {
            "Fn::Equals": [
                {"Ref": "foo"},
                {"Ref": "bar"}
            ]
        }
        self.assertDictEqual(expected, FnEquals(Ref("foo"), Ref("bar")).to_dict())

    def test_fn_not(self):
        expected = {
            "Fn::Not": [
                {"Ref": "foo"}
            ]
        }
        self.assertDictEqual(expected, FnNot(Ref("foo")).to_dict())

    def test_fn_or(self):
        expected = {
            "Fn::Or": [
                {"Ref": "foo"},
                {"Ref": "bar"}
            ]
        }
        self.assertDictEqual(expected, FnOr([Ref("foo"), Ref("bar")]).to_dict())

if __name__ == '__main__':
    unittest.main()
