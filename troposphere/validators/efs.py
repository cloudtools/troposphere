# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import one_of

Bursting = "bursting"
Provisioned = "provisioned"
Elastic = "elastic"


def throughput_mode_validator(mode):
    """
    Property: FileSystem.ThroughputMode
    """
    valid_modes = [Bursting, Provisioned, Elastic]
    if mode not in valid_modes:
        raise ValueError(
            'ThroughputMode must be one of: "%s"' % (", ".join(valid_modes))
        )
    return mode


def provisioned_throughput_validator(throughput):
    """
    Property: FileSystem.ProvisionedThroughputInMibps
    """
    if throughput < 0.0:
        raise ValueError(
            "ProvisionedThroughputInMibps must be greater than or equal to 0.0"
        )
    return throughput


def validate_backup_policy(self):
    """
    Class: BackupPolicy
    """

    conds = ["DISABLED", "DISABLING", "ENABLED", "ENABLING"]
    one_of(self.__class__.__name__, self.properties, "Status", conds)
