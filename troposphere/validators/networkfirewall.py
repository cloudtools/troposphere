# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_rule_group_type(rule_group_type):
    """
    Validate Type for RuleGroup
    Property: RuleGroup.Type
    """

    VALID_RULE_GROUP_TYPES = ("STATEFUL", "STATELESS")
    if rule_group_type not in VALID_RULE_GROUP_TYPES:
        raise ValueError(
            "RuleGroup Type must be one of %s" % ", ".join(VALID_RULE_GROUP_TYPES)
        )
    return rule_group_type
