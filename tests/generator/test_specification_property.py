import unittest
from troposphere_gen.specification import Property
from troposphere_gen.types import *


class TestProperty(unittest.TestCase):
    def test_primitive(self):
        propertydict = {
            "Documentation": "http://example.com/foo",
            "PrimitiveType": "String",
            "Required": False,
            "UpdateType": "Mutable"
        }

        prop = Property("TestProperty", propertydict)

        self.assertEqual(PrimitiveType, type(prop.primitive_type))
        self.assertEqual(None, prop.type)

    def test_map_primitive(self):
        propertydict = {
            "Documentation": "http://example.com/foo",
            "Type": "Map",
            "PrimitiveItemType": "String",
            "Required": False,
            "UpdateType": "Mutable"
        }

        prop = Property("TestProperty", propertydict)

        self.assertEqual(None, prop.primitive_type)
        self.assertEqual(MapType, type(prop.type))
        self.assertEqual(PrimitiveType, type(prop.type.itemtype))

    def test_map_subproperty(self):
        propertydict = {
            "Documentation": "http://example.com/foo",
            "Type": "Map",
            "ItemType": "SomeType",
            "Required": False,
            "UpdateType": "Mutable"
        }

        prop = Property("TestProperty", propertydict)

        self.assertEqual(None, prop.primitive_type)
        self.assertEqual(MapType, type(prop.type))
        self.assertEqual(Subproperty, type(prop.type.itemtype))

    def test_list_primitive(self):
        propertydict = {
            "Documentation": "http://example.com/foo",
            "Type": "List",
            "PrimitiveItemType": "String",
            "Required": False,
            "UpdateType": "Mutable"
        }

        prop = Property("TestProperty", propertydict)

        self.assertEqual(None, prop.primitive_type)
        self.assertEqual(ListType, type(prop.type))
        self.assertEqual(PrimitiveType, type(prop.type.itemtype))

    def test_list_subproperty(self):
        propertydict = {
            "Documentation": "http://example.com/foo",
            "Type": "List",
            "ItemType": "SomeType",
            "Required": False,
            "UpdateType": "Mutable"
        }

        prop = Property("TestProperty", propertydict)

        self.assertEqual(None, prop.primitive_type)
        self.assertEqual(ListType, type(prop.type))
        self.assertEqual(Subproperty, type(prop.type.itemtype))

    def test_subproperty(self):
        propertydict = {
            "Documentation": "http://example.com/foo",
            "Type": "SomeSubProperty",
            "PrimitiveItemType": "String",
            "Required": False,
            "UpdateType": "Mutable"
        }

        prop = Property("TestProperty", propertydict)

        self.assertEqual(None, prop.primitive_type)
        self.assertEqual(Subproperty, type(prop.type))
        self.assertEqual(None, prop.type.print_class)


if __name__ == '__main__':
    unittest.main()
