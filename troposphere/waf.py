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
    resource_type = "AWS::WAF::ByteMatchSet"

    props = {
        'ByteMatchTuples': ([ByteMatchTuples], False),
        'Name': (str, True)
    }


class IPSet(AWSObject):
    resource_type = "AWS::WAF::IPSet"

    props = {
        'IPSetDescriptors': ([IPSetDescriptors], False),
        'Name': (str, True)
    }


class Rule(AWSObject):
    resource_type = "AWS::WAF::Rule"

    props = {
        'MetricName': (str, True),
        'Name': (str, True),
        'Predicates': ([Predicates], False)
    }


class SqlInjectionMatchSet(AWSObject):
    resource_type = "AWS::WAF::SqlInjectionMatchSet"

    props = {
        'Name': (str, True),
        'SqlInjectionMatchTuples': ([SqlInjectionMatchTuples], False)
    }


class WebACL(AWSObject):
    resource_type = "AWS::WAF::WebACL"

    props = {
        'DefaultAction': (Action, True),
        'MetricName': (str, True),
        'Name': (str, True),
        'Rules': ([Rules], False)
    }


class SizeConstraint(AWSProperty):
    props = {
        'ComparisonOperator': (str, True),
        'FieldToMatch': (FieldToMatch, True),
        'Size': (integer, True),
        'TextTransformation': (str, True),
    }


class SizeConstraintSet(AWSObject):
    resource_type = "AWS::WAF::SizeConstraintSet"

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
    resource_type = "AWS::WAF::XssMatchSet"

    props = {
        'Name': (str, True),
        'XssMatchTuples': ([XssMatchTuple], False),
    }
