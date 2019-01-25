import unittest
from troposphere_gen.specification import Resource


class TestProperty(unittest.TestCase):
    def test_resource(self):
        resourcedict = {
            "Attributes": {
                "SomeAttrib": {
                    "PrimitiveType": "String"
                },
                "AnotherAttrib": {
                    "PrimitiveType": "String"
                }
            },
            "Documentation": "http://example.com/foo",
            "Properties": {
                "SomeProp": {
                    "Documentation": "http://example.com/foo",
                    "Required": True,
                    "PrimitiveType": "String",
                    "UpdateType": "Mutable"
                },
                "AnotherProp": {
                    "Documentation": "http://example.com/foo",
                    "Required": True,
                    "PrimitiveType": "String",
                    "UpdateType": "Mutable"
                }
            }
        }

        res = Resource("SomeRes", resourcedict)

        self.assertEqual(resourcedict["Documentation"], res.documentation)
        self.assertEqual(2, len(res.attributes.values()))
        self.assertEqual(2, len(res.properties.values()))
        self.assertIn("SomeAttrib", res.attributes)
        self.assertIn("AnotherAttrib", res.attributes)
        self.assertIn("SomeProp", res.properties)
        self.assertIn("AnotherProp", res.properties)


if __name__ == '__main__':
    unittest.main()
