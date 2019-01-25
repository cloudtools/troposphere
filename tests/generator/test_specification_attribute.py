import unittest
from troposphere_gen.specification import Attribute
from troposphere_gen.types import *


class TestProperty(unittest.TestCase):
    def test_primitive(self):
        attributedict = {
            "PrimitiveType": "String"
        }

        attrib = Attribute("TestAttribute", attributedict)

        self.assertEqual(PrimitiveType, type(attrib.primitive_type))
        self.assertEqual(None, attrib.type)

    def test_map_primitive(self):
        attributedict = {
            "Type": "Map",
            "PrimitiveItemType": "String",
        }

        attrib = Attribute("TestAttribute", attributedict)

        self.assertEqual(None, attrib.primitive_type)
        self.assertEqual(MapType, type(attrib.type))
        self.assertEqual(PrimitiveType, type(attrib.type.itemtype))

    def test_map_subproperty(self):
        attributedict = {
            "Type": "Map",
            "ItemType": "SomeType",
        }

        attrib = Attribute("TestAttribute", attributedict)

        self.assertEqual(None, attrib.primitive_type)
        self.assertEqual(MapType, type(attrib.type))
        self.assertEqual(Subproperty, type(attrib.type.itemtype))

    def test_list_primitive(self):
        attributedict = {
            "Type": "List",
            "PrimitiveItemType": "String",
        }

        attrib = Attribute("TestAttribute", attributedict)

        self.assertEqual(None, attrib.primitive_type)
        self.assertEqual(ListType, type(attrib.type))
        self.assertEqual(PrimitiveType, type(attrib.type.itemtype))

    def test_list_subproperty(self):
        attributedict = {
            "Type": "List",
            "ItemType": "SomeType",
        }

        attrib = Attribute("TestAttribute", attributedict)

        self.assertEqual(None, attrib.primitive_type)
        self.assertEqual(ListType, type(attrib.type))
        self.assertEqual(Subproperty, type(attrib.type.itemtype))


if __name__ == '__main__':
    unittest.main()
