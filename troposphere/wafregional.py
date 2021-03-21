# Copyright (c) 2012-2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, integer, waf_action_type


class Action(AWSProperty):
    props = {
        'Type': (waf_action_type, True)
    }


class FieldToMatch(AWSProperty):
    props = {
        'Data': (str, False),  # Conditional
        'Type': (str, True)
    }


class ByteMatchTuples(AWSProperty):
    props = {
        'FieldToMatch': (FieldToMatch, True),
        'PositionalConstraint': (str, True),
        'TargetString': (str, False),  # Conditional
        'TargetStringBase64': (str, False),  # Conditional
        'TextTransformation': (str, True)
    }


class IPSetDescriptors(AWSProperty):
    props = {
        'Type': (str, True),
        'Value': (str, True)
    }


class Predicates(AWSProperty):
    props = {
        'DataId': (str, True),
        'Negated': (boolean, True),
        'Type': (str, True)
    }


class GeoMatchConstraints(AWSProperty):
    props = {
        'Type': (str, True),
        'Value': (str, True)
    }


class Rules(AWSProperty):
    props = {
        'Action': (Action, True),
        'Priority': (integer, True),
        'RuleId': (str, True)
    }


class SqlInjectionMatchTuples(AWSProperty):
    props = {
        'FieldToMatch': (FieldToMatch, True),
        'TextTransformation': (str, True)
    }


class ByteMatchSet(AWSObject):
    resource_type = "AWS::WAFRegional::ByteMatchSet"

    props = {
        'ByteMatchTuples': ([ByteMatchTuples], False),
        'Name': (str, True)
    }


class IPSet(AWSObject):
    resource_type = "AWS::WAFRegional::IPSet"

    props = {
        'IPSetDescriptors': ([IPSetDescriptors], False),
        'Name': (str, True)
    }


class Rule(AWSObject):
    resource_type = "AWS::WAFRegional::Rule"

    props = {
        'MetricName': (str, True),
        'Name': (str, True),
        'Predicates': ([Predicates], False)
    }


class SqlInjectionMatchSet(AWSObject):
    resource_type = "AWS::WAFRegional::SqlInjectionMatchSet"

    props = {
        'Name': (str, True),
        'SqlInjectionMatchTuples': ([SqlInjectionMatchTuples], False)
    }


class WebACL(AWSObject):
    resource_type = "AWS::WAFRegional::WebACL"

    props = {
        'DefaultAction': (Action, True),
        'MetricName': (str, True),
        'Name': (str, True),
        'Rules': ([Rules], False)
    }


class WebACLAssociation(AWSObject):
    resource_type = "AWS::WAFRegional::WebACLAssociation"

    props = {
        'ResourceArn': (str, True),
        'WebACLId': (str, True),
    }


class SizeConstraint(AWSProperty):
    props = {
        'ComparisonOperator': (str, True),
        'FieldToMatch': (FieldToMatch, True),
        'Size': (integer, True),
        'TextTransformation': (str, True),
    }


class SizeConstraintSet(AWSObject):
    resource_type = "AWS::WAFRegional::SizeConstraintSet"

    props = {
        'Name': (str, True),
        'SizeConstraints': ([SizeConstraint], False),
    }


class XssMatchTuple(AWSProperty):
    props = {
        'FieldToMatch': (FieldToMatch, True),
        'TextTransformation': (str, True),
    }


class XssMatchSet(AWSObject):
    resource_type = "AWS::WAFRegional::XssMatchSet"

    props = {
        'Name': (str, True),
        'XssMatchTuples': ([XssMatchTuple], False),
    }


class RegexPatternSet(AWSObject):
    resource_type = "AWS::WAFRegional::RegexPatternSet"

    props = {
        'Name': (str, True),
        'RegexPatternStrings': ([str], True),
    }


class RateBasedRule(AWSObject):
    resource_type = "AWS::WAFRegional::RateBasedRule"

    props = {
        'MatchPredicates': ([Predicates], False),
        'MetricName': (str, True),
        'Name': (str, True),
        'RateKey': (str, True),
        'RateLimit': (integer, True),
    }


class GeoMatchSet(AWSObject):
    resource_type = "AWS::WAFRegional::GeoMatchSet"

    props = {
        'GeoMatchConstraints': ([GeoMatchConstraints], False),
        'Name': (str, True),
    }
