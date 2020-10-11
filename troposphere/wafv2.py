# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer


VALID_TRANSFORMATION_TYPES = (
    'CMD_LINE', 'COMPRESS_WHITE_SPACE', 'HTML_ENTITY_DECODE',
    'LOWERCASE', 'NONE', 'URL_DECODE')
VALID_COMPARISON_OPERATORS = ('EQ', 'GE', 'GT', 'LE', 'LT', 'NE')
VALID_IP_VERSION = ('IPV4', 'IPV6')
VALID_POSITIONAL_CONSTRAINTS = ('CONTAINS', 'CONTAINS_WORD', 'ENDS_WITH',
                                'EXACTLY', 'STARTS_WITH')


def validate_transformation_type(transformation_type):
    """Validate Transformation Type for WebACL TextTransformation"""

    if transformation_type not in VALID_TRANSFORMATION_TYPES:
        raise ValueError("WebACL TextTransformation must be one of: %s" %
                         ", ".join(VALID_TRANSFORMATION_TYPES))
    return transformation_type


def validate_comparison_operator(comparison_operator):
    """Validate Comparison Operator for WebACL SizeConstraintStatement"""

    if comparison_operator not in VALID_COMPARISON_OPERATORS:
        raise ValueError("WebACL SizeConstraintStatement must be one of: %s" %
                         ", ".join(VALID_COMPARISON_OPERATORS))
    return comparison_operator


def validate_ipaddress_version(ipaddress_version):
    """Validate IPAddress version for IPSet"""

    if ipaddress_version not in VALID_IP_VERSION:
        raise ValueError("IPSet IPAddressVersion must be one of: %s" %
                         ", ".join(VALID_IP_VERSION))
    return ipaddress_version


def validate_positional_constraint(positional_constraint):
    """Validate positional constraint for ByteMatchStatement"""

    if positional_constraint not in VALID_POSITIONAL_CONSTRAINTS:
        raise ValueError("ByteMatchStatement PositionalConstraint must be one of: %s" %  # NOQA
                         ", ".join(VALID_POSITIONAL_CONSTRAINTS))
    return positional_constraint


class ExcludedRule(AWSProperty):
    props = {
        'Name': (basestring, False)
    }


class RuleGroupReferenceStatement(AWSProperty):
    props = {
        'Arn': (basestring, False),
        'ExcludedRules': ([ExcludedRule], False)
    }


class TextTransformation(AWSProperty):
    props = {
        'Priority': (integer, False),
        'Type': (validate_transformation_type, False),
    }


class SingleHeader(AWSProperty):
    props = {
        'Name': (basestring, False)
    }


class SingleQueryArgument(AWSProperty):
    props = {
        'Name': (basestring, False)
    }


class Body(AWSProperty):
    props = {

    }


class Method(AWSProperty):
    props = {

    }


class AllQueryArguments(AWSProperty):
    props = {

    }


class QueryString(AWSProperty):
    props = {

    }


class UriPath(AWSProperty):
    props = {

    }


class FieldToMatch(AWSProperty):
    props = {
        'AllQueryArguments': (AllQueryArguments, False),
        'Body': (Body, False),
        'Method': (Method, False),
        'QueryString': (QueryString, False),
        'SingleHeader': (SingleHeader, False),
        'SingleQueryArgument': (SingleQueryArgument, False),
        'UriPath': (UriPath, False)
    }


class RegexPatternSetReferenceStatement(AWSProperty):
    props = {
        'Arn': (basestring, True),
        'FieldToMatch': (FieldToMatch, True),
        'TextTransformations': ([TextTransformation], True)
    }


class XssMatchStatement(AWSProperty):
    props = {
        'FieldToMatch': (FieldToMatch, True),
        'TextTransformations': ([TextTransformation], True)
    }


class SqliMatchStatement(AWSProperty):
    props = {
        'FieldToMatch': (FieldToMatch, True),
        'TextTransformations': ([TextTransformation], True)
    }


class SizeConstraintStatement(AWSProperty):
    props = {
        'ComparisonOperator': (validate_comparison_operator, True),
        'FieldToMatch': (FieldToMatch, True),
        'Size': (integer, True),
        'TextTransformations': ([TextTransformation], True)
    }


