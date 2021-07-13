import unittest

from troposphere.config import ONE_HOUR, SourceDetails


class TestConfig(unittest.TestCase):
    def test_SourceDetails(self):
        SourceDetails(
            EventSource="esource",
            MaximumExecutionFrequency=ONE_HOUR,
            MessageType="mtype",
        ).to_dict()

    def test_invalid_SourceDetails_MaximumExecutionFrequency(self):
        with self.assertRaises(ValueError):
            SourceDetails(
                EventSource="esource",
                MaximumExecutionFrequency="foo",
                MessageType="mtype",
            ).to_dict()


if __name__ == "__main__":
    unittest.main()
