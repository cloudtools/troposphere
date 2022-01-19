# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_ruletype(ruletype):
    """
    Validate RuleType for ResolverRule.
    Property: ResolverRule.RuleType
    """

    VALID_RULETYPES = ("SYSTEM", "FORWARD")

    if ruletype not in VALID_RULETYPES:
        raise ValueError("Rule type must be one of: %s" % ", ".join(VALID_RULETYPES))
    return ruletype
