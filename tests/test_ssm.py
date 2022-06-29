import unittest

from troposphere.ssm import Document


class TestQueue(unittest.TestCase):
    def test_Document(self):
        # dict
        Document("title", Content={"foo": "bar"}).validate()
        # Valid yaml and json
        Document("title", Content='{"foo": "bar"}').validate()
        Document("title", Content="{foo: bar}").validate()
        # Invalid json/yaml
        with self.assertRaises(ValueError):
            Document("title", Content="*foo").validate()


if __name__ == "__main__":
    unittest.main()
