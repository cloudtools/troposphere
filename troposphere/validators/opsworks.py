# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import json_checker, mutually_exclusive, tags_or_list


def validate_json_checker(x):
    """
    Property: Layer.CustomJson
    Property: Stack.CustomJson
    """
    return json_checker(x)


def validate_tags_or_list(x):
    """
    Property: Stack.Tags
    """
    return tags_or_list(x)


def validate_volume_type(volume_type):
    """
    Property: VolumeConfiguration.VolumeType
    """

    volume_types = ("standard", "io1", "gp2")
    if volume_type not in volume_types:
        raise ValueError(
            "VolumeType (given: %s) must be one of: %s"
            % (volume_type, ", ".join(volume_types))
        )
    return volume_type


def validate_volume_configuration(self):
    """
    Class: VolumeConfiguration
    """

    volume_type = self.properties.get("VolumeType")
    iops = self.properties.get("Iops")
    if volume_type == "io1" and not iops:
        raise ValueError("Must specify Iops if VolumeType is 'io1'.")
    if volume_type != "io1" and iops:
        raise ValueError("Cannot specify Iops if VolumeType is not 'io1'.")


def validate_data_source_type(data_source_type):
    """
    Property: DataSource.Type
    """
    data_source_types = (
        "AutoSelectOpsworksMysqlInstance",
        "OpsworksMysqlInstance",
        "RdsDbInstance",
    )
    if data_source_type not in data_source_types:
        raise ValueError(
            "Type (given: %s) must be one of: %s"
            % (data_source_type, ", ".join(data_source_types))
        )
    return data_source_type


def validate_block_device_mapping(self):
    """
    Class: BlockDeviceMapping
    """
    conds = [
        "Ebs",
        "VirtualName",
    ]
    mutually_exclusive(self.__class__.__name__, self.properties, conds)


def validate_stack(self):
    """
    Class: Stack
    """
    if "VpcId" in self.properties and "DefaultSubnetId" not in self.properties:
        raise ValueError("Using VpcId requires DefaultSubnetId to be" "specified")
