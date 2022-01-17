# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import exactly_one, json_checker


def dict_or_string(x):
    """
    Property: Dashboard.DashboardBody
    """

    if isinstance(x, (dict, str)):
        return x
    raise TypeError(f"Value {x} of type {type(x)} must be either dict or str")


def validate_unit(unit):
    """
    Validate Units
    Property: MetricStat.Unit
    """

    VALID_UNITS = (
        "Seconds",
        "Microseconds",
        "Milliseconds",
        "Bytes",
        "Kilobytes",
        "Megabytes",
        "Gigabytes",
        "Terabytes",
        "Bits",
        "Kilobits",
        "Megabits",
        "Gigabits",
        "Terabits",
        "Percent",
        "Count",
        "Bytes/Second",
        "Kilobytes/Second",
        "Megabytes/Second",
        "Gigabytes/Second",
        "Terabytes/Second",
        "Bits/Second",
        "Kilobits/Second",
        "Megabits/Second",
        "Gigabits/Second",
        "Terabits/Second",
        "Count/Second",
        "None",
    )

    if unit not in VALID_UNITS:
        raise ValueError("MetricStat Unit must be one of: %s" % ", ".join(VALID_UNITS))
    return unit


def validate_treat_missing_data(value):
    """
    Validate TreatMissingData
    Property: Alarm.TreatMissingData
    """

    VALID_TREAT_MISSING_DATA_TYPES = ("breaching", "notBreaching", "ignore", "missing")

    if value not in VALID_TREAT_MISSING_DATA_TYPES:
        raise ValueError(
            "Alarm TreatMissingData must be one of: %s"
            % ", ".join(VALID_TREAT_MISSING_DATA_TYPES)
        )
    return value


def validate_alarm(self):
    """
    Class: Alarm
    """

    conds = [
        "ExtendedStatistic",
        "Metrics",
        "Statistic",
    ]
    exactly_one(self.__class__.__name__, self.properties, conds)


def validate_dashboard(self):
    """
    Class: Dashboard
    """

    name = "DashboardBody"
    if name in self.properties:
        dashboard_body = self.properties.get(name)
        self.properties[name] = json_checker(dashboard_body)
