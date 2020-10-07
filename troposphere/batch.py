from . import AWSObject, AWSProperty
from .validators import boolean, exactly_one, integer, positive_integer


class LaunchTemplateSpecification(AWSProperty):
    props = {
        "LaunchTemplateId": (basestring, False),
        "LaunchTemplateName": (basestring, False),
        "Version": (basestring, False),
    }

    def validate(self):
        template_ids = [
            'LaunchTemplateId',
            'LaunchTemplateName'
        ]
        exactly_one(self.__class__.__name__, self.properties, template_ids)


def validate_allocation_strategy(allocation_strategy):
    """ Validate allocation strategy
    :param allocation_strategy: Allocation strategy for ComputeResource
    :return: The provided value if valid
    """
    valid_strategies = [
        "BEST_FIT",
        "BEST_FIT_PROGRESSIVE",
        "SPOT_CAPACITY_OPTIMIZED"
    ]
    if allocation_strategy not in valid_strategies:
        raise ValueError(
            "{} is not a valid strategy".format(allocation_strategy)
        )
    return allocation_strategy


class ComputeResources(AWSProperty):

    props = {
        "AllocationStrategy": (validate_allocation_strategy, False),
        "SpotIamFleetRole": (basestring, False),
        "MaxvCpus": (positive_integer, True),
        "SecurityGroupIds": ([basestring], True),
        "BidPercentage": (positive_integer, False),
        "Type": (basestring, True),
        "Subnets": ([basestring], True),
        "MinvCpus": (positive_integer, True),
        "LaunchTemplate": (LaunchTemplateSpecification, False),
        "ImageId": (basestring, False),
        "InstanceRole": (basestring, True),
        "InstanceTypes": ([basestring], True),
        "Ec2KeyPair": (basestring, False),
        "PlacementGroup": (basestring, False),
        "Tags": (dict, False),
        "DesiredvCpus": (positive_integer, False)
    }


class Device(AWSProperty):
    props = {
        'ContainerPath': (basestring, False),
        'HostPath': (basestring, False),
        'Permissions': ([basestring], False),
    }


class Tmpfs(AWSProperty):
    props = {
        'ContainerPath': (basestring, True),
        'MountOptions': ([basestring], False),
        'Size': (integer, True),
    }


class LinuxParameters(AWSProperty):
    props = {
        'Devices': ([Device], False),
        'InitProcessEnabled': (boolean, False),
        'MaxSwap': (integer, False),
        'SharedMemorySize': (integer, False),
        'Swappiness': (integer, False),
        'Tmpfs': ([Tmpfs], False),
    }


class Secret(AWSProperty):
    props = {
        'Name': (basestring, True),
        'ValueFrom': (basestring, True),
    }


class LogConfiguration(AWSProperty):
    props = {
        'LogDriver': (basestring, True),
        'Options': (dict, False),
        'SecretOptions': ([Secret], False),
    }


class MountPoints(AWSProperty):

    props = {
        "ReadOnly": (bool, False),
        "SourceVolume": (basestring, False),
        "ContainerPath": (basestring, False)
    }


class VolumesHost(AWSProperty):

    props = {
        "SourcePath": (basestring, False)
    }


class Volumes(AWSProperty):

    props = {
        "Host": (VolumesHost, False),
        "Name": (basestring, False)
    }


class Environment(AWSProperty):

    props = {
        "Value": (basestring, False),
        "Name": (basestring, False)
    }


class ResourceRequirement(AWSProperty):
    props = {
        'Type': (basestring, False),
        'Value': (basestring, False),
    }


class Ulimit(AWSProperty):

    props = {
        "SoftLimit": (positive_integer, True),
        "HardLimit": (positive_integer, True),
        "Name": (basestring, True)
    }


class ContainerProperties(AWSProperty):

    props = {
        'Command': ([basestring], False),
        'Environment': ([Environment], False),
        'ExecutionRoleArn': (basestring, False),
        'Image': (basestring, True),
        'InstanceType': (basestring, False),
        'JobRoleArn': (basestring, False),
        'LinuxParameters': (LinuxParameters, False),
        'LogConfiguration': (LogConfiguration, False),
        'Memory': (positive_integer, True),
        'MountPoints': ([MountPoints], False),
        'Privileged': (boolean, False),
        'ReadonlyRootFilesystem': (boolean, False),
        'ResourceRequirements': ([ResourceRequirement], False),
        'Secrets': ([Secret], False),
        'Ulimits': ([Ulimit], False),
        'User': (basestring, False),
        'Vcpus': (positive_integer, True),
        'Volumes': ([Volumes], False),
    }


class RetryStrategy(AWSProperty):

    props = {
        "Attempts": (positive_integer, False)
    }


class Timeout(AWSProperty):
    props = {
        'AttemptDurationSeconds': (integer, False),
    }


class JobDefinition(AWSObject):
    resource_type = "AWS::Batch::JobDefinition"

    props = {
        'ContainerProperties': (ContainerProperties, True),
        'JobDefinitionName': (basestring, False),
        'Parameters': (dict, False),
        'RetryStrategy': (RetryStrategy, False),
        'Timeout': (Timeout, False),
        'Type': (basestring, True),
    }


def validate_environment_state(environment_state):
    """ Validate response type
    :param environment_state: State of the environment
    :return: The provided value if valid
    """
    valid_states = [
        "ENABLED",
        "DISABLED"
    ]
    if environment_state not in valid_states:
        raise ValueError(
            "{} is not a valid environment state".format(environment_state)
        )
    return environment_state


class ComputeEnvironment(AWSObject):
    resource_type = "AWS::Batch::ComputeEnvironment"

    props = {
        "Type": (basestring, True),
        "ServiceRole": (basestring, True),
        "ComputeEnvironmentName": (basestring, False),
        "ComputeResources": (ComputeResources, True),
        "State": (validate_environment_state, False)
    }


class ComputeEnvironmentOrder(AWSProperty):

    props = {
        "ComputeEnvironment": (basestring, True),
        "Order": (positive_integer, True)
    }


def validate_queue_state(queue_state):
    """ Validate response type
    :param queue_state: State of the queue
    :return: The provided value if valid
    """
    valid_states = [
        "ENABLED",
        "DISABLED"
    ]
    if queue_state not in valid_states:
        raise ValueError(
            "{} is not a valid queue state".format(queue_state)
        )
    return queue_state


class JobQueue(AWSObject):
    resource_type = "AWS::Batch::JobQueue"

    props = {
        "ComputeEnvironmentOrder": ([ComputeEnvironmentOrder], True),
        "Priority": (positive_integer, True),
        "State": (validate_queue_state, False),
        "JobQueueName": (basestring, False)
    }
