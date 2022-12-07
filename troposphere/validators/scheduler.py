# Copyright (c) 2022, Guy Taylor <thebigguy.co.uk@gmail.com>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_flexibletimewindow_mode(flexibletimewindow_mode):
    """
    Validate State for FlexibleTimeWindow
    Property: FlexibleTimeWindow.Mode
    """

    valid_modes = ["OFF", "FLEXIBLE"]

    if flexibletimewindow_mode not in valid_modes:
        raise ValueError("{} is not a valid mode".format(flexibletimewindow_mode))
    return flexibletimewindow_mode


def validate_ecsparameters_tags(ecsparameters_tags):
    """
    Validate State for EcsParameters
    Property: EcsParameters.Tags
    """

    if ecsparameters_tags is not None:
        raise ValueError(
            "EcsParameters Tags must be None as the TagMap property is not currently supported by AWS CloudFormation"
        )
    return ecsparameters_tags
