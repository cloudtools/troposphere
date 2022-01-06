# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_homedirectory_type(homedirectory_type):
    """
    Validate HomeDirectoryType for User
    Property: User.HomeDirectoryType
    """

    VALID_HOMEDIRECTORY_TYPE = ("LOGICAL", "PATH")

    if homedirectory_type not in VALID_HOMEDIRECTORY_TYPE:  # NOQA
        raise ValueError(
            "User HomeDirectoryType must be one of: %s"
            % ", ".join(VALID_HOMEDIRECTORY_TYPE)  # NOQA
        )
    return homedirectory_type
