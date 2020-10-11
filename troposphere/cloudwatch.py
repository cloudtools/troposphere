# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import (boolean, double, exactly_one, json_checker,
                         positive_integer, integer)


VALID_UNITS = ('Seconds', 'Microseconds', 'Milliseconds', 'Bytes', 'Kilobytes',
               'Megabytes', 'Gigabytes', 'Terabytes', 'Bits', 'Kilobits',
               'Megabits', 'Gigabits', 'Terabits', 'Percent', 'Count',
               'Bytes/Second', 'Kilobytes/Second', 'Megabytes/Second',
               'Gigabytes/Second', 'Terabytes/Second', 'Bits/Second',
               'Kilobits/Second', 'Megabits/Second', 'Gigabits/Second',
               'Terabits/Second', 'Count/Second', 'None')

VALID_TREAT_MISSING_DATA_TYPES = ('breaching', 'notBreaching', 'ignore',
                                  'missing')


def validate_unit(unit):
    """Validate Units"""

    if unit not in VALID_UNITS:
        raise ValueError("MetricStat Unit must be one of: %s" %
                         ", ".join(VALID_UNITS))
    return unit


def validate_treat_missing_data(value):
    """Validate TreatMissingData"""

    if value not in VALID_TREAT_MISSING_DATA_TYPES:
        raise ValueError("Alarm TreatMissingData must be one of: %s" %
                         ", ".join(VALID_TREAT_MISSING_DATA_TYPES))
    return value


class MetricDimension(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Value': (basestring, True),
    }


class Metric(AWSProperty):
    props = {
        'Dimensions': ([MetricDimension], False),
        'MetricName': (basestring, False),
        'Namespace': (basestring, False),
    }


class MetricStat(AWSProperty):
    props = {
        'Metric': (Metric, True),
        'Period': (integer, True),
        'Stat': (basestring, True),
        'Unit': (validate_unit, False),
    }


class MetricDataQuery(AWSProperty):
    props = {
        'Expression': (basestring, False),
        'Id': (basestring, True),
        'Label': (basestring, False),
        'MetricStat': (MetricStat, False),
        'ReturnData': (boolean, False),
    }


class Alarm(AWSObject):
    resource_type = "AWS::CloudWatch::Alarm"

    props = {
        'ActionsEnabled': (boolean, False),
        'AlarmActions': ([basestring], False),
        'AlarmDescription': (basestring, False),
        'AlarmName': (basestring, False),
        'ComparisonOperator': (basestring, True),
        'DatapointsToAlarm': (positive_integer, False),
        'Dimensions': ([MetricDimension], False),
        'EvaluateLowSampleCountPercentile': (basestring, False),
        'EvaluationPeriods': (positive_integer, True),
        'ExtendedStatistic': (basestring, False),
        'InsufficientDataActions': ([basestring], False),
        'MetricName': (basestring, False),
        'Metrics': ([MetricDataQuery], False),
        'Namespace': (basestring, False),
        'OKActions': ([basestring], False),
        'Period': (positive_integer, False),
        'Statistic': (basestring, False),
        'Threshold': (double, False),
        'ThresholdMetricId': (basestring, False),
        'TreatMissingData': (validate_treat_missing_data, False),
        'Unit': (basestring, False),
    }

    def validate(self):
        conds = [
            'ExtendedStatistic',
            'Metrics',
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
            self.properties[name] = json_checker(dashboard_body)


class Range(AWSProperty):
    props = {
        'EndTime': (basestring, True),
        'StartTime': (basestring, True),
    }


class Configuration(AWSProperty):
    props = {
        'ExcludedTimeRanges': ([Range], False),
        'MetricTimeZone': (basestring, False),
    }


class AnomalyDetector(AWSObject):
    resource_type = "AWS::CloudWatch::AnomalyDetector"

    props = {
        'Configuration': (Configuration, False),
        'Dimensions': ([MetricDimension], False),
        'MetricName': (basestring, True),
        'Namespace': (basestring, True),
        'Stat': (basestring, True)
    }


class InsightRule(AWSObject):
    resource_type = "AWS::CloudWatch::InsightRule"

    props = {
        'RuleBody': (basestring, True),
        'RuleName': (basestring, True),
        'RuleState': (basestring, True),
        'Tags': (Tags, False),
    }


class CompositeAlarm(AWSObject):
    resource_type = "AWS::CloudWatch::CompositeAlarm"

    props = {
        'ActionsEnabled': (boolean, False),
        'AlarmActions': ([basestring], False),
        'AlarmDescription': (basestring, False),
        'AlarmName': (basestring, True),
        'AlarmRule': (basestring, True),
        'InsufficientDataActions': ([basestring], False),
        'OKActions': ([basestring], False),
    }
