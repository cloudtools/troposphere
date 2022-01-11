# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import json_checker


def validate_json_checker(x):
    """
    Property: Policy.SecurityServicePolicyData
    """
    return json_checker(x)
