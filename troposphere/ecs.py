from . import AWSObject, AWSProperty, Ref
from .validators import (
    boolean, network_port, positive_integer, protocol, ulimit, integer
)


class Cluster(AWSObject):
    resource_type = "AWS::ECS::Cluster"

    props = {}


class LoadBalancer(AWSProperty):
    props = {
        'ContainerName': (basestring, False),
        'ContainerPort': (network_port, False),
        'LoadBalancerName': ([basestring, Ref], False),
    }


class Service(AWSObject):
    resource_type = "AWS::ECS::Service"

    props = {
        'Cluster': (basestring, False),
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
        'Protocol': (protocol, False)
    }


class VolumesFrom(AWSProperty):
    props = {
        'SourceContainer': (basestring, True),
        'ReadOnly': (boolean, False),
    }


class ExtraHost(AWSProperty):
    props = {
        'Hostname': (basestring, True),
        'IpAddress': (basestring, True),
    }


class ULimit(AWSProperty):
    props = {
        "Name": (ulimit, True),
        "SoftLimit": (integer, True),
        "HardLimit": (integer, True),
    }


class ContainerDefinition(AWSProperty):
    props = {
        'Command': ([basestring], False),
        'Cpu': (positive_integer, False),
        'DisableNetworking': (boolean, False),
        'DnsSearchDomains': ([basestring], False),
        'DnsServers': ([basestring], False),
        'DockerSecurityOptions': ([basestring], False),
        'EntryPoint': ([basestring], False),
        'Environment': ([Environment], False),
        'ExtraHosts': ([ExtraHost], False),
        'Essential': (boolean, False),
        'Hostname': (basestring, False),
        'Image': (basestring, True),
        'Links': ([basestring], False),
        'Memory': (positive_integer, True),
        'MountPoints': ([MountPoint], False),
        'Name': (basestring, True),
        'PortMappings': ([PortMapping], False),
        'Privileged': (boolean, False),
        'ReadonlyRootFilesystem': (boolean, False),
        'User': (basestring, False),
        'ULimits': ([ULimit], False),
        'VolumesFrom': ([VolumesFrom], False),
        'Workingdirectory': (basestring, False),
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
        'Volumes': ([Volume], True),
    }
