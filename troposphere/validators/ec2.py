# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import re

from .. import AWSProperty
from ..compat import validate_policytype
from ..type_defs.compat import Final
from . import exactly_one, integer_range, network_port, tags_or_list

PERMISSION_INSTANCE_ATTACH: Final[str] = "INSTANCE-ATTACH"
PERMISSION_EIP_ASSOCIATE: Final[str] = "EIP-ASSOCIATE"

NO_DEVICE: dict = {}


def Ipv6Addresses(ipv6_address):
    """
    Export:
    """
    from ..ec2 import InstanceIpv6Address

    return InstanceIpv6Address(Ipv6Address=ipv6_address)


class Tag(AWSProperty):
    """
    Export:
    """

    props = {
        "Key": (str, True),
        "Value": (str, True),
    }

    def __init__(self, key=None, value=None, **kwargs):
        # provided for backward compatibility
        if key is not None:
            kwargs["Key"] = key
        if value is not None:
            kwargs["Value"] = value
        super().__init__(**kwargs)


def validate_int_to_str(x):
    """
    Backward compatibility - field was int and now str.
    Property: NetworkInterfaceProperty.DeviceIndex
    Property: NetworkInterfaceAttachment.DeviceIndex
    """

    if isinstance(x, int):
        return str(x)
    if isinstance(x, str):
        return str(int(x))

    raise TypeError(f"Value {x} of type {type(x)} must be either int or str")


def policytypes(policy):
    """
    Property: VPCEndpoint.PolicyDocument
    """
    return validate_policytype(policy)


def validate_networkaclentry_rulenumber(x):
    """
    Property: NetworkAclEntry.RuleNumber
    """
    return integer_range(1, 32766)(x)


def validate_network_port(x):
    """
    Property: NetworkAclEntry.Protocol
    Property: PortRange.From
    Property: PortRange.To
    Property: SecurityGroupRule.FromPort
    Property: SecurityGroupRule.ToPort
    Property: SecurityGroupEgress.FromPort
    Property: SecurityGroupEgress.ToPort
    Property: SecurityGroupIngress.FromPort
    Property: SecurityGroupIngress.ToPort
    """
    return network_port(x)


def validate_tags_or_list(x):
    """
    Property: TagSpecifications.Tags
    Property: CustomerGateway.Tags
    Property: DHCPOptions.Tags
    Property: Instance.Tags
    Property: InternetGateway.Tags
    Property: LocalGatewayRouteTableVPCAssociation.Tags
    Property: NatGateway.Tags
    Property: NetworkAcl.Tags
    Property: NetworkInterface.Tags
    Property: RouteTable.Tags
    Property: SecurityGroup.Tags
    Property: SpotFleetTagSpecification.Tags
    Property: Subnet.Tags
    Property: TransitGateway.Tags
    Property: TransitGatewayAttachment.Tags
    Property: TransitGatewayRouteTable.Tags
    Property: VPC.Tags
    Property: VPCPeeringConnection.Tags
    Property: VPNConnection.Tags
    Property: VPNGateway.Tags
    Property: Volume.Tags
    Property: VPNGateway.Tags
    Property: VPNGateway.Tags
    """
    return tags_or_list(x)


def instance_tenancy(value):
    """
    Property: VPC.InstanceTenancy
    """
    valid = ["default", "dedicated"]
    if value not in valid:
        raise ValueError("InstanceTenancy needs to be one of %r" % valid)
    return value


def check_ports(props):
    # IpProtocol is a required field but not all values allowed require
    # ToPort and FromPort. The ones that don't need these ports are:
    ports_optional = [
        "-1",  # all protocols
        "58",  # ICMPv6
    ]
    proto = props["IpProtocol"]

    if proto not in ports_optional:
        if not ("ToPort" in props and "FromPort" in props):
            raise ValueError("ToPort/FromPort must be specified for proto %s" % proto)


def validate_elasticinferenceaccelerator_type(elasticinferenceaccelerator_type):
    """
    Validate ElasticInferenceAccelerator for Instance
    Property: ElasticInferenceAccelerator.Type
    Property: LaunchTemplateElasticInferenceAccelerator.Type
    """

    VALID_ELASTICINFERENCEACCELERATOR_TYPES = (
        "eia1.medium",
        "eia1.large",
        "eia1.xlarge",
    )
    if elasticinferenceaccelerator_type not in VALID_ELASTICINFERENCEACCELERATOR_TYPES:
        raise ValueError(
            "Elastic Inference Accelerator Type must be one of: %s"
            % ", ".join(VALID_ELASTICINFERENCEACCELERATOR_TYPES)
        )
    return elasticinferenceaccelerator_type


def validate_clientvpnendpoint_selfserviceportal(value):
    """
    Validate SelfServicePortal for ClientVpnEndpoint.
    Property: ClientVpnEndpoint.SelfServicePortal
    """

    VALID_CLIENTVPNENDPOINT_SELFSERVICEPORTAL = ("disabled", "enabled")

    if value not in VALID_CLIENTVPNENDPOINT_SELFSERVICEPORTAL:
        raise ValueError(
            "ClientVpnEndpoint.SelfServicePortal must be one of: {}".format(
                ", ".join(VALID_CLIENTVPNENDPOINT_SELFSERVICEPORTAL)
            )
        )
    return value


def validate_clientvpnendpoint_vpnport(vpnport):
    """
    Validate VpnPort for ClientVpnEndpoint
    Property: ClientVpnEndpoint.VpnPort
    """

    VALID_CLIENTVPNENDPOINT_VPNPORT = (443, 1194)
    if vpnport not in VALID_CLIENTVPNENDPOINT_VPNPORT:
        raise ValueError(
            "ClientVpnEndpoint VpnPort must be one of: %s"
            % ", ".join(map(str, VALID_CLIENTVPNENDPOINT_VPNPORT))
        )
    return vpnport


