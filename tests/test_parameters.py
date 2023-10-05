import unittest

from troposphere import Parameter, Ref


class TestInitArguments(unittest.TestCase):
    def test_title_max_length(self):
        title = "i" * 256
        with self.assertRaises(ValueError):
            Parameter(title, Type="String")

    def test_ref_can_be_requested(self):
        param = Parameter("title", Type="String")
        reference = param.ref()

        self.assertIsInstance(reference, Ref)
        self.assertDictEqual(reference.data, {"Ref": "title"})


class TestParameterValidator(unittest.TestCase):
    def test_allowed_pattern_for_number(self):
        with self.assertRaises(ValueError):
            Parameter("Foo", Type="Number", AllowedPattern="^[a-zA-Z0-9]*$").validate()

    def test_allowed_pattern_for_comma_delimited_list_and_string(self):
        Parameter(
            "Foo",
            Type="CommaDelimitedList",
            AllowedPattern="^[A-Z]{2}$",
            Default="",
        ).validate()

        Parameter(
            "Foo",
            Type="String",
            AllowedPattern="^[A-Z]{2}$",
            Default="",
        ).validate()

    def test_aws_specific_type(self):
        Parameter(
            "Foo",
            Type="AWS::EC2::KeyPair::KeyName",
            Default="",
        ).validate()


if __name__ == "__main__":
    unittest.main()
