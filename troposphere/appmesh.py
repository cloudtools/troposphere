# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import integer


class VirtualNodeServiceProvider(AWSProperty):
    props = {
        'VirtualNodeName': (basestring, True),
    }


class VirtualRouterServiceProvider(AWSProperty):
    props = {
        'VirtualRouterName': (basestring, True),
    }


class VirtualServiceProvider(AWSProperty):
    props = {
        'VirtualNode': (VirtualNodeServiceProvider, False),
        'VirtualRouter': (VirtualRouterServiceProvider, False),
    }


class VirtualServiceSpec(AWSProperty):
    props = {
        'Provider': (VirtualServiceProvider, False),
    }


class TagRef(AWSProperty):
    props = {
        'Key': (basestring, True),
        'Value': (basestring, False),
    }


class VirtualService(AWSObject):
    resource_type = "AWS::AppMesh::VirtualService"

    props = {
        'MeshName': (basestring, True),
        'Spec': (VirtualServiceSpec, True),
        'Tags': ([TagRef], False),
        'VirtualServiceName': (basestring, True),
    }


class HealthCheck(AWSProperty):
    props = {
        'HealthyThreshold': (integer, True),
        'IntervalMillis': (integer, True),
        'Path': (basestring, False),
        'Port': (integer, False),
        'Protocol': (basestring, True),
        'TimeoutMillis': (integer, True),
        'UnhealthyThreshold': (integer, True),
    }


class PortMapping(AWSProperty):
    props = {
        'Port': (integer, True),
        'Protocol': (basestring, True),
    }


class Listener(AWSProperty):
    props = {
        'HealthCheck': (HealthCheck, False),
        'PortMapping': (PortMapping, True),
    }


class DnsServiceDiscovery(AWSProperty):
    props = {
        'Hostname': (basestring, True),
    }


class ServiceDiscovery(AWSProperty):
    props = {
        'DNS': (DnsServiceDiscovery, True),
    }


class FileAccessLog(AWSProperty):
    props = {
        'Path': (basestring, True),
    }


class AccessLog(AWSProperty):
    props = {
        'File': (FileAccessLog, False),
    }


class Logging(AWSProperty):
    props = {
        'AccessLog': (AccessLog, False),
    }


class VirtualServiceBackend(AWSProperty):
    props = {
        'VirtualServiceName': (basestring, True),
    }


class Backend(AWSProperty):
    props = {
        'VirtualService': (VirtualServiceBackend, False),
    }


class VirtualNodeSpec(AWSProperty):
    props = {
        'Backends': ([Backend], False),
        'Listeners': ([Listener], False),
        'Logging': (Logging, False),
        'ServiceDiscovery': (ServiceDiscovery, False),
    }


class VirtualNode(AWSObject):
    resource_type = "AWS::AppMesh::VirtualNode"

    props = {
        'MeshName': (basestring, True),
        'Spec': (VirtualNodeSpec, True),
        'Tags': ([TagRef], False),
        'VirtualNodeName': (basestring, True),
    }


class WeightedTarget(AWSProperty):
    props = {
        'VirtualNode': (basestring, True),
        'Weight': (integer, True),
    }


class HttpRouteAction(AWSProperty):
    props = {
        'WeightedTargets': ([WeightedTarget], True),
    }


class HttpRouteMatch(AWSProperty):
    props = {
        'Prefix': (basestring, True),
    }


class HttpRoute(AWSProperty):
    props = {
        'Action': (HttpRouteAction, True),
        'Match': (HttpRouteMatch, True),
    }


class TcpRouteAction(AWSProperty):
    props = {
        'WeightedTargets': ([WeightedTarget], True),
    }


class TcpRoute(AWSProperty):
    props = {
        'Action': (TcpRouteAction, True),
    }


class RouteSpec(AWSProperty):
    props = {
        'HttpRoute': (HttpRoute, False),
        'TcpRoute': (TcpRoute, False),
    }


class Route(AWSObject):
    resource_type = "AWS::AppMesh::Route"

    props = {
        'MeshName': (basestring, True),
        'RouteName': (basestring, True),
        'Spec': (RouteSpec, True),
        'Tags': ([TagRef], False),
        'VirtualRouterName': (basestring, True),
    }


class EgressFilter(AWSProperty):
    props = {
        'Type': (basestring, True),
    }


class MeshSpec(AWSProperty):
    props = {
        'EgressFilter': (EgressFilter, False),
    }


class Mesh(AWSObject):
    resource_type = "AWS::AppMesh::Mesh"

    props = {
        'MeshName': (basestring, True),
        'Spec': (MeshSpec, False),
        'Tags': ([TagRef], False),
    }
