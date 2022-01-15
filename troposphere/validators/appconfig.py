# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_growth_type(growth_type):
    """
    Property: DeploymentStrategy.GrowthType
    """

    VALID_GROWTH_TYPE = "LINEAR"

    if growth_type not in VALID_GROWTH_TYPE:
        raise ValueError(
            "DeploymentStrategy GrowthType must be one of: %s"
            % ", ".join(VALID_GROWTH_TYPE)
        )
    return growth_type


def validate_replicate_to(replicate_to):
    """
    Property: DeploymentStrategy.ReplicateTo
    """

    VALID_REPLICATION_DESTINATION = ("NONE", "SSM_DOCUMENT")

    if replicate_to not in VALID_REPLICATION_DESTINATION:
        raise ValueError(
            "DeploymentStrategy ReplicateTo must be one of: %s"
            % ", ".join(VALID_REPLICATION_DESTINATION)
        )
    return replicate_to


def validate_validator_type(validator_type):
    """
    Property: Validators.Type
    """

    VALID_VALIDATOR_TYPE = ("JSON_SCHEMA", "LAMBDA")

    if validator_type not in VALID_VALIDATOR_TYPE:
        raise ValueError(
            "ConfigurationProfile Validator Type must be one of: %s"
            % ", ".join(VALID_VALIDATOR_TYPE)  # NOQA
        )
    return validator_type
