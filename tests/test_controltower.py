import unittest

from troposphere.controltower import Parameter


class TestControltower(unittest.TestCase):
    def test_Parameter(self):
        Parameter(
            Key="foo",
            Value="bar",
        ).to_dict()

    def test_invalid_Parameter_Value_Dict(self):
        with self.assertRaises(TypeError):
            Parameter(
                Key="foo",
                Value={"foo": "bar"},
            ).to_dict()


if __name__ == "__main__":
    unittest.main()
