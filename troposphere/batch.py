from . import AWSObject, AWSProperty
from .validators import positive_integer


class ComputeResources(AWSProperty):

    props = {
        "SpotIamFleetRole": (basestring, False),
        "MaxvCpus": (positive_integer, True),
        "SecurityGroupIds": ([basestring], True),
        "BidPercentage": (positive_integer, False),
        "Type": (basestring, True),
        "Subnets": ([basestring], True),
        "MinvCpus": (positive_integer, True),
        "ImageId": (basestring, False),
        "InstanceRole": (basestring, True),
        "InstanceTypes": ([basestring], True),
        "Ec2KeyPair": (basestring, False),
        "Tags": (dict, False),
        "DesiredvCpus": (positive_integer, False)
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


class Ulimit(AWSProperty):

    props = {
        "SoftLimit": (positive_integer, True),
        "HardLimit": (positive_integer, True),
        "Name": (basestring, True)
    }


class ContainerProperties(AWSProperty):

    props = {
        "MountPoints": ([MountPoints], False),
        "User": (basestring, False),
        "Volumes": ([Volumes], False),
        "Command": ([basestring], False),
        "Memory": (positive_integer, True),
        "Privileged": (bool, False),
        "Environment": ([Environment], False),
        "JobRoleArn": (basestring, False),
        "ReadonlyRootFilesystem": (bool, False),
        "Ulimits": ([Ulimit], False),
        "Vcpus": (positive_integer, True),
        "Image": (basestring, True)
    }


class RetryStrategy(AWSProperty):

    props = {
        "Attempts": (positive_integer, False)
    }


class JobDefinition(AWSObject):
    resource_type = "AWS::Batch::JobDefinition"

    props = {
        "Type": (basestring, True),
        "Parameters": (dict, True),
        "ContainerProperties": (ContainerProperties, True),
        "JobDefinitionName": (basestring, False),
        "RetryStrategy": (RetryStrategy, False)
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
