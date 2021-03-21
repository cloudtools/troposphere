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
        "Status": (str, False),
        "TargetCapacity": (integer_range(1, 100), False),
    }


class AutoScalingGroupProvider(AWSProperty):
    """
    Class for property AutoScalingGroupProvider in AWS::ECS::CpacityProvider
    """
    props = {
        'AutoScalingGroupArn': (str, True),
        'ManagedScaling': (ManagedScaling, False),
        'ManagedTerminationProtection': (str, False),
    }


class CapacityProvider(AWSObject):
    """
    Class for AWS::ECS::CpacityProvider
    """
    resource_type = "AWS::ECS::CapacityProvider"
    props = {
        'AutoScalingGroupProvider': (AutoScalingGroupProvider, True),
        'Name': (str, False),
        'Tags': (Tags, False),
    }


class CapacityProviderStrategyItem(AWSProperty):
    """
    Class for the AWS::ECS::Cluster-CapacityProviderStrategyItem
    """
    props = {
        'Base': (integer, False),
        'CapacityProvider': (str, False),
        'Weight': (integer, False),
    }


class ExecuteCommandLogConfiguration(AWSProperty):
    props = {
        'CloudWatchEncryptionEnabled': (boolean, False),
        'CloudWatchLogGroupName': (str, False),
        'S3BucketName': (str, False),
        'S3EncryptionEnabled': (boolean, False),
        'S3KeyPrefix': (str, False),
    }


class ExecuteCommandConfiguration(AWSProperty):
    props = {
        'KmsKeyId': (str, False),
        'LogConfiguration': (ExecuteCommandLogConfiguration, False),
        'Logging': (str, False),
    }


class ClusterConfiguration(AWSProperty):
    props = {
        'ExecuteCommandConfiguration': (ExecuteCommandConfiguration, False),
    }


class ClusterSetting(AWSProperty):
    props = {
        'Name': (str, True),
        'Value': (str, True),
    }


class Cluster(AWSObject):
    resource_type = "AWS::ECS::Cluster"

    props = {
        'CapacityProviders': ([str], False),
        'ClusterName': (str, False),
        'ClusterSettings': ([ClusterSetting], False),
        'Configuration': (ClusterConfiguration, False),
        'DefaultCapacityProviderStrategy': (
            [CapacityProviderStrategyItem], False),
        'Tags': (Tags, False),
    }


class CapacityProviderStrategy(AWSProperty):
    props = {
        'Base': (integer, False),
        'CapacityProvider': (str, True),
        'Weight': (integer, False),
    }


class ClusterCapacityProviderAssociations(AWSObject):
    resource_type = "AWS::ECS::ClusterCapacityProviderAssociations"

    props = {
        'CapacityProviders': ([str], True),
        'Cluster': (str, True),
        'DefaultCapacityProviderStrategy':
            ([CapacityProviderStrategy], True),
    }


class PrimaryTaskSet(AWSObject):
    resource_type = "AWS::ECS::PrimaryTaskSet"

    props = {
        'Cluster': (str, True),
        'Service': (str, True),
        'TaskSetId': (str, True),
    }


class LoadBalancer(AWSProperty):
    props = {
        'ContainerName': (str, False),
        'ContainerPort': (network_port, True),
        'LoadBalancerName': (str, False),
        'TargetGroupArn': (str, False),
    }


class DeploymentCircuitBreaker(AWSProperty):
    """
    Property for AWS::ECS::Service DeploymentCircuitBreaker
    """
    props = {
        "Enable": (boolean, True),
        "Rollback": (boolean, True)
    }


class DeploymentConfiguration(AWSProperty):
    props = {
        'DeploymentCircuitBreaker': (DeploymentCircuitBreaker, False),
        'MaximumPercent': (positive_integer, False),
        'MinimumHealthyPercent': (positive_integer, False)
    }


class DeploymentController(AWSProperty):
    props = {
        'Type': (str, False),
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
        'Expression': (str, False),
    }


class PlacementStrategy(AWSProperty):
    props = {
        'Type': (placement_strategy_validator, True),
        'Field': (str, False),
    }


