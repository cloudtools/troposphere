import unittest

from troposphere import Template


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


if __name__ == '__main__':
    unittest.main()
