import unittest

from troposphere import Join, Parameter


class TestInitArguments(unittest.TestCase):
    def test_title_max_length(self):
        title = 'i' * 256
        with self.assertRaises(ValueError):
            Parameter(title, Type='String')

    def test_validate_with_a_join_default(self):
        Parameter(
            'test', Type='String', Default=Join('', ['a', 'b'])).validate()


if __name__ == '__main__':
    unittest.main()
