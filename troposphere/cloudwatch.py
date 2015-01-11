# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Ref
from .validators import positive_integer, boolean


class MetricDimension(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Value': (basestring, True),
    }


class Alarm(AWSObject):
    resource_type = "AWS::CloudWatch::Alarm"

    props = {
        'ActionsEnabled': (boolean, False),
        'AlarmActions': ([basestring, Ref], False),
        'AlarmDescription': (basestring, False),
        'AlarmName': (basestring, False),
        'ComparisonOperator': (basestring, True),
        'Dimensions': ([MetricDimension], False),
        'EvaluationPeriods': (positive_integer, True),
        'InsufficientDataActions': ([basestring, Ref], False),
        'MetricName': (basestring, True),
        'Namespace': (basestring, True),
        'OKActions': ([basestring, Ref], False),
        'Period': (positive_integer, True),
        'Statistic': (basestring, True),
        'Threshold': (basestring, True),
        'Unit': (basestring, False),
    }
