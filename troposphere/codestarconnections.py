# Copyright (c) 2012-2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import AWSObject, Tags


VALID_CONNECTION_PROVIDERTYPE = ('Bitbucket')


def validate_connection_providertype(connection_providertype):
    """Validate ProviderType for Connection"""

    if connection_providertype not in VALID_CONNECTION_PROVIDERTYPE:
        raise ValueError("Connection ProviderType must be one of: %s" %
                         ", ".join(VALID_CONNECTION_PROVIDERTYPE))
    return connection_providertype


class Connection(AWSObject):
    resource_type = "AWS::CodeStarConnections::Connection"

    props = {
        'ConnectionName': (str, True),
        'HostArn': (str, False),
        'ProviderType': (validate_connection_providertype, True),
        'Tags': (Tags, False),
    }
