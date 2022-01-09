# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def resourcequery_type(type):
    """
    Property: ResourceQuery.Type
    """

    valid_types = ["TAG_FILTERS_1_0", "CLOUDFORMATION_STACK_1_0"]

    if type not in valid_types:
        raise ValueError('Type must be one of: "%s"' % (", ".join(valid_types)))
    return type
