from . import AWSObject, AWSProperty
from .validators import boolean, integer, network_port, positive_integer


LAUNCH_TYPE_EC2 = 'EC2'
LAUNCH_TYPE_FARGATE = 'FARGATE'


class Cluster(AWSObject):
    resource_type = "AWS::ECS::Cluster"

    props = {
        'ClusterName': (basestring, False),
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


class Service(AWSObject):
    resource_type = "AWS::ECS::Service"

    props = {
        'Cluster': (basestring, False),
        'DeploymentConfiguration': (DeploymentConfiguration, False),
        'DesiredCount': (positive_integer, False),
        'HealthCheckGracePeriodSeconds': (positive_integer, False),
        'LaunchType': (launch_type_validator, False),
        'LoadBalancers': ([LoadBalancer], False),
        'NetworkConfiguration': (NetworkConfiguration, False),
        'Role': (basestring, False),
        'PlacementConstraints': ([PlacementConstraint], False),
        'PlacementStrategies': ([PlacementStrategy], False),
        'PlatformVersion': (basestring, False),
        'ServiceName': (basestring, False),
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


class KernelCapabilities(AWSProperty):
    props = {
        'Add': ([basestring], False),
        'Drop': ([basestring], False),
    }


class LinuxParameters(AWSProperty):
    props = {
        'Capabilities': (KernelCapabilities, False),
        'Devices': ([Device], False),
        'InitProcessEnabled': (boolean, False),
    }


class LogConfiguration(AWSProperty):
    props = {
        'LogDriver': (basestring, True),
        'Options': (dict, False),
    }


class Ulimit(AWSProperty):
    props = {
        'HardLimit': (integer, True),
        'Name': (basestring, False),
        'SoftLimit': (integer, True),
    }


class ContainerDefinition(AWSProperty):
    props = {
        'Command': ([basestring], False),
        'Cpu': (positive_integer, False),
        'DisableNetworking': (boolean, False),
        'DnsSearchDomains': ([basestring], False),
        'DnsServers': ([basestring], False),
        'DockerLabels': (dict, False),
        'DockerSecurityOptions': ([basestring], False),
        'EntryPoint': ([basestring], False),
        'Environment': ([Environment], False),
        'Essential': (boolean, False),
        'ExtraHosts': ([HostEntry], False),
        'Hostname': (basestring, False),
        'Image': (basestring, True),
        'Links': ([basestring], False),
        'LinuxParameters': (LinuxParameters, False),
        'LogConfiguration': (LogConfiguration, False),
        'Memory': (positive_integer, False),
        'MemoryReservation': (positive_integer, False),
        'MountPoints': ([MountPoint], False),
        'Name': (basestring, True),
        'PortMappings': ([PortMapping], False),
        'Privileged': (boolean, False),
        'ReadonlyRootFilesystem': (boolean, False),
        'Ulimits': ([Ulimit], False),
        'User': (basestring, False),
        'VolumesFrom': ([VolumesFrom], False),
        'WorkingDirectory': (basestring, False),
    }


class Host(AWSProperty):
    props = {
        'SourcePath': (basestring, False),
    }


class Volume(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Host': (Host, False),
    }


class TaskDefinition(AWSObject):
    resource_type = "AWS::ECS::TaskDefinition"

    props = {
        'ContainerDefinitions': ([ContainerDefinition], True),
        'Cpu': (basestring, False),
        'ExecutionRoleArn': (basestring, False),
        'Family': (basestring, False),
        'Memory': (basestring, False),
        'NetworkMode': (basestring, False),
        'PlacementConstraints': ([PlacementConstraint], False),
        'RequiresCompatibilities': ([basestring], False),
        'TaskRoleArn': (basestring, False),
        'Volumes': ([Volume], False),
    }
