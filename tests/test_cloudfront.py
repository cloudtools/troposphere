import unittest

import troposphere.cloudfront as cloudfront
from troposphere import If


class TestCorsConfig(unittest.TestCase):
    def test_allowmethods(self):
        cloudfront.AccessControlAllowMethods(Items=[])
        cloudfront.AccessControlAllowMethods(Items=["GET", "POST"])
        cloudfront.AccessControlAllowMethods(
            Items=If("SomeCondition", ["GET"], ["POST"])
        )
        with self.assertRaises(ValueError):
            cloudfront.AccessControlAllowMethods(Items=["get"])
        with self.assertRaises(ValueError):
            cloudfront.AccessControlAllowMethods(Items=["GET", "get", "PUT"])
        with self.assertRaises(TypeError):
            cloudfront.AccessControlAllowMethods(Items=10)
        with self.assertRaises(TypeError):
            cloudfront.AccessControlAllowMethods(Items="GET")


if __name__ == "__main__":
    unittest.main()
