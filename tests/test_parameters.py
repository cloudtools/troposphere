import unittest

from troposphere import Parameter


class TestInitArguments(unittest.TestCase):
    def test_title_max_length(self):
        title = 'i' * 256
        with self.assertRaises(ValueError):
            Parameter(title, Type='String')


if __name__ == '__main__':
    unittest.main()