class AwsvpcConfiguration(AWSProperty):
    props = {
        'AssignPublicIp': (str, False),
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
        'ContainerName': (str, False),
        'ContainerPort': (integer, False),
        'Port': (integer, False),
        'RegistryArn': (str, False),
    }


class Service(AWSObject):
    resource_type = "AWS::ECS::Service"

    props = {
        'CapacityProviderStrategy': ([CapacityProviderStrategyItem], False),
        'Cluster': (str, False),
        'DeploymentConfiguration': (DeploymentConfiguration, False),
        'DeploymentController': (DeploymentController, False),
        'DesiredCount': (positive_integer, False),
        'EnableECSManagedTags': (boolean, False),
        'EnableExecuteCommand': (boolean, False),
        'HealthCheckGracePeriodSeconds': (positive_integer, False),
        'LaunchType': (launch_type_validator, False),
        'LoadBalancers': ([LoadBalancer], False),
        'NetworkConfiguration': (NetworkConfiguration, False),
        'Role': (str, False),
        'PlacementConstraints': ([PlacementConstraint], False),
        'PlacementStrategies': ([PlacementStrategy], False),
        'PlatformVersion': (str, False),
        'PropagateTags': (str, False),
        'SchedulingStrategy': (str, False),
        'ServiceName': (str, False),
        'ServiceRegistries': ([ServiceRegistry], False),
        'Tags': (Tags, False),
        'TaskDefinition': (str, True),
    }


class Environment(AWSProperty):
    props = {
        'Name': (str, True),
        'Value': (str, True),
    }


class MountPoint(AWSProperty):
    props = {
        'ContainerPath': (str, True),
        'SourceVolume': (str, True),
        'ReadOnly': (boolean, False),
    }


class PortMapping(AWSProperty):
    props = {
        'ContainerPort': (network_port, True),
        'HostPort': (network_port, False),
        'Protocol': (str, False),
    }


class VolumesFrom(AWSProperty):
    props = {
        'SourceContainer': (str, True),
        'ReadOnly': (boolean, False),
    }


class HostEntry(AWSProperty):
    props = {
        'Hostname': (str, True),
        'IpAddress': (str, True),
    }


class Device(AWSProperty):
    props = {
        'ContainerPath': (str, False),
        'HostPath': (str, False),
        'Permissions': ([str], False),
    }


class FirelensConfiguration(AWSProperty):
    props = {
        'Options': (dict, False),
        'Type': (str, True),
    }


class HealthCheck(AWSProperty):
    props = {
        'Command': ([str], True),
        'Interval': (integer, False),
        'Retries': (integer, False),
        'StartPeriod': (integer, False),
        'Timeout': (integer, False),
    }


class KernelCapabilities(AWSProperty):
    props = {
        'Add': ([str], False),
        'Drop': ([str], False),
    }


class Tmpfs(AWSProperty):
    props = {
        'ContainerPath': (str, False),
        'MountOptions': ([str], False),
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
        'Name': (str, True),
        'ValueFrom': (str, True),
    }


class LogConfiguration(AWSProperty):
    props = {
        'LogDriver': (str, True),
        'Options': (dict, False),
        'SecretOptions': ([Secret], False),
    }


class RepositoryCredentials(AWSProperty):
    props = {
        'CredentialsParameter': (str, False)
    }


class ResourceRequirement(AWSProperty):
    props = {
        'Type': (str, True),
        'Value': (str, True),
    }


class SystemControl(AWSProperty):
    props = {
        'Namespace': (str, True),
        'Value': (str, True),
    }


class Ulimit(AWSProperty):
    props = {
        'HardLimit': (integer, True),
        'Name': (str, True),
        'SoftLimit': (integer, True),
    }


class ContainerDependency(AWSProperty):
    props = {
        'Condition': (str, True),
        'ContainerName': (str, True)
    }


class EnvironmentFile(AWSProperty):
    props = {
        'Type': (str, False),
        'Value': (str, False),
    }


