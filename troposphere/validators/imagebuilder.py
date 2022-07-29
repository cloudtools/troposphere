# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def component_platforms(component_platform):
    """
    Property: Component.Platform
    """
    valid_component_platforms = ["Linux", "Windows"]
    if component_platform not in valid_component_platforms:
        raise ValueError(
            'Platform must be one of: "%s"' % (", ".join(valid_component_platforms))
        )
    return component_platform


def ebsinstanceblockdevicespecification_volume_type(type):
    """
    Property: EbsInstanceBlockDeviceSpecification.VolumeType
    """
    valid_types = ["gp2", "gp3", "io1", "io2", "sc1", "st1", "standard"]
    if type not in valid_types:
        raise ValueError('VolumeType must be one of: "%s"' % (", ".join(valid_types)))
    return type


def imagepipeline_status(status):
    """
    Property: ImagePipeline.Status
    """
    valid_status = ["DISABLED", "ENABLED"]
    if status not in valid_status:
        raise ValueError('Status must be one of: "%s"' % (", ".join(valid_status)))
    return status


def schedule_pipelineexecutionstartcondition(startcondition):
    """
    Property: Schedule.PipelineExecutionStartCondition
    """
    valid_startcondition = [
        "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE",
        "EXPRESSION_MATCH_ONLY",
    ]
    if startcondition not in valid_startcondition:
        raise ValueError(
            'PipelineExecutionStartCondition must be one of: "%s"'
            % (", ".join(valid_startcondition))
        )
    return startcondition
