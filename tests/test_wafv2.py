import unittest

from troposphere.wafv2 import (
    AndStatement,
    ByteMatchStatement,
    CustomResponseBody,
    FieldToMatch,
    NotStatement,
    Statement,
    TextTransformation,
    VisibilityConfig,
    WebACLRule,
    XssMatchStatement,
    validate_custom_response_bodies,
    validate_statement,
    validate_statements,
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

    def test_statement_validator(self):
        validate_statement(Statement())
        with self.assertRaises(TypeError):
            validate_statement("foo")
        with self.assertRaises(TypeError):
            validate_statement(10)

    def test_statements_validator(self):
        validate_statements([Statement(), Statement()])
        with self.assertRaises(TypeError):
            validate_statements(
                [
                    Statement(),
                ]
            )
        with self.assertRaises(TypeError):
            validate_statements("foo")
        with self.assertRaises(TypeError):
            validate_statements(["foo", "bar"])

    def test_wafv2_snippet(self):
        web_acl_rule = WebACLRule(
            "WebACLRule",
            Name="XSSprotection",
            Priority=0,
            VisibilityConfig=VisibilityConfig(
                SampledRequestsEnabled=True,
                CloudWatchMetricsEnabled=True,
                MetricName="XSSprotection",
            ),
            Statement=Statement(
                AndStatement=AndStatement(
                    Statements=[
                        Statement(
                            XssMatchStatement=XssMatchStatement(
                                FieldToMatch=FieldToMatch(UriPath={}),
                                TextTransformations=[
                                    TextTransformation(Type="URL_DECODE", Priority=0),
                                ],
                            ),
                        ),
                        Statement(
                            NotStatement=NotStatement(
                                Statement=Statement(
                                    ByteMatchStatement=ByteMatchStatement(
                                        FieldToMatch=FieldToMatch(UriPath={}),
                                        PositionalConstraint="CONTAINS",
                                        SearchString="xxxx",
                                        TextTransformations=[
                                            TextTransformation(
                                                Type="LOWERCASE", Priority=0
                                            ),
                                        ],
                                    ),
                                ),
                            ),
                        ),
                    ],
                ),
            ),
        )
        web_acl_rule.to_dict()


if __name__ == "__main__":
    unittest.main()
