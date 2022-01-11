# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_workgroup_state(workgroup_state):
    """
    Validate State for Workgroup
    Property: WorkGroup.State
    """

    VALID_WORKGROUP_STATE = ("ENABLED", "DISABLED")

    if workgroup_state not in VALID_WORKGROUP_STATE:
        raise ValueError(
            "Workgroup State must be one of: %s" % ", ".join(VALID_WORKGROUP_STATE)
        )
    return workgroup_state


def validate_encryptionoption(encryption_option):
    """
    Validate EncryptionOption for EncryptionConfiguration
    Property: EncryptionConfiguration.EncryptionOption
    """

    VALID_ENCRYPTIONCONFIGURATION_ENCRYPTIONOPTION = [
        "CSE_KMS",
        "SSE_KMS",
        "SSE_S3",
    ]

    if encryption_option not in VALID_ENCRYPTIONCONFIGURATION_ENCRYPTIONOPTION:
        raise ValueError(
            "EncryptionConfiguration EncryptionOption must be one of: %s"
            % ", ".join(VALID_ENCRYPTIONCONFIGURATION_ENCRYPTIONOPTION)  # NOQA
        )
    return encryption_option
