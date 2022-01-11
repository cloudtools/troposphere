# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import waf_action_type


def validate_waf_action_type(action):
    """
    Property: Action.Type
    """
    return waf_action_type(action)
