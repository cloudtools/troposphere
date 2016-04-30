from . import AWSObject, AWSProperty
from .validators import boolean, network_port, positive_integer


class Cluster(AWSObject):
    resource_type = "AWS::ECS::Cluster"

    props = {}


class LoadBalancer(AWSProperty):
    props = {
        'ContainerName': (basestring, False),
        'ContainerPort': (network_port, False),
        'LoadBalancerName': (basestring, False),
    }


class DeploymentConfiguration(AWSProperty):
    props = {
        'MaximumPercent': (positive_integer, False),
        'MinimumHealthyPercent': (positive_integer, False),
    }


class Service(AWSObject):
    resource_type = "AWS::ECS::Service"

    props = {
        'Cluster': (basestring, False),
        'DeploymentConfiguration': (DeploymentConfiguration, False),
        'DesiredCount': (positive_integer, False),
        'LoadBalancers': ([LoadBalancer], False),
        'Role': (basestring, False),
        'TaskDefinition': (basestring, False),
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


class LogConfiguration(AWSProperty):
    props = {
        'LogDriver': (basestring, True),
        'Options': (dict, False),
    }


class Ulimit(AWSProperty):
    props = {
        'HardLimit': (positive_integer, True),
        'Name': (basestring, False),
        'SoftLimit': (positive_integer, True),
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
        'LogConfiguration': (LogConfiguration, False),
        'Memory': (positive_integer, True),
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
        'Volumes': ([Volume], False),
    }
