# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_listvalue(values):
    """
    Property: DataValue.ListValue
    """
    from .. import AWSHelperFn
    from ..iottwinmaker import DataValue

    if not isinstance(values, list):
        raise TypeError("ListValue must be a list")

    for v in values:
        if not isinstance(v, (DataValue, AWSHelperFn)):
            raise TypeError("ListValue must contain DataValue or AWSHelperFn")


def validate_nestedtypel(value):
    """
    Property: DataType.NestedType
    """
    from .. import AWSHelperFn
    from ..iottwinmaker import DataType

    if not isinstance(value, (DataType, AWSHelperFn)):
        raise TypeError("NestedType must be either DataType or AWSHelperFn")
