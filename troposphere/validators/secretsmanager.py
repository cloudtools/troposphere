# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from ..compat import validate_policytype
from . import tags_or_list


def policytypes(policy):
    """
    Property: ResourcePolicy.ResourcePolicy
    """
    return validate_policytype(policy)


def validate_tags_or_list(x):
    """
    Property: Secret.Tags
    """
    return tags_or_list(x)


def validate_target_types(target_type):
    """
    Target types validation rule.
    Property: SecretTargetAttachment.TargetType
    """

    VALID_TARGET_TYPES = (
        "AWS::RDS::DBInstance",
        "AWS::RDS::DBCluster",
        "AWS::Redshift::Cluster",
        "AWS::DocDB::DBInstance",
        "AWS::DocDB::DBCluster",
    )

    if target_type not in VALID_TARGET_TYPES:
        raise ValueError(
            "Target type must be one of : %s" % ", ".join(VALID_TARGET_TYPES)
        )
    return target_type
