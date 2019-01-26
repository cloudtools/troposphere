import unittest
from troposphere_gen.specification import Specification
import json

from distutils.version import StrictVersion


class TestProperty(unittest.TestCase):
    def test_resource(self):
        with open("specification_testdata.json", "r") as f:
            specificationdict = json.load(f)

        spec = Specification("SomeSpecification", specificationdict)

        # Check version and whether correct amount of resources and properties exist
        self.assertEqual(StrictVersion(specificationdict["ResourceSpecificationVersion"]),
                         spec.resource_specification_version)
        self.assertEqual(4, len(spec.property_types.values()))
        self.assertEqual(1, len(spec.resource_types.values()))


if __name__ == '__main__':
    unittest.main()
