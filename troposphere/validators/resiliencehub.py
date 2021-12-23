# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_resiliencypolicy_policy(policy):
    """
    Validate Type for Policy
    Property: ResiliencyPolicy.Policy
    """
    from ..resiliencehub import FailurePolicy

    VALID_POLICY_KEYS = ("Software", "Hardware", "AZ", "Region")

    if not isinstance(policy, dict):
        raise ValueError("Policy must be a dict")

    for k, v in policy.items():
        if k not in VALID_POLICY_KEYS:
            policy_keys = ", ".join(VALID_POLICY_KEYS)
            raise ValueError(f"Policy key must be one of {policy_keys}")

        if not isinstance(v, FailurePolicy):
            raise ValueError("Policy value must be FailurePolicy")

    return policy


def validate_resiliencypolicy_tier(tier):
    """
    Validate Type for Tier
    Property: ResiliencyPolicy.Tier
    """

    VALID_TIER_VALUES = (
        "MissionCritical",
        "Critical",
        "Important",
        "CoreServices",
        "NonCritical",
    )

    if tier not in VALID_TIER_VALUES:
        tier_values = ", ".join(VALID_TIER_VALUES)
        raise ValueError(f"Tier must be one of {tier_values}")

    return tier
