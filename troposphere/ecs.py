from . import AWSObject, AWSProperty, Tags
from .validators import (
    boolean, double, integer, network_port, positive_integer, integer_range,
    ecs_proxy_type, ecs_efs_encryption_status
)

LAUNCH_TYPE_EC2 = 'EC2'
LAUNCH_TYPE_FARGATE = 'FARGATE'

SCHEDULING_STRATEGY_REPLICA = 'REPLICA'
SCHEDULING_STRATEGY_DAEMON = 'DAEMON'


class ManagedScaling(AWSProperty):
    """
    Class for ManagedScaling for AutoScalingGroupProvider
    """
    props = {
        "MaximumScalingStepSize": (integer_range(1, 10000), False),
        "MinimumScalingStepSize": (integer_range(1, 10000), False),
        "Status": (basestring, False),
        "TargetCapacity": (integer_range(1, 100), False),
    }


class AutoScalingGroupProvider(AWSProperty):
    """
    Class for property AutoScalingGroupProvider in AWS::ECS::CpacityProvider
    """
    props = {
        'AutoScalingGroupArn': (basestring, True),
        'ManagedScaling': (ManagedScaling, False),
        'ManagedTerminationProtection': (basestring, False),
    }


class CapacityProvider(AWSObject):
    """
    Class for AWS::ECS::CpacityProvider
    """
    resource_type = "AWS::ECS::CapacityProvider"
    props = {
        'AutoScalingGroupProvider': (AutoScalingGroupProvider, True),
        'Name': (basestring, False),
        'Tags': (Tags, False),
    }


class CapacityProviderStrategyItem(AWSProperty):
    """
    Class for the AWS::ECS::Cluster-CapacityProviderStrategyItem
    """
    props = {
        'Base': (integer, False),
        'CapacityProvider': (basestring, False),
        'Weight': (integer, False),
    }


class ClusterSetting(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Value': (basestring, True),
    }


class Cluster(AWSObject):
    resource_type = "AWS::ECS::Cluster"

    props = {
        'CapacityProviders': ([basestring], False),
        'ClusterName': (basestring, False),
        'ClusterSettings': ([ClusterSetting], False),
        'DefaultCapacityProviderStrategy': (
            [CapacityProviderStrategyItem], False),
        'Tags': (Tags, False),
    }


class PrimaryTaskSet(AWSObject):
    resource_type = "AWS::ECS::PrimaryTaskSet"

    props = {
        'Cluster': (basestring, True),
        'Service': (basestring, True),
        'TaskSetId': (basestring, True),
    }


class LoadBalancer(AWSProperty):
    props = {
        'ContainerName': (basestring, False),
        'ContainerPort': (network_port, True),
        'LoadBalancerName': (basestring, False),
        'TargetGroupArn': (basestring, False),
    }


class DeploymentConfiguration(AWSProperty):
    props = {
        'MaximumPercent': (positive_integer, False),
        'MinimumHealthyPercent': (positive_integer, False),
    }


class DeploymentController(AWSProperty):
    props = {
        'Type': (basestring, False),
    }


def placement_strategy_validator(x):
    valid_values = ['random', 'spread', 'binpack']
    if x not in valid_values:
        raise ValueError("Placement Strategy type must be one of: %s" %
                         ', '.join(valid_values))
    return x


def placement_constraint_validator(x):
    valid_values = ['distinctInstance', 'memberOf']
    if x not in valid_values:
        raise ValueError("Placement Constraint type must be one of: %s" %
                         ', '.join(valid_values))
    return x


def scope_validator(x):
    valid_values = ['shared', 'task']
    if x not in valid_values:
        raise ValueError("Scope type must be one of: %s" %
                         ', '.join(valid_values))
    return x


class PlacementConstraint(AWSProperty):
    props = {
        'Type': (placement_constraint_validator, True),
        'Expression': (basestring, False),
    }


class PlacementStrategy(AWSProperty):
    props = {
        'Type': (placement_strategy_validator, True),
        'Field': (basestring, False),
    }


class AwsvpcConfiguration(AWSProperty):
    props = {
        'AssignPublicIp': (basestring, False),
        'SecurityGroups': (list, False),
        'Subnets': (list, True),
    }


class NetworkConfiguration(AWSProperty):
    props = {
        'AwsvpcConfiguration': (AwsvpcConfiguration, False),
    }


def launch_type_validator(x):
    valid_values = [LAUNCH_TYPE_EC2, LAUNCH_TYPE_FARGATE]
    if x not in valid_values:
        raise ValueError("Launch Type must be one of: %s" %
                         ', '.join(valid_values))
    return x