class ContainerDefinition(AWSProperty):
    props = {
        'Command': ([str], False),
        'Cpu': (integer, False),
        'DependsOn': ([ContainerDependency], False),
        'DisableNetworking': (boolean, False),
        'DnsSearchDomains': ([str], False),
        'DnsServers': ([str], False),
        'DockerLabels': (dict, False),
        'DockerSecurityOptions': ([str], False),
        'EntryPoint': ([str], False),
        'Environment': ([Environment], False),
        'EnvironmentFiles': ([EnvironmentFile], False),
        'Essential': (boolean, False),
        'ExtraHosts': ([HostEntry], False),
        'FirelensConfiguration': (FirelensConfiguration, False),
        'HealthCheck': (HealthCheck, False),
        'Hostname': (str, False),
        'Image': (str, False),
        'Interactive': (boolean, False),
        'Links': ([str], False),
        'LinuxParameters': (LinuxParameters, False),
        'LogConfiguration': (LogConfiguration, False),
        'Memory': (integer, False),
        'MemoryReservation': (integer, False),
        'MountPoints': ([MountPoint], False),
        'Name': (str, False),
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
        'User': (str, False),
        'VolumesFrom': ([VolumesFrom], False),
        'WorkingDirectory': (str, False),
    }


class Host(AWSProperty):
    props = {
        'SourcePath': (str, False),
    }


class DockerVolumeConfiguration(AWSProperty):
    props = {
        'Autoprovision': (boolean, False),
        'Driver': (str, False),
        'DriverOpts': (dict, False),
        'Labels': (dict, False),
        'Scope': (scope_validator, False)
    }


class AuthorizationConfig(AWSProperty):
    props = {
        'AccessPointId': (str, False),
        'IAM': (str, False)
    }


class EFSVolumeConfiguration(AWSProperty):
    props = {
        'AuthorizationConfig': (AuthorizationConfig, False),
        'FilesystemId': (str, True),
        'RootDirectory': (str, False),
        'TransitEncryption': (ecs_efs_encryption_status, False),
        'TransitEncryptionPort': (integer_range(1, (2 ** 16) - 1), False)
    }


class Volume(AWSProperty):
    props = {
        'DockerVolumeConfiguration': (DockerVolumeConfiguration, False),
        'Name': (str, True),
        'Host': (Host, False),
        'EFSVolumeConfiguration': (EFSVolumeConfiguration, False)
    }


class InferenceAccelerator(AWSProperty):
    props = {
        'DeviceName': (str, False),
        'DeviceType': (str, False),
    }


class ProxyConfiguration(AWSProperty):
    props = {
        'ContainerName': (str, True),
        'ProxyConfigurationProperties': (list, False),
        'Type': (ecs_proxy_type, False)
    }


class TaskDefinition(AWSObject):
    resource_type = "AWS::ECS::TaskDefinition"

    props = {
        'ContainerDefinitions': ([ContainerDefinition], False),
        'Cpu': (str, False),
        'ExecutionRoleArn': (str, False),
        'Family': (str, False),
        'InferenceAccelerators': ([InferenceAccelerator], False),
        'IpcMode': (str, False),
        'Memory': (str, False),
        'NetworkMode': (str, False),
        'PidMode': (str, False),
        'PlacementConstraints': ([PlacementConstraint], False),
        'ProxyConfiguration': (ProxyConfiguration, False),
        'RequiresCompatibilities': ([str], False),
        'Tags': (Tags, False),
        'TaskRoleArn': (str, False),
        'Volumes': ([Volume], False),
    }


class Scale(AWSProperty):
    props = {
        'Unit': (str, False),
        'Value': (double, False),
    }


class TaskSet(AWSObject):
    resource_type = "AWS::ECS::TaskSet"

    props = {
        'Cluster': (str, True),
        'ExternalId': (str, False),
        'LaunchType': (str, False),
        'LoadBalancers': ([LoadBalancer], False),
        'NetworkConfiguration': (NetworkConfiguration, False),
        'PlatformVersion': (str, False),
        'Scale': (Scale, False),
        'Service': (str, True),
        'ServiceRegistries': ([ServiceRegistry], False),
        'TaskDefinition': (str, True),
    }