class ByteMatchStatement(AWSProperty):
    props = {
        'FieldToMatch': (FieldToMatch, True),
        'PositionalConstraint': (validate_positional_constraint, True),
        'SearchString': (basestring, True),
        'SearchStringBase64': (basestring, False),
        'TextTransformations': ([TextTransformation], True)
    }


class ForwardedIPConfiguration(AWSProperty):
    props = {
        'FallbackBehavior': (basestring, True),
        'HeaderName': (basestring, True),
    }


class GeoMatchStatement(AWSProperty):
    props = {
        'CountryCodes': ([basestring], False),
        'ForwardedIPConfig': (ForwardedIPConfiguration, False),
    }


class IPSetForwardedIPConfiguration(AWSProperty):
    props = {
        'FallbackBehavior': (basestring, True),
        'HeaderName': (basestring, True),
        'Position': (basestring, True),
    }


class IPSetReferenceStatement(AWSProperty):
    props = {
        'Arn': (basestring, False),
        'IPSetForwardedIPConfig': (IPSetForwardedIPConfiguration, False),
    }


class ManagedRuleGroupStatement(AWSProperty):
    props = {
        'ExcludedRules': ([ExcludedRule], False),
        'Name': (basestring, False),
        'VendorName': (basestring, False),
    }


class StatementThree(AWSProperty):
    props = {
        'ByteMatchStatement': (ByteMatchStatement, False),
        'GeoMatchStatement': (GeoMatchStatement, False),
        'IPSetReferenceStatement': (IPSetReferenceStatement, False),
        'ManagedRuleGroupStatement': (ManagedRuleGroupStatement, False),
        'RegexPatternSetReferenceStatement': (
            RegexPatternSetReferenceStatement,
            False),
        'RuleGroupReferenceStatement': (RuleGroupReferenceStatement, False),
        'SizeConstraintStatement': (SizeConstraintStatement, False),
        'SqliMatchStatement': (SqliMatchStatement, False),
        'XssMatchStatement': (XssMatchStatement, False),
    }


class AndStatementTwo(AWSProperty):
    props = {
        'Statements': ([StatementThree], False)
    }


class NotStatementTwo(AWSProperty):
    props = {
        'Statement': (StatementThree, False)
    }


class OrStatementTwo(AWSProperty):
    props = {
        'Statements': ([StatementThree], False)
    }


class RateBasedStatementTwo(AWSProperty):
    props = {
        'AggregateKeyType': (basestring, False),
        'ForwardedIPConfig': (ForwardedIPConfiguration, False),
        'Limit': (integer, False),
        'ScopeDownStatement': StatementThree
    }


class StatementTwo(AWSProperty):
    props = {
        'AndStatement': (AndStatementTwo, False),
        'ByteMatchStatement': (ByteMatchStatement, False),
        'GeoMatchStatement': (GeoMatchStatement, False),
        'IPSetReferenceStatement': (IPSetReferenceStatement, False),
        'ManagedRuleGroupStatement': (ManagedRuleGroupStatement, False),
        'NotStatement': (NotStatementTwo, False),
        'OrStatement': (OrStatementTwo, False),
        'RateBasedStatement': (RateBasedStatementTwo, False),
        'RegexPatternSetReferenceStatement': (
            RegexPatternSetReferenceStatement,
            False),
        'RuleGroupReferenceStatement': (RuleGroupReferenceStatement, False),
        'SizeConstraintStatement': (SizeConstraintStatement, False),
        'SqliMatchStatement': (SqliMatchStatement, False),
        'XssMatchStatement': (XssMatchStatement, False),
    }


class AndStatementOne(AWSProperty):
    props = {
        'Statements': ([StatementTwo], False)
    }


class NotStatementOne(AWSProperty):
    props = {
        'Statement': (StatementTwo, False)
    }


class OrStatementOne(AWSProperty):
    props = {
        'Statements': ([StatementTwo], False)
    }


class RateBasedStatementOne(AWSProperty):
    props = {
        'AggregateKeyType': (basestring, False),
        'ForwardedIPConfig': (ForwardedIPConfiguration, False),
        'Limit': (integer, False),
        'ScopeDownStatement': (StatementTwo, False)
    }


