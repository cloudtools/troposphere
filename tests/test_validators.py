import unittest

from base import ARMParameter
from ionosphere import Parameter, Ref
from ionosphere.validators import boolean, integer, integer_range
from ionosphere.validators import positive_integer, network_port
from ionosphere.validators import tg_healthcheck_port
from ionosphere.validators import s3_bucket_name, encoding, status
from ionosphere.validators import iam_path, iam_names, iam_role_name
from ionosphere.validators import iam_group_name, iam_user_name, elb_name
from ionosphere.validators import mutually_exclusive, notification_type
from ionosphere.validators import notification_event, task_type
from ionosphere.validators import compliance_level, operating_system


class TestValidators(unittest.TestCase):

    def test_boolean(self):
        for x in [True, "True", "true", 1, "1"]:
            self.assertEqual(boolean(x), "true", repr(x))
        for x in [False, "False", "false", 0, "0"]:
            self.assertEqual(boolean(x), "false", repr(x))
        for x in ["000", "111", "abc"]:
            with self.assertRaises(ValueError):
                boolean(x)

    def test_integer(self):
        self.assertEqual(integer(-1), -1)
        self.assertEqual(integer("-1"), "-1")
        self.assertEqual(integer(0), 0)
        self.assertEqual(integer("0"), "0")
        self.assertEqual(integer(65535), 65535)
        self.assertEqual(integer("65535"), "65535")
        self.assertEqual(integer(1.0), 1.0)
        with self.assertRaises(ValueError):
            integer("string")
        with self.assertRaises(ValueError):
            integer(object)
        with self.assertRaises(ValueError):
            integer(None)

    def test_positive_integer(self):
        for x in [0, 1, 65535]:
            positive_integer(x)
        for x in [-1, -10]:
            with self.assertRaises(ValueError):
                positive_integer(x)

    def test_integer_range(self):
        between_ten_and_twenty = integer_range(10, 20)
        self.assertEqual(between_ten_and_twenty(10), 10)
        self.assertEqual(between_ten_and_twenty(15), 15)
        self.assertEqual(between_ten_and_twenty(20), 20)
        for i in (-1, 9, 21, 1111111):
            with self.assertRaises(ValueError):
                between_ten_and_twenty(i)

    def test_network_port(self):
        for x in [-1, 0, 1, 1024, 65535]:
            network_port(x)
        for x in [-2, -10, 65536, 100000]:
            with self.assertRaises(ValueError):
                network_port(x)
