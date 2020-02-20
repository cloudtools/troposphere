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


class ExcludedRules(AWSProperty):
    props = {
        'ExcludedRules': ([ExcludedRule], False)
    }


class RuleGroupReferenceStatement(AWSProperty):
    props = {
        'Arn': (basestring, False),
        'ExcludedRules': (ExcludedRules, False)
    }


class TextTransformation(AWSProperty):
    props = {
        'Priority': (integer, False),
        'Type': (validate_transformation_type, False),
    }


class TextTransformations(AWSProperty):
    props = {
        'TextTransformations': ([TextTransformation], False)
    }


class SingleHeader(AWSProperty):
    props = {
        'Name': (basestring, False)
    }


class SingleQueryArgument(AWSProperty):
    props = {
        'Name': (basestring, False)
    }


class Body(AWSObject):
    props = {

    }


class Method(AWSObject):
    props = {

    }


class AllQueryArguments(AWSObject):
    props = {

    }


class QueryString(AWSObject):
    props = {

    }


class UriPath(AWSObject):
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
        'Arn': (basestring, False),
        'FieldToMatch': (FieldToMatch, False),
        'TextTransformations': (TextTransformations, False)
    }


class XssMatchStatement(AWSProperty):
    props = {
        'FieldToMatch': (FieldToMatch, False),
        'TextTransformations': (TextTransformations, False)
    }


class SqliMatchStatement(AWSProperty):
    props = {
        'FieldToMatch': (FieldToMatch, False),
        'TextTransformations': (TextTransformations, False)
    }


class SizeConstraintStatement(AWSProperty):
    props = {
        'ComparisonOperator': (validate_comparison_operator, False),
        'FieldToMatch': (FieldToMatch, False),
        'Size': (integer, False),
        'TextTransformations': (TextTransformations, False)
    }


class ByteMatchStatement(AWSProperty):
    props = {
        'FieldToMatch': (FieldToMatch, False),
        'PositionalConstraint': (validate_positional_constraint, False),
        'SearchString': (basestring, False),
        'SearchStringBase64': (basestring, False),
        'TextTransformations': (TextTransformations, False)
    }


class CountryCodes(AWSProperty):
    props = {
        'CountryCodes': ([basestring], False)
    }


class GeoMatchStatement(AWSProperty):
    props = {
        'CountryCodes': (CountryCodes, False)
    }


class IPSetReferenceStatement(AWSProperty):
    props = {
        'Arn': (basestring, False)
    }


class ManagedRuleGroupStatement(AWSProperty):
    props = {
        'ExcludedRules': (ExcludedRules, False),
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


class StatementThrees(AWSProperty):
    props = {
        'StatementThrees': ([StatementThree], False)
    }


class AndStatementTwo(AWSProperty):
    props = {
        'Statements': (StatementThrees, False)
    }


class NotStatementTwo(AWSProperty):
    props = {
        'Statement': (StatementThree, False)
    }


class OrStatementTwo(AWSProperty):
    props = {
        'Statements': (StatementThrees, False)
    }


class RateBasedStatementTwo(AWSProperty):
    props = {
        'AggregateKeyType': (basestring, False),
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


class StatementTwos(AWSProperty):
    props = {
        'StatementTwos': ([StatementTwo], False)
    }


class AndStatementOne(AWSProperty):
    props = {
        'Statements': (StatementTwos, False)
    }


class NotStatementOne(AWSProperty):
    props = {
        'Statement': (StatementTwo, False)
    }


class OrStatementOne(AWSProperty):
    props = {
        'Statements': (StatementTwos, False)
    }


class RateBasedStatementOne(AWSProperty):
    props = {
        'AggregateKeyType': (basestring, False),
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


class Rule(AWSProperty):
    props = {
        'Action': (RuleAction, False),
        'Name': (basestring, False),
        'OverrideAction': (OverrideAction, False),
        'Priority': (integer, False),
        'Statement': (StatementOne, False),
        'VisibilityConfig': (VisibilityConfig, False)
    }


class Rules(AWSProperty):
    props = {
        'Rules': ([Rule], False),
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
        'Name': (basestring, True),
        'Rules': (Rules, False),
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
        'Name': (basestring, True),
        'Scope': (basestring, True),
        'Tags': (Tags, False),
    }


class Regex(AWSProperty):
    props = {
        'RegexString': (basestring, False)
    }


class RegularExpressionList(AWSProperty):
    props = {
        'RegularExpressionList': ([Regex], False)
    }


class RegexPatternSet(AWSObject):
    resource_type = "AWS::WAFv2::RegexPatternSet"

    props = {
        'Description': (basestring, False),
        'Name': (basestring, True),
        'RegularExpressionList': (RegularExpressionList, False),
        'Scope': (basestring, True),
        'Tags': (Tags, False),
    }


class RuleGroup(AWSObject):
    resource_type = "AWS::WAFv2::RuleGroup"

    props = {
        'Capacity': (integer, False),
        'Description': (basestring, False),
        'Name': (basestring, True),
        'Rules': (Rules, False),
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
