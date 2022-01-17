# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_recoveryoption_name(recoveryoption_name):
    """
    Validate Name for RecoveryOption
    Property: RecoveryOption.Name
    """

    VALID_RECOVERYOPTION_NAME = (
        "admin_only",
        "verified_email",
        "verified_phone_number",
    )

    if recoveryoption_name not in VALID_RECOVERYOPTION_NAME:
        raise ValueError(
            "RecoveryOption Name must be one of: %s"
            % ", ".join(VALID_RECOVERYOPTION_NAME)
        )
    return recoveryoption_name
