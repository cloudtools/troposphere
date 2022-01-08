# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def accelerator_ipaddresstype(type):
    """
    Property: Accelerator.IpAddressType
    """

    valid_types = ["IPV4"]
    if type not in valid_types:
        raise ValueError(
            'IpAddressType must be one of: "%s"' % (", ".join(valid_types))
        )
    return type


def endpointgroup_healthcheckprotocol(protocol):
    """
    Property: EndpointGroup.HealthCheckProtocol
    """

    valid_protocols = ["HTTP", "HTTPS", "TCP"]
    if protocol not in valid_protocols:
        raise ValueError(
            'HealthCheckProtocol must be one of: "%s"' % (", ".join(valid_protocols))
        )
    return protocol


def listener_clientaffinity(affinity):
    """
    Property: Listener.ClientAffinity
    """
    valid_affinities = ["NONE", "SOURCE_IP"]
    if affinity not in valid_affinities:
        raise ValueError(
            'ClientAffinity must be one of: "%s"' % (", ".join(valid_affinities))
        )
    return affinity


def listener_protocol(protocol):
    """
    Property: Listener.Protocol
    """
    valid_protocols = ["TCP", "UDP"]
    if protocol not in valid_protocols:
        raise ValueError('Protocol must be one of: "%s"' % (", ".join(valid_protocols)))
    return protocol