class ServiceRegistry(AWSProperty):
    props = {
        'ContainerName': (basestring, False),
        'ContainerPort': (integer, False),
        'Port': (integer, False),
        'RegistryArn': (basestring, False),
    }


class Service(AWSObject):
    resource_type = "AWS::ECS::Service"

    props = {
        'CapacityProviderStrategy': ([CapacityProviderStrategyItem], False),
        'Cluster': (basestring, False),
        'DeploymentConfiguration': (DeploymentConfiguration, False),
        'DeploymentController': (DeploymentController, False),
        'DesiredCount': (positive_integer, False),
        'EnableECSManagedTags': (boolean, False),
        'HealthCheckGracePeriodSeconds': (positive_integer, False),
        'LaunchType': (launch_type_validator, False),
        'LoadBalancers': ([LoadBalancer], False),
        'NetworkConfiguration': (NetworkConfiguration, False),
        'Role': (basestring, False),
        'PlacementConstraints': ([PlacementConstraint], False),
        'PlacementStrategies': ([PlacementStrategy], False),
        'PlatformVersion': (basestring, False),
        'PropagateTags': (basestring, False),
        'SchedulingStrategy': (basestring, False),
        'ServiceName': (basestring, False),
        'ServiceRegistries': ([ServiceRegistry], False),
        'Tags': (Tags, False),
        'TaskDefinition': (basestring, True),
    }


class Environment(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Value': (basestring, True),
    }


class MountPoint(AWSProperty):
    props = {
        'ContainerPath': (basestring, True),
        'SourceVolume': (basestring, True),
        'ReadOnly': (boolean, False),
    }


class PortMapping(AWSProperty):
    props = {
        'ContainerPort': (network_port, True),
        'HostPort': (network_port, False),
        'Protocol': (basestring, False),
    }


class VolumesFrom(AWSProperty):
    props = {
        'SourceContainer': (basestring, True),
        'ReadOnly': (boolean, False),
    }


class HostEntry(AWSProperty):
    props = {
        'Hostname': (basestring, True),
        'IpAddress': (basestring, True),
    }


class Device(AWSProperty):
    props = {
        'ContainerPath': (basestring, False),
        'HostPath': (basestring, False),
        'Permissions': ([basestring], False),
    }


class FirelensConfiguration(AWSProperty):
    props = {
        'Options': (dict, False),
        'Type': (basestring, True),
    }


class HealthCheck(AWSProperty):
    props = {
        'Command': ([basestring], True),
        'Interval': (integer, False),
        'Retries': (integer, False),
        'StartPeriod': (integer, False),
        'Timeout': (integer, False),
    }


class KernelCapabilities(AWSProperty):
    props = {
        'Add': ([basestring], False),
        'Drop': ([basestring], False),
    }


class Tmpfs(AWSProperty):
    props = {
        'ContainerPath': (basestring, False),
        'MountOptions': ([basestring], False),
        'Size': (integer, False),
    }


