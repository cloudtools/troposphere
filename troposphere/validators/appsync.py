# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def resolver_kind_validator(x):
    """
    Property: Resolver.Kind
    """
    valid_types = ["UNIT", "PIPELINE"]
    if x not in valid_types:
        raise ValueError("Kind must be one of: %s" % ", ".join(valid_types))
    return x
