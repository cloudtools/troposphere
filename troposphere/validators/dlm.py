# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import tags_or_list


def validate_tags_or_list(x):
    """
    Property: LifecyclePolicy.Tags
    Property: PolicyDetails.TargetTags
    Property: Schedule.TagsToAdd
    """
    return tags_or_list(x)


def validate_interval(interval):
    """
    Interval validation rule.
    Property: CreateRule.Interval
    """

    VALID_INTERVALS = (2, 3, 4, 6, 8, 12, 24)

    if interval not in VALID_INTERVALS:
        raise ValueError("Interval must be one of : %s" % ", ".join(VALID_INTERVALS))
    return interval


def validate_interval_unit(interval_unit):
    """
    Interval unit validation rule.
    Property: CreateRule.IntervalUnit
    """

    VALID_INTERVAL_UNITS = "HOURS"

    if interval_unit not in VALID_INTERVAL_UNITS:
        raise ValueError(
            "Interval unit must be one of : %s" % ", ".join(VALID_INTERVAL_UNITS)
        )
    return interval_unit


def validate_state(state):
    """
    State validation rule.
    Property: LifecyclePolicy.State
    """

    VALID_STATES = ("ENABLED", "DISABLED")

    if state not in VALID_STATES:
        raise ValueError("State must be one of : %s" % ", ".join(VALID_STATES))
    return state
