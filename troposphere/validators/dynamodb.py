# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from .. import AWSHelperFn, If


def attribute_type_validator(x):
    """
    Property: AttributeDefinition.AttributeType
    """
    valid_types = ["S", "N", "B"]
    if x not in valid_types:
        raise ValueError("AttributeType must be one of: %s" % ", ".join(valid_types))
    return x


def key_type_validator(x):
    """
    Property: KeySchema.KeyType
    """
    valid_types = ["HASH", "RANGE"]
    if x not in valid_types:
        raise ValueError("KeyType must be one of: %s" % ", ".join(valid_types))
    return x


def projection_type_validator(x):
    """
    Property: Projection.ProjectionType
    """
    valid_types = ["KEYS_ONLY", "INCLUDE", "ALL"]
    if x not in valid_types:
        raise ValueError("ProjectionType must be one of: %s" % ", ".join(valid_types))
    return x


def billing_mode_validator(x):
    """
    Property: Table.BillingMode
    """
    valid_modes = ["PROVISIONED", "PAY_PER_REQUEST"]
    if x not in valid_modes:
        raise ValueError(
            "Table billing mode must be one of: %s" % ", ".join(valid_modes)
        )
    return x


def table_class_validator(x):
    """
    Property: Table.TableClass
    """
    valid_table_classes = ["STANDARD", "STANDARD_INFREQUENT_ACCESS"]
    if x not in valid_table_classes:
        raise ValueError(
            "Table class must be one of: %s" % ", ".join(valid_table_classes)
        )
    return x


def validate_table(self):
    """
    Class: Table
    """
    billing_mode = self.properties.get("BillingMode", "PROVISIONED")
    indexes = self.properties.get("GlobalSecondaryIndexes", [])
    tput_props = [self.properties]
    tput_props.extend([x.properties for x in indexes if not isinstance(x, AWSHelperFn)])

    def check_if_all(name, props):
        validated = []
        for prop in props:
            is_helper = isinstance(prop.get(name), AWSHelperFn)
            validated.append(name in prop or is_helper)
        return all(validated)

    def check_any(name, props):
        validated = []
        for prop in props:
            is_helper = isinstance(prop.get(name), AWSHelperFn)
            validated.append(name in prop and not is_helper)
        return any(validated)

    if isinstance(billing_mode, If):
        if check_any("ProvisionedThroughput", tput_props):
            raise ValueError(
                "Table billing mode is per-request. "
                "ProvisionedThroughput property is mutually exclusive"
            )
        return

    if billing_mode == "PROVISIONED":
        if not check_if_all("ProvisionedThroughput", tput_props):
            raise ValueError(
                "Table billing mode is provisioned. "
                "ProvisionedThroughput required if available"
            )
    elif billing_mode == "PAY_PER_REQUEST":
        if check_any("ProvisionedThroughput", tput_props):
            raise ValueError(
                "Table billing mode is per-request. "
                "ProvisionedThroughput property is mutually exclusive"
            )
