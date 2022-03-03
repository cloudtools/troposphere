# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_statement(statement):
    """
    Validate Transformation Type for WebACL TextTransformation
    Property: RuleGroupRule.Statement
    Property: WebACLRule.Statement
    Property: ManagedRuleGroupStatement.ScopeDownStatement
    Property: NotStatement.Statement
    Property: RateBasedStatement.ScopeDownStatement
    """

    from .. import AWSHelperFn
    from ..wafv2 import Statement

    if not isinstance(statement, (Statement, AWSHelperFn)):
        raise TypeError(f"{statement} is not a valid Statement")

    return statement


def validate_statements(statements):
    """
    Property: AndStatement.Statements
    Property: OrStatement.Statements
    """

    if not isinstance(statements, list) or len(statements) != 2:
        raise TypeError("Statements must be a list of 2 Statement elements")

    for s in statements:
        validate_statement(s)

    return statements


def validate_transformation_type(transformation_type):
    """
    Validate Transformation Type for WebACL TextTransformation
    Property: TextTransformation.Type
    """

    VALID_TRANSFORMATION_TYPES = (
        "BASE64_DECODE",
        "BASE64_DECODE_EXT",
        "CMD_LINE",
        "COMPRESS_WHITE_SPACE",
        "CSS_DECODE",
        "ESCAPE_SEQ_DECODE",
        "HEX_DECODE",
        "HTML_ENTITY_DECODE",
        "JS_DECODE",
        "LOWERCASE",
        "MD5",
        "NONE",
        "NORMALIZE_PATH",
        "NORMALIZE_PATH_WIN",
        "REMOVE_NULLS",
        "REPLACE_COMMENTS",
        "REPLACE_NULLS",
        "SQL_HEX_DECODE",
        "URL_DECODE",
        "URL_DECODE_UNI",
        "UTF8_TO_UNICODE",
    )

    if transformation_type not in VALID_TRANSFORMATION_TYPES:
        raise ValueError(
            "WebACL TextTransformation must be one of: %s"
            % ", ".join(VALID_TRANSFORMATION_TYPES)
        )
    return transformation_type


def validate_comparison_operator(comparison_operator):
    """
    Validate Comparison Operator for WebACL SizeConstraintStatement
    Property: SizeConstraintStatement.ComparisonOperator
    """

    VALID_COMPARISON_OPERATORS = (
        "EQ",
        "GE",
        "GT",
        "LE",
        "LT",
        "NE",
    )

    if comparison_operator not in VALID_COMPARISON_OPERATORS:
        raise ValueError(
            "WebACL SizeConstraintStatement must be one of: %s"
            % ", ".join(VALID_COMPARISON_OPERATORS)
        )
    return comparison_operator


def validate_ipaddress_version(ipaddress_version):
    """
    Validate IPAddress version for IPSet
    Property: IPSet.IPAddressVersion
    """

    VALID_IP_VERSION = ("IPV4", "IPV6")

    if ipaddress_version not in VALID_IP_VERSION:
        raise ValueError(
            "IPSet IPAddressVersion must be one of: %s" % ", ".join(VALID_IP_VERSION)
        )
    return ipaddress_version


def validate_positional_constraint(positional_constraint):
    """
    Validate positional constraint for ByteMatchStatement
    Property: ByteMatchStatement.PositionalConstraint
    """

    VALID_POSITIONAL_CONSTRAINTS = (
        "CONTAINS",
        "CONTAINS_WORD",
        "ENDS_WITH",
        "EXACTLY",
        "STARTS_WITH",
    )

    if positional_constraint not in VALID_POSITIONAL_CONSTRAINTS:
        raise ValueError(
            "ByteMatchStatement PositionalConstraint must be one of: %s"
            % ", ".join(VALID_POSITIONAL_CONSTRAINTS)  # NOQA
        )
    return positional_constraint


def validate_custom_response_bodies(custom_response_bodies):
    """
    Validate custom response bodies
    Property: RuleGroup.CustomResponseBodies
    Property: WebACL.CustomResponseBodies
    """

    from ..wafv2 import CustomResponseBody

    if not isinstance(custom_response_bodies, dict):
        raise ValueError("CustomResponseBodies must be dict")

    for k, v in custom_response_bodies.items():
        if not isinstance(v, CustomResponseBody):
            raise ValueError("value of %s must be type of CustomResponseBody" % (k))

    return custom_response_bodies


def wafv2_custom_body_response_content(content):
    """
    Validate wafv2 custom body response content. Any character between 1 to 10240
    Property: CustomResponseBody.Content
    """

    if not content:
        raise ValueError("Content must not be empty")
    if len(content) > 10240:
        raise ValueError("Content maximum length must not exceed 10240")

    return content


def wafv2_custom_body_response_content_type(content_type):
    """
    validate wafv2 custom response content type
    Property: CustomResponseBody.ContentType
    """

    valid_types = ["APPLICATION_JSON", "TEXT_HTML", "TEXT_PLAIN"]
    if content_type not in valid_types:
        raise ValueError('ContentType must be one of: "%s"' % (", ".join(valid_types)))
    return content_type
