import unittest

from troposphere import Name
from troposphere.iottwinmaker import DataType, DataValue


class TestPlacementTemplate(unittest.TestCase):
    def test_datatype_nestedtype(self):
        with self.assertRaises(TypeError):
            DataType(NestedType="foo")

        DataType(NestedType=DataType())
        DataType(NestedType=Name("foo"))

    def test_datavalue_listvalue(self):
        with self.assertRaises(TypeError):
            DataValue(ListValue="foo")

        with self.assertRaises(TypeError):
            DataValue(ListValue=["foo"])

        DataValue(ListValue=[DataValue(), Name("foo")])
