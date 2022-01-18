# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_tag_update(update):
    """
    Property: ResourceUpdateConstraint.TagUpdateOnProvisionedProduct
    """
    valid_tag_update_values = [
        "ALLOWED",
        "NOT_ALLOWED",
    ]
    if update not in valid_tag_update_values:
        raise ValueError("{} is not a valid tag update value".format(update))
    return update
