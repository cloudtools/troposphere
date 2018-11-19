# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import (integer, boolean)

VALID_STATES = ('ENABLED', 'DISABLED')
VALID_RESOURCE_TYPES = ('VOLUME')
VALID_INTERVALS = (12, 24)
VALID_INTERVAL_UNITS = ('HOURS')


def validate_interval(interval):
    """Interval validation rule."""

    if interval not in VALID_INTERVALS:
        raise ValueError("Interval must be one of : %s" %
                         ", ".join(VALID_INTERVALS))
    return interval


def validate_interval_unit(interval_unit):
    """Interval unit validation rule."""

    if interval_unit not in VALID_INTERVAL_UNITS:
        raise ValueError("Interval unit must be one of : %s" %
                         ", ".join(VALID_INTERVAL_UNITS))
    return interval_unit


def validate_state(state):
    """State validation rule."""

    if state not in VALID_STATES:
        raise ValueError("State must be one of : %s" %
                         ", ".join(VALID_STATES))
    return state


class CreateRule(AWSProperty):
    props = {
        'Interval': (validate_interval, True),
        'IntervalUnit': (validate_interval_unit, True),
        'Times': ([basestring], False),
    }


class RetainRule(AWSProperty):
    props = {
        'Count': (integer, True),
    }


class Schedule(AWSProperty):
    props = {
        'CopyTags': (boolean, False),
        'CreateRule': (CreateRule, False),
        'Name': (basestring, False),
        'RetainRule': (RetainRule, False),
        'TagsToAdd': ((Tags, list), False),
    }


class PolicyDetails(AWSProperty):
    props = {
        'ResourceTypes': ([basestring], False),
        'Schedules': ([Schedule], False),
        'TargetTags': ((Tags, list), False),
    }


class LifecyclePolicy(AWSObject):
    resource_type = "AWS::DLM::LifecyclePolicy"

    props = {
        'Description': (basestring, False),
        'ExecutionRoleArn': (basestring, False),
        'PolicyDetails': (PolicyDetails, False),
        'State': (validate_state, False),
    }
