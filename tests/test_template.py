import unittest

from troposphere import Template, Parameter, Output
from troposphere.s3 import Bucket


class TestInitArguments(unittest.TestCase):
    def test_description_default(self):
        template = Template()
        self.assertIsNone(template.description)

    def test_description(self):
        value = 'foo'
        template = Template(Description=value)
        self.assertEqual(template.description, value)

    def test_metadata_default(self):
        template = Template()
        self.assertEqual(template.metadata, {})

    def test_metadata(self):
        value = 'foo'
        template = Template(Metadata=value)
        self.assertEqual(template.metadata, value)


class TestValidate(unittest.TestCase):
    def test_max_parameters(self):
        template = Template()
        for i in range(1, 61):
            template.add_parameter(Parameter("parameter%d" % i, Type='String'))
        with self.assertRaises(ValueError):
            template.add_parameter(Parameter("Parameter61", Type='String'))

    def test_max_resources(self):
        template = Template()
        for i in range(1, 201):
            template.add_resource(Bucket(str(i)))
        with self.assertRaises(ValueError):
            template.add_resource(Bucket(str(201)))

    def test_max_outputs(self):
        template = Template()
        for i in range(1, 61):
            template.add_output(Output("output%d" % i, Value="Output%s" % str(i)))
        with self.assertRaises(ValueError):
            template.add_output(Output("output61", Value="Output%s" % str(61)))

    def test_max_mappings(self):
        template = Template()
        for i in range(1, 101):
            template.add_mapping("mapping%d" % i, { "name%d" % i: "value%d" %i })
        with self.assertRaises(ValueError):
            template.add_mapping("mapping101", { "name101": "value101" })

if __name__ == '__main__':
    unittest.main()
