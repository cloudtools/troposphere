# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from .. import AWSHelperFn


def validate_trigger(self):
    """
    Class: Trigger
    """
    valid = [
        "all",
        "createReference",
        "deleteReference",
        "updateReference",
    ]
    events = self.properties.get("Events")
    if events and not isinstance(events, AWSHelperFn):
        if "all" in events and len(events) != 1:
            raise ValueError("Trigger events: all must be used alone")
        else:
            for e in events:
                if e not in valid and not isinstance(e, AWSHelperFn):
                    raise ValueError("Trigger: invalid event %s" % e)
