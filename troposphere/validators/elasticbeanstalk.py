# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


WebServer = "WebServer"
Worker = "Worker"
WebServerType = "Standard"
WorkerType = "SQS/HTTP"


def validate_tier_name(name):
    """
    Property: Tier.Name
    """
    valid_names = [WebServer, Worker]
    if name not in valid_names:
        raise ValueError("Tier name needs to be one of %r" % valid_names)
    return name


def validate_tier_type(tier_type):
    """
    Property: Tier.Type
    """
    valid_types = [WebServerType, WorkerType]
    if tier_type not in valid_types:
        raise ValueError("Tier type needs to be one of %r" % valid_types)
    return tier_type
