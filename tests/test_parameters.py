import unittest

from troposphere import Parameter, Ref


class TestInitArguments(unittest.TestCase):
    def test_title_max_length(self):
        title = 'i' * 256
        with self.assertRaises(ValueError):
            Parameter(title, Type='String')

    def test_ref_can_be_requested(self):
        param = Parameter('title', Type='String')
        reference = param.ref()

        self.assertIsInstance(reference, Ref)
        self.assertDictEqual(reference.data, {'Ref': 'title'})


if __name__ == '__main__':
    unittest.main()
