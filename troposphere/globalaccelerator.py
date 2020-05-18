# Copyright (c) 2012-2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import AWSObject, AWSProperty
from troposphere import Tags
from .validators import (boolean, integer, double, accelerator_ipaddresstype,
                         listener_clientaffinity, listener_protocol,
                         endpointgroup_healthcheckprotocol)


class Accelerator(AWSObject):
    resource_type = "AWS::GlobalAccelerator::Accelerator"

    props = {
        'Enabled': (boolean, False),
        'IpAddresses': ([basestring], False),
        'IpAddressType': (accelerator_ipaddresstype, False),
        'Name': (basestring, True),
        'Tags': (Tags, False),
    }


class PortRange(AWSProperty):
    props = {
        'FromPort': (integer, True),
        'ToPort': (integer, True),
    }


class Listener(AWSObject):
    resource_type = "AWS::GlobalAccelerator::Listener"

    props = {
        'AcceleratorArn': (basestring, True),
        'ClientAffinity': (listener_clientaffinity, False),
        'PortRanges': ([PortRange], True),
        'Protocol': (listener_protocol, False),
    }


class EndpointConfiguration(AWSProperty):
    props = {
        'ClientIPPreservationEnabled': (boolean, False),
        'EndpointId': (basestring, True),
        'Weight': (integer, False),
    }


class EndpointGroup(AWSObject):
    resource_type = "AWS::GlobalAccelerator::EndpointGroup"

    props = {
        'EndpointConfigurations': ([EndpointConfiguration], False),
        'EndpointGroupRegion': (basestring, True),
        'HealthCheckIntervalSeconds': (integer, False),
        'HealthCheckPath': (basestring, False),
        'HealthCheckPort': (integer, False),
        'HealthCheckProtocol': (endpointgroup_healthcheckprotocol, False),
        'ListenerArn': (basestring, True),
        'ThresholdCount': (integer, False),
        'TrafficDialPercentage': (double, False),
    }
