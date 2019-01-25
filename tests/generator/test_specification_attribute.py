import unittest
from troposphere_gen.specification import Attribute
from troposphere_gen.types import *


class TestProperty(unittest.TestCase):
    def test_primitive(self):
        attributedict = {
            "PrimitiveType": "String"
        }

        prop = Attribute("TestAttribute", attributedict)

        self.assertEqual(PrimitiveType, type(prop.primitive_type))
        self.assertEqual(None, prop.type)

    def test_map_primitive(self):
        attributedict = {
            "Type": "Map",
            "PrimitiveItemType": "String",
        }

        prop = Attribute("TestAttribute", attributedict)

        self.assertEqual(None, prop.primitive_type)
        self.assertEqual(MapType, type(prop.type))
        self.assertEqual(PrimitiveType, type(prop.type.itemtype))

    def test_map_subproperty(self):
        attributedict = {
            "Type": "Map",
            "ItemType": "SomeType",
        }

        prop = Attribute("TestAttribute", attributedict)

        self.assertEqual(None, prop.primitive_type)
        self.assertEqual(MapType, type(prop.type))
        self.assertEqual(Subproperty, type(prop.type.itemtype))

    def test_list_primitive(self):
        attributedict = {
            "Type": "List",
            "PrimitiveItemType": "String",
        }

        prop = Attribute("TestAttribute", attributedict)

        self.assertEqual(None, prop.primitive_type)
        self.assertEqual(ListType, type(prop.type))
        self.assertEqual(PrimitiveType, type(prop.type.itemtype))

    def test_list_subproperty(self):
        attributedict = {
            "Type": "List",
            "ItemType": "SomeType",
        }

        prop = Attribute("TestAttribute", attributedict)

        self.assertEqual(None, prop.primitive_type)
        self.assertEqual(ListType, type(prop.type))
        self.assertEqual(Subproperty, type(prop.type.itemtype))


if __name__ == '__main__':
    unittest.main()
