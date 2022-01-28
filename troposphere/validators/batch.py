# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import exactly_one


def validate_launch_template_specification(self):
    """
    Class: LaunchTemplateSpecification
    """
    template_ids = ["LaunchTemplateId", "LaunchTemplateName"]
    exactly_one(self.__class__.__name__, self.properties, template_ids)


def validate_allocation_strategy(allocation_strategy):
    """Validate allocation strategy
    :param allocation_strategy: Allocation strategy for ComputeResource
    :return: The provided value if valid
    Property: ComputeResources.AllocationStrategy
    """

    valid_strategies = [
        "BEST_FIT",
        "BEST_FIT_PROGRESSIVE",
        "SPOT_CAPACITY_OPTIMIZED",
    ]

    if allocation_strategy not in valid_strategies:
        raise ValueError("{} is not a valid strategy".format(allocation_strategy))
    return allocation_strategy


def validate_environment_state(environment_state):
    """Validate response type
    :param environment_state: State of the environment
    :return: The provided value if valid
    Property: ComputeEnvironment.State
    """

    valid_states = ["ENABLED", "DISABLED"]

    if environment_state not in valid_states:
        raise ValueError(
            "{} is not a valid environment state".format(environment_state)
        )
    return environment_state


def validate_queue_state(queue_state):
    """Validate response type
    :param queue_state: State of the queue
    :return: The provided value if valid
    Property: JobQueue.State
    """

    valid_states = ["ENABLED", "DISABLED"]

    if queue_state not in valid_states:
        raise ValueError("{} is not a valid queue state".format(queue_state))
    return queue_state