class LinuxParameters(AWSProperty):
    props = {
        'Capabilities': (KernelCapabilities, False),
        'Devices': ([Device], False),
        'InitProcessEnabled': (boolean, False),
        'SharedMemorySize': (integer, False),
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


class RepositoryCredentials(AWSProperty):
    props = {
        'CredentialsParameter': (basestring, False)
    }


class ResourceRequirement(AWSProperty):
    props = {
        'Type': (basestring, True),
        'Value': (basestring, True),
    }


class SystemControl(AWSProperty):
    props = {
        'Namespace': (basestring, True),
        'Value': (basestring, True),
    }


class Ulimit(AWSProperty):
    props = {
        'HardLimit': (integer, True),
        'Name': (basestring, True),
        'SoftLimit': (integer, True),
    }


class ContainerDependency(AWSProperty):
    props = {
        'Condition': (basestring, True),
        'ContainerName': (basestring, True)
    }


class EnvironmentFile(AWSProperty):
    props = {
        'Type': (basestring, False),
        'Value': (basestring, False),
    }


class ContainerDefinition(AWSProperty):
    props = {
        'Command': ([basestring], False),
        'Cpu': (integer, False),
        'DependsOn': ([ContainerDependency], False),
        'DisableNetworking': (boolean, False),
        'DnsSearchDomains': ([basestring], False),
        'DnsServers': ([basestring], False),
        'DockerLabels': (dict, False),
        'DockerSecurityOptions': ([basestring], False),
        'EntryPoint': ([basestring], False),
        'Environment': ([Environment], False),
        'EnvironmentFiles': ([EnvironmentFile], False),
        'Essential': (boolean, False),
        'ExtraHosts': ([HostEntry], False),
        'FirelensConfiguration': (FirelensConfiguration, False),
        'HealthCheck': (HealthCheck, False),
        'Hostname': (basestring, False),
        'Image': (basestring, False),
        'Interactive': (boolean, False),
        'Links': ([basestring], False),
        'LinuxParameters': (LinuxParameters, False),
        'LogConfiguration': (LogConfiguration, False),
        'Memory': (integer, False),
        'MemoryReservation': (integer, False),
        'MountPoints': ([MountPoint], False),
        'Name': (basestring, False),
        'PortMappings': ([PortMapping], False),
        'Privileged': (boolean, False),
        'PseudoTerminal': (boolean, False),
        'ReadonlyRootFilesystem': (boolean, False),
        'RepositoryCredentials': (RepositoryCredentials, False),
        'ResourceRequirements': ([ResourceRequirement], False),
        'Secrets': ([Secret], False),
        'StartTimeout': (integer, False),
        'StopTimeout': (integer, False),
        'SystemControls': ([SystemControl], False),
        'Ulimits': ([Ulimit], False),
        'User': (basestring, False),
        'VolumesFrom': ([VolumesFrom], False),
        'WorkingDirectory': (basestring, False),
    }


class Host(AWSProperty):
    props = {
        'SourcePath': (basestring, False),
    }


class DockerVolumeConfiguration(AWSProperty):
    props = {
        'Autoprovision': (boolean, False),
        'Driver': (basestring, False),
        'DriverOpts': (dict, False),
        'Labels': (dict, False),
        'Scope': (scope_validator, False)
    }


class AuthorizationConfig(AWSProperty):
    props = {
        'AccessPointId': (basestring, False),
        'IAM': (basestring, False)
    }


class EFSVolumeConfiguration(AWSProperty):
    props = {
        'AuthorizationConfig': AuthorizationConfig,
        'FilesystemId': (basestring, True),
        'RootDirectory': (basestring, False),
        'TransitEncryption': (ecs_efs_encryption_status, False),
        'TransitEncryptionPort': (integer_range(1, (2 ** 16) - 1), False)
    }


class Volume(AWSProperty):
    props = {
        'DockerVolumeConfiguration': (DockerVolumeConfiguration, False),
        'Name': (basestring, True),
        'Host': (Host, False),
        'EFSVolumeConfiguration': (EFSVolumeConfiguration, False)
    }


class InferenceAccelerator(AWSProperty):
    props = {
        'DeviceName': (basestring, False),
        'DeviceType': (basestring, False),
    }


class ProxyConfiguration(AWSProperty):
    props = {
        'ContainerName': (basestring, True),
        'ProxyConfigurationProperties': (list, False),
        'Type': (ecs_proxy_type, False)
    }


class TaskDefinition(AWSObject):
    resource_type = "AWS::ECS::TaskDefinition"

    props = {
        'ContainerDefinitions': ([ContainerDefinition], False),
        'Cpu': (basestring, False),
        'ExecutionRoleArn': (basestring, False),
        'Family': (basestring, False),
        'InferenceAccelerators': ([InferenceAccelerator], False),
        'IpcMode': (basestring, False),
        'Memory': (basestring, False),
        'NetworkMode': (basestring, False),
        'PidMode': (basestring, False),
        'PlacementConstraints': ([PlacementConstraint], False),
        'ProxyConfiguration': (ProxyConfiguration, False),
        'RequiresCompatibilities': ([basestring], False),
        'Tags': (Tags, False),
        'TaskRoleArn': (basestring, False),
        'Volumes': ([Volume], False),
    }


class Scale(AWSProperty):
    props = {
        'Unit': (basestring, False),
        'Value': (double, False),
    }


class TaskSet(AWSObject):
    resource_type = "AWS::ECS::TaskSet"

    props = {
        'Cluster': (basestring, True),
        'ExternalId': (basestring, False),
        'LaunchType': (basestring, False),
        'LoadBalancers': ([LoadBalancer], False),
        'NetworkConfiguration': (NetworkConfiguration, False),
        'PlatformVersion': (basestring, False),
        'Scale': (Scale, False),
        'Service': (basestring, True),
        'ServiceRegistries': ([ServiceRegistry], False),
        'TaskDefinition': (basestring, True),
    }
