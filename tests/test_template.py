import unittest

from base import ARMTemplate, ARMParameter
from network import PublicIPAddress

# Template Limits
MAX_MAPPINGS = 100
MAX_OUTPUTS = 64
MAX_PARAMETERS = 256
MAX_RESOURCES = 800


class TestInitArguments(unittest.TestCase):
    def test_description_default(self):
        template = ARMTemplate()
        self.assertIsNone(template.description)

    def test_description(self):
        value = 'foo'
        template = ARMTemplate(Description=value)
        self.assertEqual(template.description, value)


class TestValidate(unittest.TestCase):
    def test_max_parameters(self):
        template = ARMTemplate()
        for i in range(0, MAX_PARAMETERS):
            template.add_parameter(ARMParameter(str(i), type='string'))
        with self.assertRaises(ValueError):
            template.add_parameter(ARMParameter("parameter", type='string'))

    def test_max_resources(self):
        template = ARMTemplate()
        for i in range(0, MAX_RESOURCES):
            template.add_resource(PublicIPAddress(str(i)))
        with self.assertRaises(ValueError):
            template.add_resource(PublicIPAddress("address"))

    # todo - add outputs
    # def test_max_outputs(self):
    #     template = ARMTemplate()
    #     for i in range(0, MAX_OUTPUTS):
    #         template.add_output(Output(str(i), Value=str(i)))
    #     with self.assertRaises(ValueError):
    #         template.add_output(Output("output", Value="output"))


if __name__ == '__main__':
    unittest.main()
