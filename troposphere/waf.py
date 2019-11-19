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
        'Data': (basestring, False),  # Conditional
        'Type': (basestring, True)
    }


class ByteMatchTuples(AWSProperty):
    props = {
        'FieldToMatch': (FieldToMatch, True),
        'PositionalConstraint': (basestring, True),
        'TargetString': (basestring, False),  # Conditional
        'TargetStringBase64': (basestring, False),  # Conditional
        'TextTransformation': (basestring, True)
    }


class IPSetDescriptors(AWSProperty):
    props = {
        'Type': (basestring, True),
        'Value': (basestring, True)
    }


class Predicates(AWSProperty):
    props = {
        'DataId': (basestring, True),
        'Negated': (boolean, True),
        'Type': (basestring, True)
    }


class Rules(AWSProperty):
    props = {
        'Action': (Action, True),
        'Priority': (integer, True),
        'RuleId': (basestring, True)
    }


class SqlInjectionMatchTuples(AWSProperty):
    props = {
        'FieldToMatch': (FieldToMatch, True),
        'TextTransformation': (basestring, True)
    }


class ByteMatchSet(AWSObject):
    resource_type = "AWS::WAF::ByteMatchSet"

    props = {
        'ByteMatchTuples': ([ByteMatchTuples], False),
        'Name': (basestring, True)
    }


class IPSet(AWSObject):
    resource_type = "AWS::WAF::IPSet"

    props = {
        'IPSetDescriptors': ([IPSetDescriptors], False),
        'Name': (basestring, True)
    }


class Rule(AWSObject):
    resource_type = "AWS::WAF::Rule"

    props = {
        'MetricName': (basestring, True),
        'Name': (basestring, True),
        'Predicates': ([Predicates], False)
    }


class SqlInjectionMatchSet(AWSObject):
    resource_type = "AWS::WAF::SqlInjectionMatchSet"

    props = {
        'Name': (basestring, True),
        'SqlInjectionMatchTuples': ([SqlInjectionMatchTuples], False)
    }


class WebACL(AWSObject):
    resource_type = "AWS::WAF::WebACL"

    props = {
        'DefaultAction': (Action, True),
        'MetricName': (basestring, True),
        'Name': (basestring, True),
        'Rules': ([Rules], False)
    }


class SizeConstraint(AWSProperty):
    props = {
        'ComparisonOperator': (basestring, True),
        'FieldToMatch': (FieldToMatch, True),
        'Size': (integer, True),
        'TextTransformation': (basestring, True),
    }


class SizeConstraintSet(AWSObject):
    resource_type = "AWS::WAF::SizeConstraintSet"

    props = {
        'Name': (basestring, True),
        'SizeConstraints': ([SizeConstraint], False),
    }


class XssMatchTuple(AWSProperty):
    props = {
        'FieldToMatch': (FieldToMatch, True),
        'TextTransformation': (basestring, True),
    }


class XssMatchSet(AWSObject):
    resource_type = "AWS::WAF::XssMatchSet"

    props = {
        'Name': (basestring, True),
        'XssMatchTuples': ([XssMatchTuple], False),
    }
