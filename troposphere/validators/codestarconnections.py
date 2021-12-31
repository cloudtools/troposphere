# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_connection_providertype(connection_providertype):
    """
    Validate ProviderType for Connection
    Property: Connection.ProviderType
    """

    VALID_CONNECTION_PROVIDERTYPE = ["Bitbucket", "GitHub", "GitHubEnterpriseServer"]

    if connection_providertype not in VALID_CONNECTION_PROVIDERTYPE:
        raise ValueError(
            "Connection ProviderType must be one of: %s"
            % ", ".join(VALID_CONNECTION_PROVIDERTYPE)
        )
    return connection_providertype
