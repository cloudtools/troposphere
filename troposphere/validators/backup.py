# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


import re

from .. import If
from . import exactly_one, json_checker


def validate_json_checker(x):
    """
    Property: BackupVault.AccessPolicy
    """
    return json_checker(x)


def backup_vault_name(name):
    """
    Property: BackupVault.BackupVaultName
    """
    vault_name_re = re.compile(r"^[a-zA-Z0-9\-\_\.]{1,50}$")  # noqa
    if vault_name_re.match(name):
        return name
    else:
        raise ValueError("%s is not a valid backup vault name" % name)


def validate_backup_selection(self):
    """
    Class: BackupSelectionResourceType
    """
    conds = [
        "ListOfTags",
        "Resources",
    ]

    def check_if(names, props):
        validated = []
        for name in names:
            validated.append(name in props and isinstance(props[name], If))
        return all(validated)

    if check_if(conds, self.properties):
        return

    exactly_one(self.__class__.__name__, self.properties, conds)
