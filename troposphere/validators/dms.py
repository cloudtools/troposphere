# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from ..type_defs.compat import Final
from . import network_port

CDC: Final = "cdc"
FULL_LOAD: Final = "full-load"
FULL_LOAD_AND_CDC: Final = "full-load-and-cdc"


def validate_network_port(x):
    """
    Property: Endpoint.Port
    Property: MongoDbSettings.Port
    Property: RedisSettings.Port
    """
    return network_port(x)
