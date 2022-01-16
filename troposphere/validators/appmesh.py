# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_listenertls_mode(listenertls_mode):
    """
    Validate Mode for ListernerTls
    Property: ListenerTls.Mode
    """

    VALID_LISTENERTLS_MODE = ("STRICT", "PERMISSIVE", "DISABLED")

    if listenertls_mode not in VALID_LISTENERTLS_MODE:
        raise ValueError(
            "ListernerTls Mode must be one of: %s" % ", ".join(VALID_LISTENERTLS_MODE)
        )
    return listenertls_mode
