# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_policy_type(policy_type):
    """
    Property: Policy.Type
    """
    valid_types = [
        "AISERVICES_OPT_OUT_POLICY",
        "BACKUP_POLICY",
        "CHATBOT_POLICY",
        "DECLARATIVE_POLICY_EC2",
        "RESOURCE_CONTROL_POLICY",
        "SERVICE_CONTROL_POLICY",
        "TAG_POLICY",
    ]
    if policy_type not in valid_types:
        raise ValueError("Type must be one of: %s" % ", ".join(valid_types))
    return policy_type
