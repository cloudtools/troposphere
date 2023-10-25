import unittest

from troposphere import (
    MAX_MAPPINGS,
    MAX_OUTPUTS,
    MAX_PARAMETERS,
    MAX_RESOURCES,
    Output,
    Parameter,
    Template,
)
from troposphere.s3 import Bucket
from troposphere.serverless import Globals


class TestInitArguments(unittest.TestCase):
    def test_description_default(self):
        template = Template()
        self.assertIsNone(template.description)

    def test_description(self):
        value = "foo"
        template = Template(Description=value)
        self.assertEqual(template.description, value)

    def test_metadata_default(self):
        template = Template()
        self.assertEqual(template.metadata, {})

    def test_metadata(self):
        value = "foo"
        template = Template(Metadata=value)
        self.assertEqual(template.metadata, value)

    def test_transform(self):
        transform = "AWS::Serverless-2016-10-31"
        template = Template()
        template.set_transform(transform)
        self.assertEqual(template.transform, transform)

    def test_globals(self):
        template = Template()
        globals = Globals()
        with self.assertRaises(ValueError):
            template.set_globals(globals)
        transform = "AWS::Serverless-2016-10-31"
        template.set_transform(transform)
        template.set_globals(globals)
        self.assertEqual(template.globals, globals)
        with self.assertRaises(ValueError):
            template.set_transform("other_transform")


class TestValidate(unittest.TestCase):
    def test_max_parameters(self):
        template = Template()
        for i in range(0, MAX_PARAMETERS):
            template.add_parameter(Parameter(str(i), Type="String"))
        with self.assertRaises(ValueError):
            template.add_parameter(Parameter("parameter", Type="String"))

    def test_max_resources(self):
        template = Template()
        for i in range(0, MAX_RESOURCES):
            template.add_resource(Bucket(str(i)))
        with self.assertRaises(ValueError):
            template.add_resource(Bucket("bucket"))

    def test_max_outputs(self):
        template = Template()
        for i in range(0, MAX_OUTPUTS):
            template.add_output(Output(str(i), Value=str(i)))
        with self.assertRaises(ValueError):
            template.add_output(Output("output", Value="output"))

    def test_max_mappings(self):
        template = Template()
        for i in range(0, MAX_MAPPINGS):
            template.add_mapping(str(i), {"n": "v"})
        with self.assertRaises(ValueError):
            template.add_mapping("mapping", {"n": "v"})


class TypeComparator:
    """Helper to test the __eq__ protocol"""

    def __init__(self, valid_types):
        self.valid_types = valid_types

    def __eq__(self, other):
        return isinstance(other, self.valid_types)

    def __ne__(self, other):
        return not self == other


class TestEquality(unittest.TestCase):
    def test_eq(self):
        metadata = "foo"
        description = "bar"
        resource = Bucket("Baz")
        output = Output("qux", Value="qux")

        t1 = Template(Description=description, Metadata=metadata)
        t1.add_resource(resource)
        t1.add_output(output)

        t2 = Template(Description=description, Metadata=metadata)
        t2.add_resource(resource)
        t2.add_output(output)

        self.assertEqual(t1, t2)

        self.assertEqual(t1, TypeComparator(Template))
        self.assertEqual(TypeComparator(Template), t1)

    def test_ne(self):
        t1 = Template(Description="foo1", Metadata="bar1")
        t1.add_resource(Bucket("Baz1"))
        t1.add_output(Output("qux1", Value="qux1"))

        t2 = Template(Description="foo2", Metadata="bar2")
        t2.add_resource(Bucket("Baz2"))
        t2.add_output(Output("qux2", Value="qux2"))

        self.assertNotEqual(t1, t2)

        self.assertNotEqual(t1, TypeComparator(Output))
        self.assertNotEqual(TypeComparator(Output), t1)

    def test_hash(self):
        metadata = "foo"
        description = "bar"
        resource = Bucket("Baz")
        output = Output("qux", Value="qux")

        t1 = Template(Description=description, Metadata=metadata)
        t1.add_resource(resource)
        t1.add_output(output)

        t2 = Template(Description=description, Metadata=metadata)
        t2.add_resource(resource)
        t2.add_output(output)

        self.assertEqual(len(set([t1, t2])), 1)


class TestAwsInterface(unittest.TestCase):
    def test_parameter_label(self):
        t = Template()
        p1 = t.add_parameter(Parameter("Foo"))
        t.add_parameter(Parameter("Bar"))
        t.set_parameter_label(p1, "Foo label")

        t.set_parameter_label("Bar", "Bar label")

        self.assertEqual(
            t.metadata,
            {
                "AWS::CloudFormation::Interface": {
                    "ParameterLabels": {
                        "Foo": {"default": "Foo label"},
                        "Bar": {"default": "Bar label"},
                    },
                },
            },
        )

    def test_parameter_label_replace(self):
        t = Template()
        p1 = t.add_parameter(Parameter("Foo"))
        t.add_parameter(Parameter("Bar"))
        t.set_parameter_label(p1, "Foo label")
        t.set_parameter_label("Foo", "Bar label")

        self.assertEqual(
            t.metadata,
            {
                "AWS::CloudFormation::Interface": {
                    "ParameterLabels": {
                        "Foo": {"default": "Bar label"},
                    },
                },
            },
        )

    def test_parameter_group(self):
        t = Template()
        p1 = t.add_parameter(Parameter("Foo"))
        t.add_parameter(Parameter("Bar"))
        t.add_parameter_to_group(p1, "gr")
        t.add_parameter_to_group("Bar", "gr")

        self.assertEqual(
            t.metadata,
            {
                "AWS::CloudFormation::Interface": {
                    "ParameterGroups": [
                        {
                            "Label": {"default": "gr"},
                            "Parameters": ["Foo", "Bar"],
                        },
                    ],
                },
            },
        )


class TestRules(unittest.TestCase):
    def test_rules(self):
        t = Template()
        t.add_parameter("One")
        t.add_parameter("Two")

        rule = {
            "Assertions": [
                {
                    "Assert": {
                        "Fn::Equals": [
                            {"Ref": "One"},
                            {"Ref": "Two"},
                        ],
                    },
                },
            ],
        }
        t.add_rule("ValidateEqual", rule)

        self.assertTrue("ValidateEqual" in t.rules)

        rendered = t.to_dict()
        self.assertEqual(rendered["Rules"]["ValidateEqual"], rule)


if __name__ == "__main__":
    unittest.main()
