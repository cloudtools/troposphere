import unittest

import troposphere.eks as eks


class TestEKSValidators(unittest.TestCase):
    def test_validate_taint_effect(self):
        valid_values = ["NO_EXECUTE", "NO_SCHEDULE", "PREFER_NO_SCHEDULE"]
        for x in valid_values:
            eks.validate_taint_effect(x)

        with self.assertRaises(ValueError):
            eks.validate_taint_effect("NOT_OK")

    def test_validate_taint_key(self):
        valid_values = ["OK", "O", "o" * 63]
        for x in valid_values:
            eks.validate_taint_key(x)

        invalid_values = ["", "o" * 64]
        for x in invalid_values:
            with self.assertRaises(ValueError):
                eks.validate_taint_key(x)

    def test_validate_taint_value(self):
        valid_values = ["", "O", "o" * 63]
        for x in valid_values:
            eks.validate_taint_value(x)

        invalid_values = ["o" * 64]
        for x in invalid_values:
            with self.assertRaises(ValueError):
                eks.validate_taint_value(x)
