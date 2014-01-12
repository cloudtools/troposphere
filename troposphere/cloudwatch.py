# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import integer


class Alarm(AWSObject):
    type = "AWS::CloudWatch::Alarm"

    props = {
        'ActionsEnabled': (basestring, False),
        'AlarmActions': (list, False),
        'AlarmDescription': (basestring, False),
        'AlarmName': (basestring, False),
        'ComparisonOperator': (basestring, True),
        'Dimensions': (list, False),
        'EvaluationPeriods': (integer, True),
        'InsufficientDataActions': (list, False),
        'MetricName': (basestring, True),
        'Namespace': (basestring, True),
        'OKActions': (list, False),
        'Period': (integer, True),
        'Statistic': (basestring, True),
        'Threshold': (integer, True),
        'Unit': (basestring, False),
    }


class MetricDimension(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Value': (basestring, True),
    }
