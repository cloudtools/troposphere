# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags


class Instance(AWSObject):
    resource_type = "AWS::ServiceDiscovery::Instance"

    props = {
        'InstanceAttributes': (dict, True),
        'InstanceId': (str, False),
        'ServiceId': (str, True),
    }


class PrivateDnsNamespace(AWSObject):
    resource_type = "AWS::ServiceDiscovery::PrivateDnsNamespace"

    props = {
        'Description': (str, False),
        'Name': (str, True),
        'Tags': (Tags, False),
        'Vpc': (str, True),
    }


class PublicDnsNamespace(AWSObject):
    resource_type = "AWS::ServiceDiscovery::PublicDnsNamespace"

    props = {
        'Description': (str, False),
        'Name': (str, True),
        'Tags': (Tags, False),
    }


class HealthCheckConfig(AWSProperty):
    props = {
        'FailureThreshold': (float, False),
        'ResourcePath': (str, False),
        'Type': (str, True),
    }


class HealthCheckCustomConfig(AWSProperty):
    props = {
        'FailureThreshold': (float, True)
    }


class DnsRecord(AWSProperty):
    props = {
        'TTL': (str, True),
        'Type': (str, True),
    }


class DnsConfig(AWSProperty):
    props = {
        'DnsRecords': ([DnsRecord], True),
        'NamespaceId': (str, False),
        'RoutingPolicy': (str, False),
    }


class Service(AWSObject):
    resource_type = "AWS::ServiceDiscovery::Service"

    props = {
        'Description': (str, False),
        'DnsConfig': (DnsConfig, False),
        'HealthCheckConfig': (HealthCheckConfig, False),
        'HealthCheckCustomConfig': (HealthCheckCustomConfig, False),
        'Name': (str, False),
        'NamespaceId': (str, False),
        'Tags': (Tags, False),
    }


class HttpNamespace(AWSObject):
    resource_type = "AWS::ServiceDiscovery::HttpNamespace"

    props = {
        'Description': (str, False),
        'Name': (str, True),
        'Tags': (Tags, False),
    }
