# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import json_checker


def validate_json_checker(x):
    """
    Property: Placement.AssociatedDevices
    Property: Placement.Attributes
    Property: PlacementTemplate.DefaultAttributes
    Property: PlacementTemplate.DeviceTemplates
    """
    return json_checker(x)
