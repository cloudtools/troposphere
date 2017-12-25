# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty


class Instance(AWSObject):
    resource_type = "AWS::ServiceDiscovery::Instance"

    props = {
        'InstanceAttributes': (dict, True),
        'InstanceId': (basestring, False),
        'ServiceId': (basestring, True),
    }


class PrivateDnsNamespace(AWSObject):
    resource_type = "AWS::ServiceDiscovery::PrivateDnsNamespace"

    props = {
        'Description': (basestring, False),
        'Name': (basestring, True),
        'Vpc': (basestring, True),
    }


class PublicDnsNamespace(AWSObject):
    resource_type = "AWS::ServiceDiscovery::PublicDnsNamespace"

    props = {
        'Description': (basestring, False),
        'Name': (basestring, True),
    }


class HealthCheckConfig(AWSProperty):
    props = {
        'FailureThreshold': (float, False),
        'ResourcePath': (basestring, False),
        'Type': (basestring, True),
    }


class DnsRecord(AWSProperty):
    props = {
        'TTL': (basestring, True),
        'Type': (basestring, True),
    }


class DnsConfig(AWSProperty):
    props = {
        'DnsRecords': ([DnsRecord], True),
        'NamespaceId': (basestring, True),
    }


class Service(AWSObject):
    resource_type = "AWS::ServiceDiscovery::Service"

    props = {
        'Description': (basestring, False),
        'DnsConfig': (DnsConfig, True),
        'HealthCheckConfig': (HealthCheckConfig, False),
        'Name': (basestring, False),
    }
