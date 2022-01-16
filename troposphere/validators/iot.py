# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from ..compat import validate_policytype
from . import json_checker


def policytypes(policy):
    """
    Property: Policy.PolicyDocument
    """
    return validate_policytype(policy)


def validate_json_checker(x):
    """
    Property: JobTemplate.AbortConfig
    Property: JobTemplate.JobExecutionsRolloutConfig
    Property: JobTemplate.TimeoutConfig
    """
    return json_checker(x)
