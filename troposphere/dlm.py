# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import (integer, boolean)

VALID_STATES = ('ENABLED', 'DISABLED')
VALID_RESOURCE_TYPES = ('VOLUME')
VALID_INTERVALS = (2, 3, 4, 6, 8, 12, 24)
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


class Parameters(AWSProperty):
    props = {
        'ExcludeBootVolume': (boolean, False),
    }


class CreateRule(AWSProperty):
    props = {
        'Interval': (validate_interval, True),
        'IntervalUnit': (validate_interval_unit, True),
        'Times': ([str], False),
    }


class CrossRegionCopyRetainRule(AWSProperty):
    props = {
        'Interval': (integer, True),
        'IntervalUnit': (str, True),
    }


class CrossRegionCopyRule(AWSProperty):
    props = {
        'CmkArn': (str, False),
        'CopyTags': (boolean, False),
        'Encrypted': (boolean, True),
        'RetainRule': (CrossRegionCopyRetainRule, False),
        'TargetRegion': (str, True),
    }


class FastRestoreRule(AWSProperty):
    props = {
        'AvailabilityZones': ([str], False),
        'Count': (integer, False),
        'Interval': (integer, False),
        'IntervalUnit': (str, False),
    }


class RetainRule(AWSProperty):
    props = {
        'Count': (integer, True),
    }


class Schedule(AWSProperty):
    props = {
        'CopyTags': (boolean, False),
        'CreateRule': (CreateRule, False),
        'CrossRegionCopyRules': ([CrossRegionCopyRule], False),
        'FastRestoreRule': (FastRestoreRule, False),
        'Name': (str, False),
        'RetainRule': (RetainRule, False),
        'TagsToAdd': ((Tags, list), False),
    }


class PolicyDetails(AWSProperty):
    props = {
        'Parameters': (Parameters, False),
        'PolicyType': (str, False),
        'ResourceTypes': ([str], False),
        'Schedules': ([Schedule], False),
        'TargetTags': ((Tags, list), False),
    }


class LifecyclePolicy(AWSObject):
    resource_type = "AWS::DLM::LifecyclePolicy"

    props = {
        'Description': (str, False),
        'ExecutionRoleArn': (str, False),
        'PolicyDetails': (PolicyDetails, False),
        'State': (validate_state, False),
    }
