# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, exactly_one, json_checker, positive_integer


class MetricDimension(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Value': (basestring, True),
    }


class Alarm(AWSObject):
    resource_type = "AWS::CloudWatch::Alarm"

    props = {
        'ActionsEnabled': (boolean, False),
        'AlarmActions': ([basestring], False),
        'AlarmDescription': (basestring, False),
        'AlarmName': (basestring, False),
        'ComparisonOperator': (basestring, True),
        'Dimensions': ([MetricDimension], False),
        'EvaluateLowSampleCountPercentile': (basestring, False),
        'EvaluationPeriods': (positive_integer, True),
        'ExtendedStatistic': (basestring, False),
        'InsufficientDataActions': ([basestring], False),
        'MetricName': (basestring, True),
        'Namespace': (basestring, True),
        'OKActions': ([basestring], False),
        'Period': (positive_integer, True),
        'Statistic': (basestring, False),
        'Threshold': (basestring, True),
        'TreatMissingData': (basestring, False),
        'Unit': (basestring, False),
    }

    def validate(self):
        conds = [
            'ExtendedStatistic',
            'Statistic',
        ]
        exactly_one(self.__class__.__name__, self.properties, conds)


class Dashboard(AWSObject):
    resource_type = "AWS::CloudWatch::Dashboard"

    props = {
        'DashboardBody': ((basestring, dict), True),
        'DashboardName': (basestring, False),
    }

    def validate(self):
        name = 'DashboardBody'
        if name in self.properties:
            dashboard_body = self.properties.get(name)
            self.properties[name] = json_checker(name, dashboard_body)
