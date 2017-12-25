import unittest
from troposphere import Join
from troposphere.sqs import Queue


class TestQueue(unittest.TestCase):
    def test_QueueName(self):
        Queue(
            "q",
            FifoQueue=False,
        ).validate()

        Queue(
            "q",
            FifoQueue=True,
            QueueName="foobar.fifo",
        ).validate()

        Queue(
            "q",
            FifoQueue=True,
            QueueName=Join("foo", "bar"),
        ).validate()

        Queue(
            "q",
            FifoQueue=True,
        ).validate()

        with self.assertRaises(ValueError):
            Queue(
                "q",
                FifoQueue=True,
                QueueName="foobar",
            ).validate()


if __name__ == '__main__':
    unittest.main()
