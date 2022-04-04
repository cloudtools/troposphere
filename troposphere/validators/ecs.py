# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import integer_range, network_port, one_of

LAUNCH_TYPE_EC2 = "EC2"
LAUNCH_TYPE_FARGATE = "FARGATE"

SCHEDULING_STRATEGY_REPLICA = "REPLICA"
SCHEDULING_STRATEGY_DAEMON = "DAEMON"


RUNTIME_PLATFORM_CPU_CONFIGURATIONS = ["ARM64", "X86_64"]
RUNTIME_PLATFORM_OS_FAMILY = [
    "LINUX",
    "WINDOWS_SERVER_2004_CORE",
    "WINDOWS_SERVER_2016_FULL",
    "WINDOWS_SERVER_2019_CORE",
    "WINDOWS_SERVER_2019_FULL",
    "WINDOWS_SERVER_2022_CORE",
    "WINDOWS_SERVER_2022_FULL",
    "WINDOWS_SERVER_20H2_CORE",
]


def validate_scaling_step_size(port):
    """
    Property: ManagedScaling.MaximumScalingStepSize
    Property: ManagedScaling.MinimumScalingStepSize
    """
    return integer_range(1, 10000)(port)


def validate_target_capacity(x):
    """
    Property: ManagedScaling.TargetCapacity
    """
    return integer_range(1, 100)(x)


def validate_ephemeral_storage_size(x):
    """
    Property: EphemeralStorage.SizeInGiB
    """
    return integer_range(21, 200)(x)


def validate_transit_encryption_port(port):
    """
    Property: EFSVolumeConfiguration.TransitEncryptionPort
    """
    return integer_range(1, (2**16) - 1)(port)


def validate_network_port(x):
    """
    Property: LoadBalancer.ContainerPort
    Property: PortMapping.ContainerPort
    Property: PortMapping.HostPort
    """
    return network_port(x)


def ecs_efs_encryption_status(status):
    """
    Property: EFSVolumeConfiguration.TransitEncryption
    """

    valid_status = ["ENABLED", "DISABLED"]
    if status not in valid_status:
        raise ValueError(
            'ECS EFS Encryption in transit can only be one of: "%s"'
            % (", ".join(valid_status))
        )
    return status


def ecs_proxy_type(proxy_type):
    """
    Property: ProxyConfiguration.Type
    """

    valid_types = ["APPMESH"]
    if proxy_type not in valid_types:
        raise ValueError('Type must be one of: "%s"' % (", ".join(valid_types)))
    return proxy_type


def placement_strategy_validator(x):
    """
    Property: PlacementStrategy.Type
    """

    valid_values = ["random", "spread", "binpack"]
    if x not in valid_values:
        raise ValueError(
            "Placement Strategy type must be one of: %s" % ", ".join(valid_values)
        )
    return x


def placement_constraint_validator(x):
    """
    Property: PlacementConstraint.Type
    """

    valid_values = ["distinctInstance", "memberOf"]
    if x not in valid_values:
        raise ValueError(
            "Placement Constraint type must be one of: %s" % ", ".join(valid_values)
        )
    return x


def scope_validator(x):
    """
    Property: DockerVolumeConfiguration.Scope
    """

    valid_values = ["shared", "task"]
    if x not in valid_values:
        raise ValueError("Scope type must be one of: %s" % ", ".join(valid_values))
    return x


def launch_type_validator(x):
    """
    Property: Service.LaunchType
    """

    valid_values = [LAUNCH_TYPE_EC2, LAUNCH_TYPE_FARGATE]
    if x not in valid_values:
        raise ValueError("Launch Type must be one of: %s" % ", ".join(valid_values))
    return x


def validate_runtime_platform(self):
    """
    Class: RuntimePlatform
    """

    one_of(
        self.__class__.__name__,
        self.properties,
        "CpuArchitecture",
        RUNTIME_PLATFORM_CPU_CONFIGURATIONS,
    )
    one_of(
        self.__class__.__name__,
        self.properties,
        "OperatingSystemFamily",
        RUNTIME_PLATFORM_OS_FAMILY,
    )
