# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty


class Alarm(AWSObject):
    props = {
        'ActionsEnabled': (basestring, False),
        'AlarmActions': (list, False),
        'AlarmDescription': (basestring, False),
        'ComparisonOperator': (basestring, True),
        'Dimensions': (list, False),
        'EvaluationPeriods': (int, True),
        'InsufficientDataActions': (list, False),
        'MetricName': (basestring, True),
        'Namespace': (basestring, True),
        'OKActions': (list, False),
        'Period': (int, True),
        'Statistic': (basestring, True),
        'Threshold': (float, True),
        'Unit': (basestring, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::CloudWatch::Alarm"
        sup = super(Alarm, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class MetricDimension(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Value': (basestring, True),
    }
