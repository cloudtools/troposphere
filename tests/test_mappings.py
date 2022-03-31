import unittest

from troposphere import Template

single_mapping = """\
{
 "Mappings": {
  "map": {
   "n": "v"
  }
 },
 "Resources": {}
}"""

multiple_mappings = """\
{
 "Mappings": {
  "map": {
   "k1": {
    "n1": "v1"
   },
   "k2": {
    "n2": "v2"
   }
  }
 },
 "Resources": {}
}"""


class TestMappings(unittest.TestCase):
    def test_single_mapping(self):
        template = Template()
        template.add_mapping("map", {"n": "v"})
        json = template.to_json()
        self.assertEqual(single_mapping, json)

    def test_multiple_mappings(self):
        template = Template()
        template.add_mapping("map", {"k1": {"n1": "v1"}})
        template.add_mapping("map", {"k2": {"n2": "v2"}})
        json = template.to_json()
        self.assertEqual(multiple_mappings, json)


if __name__ == "__main__":
    unittest.main()
