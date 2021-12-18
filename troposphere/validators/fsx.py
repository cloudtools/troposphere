# Copyright (c) 2019-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def storage_type(storage_type):
    """Property: FileSystem.StorageType"""

    valid_storage_types = ["SSD", "HDD"]
    if storage_type not in valid_storage_types:
        raise ValueError(
            'StorageType must be one of: "%s"' % (", ".join(valid_storage_types))
        )
    return storage_type


def validate_lustreconfiguration_deploymenttype(lustreconfiguration_deploymenttype):
    """
    Validate DeploymentType for LustreConfiguration
    Property: LustreConfiguration.DeploymentType
    """

    VALID_LUSTRECONFIGURATION_DEPLOYMENTTYPE = (
        "PERSISTENT_1",
        "SCRATCH_1",
        "SCRATCH_2",
    )

    if (
        lustreconfiguration_deploymenttype
        not in VALID_LUSTRECONFIGURATION_DEPLOYMENTTYPE
    ):
        raise ValueError(
            "LustreConfiguration DeploymentType must be one of: %s"
            % ", ".join(VALID_LUSTRECONFIGURATION_DEPLOYMENTTYPE)
        )
    return lustreconfiguration_deploymenttype


def validate_lustreconfiguration_perunitstoragethroughput(
    lustreconfiguration_perunitstoragethroughput,
):
    """
    Validate PerUnitStorageThroughput for LustreConfiguration
    Property: LustreConfiguration.PerUnitStorageThroughput
    """

    VALID_LUSTRECONFIGURATION_PERUNITSTORAGETHROUGHPUT = (50, 100, 200)
    if (
        lustreconfiguration_perunitstoragethroughput
        not in VALID_LUSTRECONFIGURATION_PERUNITSTORAGETHROUGHPUT
    ):
        raise ValueError(
            "LustreConfiguration PerUnitStorageThroughput must be one of: %s"
            % ", ".join(VALID_LUSTRECONFIGURATION_PERUNITSTORAGETHROUGHPUT)  # NOQA
        )
    return lustreconfiguration_perunitstoragethroughput
