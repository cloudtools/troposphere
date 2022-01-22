# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import integer_range


def validate_sortorder(x):
    """
    Property: Order.SortOrder
    """
    return integer_range(0, 1)(x)


def connection_type_validator(type):
    """
    Property: ConnectionInput.ConnectionType
    """
    valid_types = [
        "CUSTOM",
        "JDBC",
        "KAFKA",
        "MARKETPLACE",
        "MONGODB",
        "NETWORK",
        "SFTP",
    ]
    if type not in valid_types:
        raise ValueError("% is not a valid value for ConnectionType" % type)
    return type


def delete_behavior_validator(value):
    """
    Property: SchemaChangePolicy.DeleteBehavior
    """
    valid_values = [
        "LOG",
        "DELETE_FROM_DATABASE",
        "DEPRECATE_IN_DATABASE",
    ]
    if value not in valid_values:
        raise ValueError("% is not a valid value for DeleteBehavior" % value)
    return value


def update_behavior_validator(value):
    """
    Property: SchemaChangePolicy.UpdateBehavior
    """
    valid_values = [
        "LOG",
        "UPDATE_IN_DATABASE",
    ]
    if value not in valid_values:
        raise ValueError("% is not a valid value for UpdateBehavior" % value)
    return value


def table_type_validator(type):
    """
    Property: TableInput.TableType
    """
    valid_types = [
        "EXTERNAL_TABLE",
        "VIRTUAL_VIEW",
    ]
    if type not in valid_types:
        raise ValueError("% is not a valid value for TableType" % type)
    return type


def trigger_type_validator(type):
    """
    Property: Trigger.Type
    """
    valid_types = [
        "SCHEDULED",
        "CONDITIONAL",
        "ON_DEMAND",
    ]
    if type not in valid_types:
        raise ValueError("% is not a valid value for Type" % type)
    return type