class StatementOne(AWSProperty):
    props = {
        'AndStatement': (AndStatementOne, False),
        'ByteMatchStatement': (ByteMatchStatement, False),
        'GeoMatchStatement': (GeoMatchStatement, False),
        'IPSetReferenceStatement': (IPSetReferenceStatement, False),
        'ManagedRuleGroupStatement': (ManagedRuleGroupStatement, False),
        'NotStatement': (NotStatementOne, False),
        'OrStatement': (OrStatementOne, False),
        'RateBasedStatement': (RateBasedStatementOne, False),
        'RegexPatternSetReferenceStatement': (
            RegexPatternSetReferenceStatement,
            False),
        'RuleGroupReferenceStatement': (RuleGroupReferenceStatement, False),
        'SizeConstraintStatement': (SizeConstraintStatement, False),
        'SqliMatchStatement': (SqliMatchStatement, False),
        'XssMatchStatement': (XssMatchStatement, False),
    }


class VisibilityConfig(AWSProperty):
    props = {
        'CloudWatchMetricsEnabled': (boolean, False),
        'MetricName': (basestring, False),
        'SampledRequestsEnabled': (boolean, False)
    }


class AllowAction(AWSProperty):
    props = {

    }


class BlockAction(AWSProperty):
    props = {

    }


class CountAction(AWSProperty):
    props = {

    }


class NoneAction(AWSProperty):
    props = {

    }


class RuleAction(AWSProperty):
    props = {
        'Allow': (AllowAction, False),
        'Block': (BlockAction, False),
        'Count': (CountAction, False),
    }


class OverrideAction(AWSProperty):
    props = {
        'Count': (CountAction, False),
        'None': (NoneAction, False),
    }


class WebACLRule(AWSProperty):
    props = {
        'Action': (RuleAction, False),
        'Name': (basestring, False),
        'OverrideAction': (OverrideAction, False),
        'Priority': (integer, False),
        'Statement': (StatementOne, False),
        'VisibilityConfig': (VisibilityConfig, False)
    }


class DefaultAction(AWSProperty):
    props = {
        'Allow': (AllowAction, False),
        'Block': (BlockAction, False),
    }


class WebACL(AWSObject):
    resource_type = "AWS::WAFv2::WebACL"

    props = {
        'DefaultAction': (DefaultAction, False),
        'Description': (basestring, False),
        'Name': (basestring, False),
        'Rules': ([WebACLRule], False),
        'Scope': (basestring, True),
        'Tags': (Tags, False),
        'VisibilityConfig': (VisibilityConfig, False)
    }


class IPSet(AWSObject):
    resource_type = "AWS::WAFv2::IPSet"

    props = {
        'Addresses': ([basestring], False),
        'Description': (basestring, False),
        'IPAddressVersion': (validate_ipaddress_version, False),
        'Name': (basestring, False),
        'Scope': (basestring, True),
        'Tags': (Tags, False),
    }


class RegexPatternSet(AWSObject):
    resource_type = "AWS::WAFv2::RegexPatternSet"

    props = {
        'Description': (basestring, False),
        'Name': (basestring, False),
        'RegularExpressionList': ([basestring], True),
        'Scope': (basestring, True),
        'Tags': (Tags, False),
    }


class RuleGroupRule(AWSProperty):
    props = {
        'Action': (RuleAction, False),
        'Name': (basestring, False),
        'Priority': (integer, False),
        'Statement': (StatementOne, False),
        'VisibilityConfig': (VisibilityConfig, False)
    }


class RuleGroup(AWSObject):
    resource_type = "AWS::WAFv2::RuleGroup"

    props = {
        'Capacity': (integer, False),
        'Description': (basestring, False),
        'Name': (basestring, False),
        'Rules': ([RuleGroupRule], False),
        'Scope': (basestring, False),
        'Tags': (Tags, False),
        'VisibilityConfig': (VisibilityConfig, False)
    }


class WebACLAssociation(AWSObject):
    resource_type = "AWS::WAFv2::WebACLAssociation"

    props = {
        'ResourceArn': (basestring, True),
        'WebACLArn': (basestring, True),
    }
