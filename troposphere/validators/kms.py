# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from ..compat import validate_policytype
from . import integer_range, tags_or_list


def policytypes(policy):
    """
    Property: Key.KeyPolicy
    """
    return validate_policytype(policy)


def key_usage_type(key):
    """
    Property: Key.KeyUsage
    """
    valid_values = ["ENCRYPT_DECRYPT", "SIGN_VERIFY"]
    if key not in valid_values:
        raise ValueError('KeyUsage must be one of: "%s"' % (", ".join(valid_values)))
    return key


def validate_pending_window_in_days(port):
    """
    Property: Key.PendingWindowInDays
    """
    return integer_range(7, 30)(port)


def validate_tags_or_list(x):
    """
    Property: Key.Tags
    """
    return tags_or_list(x)
