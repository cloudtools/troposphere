import json
import unittest

from troposphere import AWSObject, Cidr, GetAZs, Split, Template
from troposphere.template_generator import (
    ResourceTypeNotDefined,
    ResourceTypeNotFound,
    TemplateGenerator,
)


class TestTemplateGenerator(unittest.TestCase):
    def test_resource_type_not_defined(self):
        template_json = json.loads(
            """
        {
          "Resources": {
            "Foo": {
            }
          }
        }
        """
        )
        with self.assertRaises(ResourceTypeNotDefined) as context:
            TemplateGenerator(template_json)
        self.assertEqual("ResourceType not defined for Foo", str(context.exception))
        self.assertEqual("Foo", context.exception.resource)

    def test_unknown_resource_type(self):
        template_json = json.loads(
            """
        {
          "Resources": {
            "Foo": {
              "Type": "Some::Unknown::Type"
            }
          }
        }
        """
        )
        with self.assertRaises(ResourceTypeNotFound) as context:
            TemplateGenerator(template_json)
        self.assertEqual(
            "ResourceType not found for Some::Unknown::Type - Foo",
            str(context.exception),
        )
        self.assertEqual("Foo", context.exception.resource)
        self.assertEqual("Some::Unknown::Type", context.exception.resource_type)

    def test_custom_resource_override(self):
        """
        Ensures that a custom member can be defined.
        """
        template = Template()
        template.add_resource(MyCustomResource("foo", Foo="bar", ServiceToken="baz"))
        generated = TemplateGenerator(
            json.loads(template.to_json()), CustomMembers=[MyCustomResource]
        )

        # validated that the templates are equal to each other
        self.assertDictEqual(template.to_dict(), generated.to_dict())
        foo = generated.resources["foo"]
        self.assertTrue(isinstance(foo, MyCustomResource))

    def test_custom_resource_type(self):
        """
        Ensures that a custom resource type is implicitly defined.
        """
        template = Template()
        template.add_resource(MyCustomResource("foo", Foo="bar", ServiceToken="baz"))
        generated = TemplateGenerator(json.loads(template.to_json()))

        # validated that the templates are equal to each other
        self.assertDictEqual(template.to_dict(), generated.to_dict())
        foo = generated.resources["foo"]
        self.assertFalse(isinstance(foo, MyCustomResource))

    def test_macro_resource(self):
        """
        Ensures that a custom member can be defined.
        """
        template = Template()
        template.add_resource(MyMacroResource("foo", Foo="bar"))
        generated = TemplateGenerator(
            json.loads(template.to_json()), CustomMembers=[MyMacroResource]
        )

        # validated that the templates are equal to each other
        self.assertDictEqual(template.to_dict(), generated.to_dict())
        foo = generated.resources["foo"]
        self.assertTrue(isinstance(foo, MyMacroResource))
        self.assertEqual("bar", foo.Foo)

    def test_no_nested_name(self):
        """
        Prevent regression for  ensuring no nested Name (Issue #977)
        """
        template_json = json.loads(
            """
        {
          "AWSTemplateFormatVersion": "2010-09-09",
          "Description": "Description",
          "Outputs": {
            "TestOutput": {
              "Description": "ARN for TestData",
              "Export": {
                "Name": {"Fn::Sub": "${AWS::StackName}-TestOutput"}
              },
              "Value": {"Ref": "TestPolicy"}
            }
          }
        }
        """
        )

        d = TemplateGenerator(template_json).to_dict()
        name = d["Outputs"]["TestOutput"]["Export"]["Name"]
        self.assertIn("Fn::Sub", name)

    def test_list_functions(self):
        """
        Ensures that list functions are handled properly..
        """
        template = Template()
        template.add_resource(
            MyListResource(
                "foo",
                AZs=GetAZs(""),
                Cidr=Cidr("192.168.0.0/24", "6", "5"),
                Split=Split(",", "a,b,c"),
            )
        )
        generated = TemplateGenerator(
            json.loads(template.to_json()), CustomMembers=[MyListResource]
        )

        # validated that the templates are equal to each other
        self.assertDictEqual(template.to_dict(), generated.to_dict())

        # Further validate the list types are correct
        generated_azs = generated.resources["foo"].properties["AZs"]
        assert isinstance(generated_azs, GetAZs)
        generated_cidr = generated.resources["foo"].properties["Cidr"]
        assert isinstance(generated_cidr, Cidr)
        generated_split = generated.resources["foo"].properties["Split"]
        assert isinstance(generated_split, Split)


class MyCustomResource(AWSObject):
    resource_type = "Custom::Resource"

    props = {
        "Foo": (str, True),
        "ServiceToken": (str, True),
    }


class MyMacroResource(AWSObject):
    resource_type = "Some::Special::Resource"

    props = {
        "Foo": (str, True),
    }


class MyListResource(AWSObject):
    resource_type = "Some::Special::Resource"

    props = {
        "AZs": ([str], True),
        "Cidr": ([str], True),
        "Split": ([str], True),
    }


if __name__ == "__main__":
    unittest.main()
