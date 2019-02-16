import unittest
from troposphere_gen.validatordata import *

validatordata = {
    "PropertyTypes": {
        "AWS::SomeService::SomeResource.SomeProperty": {
            "Properties": {
                "SubProperty1": {
                    "Validator": "Map",
                    "ValidatorKey": {
                        "Validator": "somefunc1",
                        "kwarg1": "foo",
                        "kwarg2": "bar",
                    },
                    "ValidatorValue": {
                        "Validator": "somefunc2",
                        "kwarg3": "baz"
                    }
                },
                "SubProperty2": {
                    "Validator": "somefunc3",
                    "kwarg1": "foo",
                    "kwarg2": "bar",
                    "kwarg3": "baz"
                }
            }
        }
    },
    "ResourceTypes": {}
}


class TestValidatorData(unittest.TestCase):
    def test_validatordata(self):
        valdata = ValidatorData(validatordata["PropertyTypes"]["AWS::SomeService::SomeResource.SomeProperty"])

        # Check that both Properties were found
        self.assertEqual(2, len(valdata.validators))
        self.assertIn("SubProperty1", valdata.validators)
        self.assertIn("SubProperty2", valdata.validators)

        # Check Map-type validator
        mapval = valdata.validators["SubProperty1"]
        self.assertIsNone(mapval.function)
        self.assertDictEqual({}, mapval.kwargs)
        self.assertEqual("somefunc1", mapval.map_key_function)
        self.assertDictEqual({"kwarg1": "foo", "kwarg2": "bar"}, mapval.map_key_kwargs)
        self.assertEqual("somefunc2", mapval.map_value_function)
        self.assertDictEqual({"kwarg3": "baz"}, mapval.map_value_kwargs)

        # Check regular validator (non-Map)
        val = valdata.validators["SubProperty2"]
        self.assertEqual("somefunc3", val.function)
        self.assertDictEqual({"kwarg1": "foo", "kwarg2": "bar", "kwarg3": "baz"}, val.kwargs)


if __name__ == '__main__':
    unittest.main()
