# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def findingsfilter_action(action):
    """
    Property: FindingsFilter.Action
    """

    valid_actions = ["ARCHIVE", "NOOP"]

    if action not in valid_actions:
        raise ValueError('Action must be one of: "%s"' % (", ".join(valid_actions)))
    return action


def session_findingpublishingfrequency(frequency):
    """
    Property: Session.FindingPublishingFrequency
    """

    valid_frequencies = ["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"]

    if frequency not in valid_frequencies:
        raise ValueError(
            'FindingPublishingFrequency must be one of: "%s"'
            % (", ".join(valid_frequencies))
        )
    return frequency


def session_status(status):
    """
    Property: Session.Status
    """

    valid_status = ["ENABLED", "DISABLED"]

    if status not in valid_status:
        raise ValueError('Status must be one of: "%s"' % (", ".join(valid_status)))
    return status