def vpn_pre_shared_key(key):
    """
    Property: VpnTunnelOptionsSpecification.PreSharedKey
    """
    pre_shared_key_match_re = re.compile(r"^(?!0)([A-Za-z0-9]|\_|\.){8,64}$")
    if not pre_shared_key_match_re.match(key):
        raise ValueError(
            "%s is not a valid key."
            " Allowed characters are alphanumeric characters and ._. Must"
            " be between 8 and 64 characters in length and cannot"
            " start with zero (0)." % key
        )
    return key


def vpn_tunnel_inside_cidr(cidr):
    """
    Property: VpnTunnelOptionsSpecification.TunnelInsideCidr
    """
    reserved_cidrs = [
        "169.254.0.0/30",
        "169.254.1.0/30",
        "169.254.2.0/30",
        "169.254.3.0/30",
        "169.254.4.0/30",
        "169.254.5.0/30",
        "169.254.169.252/30",
    ]
    cidr_match_re = re.compile(
        r"^169\.254\.(?:25[0-5]|2[0-4]\d|[01]?\d\d?)"
        r"\.(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\/30$"
    )
    if cidr in reserved_cidrs:
        raise ValueError(
            'The following CIDR blocks are reserved and cannot be used: "%s"'
            % (", ".join(reserved_cidrs))
        )
    elif not cidr_match_re.match(cidr):
        raise ValueError(
            "%s is not a valid CIDR."
            " A size /30 CIDR block from the 169.254.0.0/16 must be specified." % cidr
        )
    return cidr


def vpc_endpoint_type(endpoint_type):
    """
    Property: VPCEndpoint.VpcEndpointType
    """
    valid_types = ["Interface", "Gateway", "GatewayLoadBalancer"]
    if endpoint_type not in valid_types:
        raise ValueError(
            'VpcEndpointType must be one of: "%s"' % (", ".join(valid_types))
        )
    return endpoint_type


def validate_network_acl_entry(self):
    """
    Class: NetworkAclEntry
    """
    conds = [
        "CidrBlock",
        "Ipv6CidrBlock",
    ]
    exactly_one(self.__class__.__name__, self.properties, conds)


def validate_route(self):
    """
    Class: Route
    """
    cidr_conds = [
        "DestinationCidrBlock",
        "DestinationIpv6CidrBlock",
        "DestinationPrefixListId",
    ]
    gateway_conds = [
        "CarrierGatewayId",
        "CoreNetworkArn",
        "EgressOnlyInternetGatewayId",
        "GatewayId",
        "InstanceId",
        "LocalGatewayId",
        "NatGatewayId",
        "NetworkInterfaceId",
        "TransitGatewayId",
        "VpcEndpointId",
        "VpcPeeringConnectionId",
    ]
    exactly_one(self.__class__.__name__, self.properties, cidr_conds)
    exactly_one(self.__class__.__name__, self.properties, gateway_conds)


def validate_security_group_egress(self):
    """
    Class: SecurityGroupEgress
    """
    conds = [
        "CidrIp",
        "CidrIpv6",
        "DestinationPrefixListId",
        "DestinationSecurityGroupId",
    ]
    exactly_one(self.__class__.__name__, self.properties, conds)
    check_ports(self.properties)


def validate_security_group_ingress(self):
    """
    Class: SecurityGroupIngress
    """
    conds = [
        "CidrIp",
        "CidrIpv6",
        "SourcePrefixListId",
        "SourceSecurityGroupName",
        "SourceSecurityGroupId",
    ]
    exactly_one(self.__class__.__name__, self.properties, conds)
    check_ports(self.properties)


def validate_spot_fleet_request_config_data(self):
    """
    Class: SpotFleetRequestConfigData
    """
    conds = ["LaunchSpecifications", "LaunchTemplateConfigs"]
    exactly_one(self.__class__.__name__, self.properties, conds)


def validate_subnet(self):
    """
    Class: Subnet
    """
    if self.properties.get("AssignIpv6AddressOnCreation"):
        if "Ipv6CidrBlock" not in self.properties:
            raise ValueError(
                "If AssignIpv6AddressOnCreation is set to True, "
                "Ipv6CidrBlock must be present"
            )


def validate_vpn_connection(self):
    """
    Class: VPNConnection
    """
    conds = [
        "VpnGatewayId",
        "TransitGatewayId",
    ]
    exactly_one(self.__class__.__name__, self.properties, conds)


def validate_placement_strategy(strategy):
    """
    Validate PlacementGroup Strategy
    Property: PlacementGroup.Strategy
    """

    VALID_PLACEMENT_STRATEGIES = ["cluster", "partition", "spread"]

    if strategy not in VALID_PLACEMENT_STRATEGIES:
        raise ValueError(
            "PlacementGroup Strategy must be one of: %s"
            % ", ".join(VALID_PLACEMENT_STRATEGIES)
        )
    return strategy


def validate_placement_spread_level(spread_level):
    """
    Validate PlacementGroup SpreadLevel
    Property: PlacementGroup.SpreadLevel
    """

    VALID_PLACEMENT_SPREAD_LEVEL = [
        "host",
        "rack",
    ]

    if spread_level not in VALID_PLACEMENT_SPREAD_LEVEL:
        raise ValueError(
            "PlacementGroup SpreadLevel must be one of: %s"
            % ", ".join(VALID_PLACEMENT_SPREAD_LEVEL)
        )
    return spread_level
