import unittest
from troposphere import Parameter, Ref
from troposphere.validators import boolean, integer, integer_range
from troposphere.validators import positive_integer, network_port


class TestValidators(unittest.TestCase):

    def test_boolean(self):
        for x in [True, "True", "true", 1, "1"]:
            self.assertEqual(boolean(x), True, repr(x))
        for x in [False, "False", "false", 0, "0"]:
            self.assertEqual(boolean(x), False, repr(x))
        for x in ["000", "111", "abc"]:
            with self.assertRaises(ValueError):
                boolean(x)

    def test_integer(self):
        for x in [-1, "-1", 0, "0", 65535, "65535"]:
            integer(x)
        for x in [False, "False", "false", 0, "0"]:
            self.assertEqual(boolean(x), False, repr(x))

    def test_positive_integer(self):
        for x in [0, 1, 65535]:
            positive_integer(x)
        for x in [-1, -10]:
            with self.assertRaises(ValueError):
                positive_integer(x)

    def test_integer_range(self):
        between_ten_and_twenty = integer_range(10, 20)
        between_ten_and_twenty(10)
        between_ten_and_twenty(15)
        between_ten_and_twenty(20)
        with self.assertRaises(ValueError):
            between_ten_and_twenty(-1)
            between_ten_and_twenty(9)
            between_ten_and_twenty(21)
            between_ten_and_twenty(111111111)

    def test_network_port(self):
        for x in [-1, 0, 1, 1024, 65535]:
            network_port(x)
        for x in [-2, -10, 65536, 100000]:
            with self.assertRaises(ValueError):
                network_port(x)

    def test_network_port_ref(self):
        p = Parameter('myport')
        network_port(Ref(p))

if __name__ == '__main__':
    unittest.main()
