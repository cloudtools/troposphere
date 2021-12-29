import unittest

from troposphere.wafv2 import (
    CustomResponseBody,
    validate_custom_response_bodies,
    wafv2_custom_body_response_content,
    wafv2_custom_body_response_content_type,
)


class TestWafV2CustomBodies(unittest.TestCase):
    def test_valid_empty_dict(self):
        validate_custom_response_bodies({})

    def test_valid_dict(self):
        validate_custom_response_bodies({"foo": CustomResponseBody()})

    def test_not_a_dict(self):
        with self.assertRaises(ValueError):
            validate_custom_response_bodies("foo")

    def test_not_containing_a_custom_response_body(self):
        with self.assertRaises(ValueError):
            validate_custom_response_bodies({"foo": "bar"})

    def test_wafv2_custom_body_response_content(self):
        for s in [
            "{'hello': 'world'}",
            "<!DOCTYPE html><html><head><title>Test</title></head><body><h1>Test</h1><p>Test.</p></body></html>",
            "Health",
        ]:
            wafv2_custom_body_response_content(s)
        for s in ["", "a" * 10241]:
            with self.assertRaises(ValueError):
                wafv2_custom_body_response_content(s)

    def test_wafv2_custom_body_response_content_type(self):
        for s in ["APPLICATION_JSON", "TEXT_HTML", "TEXT_PLAIN"]:
            wafv2_custom_body_response_content_type(s)
        for s in ["", "APPLICATION", "HTML", "TEXT"]:
            with self.assertRaises(ValueError):
                wafv2_custom_body_response_content_type(s)


if __name__ == "__main__":
    unittest.main()
