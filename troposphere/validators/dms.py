# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import network_port

CDC = "cdc"
FULL_LOAD = "full-load"
FULL_LOAD_AND_CDC = "full-load-and-cdc"


def validate_network_port(x):
    """
    Property: Endpoint.Port
    Property: MongoDbSettings.Port
    Property: RedisSettings.Port
    """
    return network_port(x)
