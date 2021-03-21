# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty, Tags
from .compat import policytypes
from .validators import (
    boolean, exactly_one, integer, integer_range, double,
    network_port, positive_integer, vpn_pre_shared_key, vpn_tunnel_inside_cidr,
    vpc_endpoint_type
)

VALID_ELASTICINFERENCEACCELERATOR_TYPES = ('eia1.medium', 'eia1.large',
                                           'eia1.xlarge')
VALID_CLIENTVPNENDPOINT_SELFSERVICEPORTAL = ('disabled', 'enabled')
VALID_CLIENTVPNENDPOINT_VPNPORT = (443, 1194)


def validate_elasticinferenceaccelerator_type(
        elasticinferenceaccelerator_type):
    """Validate ElasticInferenceAccelerator for Instance"""

    if elasticinferenceaccelerator_type not in VALID_ELASTICINFERENCEACCELERATOR_TYPES:  # NOQA
        raise ValueError("Elastic Inference Accelerator Type must be one of: %s" %  # NOQA
                         ", ".join(VALID_ELASTICINFERENCEACCELERATOR_TYPES))
    return elasticinferenceaccelerator_type


def validate_clientvpnendpoint_selfserviceportal(value):
    """Validate SelfServicePortal for ClientVpnEndpoint."""
    if value not in VALID_CLIENTVPNENDPOINT_SELFSERVICEPORTAL:
        raise ValueError(
            "ClientVpnEndpoint.SelfServicePortal must be one of: {}".format(
                ", ".join(VALID_CLIENTVPNENDPOINT_SELFSERVICEPORTAL)
            )
        )
    return value


def validate_clientvpnendpoint_vpnport(vpnport):
    """Validate VpnPort for ClientVpnEndpoint"""

    if vpnport not in VALID_CLIENTVPNENDPOINT_VPNPORT:
        raise ValueError("ClientVpnEndpoint VpnPort must be one of: %s" %  # NOQA
                         ", ".join(VALID_CLIENTVPNENDPOINT_VPNPORT))
    return vpnport


class Tag(AWSProperty):
    props = {
        'Key': (str, True),
        'Value': (str, True)
    }

    def __init__(self, key=None, value=None, **kwargs):
        # provided for backward compatibility
        if key is not None:
            kwargs['Key'] = key
        if value is not None:
            kwargs['Value'] = value
        super(Tag, self).__init__(**kwargs)


class CarrierGateway(AWSObject):
    resource_type = "AWS::EC2::CarrierGateway"

    props = {
        'Tags': (Tags, False),
        'VpcId': (str, True),
    }


class CustomerGateway(AWSObject):
    resource_type = "AWS::EC2::CustomerGateway"

    props = {
        'BgpAsn': (integer, True),
        'IpAddress': (str, True),
        'Tags': ((Tags, list), False),
        'Type': (str, True),
    }


class DHCPOptions(AWSObject):
    resource_type = "AWS::EC2::DHCPOptions"

    props = {
        'DomainName': (str, False),
        'DomainNameServers': (list, False),
        'NetbiosNameServers': (list, False),
        'NetbiosNodeType': (integer, False),
        'NtpServers': (list, False),
        'Tags': ((Tags, list), False),
    }


class EgressOnlyInternetGateway(AWSObject):
    resource_type = "AWS::EC2::EgressOnlyInternetGateway"

    props = {
        'VpcId': (str, True),
    }


class EIP(AWSObject):
    resource_type = "AWS::EC2::EIP"

    props = {
        'InstanceId': (str, False),
        'Domain': (str, False),
        'PublicIpv4Pool': (str, False),
        'Tags': (Tags, False),
    }


class EIPAssociation(AWSObject):
    resource_type = "AWS::EC2::EIPAssociation"

    props = {
        'AllocationId': (str, False),
        'EIP': (str, False),
        'InstanceId': (str, False),
        'NetworkInterfaceId': (str, False),
        'PrivateIpAddress': (str, False),
    }


class FlowLog(AWSObject):
    resource_type = "AWS::EC2::FlowLog"

    props = {
        'DeliverLogsPermissionArn': (str, False),
        'LogDestination': (str, False),
        'LogDestinationType': (str, False),
        'LogFormat': (str, False),
        'LogGroupName': (str, False),
        'MaxAggregationInterval': (integer, False),
        'ResourceId': (str, True),
        'ResourceType': (str, True),
        'Tags': (Tags, False),
        'TrafficType': (str, True),
    }


class NatGateway(AWSObject):
    resource_type = "AWS::EC2::NatGateway"

    props = {
        'AllocationId': (str, True),
        'SubnetId': (str, True),
        'Tags': ((Tags, list), False),
    }


class EBSBlockDevice(AWSProperty):
    props = {
        'DeleteOnTermination': (boolean, False),
        'Encrypted': (boolean, False),
        'KmsKeyId': (str, False),
        'Iops': (integer, False),  # Conditional
        'Throughput': (integer, False),  # Conditional
        'SnapshotId': (str, False),  # Conditional
        'VolumeSize': (integer, False),  # Conditional
        'VolumeType': (str, False),
    }


NO_DEVICE = {}


class BlockDeviceMapping(AWSProperty):
    props = {
        'DeviceName': (str, True),
        'Ebs': (EBSBlockDevice, False),  # Conditional
        'VirtualName': (str, False),  # Conditional
        'NoDevice': (dict, False)
    }


class LaunchTemplateBlockDeviceMapping(AWSProperty):
    props = {
        'DeviceName': (str, True),
        'Ebs': (EBSBlockDevice, False),  # Conditional
        'VirtualName': (str, False),  # Conditional
        'NoDevice': (str, False)
    }


class MountPoint(AWSProperty):
    props = {
        'Device': (str, True),
        'VolumeId': (str, True),
    }


class Placement(AWSProperty):
    props = {
        'Affinity': (str, False),
        'AvailabilityZone': (str, False),
        'GroupName': (str, False),
        'HostId': (str, False),
        'HostResourceGroupArn': (str, False),
        'PartitionNumber': (integer, False),
        'Tenancy': (str, False)
    }


class CpuOptions(AWSProperty):
    props = {
        'CoreCount': (integer, False),
        'ThreadsPerCore': (integer, False),
    }


class CreditSpecification(AWSProperty):
    props = {
        'CPUCredits': (str, False),
    }


class ElasticGpuSpecification(AWSProperty):
    props = {
        'Type': (str, True),
    }


class Ipv6Addresses(AWSHelperFn):
    def __init__(self, address):
        self.data = {
            'Ipv6Address': address,
        }


class LaunchTemplateSpecification(AWSProperty):
    props = {
        'LaunchTemplateId': (str, False),
        'LaunchTemplateName': (str, False),
        'Version': (str, True),
    }


class NetworkInsightsAnalysis(AWSObject):
    resource_type = "AWS::EC2::NetworkInsightsAnalysis"

    props = {
        'FilterInArns': ([str], False),
        'NetworkInsightsPathId': (str, True),
        'Tags': (Tags, False),
    }


class NetworkInsightsPath(AWSObject):
    resource_type = "AWS::EC2::NetworkInsightsPath"

    props = {
        'Destination': (str, True),
        'DestinationIp': (str, False),
        'DestinationPort': (integer, False),
        'Protocol': (str, True),
        'Source': (str, True),
        'SourceIp': (str, False),
        'Tags': (Tags, False),
    }


class PrivateIpAddressSpecification(AWSProperty):
    props = {
        'Primary': (boolean, True),
        'PrivateIpAddress': (str, True),
    }


class NetworkInterfaceProperty(AWSProperty):
    props = {
        'AssociateCarrierIpAddress': (boolean, False),
        'AssociatePublicIpAddress': (boolean, False),
        'DeleteOnTermination': (boolean, False),
        'Description': (str, False),
        'DeviceIndex': (integer, True),
        'GroupSet': ([str], False),
        'Ipv6AddressCount': (integer, False),
        'Ipv6Addresses': ([Ipv6Addresses], False),
        'NetworkCardIndex': (integer, False),
        'NetworkInterfaceId': (str, False),
        'PrivateIpAddress': (str, False),
        'PrivateIpAddresses': ([PrivateIpAddressSpecification], False),
        'SecondaryPrivateIpAddressCount': (integer, False),
        'SubnetId': (str, False),
    }


class AssociationParameters(AWSProperty):
    props = {
        'Key': (str, True),
        'Value': ([str], True),
    }


class SsmAssociations(AWSProperty):
    props = {
        'AssociationParameters': ([AssociationParameters], False),
        'DocumentName': (str, True),
    }


class GatewayRouteTableAssociation(AWSObject):
    resource_type = "AWS::EC2::GatewayRouteTableAssociation"

    props = {
        'GatewayId': (str, True),
        'RouteTableId': (str, True),
    }


class Host(AWSObject):
    resource_type = "AWS::EC2::Host"

    props = {
        'AutoPlacement': (str, False),
        'AvailabilityZone': (str, True),
        'HostRecovery': (str, False),
        'InstanceType': (str, True),
    }


class ElasticInferenceAccelerator(AWSProperty):
    props = {
        'Count': (integer, False),
        'Type': (validate_elasticinferenceaccelerator_type, True),
    }


class LicenseSpecification(AWSProperty):
    props = {
        'LicenseConfigurationArn': (str, True),
    }


class EnclaveOptions(AWSProperty):
    props = {
        'Enabled': (boolean, False),
    }


class HibernationOptions(AWSProperty):
    props = {
        'Configured': (boolean, False),
    }


class Instance(AWSObject):
    resource_type = "AWS::EC2::Instance"

    props = {
        'Affinity': (str, False),
        'AvailabilityZone': (str, False),
        'BlockDeviceMappings': (list, False),
        'CpuOptions': (CpuOptions, False),
        'CreditSpecification': (CreditSpecification, False),
        'DisableApiTermination': (boolean, False),
        'EbsOptimized': (boolean, False),
        'ElasticGpuSpecifications': ([ElasticGpuSpecification], False),
        'ElasticInferenceAccelerators': ([ElasticInferenceAccelerator], False),
        'EnclaveOptions': (EnclaveOptions, False),
        'HibernationOptions': (HibernationOptions, False),
        'HostId': (str, False),
        'HostResourceGroupArn': (str, False),
        'IamInstanceProfile': (str, False),
        'ImageId': (str, False),
        'InstanceInitiatedShutdownBehavior': (str, False),
        'InstanceType': (str, False),
        'Ipv6AddressCount': (integer, False),
        'Ipv6Addresses': ([Ipv6Addresses], False),
        'KernelId': (str, False),
        'KeyName': (str, False),
        'LaunchTemplate': (LaunchTemplateSpecification, False),
        'LicenseSpecifications': ([LicenseSpecification], False),
        'Monitoring': (boolean, False),
        'NetworkInterfaces': ([NetworkInterfaceProperty], False),
        'PlacementGroupName': (str, False),
        'PrivateIpAddress': (str, False),
        'RamdiskId': (str, False),
        'SecurityGroupIds': (list, False),
        'SecurityGroups': (list, False),
        'SsmAssociations': ([SsmAssociations], False),
        'SourceDestCheck': (boolean, False),
        'SubnetId': (str, False),
        'Tags': ((Tags, list), False),
        'Tenancy': (str, False),
        'UserData': (str, False),
        'Volumes': (list, False),
    }


class InternetGateway(AWSObject):
    resource_type = "AWS::EC2::InternetGateway"

    props = {
        'Tags': ((Tags, list), False),
    }


class NetworkAcl(AWSObject):
    resource_type = "AWS::EC2::NetworkAcl"

    props = {
        'Tags': ((Tags, list), False),
        'VpcId': (str, True),
    }


class ICMP(AWSProperty):
    props = {
        'Code': (integer, False),
        'Type': (integer, False),
    }


class PortRange(AWSProperty):
    props = {
        'From': (network_port, False),
        'To': (network_port, False),
    }


class NetworkAclEntry(AWSObject):
    resource_type = "AWS::EC2::NetworkAclEntry"

    props = {
        'CidrBlock': (str, False),
        'Egress': (boolean, False),
        'Icmp': (ICMP, False),  # Conditional
        'Ipv6CidrBlock': (str, False),
        'NetworkAclId': (str, True),
        'PortRange': (PortRange, False),  # Conditional
        'Protocol': (network_port, True),
        'RuleAction': (str, True),
        'RuleNumber': (integer_range(1, 32766), True),
    }

    def validate(self):
        conds = [
            'CidrBlock',
            'Ipv6CidrBlock',
        ]
        exactly_one(self.__class__.__name__, self.properties, conds)


class NetworkInterface(AWSObject):
    resource_type = "AWS::EC2::NetworkInterface"

    props = {
        'Description': (str, False),
        'GroupSet': (list, False),
        'Ipv6AddressCount': (integer, False),
        'Ipv6Addresses': ([Ipv6Addresses], False),
        'PrivateIpAddress': (str, False),
        'PrivateIpAddresses': ([PrivateIpAddressSpecification], False),
        'SecondaryPrivateIpAddressCount': (integer, False),
        'SourceDestCheck': (boolean, False),
        'SubnetId': (str, True),
        'Tags': ((Tags, list), False),
    }


class NetworkInterfaceAttachment(AWSObject):
    resource_type = "AWS::EC2::NetworkInterfaceAttachment"

    props = {
        'DeleteOnTermination': (boolean, False),
        'DeviceIndex': (integer, True),
        'InstanceId': (str, True),
        'NetworkInterfaceId': (str, True),
    }


PERMISSION_INSTANCE_ATTACH = 'INSTANCE-ATTACH'
PERMISSION_EIP_ASSOCIATE = 'EIP-ASSOCIATE'


class NetworkInterfacePermission(AWSObject):
    resource_type = "AWS::EC2::NetworkInterfacePermission"

    props = {
        'AwsAccountId': (str, True),
        'NetworkInterfaceId': (str, True),
        'Permission': (str, True),
    }


class Entry(AWSProperty):
    props = {
        'Cidr': (str, True),
        'Description': (str, False),
    }


class PrefixList(AWSObject):
    resource_type = "AWS::EC2::PrefixList"

    props = {
        'AddressFamily': (str, True),
        'Entries': ([Entry], False),
        'MaxEntries': (integer, True),
        'PrefixListName': (str, True),
        'Tags': (Tags, False),
    }


class Route(AWSObject):
    resource_type = "AWS::EC2::Route"

    props = {
        'CarrierGatewayId': (str, False),
        'DestinationCidrBlock': (str, False),
        'DestinationIpv6CidrBlock': (str, False),
        'EgressOnlyInternetGatewayId': (str, False),
        'GatewayId': (str, False),
        'InstanceId': (str, False),
        'LocalGatewayId': (str, False),
        'NatGatewayId': (str, False),
        'NetworkInterfaceId': (str, False),
        'RouteTableId': (str, True),
        'TransitGatewayId': (str, False),
        'VpcEndpointId': (str, False),
        'VpcPeeringConnectionId': (str, False),
    }

    def validate(self):
        cidr_conds = [
            'DestinationCidrBlock',
            'DestinationIpv6CidrBlock',
        ]
        gateway_conds = [
            'CarrierGatewayId',
            'EgressOnlyInternetGatewayId',
            'GatewayId',
            'InstanceId',
            'LocalGatewayId',
            'NatGatewayId',
            'NetworkInterfaceId',
            'TransitGatewayId',
            'VpcEndpointId',
            'VpcPeeringConnectionId',
        ]
        exactly_one(self.__class__.__name__, self.properties, cidr_conds)
        exactly_one(self.__class__.__name__, self.properties, gateway_conds)


class RouteTable(AWSObject):
    resource_type = "AWS::EC2::RouteTable"

    props = {
        'Tags': ((Tags, list), False),
        'VpcId': (str, True),
    }


def check_ports(props):
    # IpProtocol is a required field but not all values allowed require
    # ToPort and FromPort. The ones that don't need these ports are:
    ports_optional = [
        "-1",  # all protocols
        "58",  # ICMPv6
    ]
    proto = props['IpProtocol']

    if proto not in ports_optional:
        if not ('ToPort' in props and 'FromPort' in props):
            raise ValueError(
                "ToPort/FromPort must be specified for proto %s" % proto)


class SecurityGroupEgress(AWSObject):
    resource_type = "AWS::EC2::SecurityGroupEgress"

    props = {
        'CidrIp': (str, False),
        'CidrIpv6': (str, False),
        'Description': (str, False),
        'DestinationPrefixListId': (str, False),
        'DestinationSecurityGroupId': (str, False),
        'FromPort': (network_port, False),
        'GroupId': (str, True),
        'IpProtocol': (str, True),
        'ToPort': (network_port, False),
        #
        # Workaround for a bug in CloudFormation and EC2 where the
        # DestinationSecurityGroupId property is ignored causing
        # egress rules targeting a security group to be ignored.
        # Using SourceSecurityGroupId instead works fine even in
        # egress rules. AWS have known about this bug for a while.
        #
        'SourceSecurityGroupId': (str, False),
    }

    def validate(self):
        conds = [
            'CidrIp',
            'CidrIpv6',
            'DestinationPrefixListId',
            'DestinationSecurityGroupId',
        ]
        exactly_one(self.__class__.__name__, self.properties, conds)
        check_ports(self.properties)


class SecurityGroupIngress(AWSObject):
    resource_type = "AWS::EC2::SecurityGroupIngress"

    props = {
        'CidrIp': (str, False),
        'CidrIpv6': (str, False),
        'Description': (str, False),
        'FromPort': (network_port, False),
        'GroupName': (str, False),
        'GroupId': (str, False),
        'IpProtocol': (str, True),
        'SourcePrefixListId': (str, False),
        'SourceSecurityGroupName': (str, False),
        'SourceSecurityGroupId': (str, False),
        'SourceSecurityGroupOwnerId': (str, False),
        'ToPort': (network_port, False),
    }

    def validate(self):
        conds = [
            'CidrIp',
            'CidrIpv6',
            'SourcePrefixListId',
            'SourceSecurityGroupName',
            'SourceSecurityGroupId',
        ]
        exactly_one(self.__class__.__name__, self.properties, conds)
        check_ports(self.properties)


class SecurityGroupRule(AWSProperty):
    props = {
        'CidrIp': (str, False),
        'CidrIpv6': (str, False),
        'Description': (str, False),
        'DestinationPrefixListId': (str, False),
        'DestinationSecurityGroupId': (str, False),
        'FromPort': (network_port, False),
        'IpProtocol': (str, True),
        'SourcePrefixListId': (str, False),
        'SourceSecurityGroupId': (str, False),
        'SourceSecurityGroupName': (str, False),
        'SourceSecurityGroupOwnerId': (str, False),
        'ToPort': (network_port, False),
    }


class SecurityGroup(AWSObject):
    resource_type = "AWS::EC2::SecurityGroup"

    props = {
        'GroupName': (str, False),
        'GroupDescription': (str, True),
        'SecurityGroupEgress': (list, False),
        'SecurityGroupIngress': (list, False),
        'VpcId': (str, False),
        'Tags': ((Tags, list), False),
    }


class Subnet(AWSObject):
    resource_type = "AWS::EC2::Subnet"

    props = {
        'AssignIpv6AddressOnCreation': (boolean, False),
        'AvailabilityZone': (str, False),
        'CidrBlock': (str, True),
        'Ipv6CidrBlock': (str, False),
        'MapPublicIpOnLaunch': (boolean, False),
        'OutpostArn': (str, False),
        'Tags': ((Tags, list), False),
        'VpcId': (str, True),
    }

    def validate(self):
        if 'Ipv6CidrBlock' in self.properties:
            if not self.properties.get('AssignIpv6AddressOnCreation'):
                raise ValueError(
                    "If Ipv6CidrBlock is present, "
                    "AssignIpv6AddressOnCreation must be set to True"
                )


class SubnetNetworkAclAssociation(AWSObject):
    resource_type = "AWS::EC2::SubnetNetworkAclAssociation"

    props = {
        'SubnetId': (str, True),
        'NetworkAclId': (str, True),
    }


class SubnetRouteTableAssociation(AWSObject):
    resource_type = "AWS::EC2::SubnetRouteTableAssociation"

    props = {
        'RouteTableId': (str, True),
        'SubnetId': (str, True),
    }


class Volume(AWSObject):
    resource_type = "AWS::EC2::Volume"

    props = {
        'AutoEnableIO': (boolean, False),
        'AvailabilityZone': (str, True),
        'Encrypted': (boolean, False),
        'Iops': (positive_integer, False),
        'KmsKeyId': (str, False),
        'MultiAttachEnabled': (boolean, False),
        'OutpostArn': (str, False),
        'Size': (positive_integer, False),
        'SnapshotId': (str, False),
        'Tags': ((Tags, list), False),
        'VolumeType': (str, False),
    }


class VolumeAttachment(AWSObject):
    resource_type = "AWS::EC2::VolumeAttachment"

    props = {
        'Device': (str, True),
        'InstanceId': (str, True),
        'VolumeId': (str, True),
    }


def instance_tenancy(value):
    valid = ['default', 'dedicated']
    if value not in valid:
        raise ValueError('InstanceTenancy needs to be one of %r' % valid)
    return value


class VPC(AWSObject):
    resource_type = "AWS::EC2::VPC"

    props = {
        'CidrBlock': (str, True),
        'EnableDnsSupport': (boolean, False),
        'EnableDnsHostnames': (boolean, False),
        'InstanceTenancy': (instance_tenancy, False),
        'Tags': ((Tags, list), False),
    }


class VPCDHCPOptionsAssociation(AWSObject):
    resource_type = "AWS::EC2::VPCDHCPOptionsAssociation"

    props = {
        'DhcpOptionsId': (str, True),
        'VpcId': (str, True),
    }


class VPCEndpoint(AWSObject):
    resource_type = "AWS::EC2::VPCEndpoint"

    props = {
        'PolicyDocument': (policytypes, False),
        'PrivateDnsEnabled': (boolean, False),
        'RouteTableIds': ([str], False),
        'SecurityGroupIds': ([str], False),
        'ServiceName': (str, True),
        'SubnetIds': ([str], False),
        'VpcEndpointType': (vpc_endpoint_type, False),
        'VpcId': (str, True),
    }


class VPCEndpointConnectionNotification(AWSObject):
    resource_type = "AWS::EC2::VPCEndpointConnectionNotification"

    props = {
        'ConnectionEvents': ([str], True),
        'ConnectionNotificationArn': (str, True),
        'ServiceId': (str, False),
        'VPCEndpointId': (str, False),
    }


class VPCEndpointService(AWSObject):
    resource_type = "AWS::EC2::VPCEndpointService"

    props = {
        'AcceptanceRequired': (boolean, False),
        'GatewayLoadBalancerArns': ([str], False),
        'NetworkLoadBalancerArns': ([str], False),
    }


class VPCEndpointServicePermissions(AWSObject):
    resource_type = "AWS::EC2::VPCEndpointServicePermissions"

    props = {
        'AllowedPrincipals': ([str], False),
        'ServiceId': (str, True),
    }


class VPCGatewayAttachment(AWSObject):
    resource_type = "AWS::EC2::VPCGatewayAttachment"

    props = {
        'InternetGatewayId': (str, False),
        'VpcId': (str, True),
        'VpnGatewayId': (str, False),
    }


class VpnTunnelOptionsSpecification(AWSProperty):
    props = {
        'PreSharedKey': (vpn_pre_shared_key, False),
        'TunnelInsideCidr': (vpn_tunnel_inside_cidr, False),
    }


class VPNConnection(AWSObject):
    resource_type = "AWS::EC2::VPNConnection"

    props = {
        'CustomerGatewayId': (str, True),
        'StaticRoutesOnly': (boolean, False),
        'Tags': ((Tags, list), False),
        'TransitGatewayId': (str, False),
        'Type': (str, True),
        'VpnGatewayId': (str, False),
        'VpnTunnelOptionsSpecifications':
            ([VpnTunnelOptionsSpecification], False),
    }

    def validate(self):
        conds = [
            'VpnGatewayId',
            'TransitGatewayId',
        ]
        exactly_one(self.__class__.__name__, self.properties, conds)


class VPNConnectionRoute(AWSObject):
    resource_type = "AWS::EC2::VPNConnectionRoute"

    props = {
        'DestinationCidrBlock': (str, True),
        'VpnConnectionId': (str, True),
    }


class VPNGateway(AWSObject):
    resource_type = "AWS::EC2::VPNGateway"

    props = {
        'AmazonSideAsn': (positive_integer, False),
        'Type': (str, True),
        'Tags': ((Tags, list), False),
    }


class VPNGatewayRoutePropagation(AWSObject):
    resource_type = "AWS::EC2::VPNGatewayRoutePropagation"

    props = {
        'RouteTableIds': ([str], True),
        'VpnGatewayId': (str, True),
    }


class VPCPeeringConnection(AWSObject):
    resource_type = "AWS::EC2::VPCPeeringConnection"

    props = {
        'PeerVpcId': (str, True),
        'VpcId': (str, True),
        'Tags': ((Tags, list), False),
        'PeerRegion': (str, False),
        'PeerOwnerId': (str, False),
        'PeerRoleArn': (str, False),
    }


class Monitoring(AWSProperty):
    props = {
        'Enabled': (boolean, False),
    }


class NetworkInterfaces(AWSProperty):
    props = {
        'AssociatePublicIpAddress': (boolean, False),
        'DeleteOnTermination': (boolean, False),
        'Description': (str, False),
        'DeviceIndex': (integer, True),
        'Groups': ([str], False),
        'InterfaceType': (str, False),
        'Ipv6AddressCount': (integer, False),
        'Ipv6Addresses': ([Ipv6Addresses], False),
        'NetworkInterfaceId': (str, False),
        'PrivateIpAddresses': ([PrivateIpAddressSpecification], False),
        'SecondaryPrivateIpAddressCount': (integer, False),
        'SubnetId': (str, False),
    }


class SecurityGroups(AWSProperty):
    props = {
        'GroupId': (str, False),
    }


class IamInstanceProfile(AWSProperty):
    props = {
        'Arn': (str, False),
    }


class SpotFleetTagSpecification(AWSProperty):
    props = {
        'ResourceType': (str, True),
        'Tags': ((Tags, list), False),
    }


class LaunchSpecifications(AWSProperty):
    props = {
        'BlockDeviceMappings': ([BlockDeviceMapping], False),
        'EbsOptimized': (boolean, False),
        'IamInstanceProfile': (IamInstanceProfile, False),
        'ImageId': (str, True),
        'InstanceType': (str, True),
        'KernelId': (str, False),
        'KeyName': (str, False),
        'Monitoring': (Monitoring, False),
        'NetworkInterfaces': ([NetworkInterfaces], False),
        'Placement': (Placement, False),
        'RamdiskId': (str, False),
        'SecurityGroups': ([SecurityGroups], False),
        'SpotPrice': (str, False),
        'SubnetId': (str, False),
        'TagSpecifications': ([SpotFleetTagSpecification], False),
        'UserData': (str, False),
        'WeightedCapacity': (positive_integer, False),
    }


class LaunchTemplateOverrides(AWSProperty):
    props = {
        'AvailabilityZone': (str, False),
        'InstanceType': (str, False),
        'SpotPrice': (str, False),
        'SubnetId': (str, False),
        'WeightedCapacity': (double, False)
    }


class LaunchTemplateConfigs(AWSProperty):
    props = {
        'LaunchTemplateSpecification': (LaunchTemplateSpecification, True),
        'Overrides': ([LaunchTemplateOverrides], False)
    }


class ClassicLoadBalancer(AWSProperty):
    props = {
        'Name': (str, True)
    }


class ClassicLoadBalancersConfig(AWSProperty):
    props = {
        'ClassicLoadBalancers': ([ClassicLoadBalancer], True)
    }


class TargetGroup(AWSProperty):
    props = {
        'Arn': (str, True)
    }


class TargetGroupConfig(AWSProperty):
    props = {
        'TargetGroups': ([TargetGroup], True),
    }


class LoadBalancersConfig(AWSProperty):
    props = {
        'ClassicLoadBalancersConfig': ([ClassicLoadBalancersConfig], False),
        'TargetGroupsConfig': (TargetGroupConfig, False)
    }


class SpotCapacityRebalance(AWSProperty):
    props = {
        'ReplacementStrategy': (str, False),
    }


class SpotMaintenanceStrategies(AWSProperty):
    props = {
        'CapacityRebalance': (SpotCapacityRebalance, False),
    }


class SpotFleetRequestConfigData(AWSProperty):

    props = {
        'AllocationStrategy': (str, False),
        'ExcessCapacityTerminationPolicy': (str, False),
        'IamFleetRole': (str, True),
        'InstanceInterruptionBehavior': (str, False),
        'InstancePoolsToUseCount': (integer, False),
        'LaunchSpecifications': ([LaunchSpecifications], False),
        'LaunchTemplateConfigs': ([LaunchTemplateConfigs], False),
        'LoadBalancersConfig': (LoadBalancersConfig, False),
        'OnDemandAllocationStrategy': (str, False),
        'OnDemandMaxTotalPrice': (str, False),
        'OnDemandTargetCapacity': (integer, False),
        'ReplaceUnhealthyInstances': (boolean, False),
        'SpotMaintenanceStrategies': (SpotMaintenanceStrategies, False),
        'SpotMaxTotalPrice': (str, False),
        'SpotPrice': (str, False),
        'TargetCapacity': (positive_integer, True),
        'TerminateInstancesWithExpiration': (boolean, False),
        'Type': (str, False),
        'ValidFrom': (str, False),
        'ValidUntil': (str, False),
    }

    def validate(self):
        conds = [
            'LaunchSpecifications',
            'LaunchTemplateConfigs'
        ]
        exactly_one(self.__class__.__name__, self.properties, conds)


class SpotFleet(AWSObject):
    resource_type = "AWS::EC2::SpotFleet"

    props = {
        'SpotFleetRequestConfigData': (SpotFleetRequestConfigData, True),
    }


class PlacementGroup(AWSObject):
    resource_type = "AWS::EC2::PlacementGroup"

    props = {
        'Strategy': (str, False),
    }


class SubnetCidrBlock(AWSObject):
    resource_type = "AWS::EC2::SubnetCidrBlock"

    props = {
        'Ipv6CidrBlock': (str, True),
        'SubnetId': (str, True),
    }


class VPCCidrBlock(AWSObject):
    resource_type = "AWS::EC2::VPCCidrBlock"

    props = {
        'AmazonProvidedIpv6CidrBlock': (boolean, False),
        'CidrBlock': (str, False),
        'VpcId': (str, True),
    }


class TagSpecifications(AWSProperty):
    props = {
        'ResourceType': (str, False),
        'Tags': ((Tags, list), False)
    }


class CapacityReservationTarget(AWSProperty):
    props = {
        'CapacityReservationId': (str, False),
    }


class CapacityReservationSpecification(AWSProperty):
    props = {
        'CapacityReservationPreference': (str, False),
        'CapacityReservationTarget': (CapacityReservationTarget, False),
    }


class SpotOptions(AWSProperty):
    props = {
        'BlockDurationMinutes': (integer, False),
        'InstanceInterruptionBehavior': (str, False),
        'MaxPrice': (str, False),
        'SpotInstanceType': (str, False),
        'ValidUntil': (str, False),
    }


class InstanceMarketOptions(AWSProperty):
    props = {
        'MarketType': (str, False),
        'SpotOptions': (SpotOptions, False)
    }


class LaunchTemplateCreditSpecification(AWSProperty):
    props = {
        'CpuCredits': (str, False),
    }


class MetadataOptions(AWSProperty):
    props = {
        'HttpEndpoint': (str, False),
        'HttpPutResponseHopLimit': (integer, False),
        'HttpTokens': (str, False),
    }


class LaunchTemplateElasticInferenceAccelerator(AWSProperty):
    props = {
        'Count': (integer, False),
        'Type': (validate_elasticinferenceaccelerator_type, False),
    }


class LaunchTemplateData(AWSProperty):
    props = {
        'BlockDeviceMappings': ([LaunchTemplateBlockDeviceMapping], False),
        'CapacityReservationSpecification':
            (CapacityReservationSpecification, False),
        'CpuOptions': (CpuOptions, False),
        'CreditSpecification': (LaunchTemplateCreditSpecification, False),
        'DisableApiTermination': (boolean, False),
        'EbsOptimized': (boolean, False),
        'ElasticGpuSpecifications': ([ElasticGpuSpecification], False),
        'ElasticInferenceAccelerators': ([LaunchTemplateElasticInferenceAccelerator], False),  # NOQA
        'EnclaveOptions': (EnclaveOptions, False),
        'HibernationOptions': (HibernationOptions, False),
        'IamInstanceProfile': (IamInstanceProfile, False),
        'ImageId': (str, False),
        'InstanceInitiatedShutdownBehavior': (str, False),
        'InstanceMarketOptions': (InstanceMarketOptions, False),
        'InstanceType': (str, False),
        'KernelId': (str, False),
        'KeyName': (str, False),
        'LicenseSpecifications': ([LicenseSpecification], False),
        'MetadataOptions': (MetadataOptions, False),
        'Monitoring': (Monitoring, False),
        'NetworkInterfaces': ([NetworkInterfaces], False),
        'Placement': (Placement, False),
        'RamDiskId': (str, False),
        'SecurityGroups': (list, False),
        'SecurityGroupIds': (list, False),
        'TagSpecifications': ([TagSpecifications], False),
        'UserData': (str, False)
    }


class LaunchTemplate(AWSObject):
    resource_type = "AWS::EC2::LaunchTemplate"
    props = {
        'LaunchTemplateData': (LaunchTemplateData, False),
        'LaunchTemplateName': (str, False),
        'TagSpecifications': ([TagSpecifications], False),
    }


class TrafficMirrorFilter(AWSObject):
    resource_type = "AWS::EC2::TrafficMirrorFilter"

    props = {
        'Description': (str, False),
        'NetworkServices': ([str], False),
        'Tags': (Tags, False),
    }


class TrafficMirrorPortRange(AWSProperty):
    props = {
        'FromPort': (integer, True),
        'ToPort': (integer, True),
    }


class TrafficMirrorFilterRule(AWSObject):
    resource_type = "AWS::EC2::TrafficMirrorFilterRule"

    props = {
        'Description': (str, False),
        'DestinationCidrBlock': (str, True),
        'DestinationPortRange': (TrafficMirrorPortRange, False),
        'Protocol': (integer, False),
        'RuleAction': (str, True),
        'RuleNumber': (integer, True),
        'SourceCidrBlock': (str, True),
        'SourcePortRange': (TrafficMirrorPortRange, False),
        'TrafficDirection': (str, True),
        'TrafficMirrorFilterId': (str, True),
    }


class TrafficMirrorSession(AWSObject):
    resource_type = "AWS::EC2::TrafficMirrorSession"

    props = {
        'Description': (str, False),
        'NetworkInterfaceId': (str, True),
        'PacketLength': (integer, False),
        'SessionNumber': (integer, True),
        'Tags': (Tags, False),
        'TrafficMirrorFilterId': (str, True),
        'TrafficMirrorTargetId': (str, True),
        'VirtualNetworkId': (integer, False),
    }


class TrafficMirrorTarget(AWSObject):
    resource_type = "AWS::EC2::TrafficMirrorTarget"

    props = {
        'Description': (str, False),
        'NetworkInterfaceId': (str, False),
        'NetworkLoadBalancerArn': (str, False),
        'Tags': (Tags, False),
    }


class TransitGateway(AWSObject):
    resource_type = "AWS::EC2::TransitGateway"
    props = {
        'AmazonSideAsn': (integer, False),
        'AutoAcceptSharedAttachments': (str, False),
        'DefaultRouteTableAssociation': (str, False),
        'DefaultRouteTablePropagation': (str, False),
        'Description': (str, False),
        'DnsSupport': (str, False),
        'Tags': ((Tags, list), False),
        'VpnEcmpSupport': (str, False),
    }


class TransitGatewayAttachment(AWSObject):
    resource_type = "AWS::EC2::TransitGatewayAttachment"
    props = {
        'SubnetIds': ([str], True),
        'Tags': ((Tags, list), False),
        'TransitGatewayId': (str, True),
        'VpcId': (str, True),
    }


class TransitGatewayConnectOptions(AWSProperty):
    props = {
        'Protocol': (str, False),
    }


class TransitGatewayConnect(AWSObject):
    resource_type = "AWS::EC2::TransitGatewayConnect"

    props = {
        'Options': (TransitGatewayConnectOptions, True),
        'Tags': (Tags, False),
        'TransportTransitGatewayAttachmentId': (str, True),
    }


class TransitGatewayMulticastDomain(AWSObject):
    resource_type = "AWS::EC2::TransitGatewayMulticastDomain"

    props = {
        'Options': (dict, False),
        'Tags': (Tags, False),
        'TransitGatewayId': (str, True),
    }


class TransitGatewayMulticastDomainAssociation(AWSObject):
    resource_type = "AWS::EC2::TransitGatewayMulticastDomainAssociation"

    props = {
        'SubnetId': (str, True),
        'TransitGatewayAttachmentId': (str, True),
        'TransitGatewayMulticastDomainId': (str, True),
    }


class TransitGatewayMulticastGroupMember(AWSObject):
    resource_type = "AWS::EC2::TransitGatewayMulticastGroupMember"

    props = {
        'GroupIpAddress': (str, True),
        'NetworkInterfaceId': (str, True),
        'TransitGatewayMulticastDomainId': (str, True),
    }


class TransitGatewayMulticastGroupSource(AWSObject):
    resource_type = "AWS::EC2::TransitGatewayMulticastGroupSource"

    props = {
        'GroupIpAddress': (str, True),
        'NetworkInterfaceId': (str, True),
        'TransitGatewayMulticastDomainId': (str, True),
    }


class TransitGatewayRoute(AWSObject):
    resource_type = "AWS::EC2::TransitGatewayRoute"
    props = {
        'Blackhole': (boolean, False),
        'DestinationCidrBlock': (str, False),
        'TransitGatewayAttachmentId': (str, False),
        'TransitGatewayRouteTableId': (str, True),
    }


class TransitGatewayRouteTable(AWSObject):
    resource_type = "AWS::EC2::TransitGatewayRouteTable"
    props = {
        'Tags': ((Tags, list), False),
        'TransitGatewayId': (str, True),
    }


class TransitGatewayRouteTableAssociation(AWSObject):
    resource_type = "AWS::EC2::TransitGatewayRouteTableAssociation"
    props = {
        'TransitGatewayAttachmentId': (str, True),
        'TransitGatewayRouteTableId': (str, True),
    }


class TransitGatewayRouteTablePropagation(AWSObject):
    resource_type = "AWS::EC2::TransitGatewayRouteTablePropagation"
    props = {
        'TransitGatewayAttachmentId': (str, True),
        'TransitGatewayRouteTableId': (str, True),
    }


class FleetLaunchTemplateSpecificationRequest(AWSProperty):
    props = {
        'LaunchTemplateId': (str, False),
        'LaunchTemplateName': (str, False),
        'Version': (str, False),
    }


class FleetLaunchTemplateOverridesRequest(AWSProperty):
    props = {
        'AvailabilityZone': (str, False),
        'InstanceType': (str, False),
        'MaxPrice': (str, False),
        'Priority': (double, False),
        'SubnetId': (str, False),
        'WeightedCapacity': (double, False),
    }


class FleetLaunchTemplateConfigRequest(AWSProperty):
    props = {
        'LaunchTemplateSpecification': (
            FleetLaunchTemplateSpecificationRequest,
            False
        ),
        'Overrides': ([FleetLaunchTemplateOverridesRequest], False),
    }


class OnDemandOptionsRequest(AWSProperty):
    props = {
        'AllocationStrategy': (str, False),
    }


class SpotOptionsRequest(AWSProperty):
    props = {
        'AllocationStrategy': (str, False),
        'InstanceInterruptionBehavior': (str, False),
        'InstancePoolsToUseCount': (integer, False),
    }


class TargetCapacitySpecificationRequest(AWSProperty):
    props = {
        'DefaultTargetCapacityType': (str, False),
        'OnDemandTargetCapacity': (integer, False),
        'SpotTargetCapacity': (integer, False),
        'TotalTargetCapacity': (integer, False),
    }


class EC2Fleet(AWSObject):
    resource_type = "AWS::EC2::EC2Fleet"
    props = {
        'ExcessCapacityTerminationPolicy': (str, False),
        'LaunchTemplateConfigs': ([FleetLaunchTemplateConfigRequest], True),
        'OnDemandOptions': (OnDemandOptionsRequest, False),
        'ReplaceUnhealthyInstances': (boolean, False),
        'SpotOptions': (SpotOptionsRequest, False),
        'TagSpecifications': ([TagSpecifications], False),
        'TargetCapacitySpecification': (TargetCapacitySpecificationRequest,
                                        False),
        'TerminateInstancesWithExpiration': (boolean, False),
        'Type': (str, False),
        'ValidFrom': (str, False),
        'ValidUntil': (str, False),
    }


class CapacityReservation(AWSObject):
    resource_type = "AWS::EC2::CapacityReservation"
    props = {
        'AvailabilityZone': (str, True),
        'EbsOptimized': (boolean, False),
        'EndDate': (str, False),
        'EndDateType': (str, False),
        'EphemeralStorage': (boolean, False),
        'InstanceCount': (integer, True),
        'InstanceMatchCriteria': (str, False),
        'InstancePlatform': (str, True),
        'InstanceType': (str, True),
        'TagSpecifications': ([TagSpecifications], False),
        'Tenancy': (str, False),
    }


class ClientVpnAuthorizationRule(AWSObject):
    resource_type = "AWS::EC2::ClientVpnAuthorizationRule"

    props = {
        'AccessGroupId': (str, False),
        'AuthorizeAllGroups': (boolean, False),
        'ClientVpnEndpointId': (str, True),
        'Description': (str, False),
        'TargetNetworkCidr': (str, True),
    }


class CertificateAuthenticationRequest(AWSProperty):
    props = {
        'ClientRootCertificateChainArn': (str, True),
    }


class DirectoryServiceAuthenticationRequest(AWSProperty):
    props = {
        'DirectoryId': (str, True)
    }


class FederatedAuthenticationRequest(AWSProperty):
    props = {
        'SAMLProviderArn': (str, True),
        'SelfServiceSAMLProviderArn': (str, False)
    }


class ClientAuthenticationRequest(AWSProperty):
    props = {
        'ActiveDirectory': (DirectoryServiceAuthenticationRequest, False),
        'FederatedAuthentication': (FederatedAuthenticationRequest, False),
        'MutualAuthentication': (CertificateAuthenticationRequest, False),
        'Type': (str, True),
    }


class ClientConnectOptions(AWSProperty):
    props = {
        'Enabled': (bool, True),
        'LambdaFunctionArn': (str, False)
    }


class ConnectionLogOptions(AWSProperty):
    props = {
        'CloudwatchLogGroup': (str, False),
        'CloudwatchLogStream': (str, False),
        'Enabled': (boolean, True),
    }


class ClientVpnEndpoint(AWSObject):
    resource_type = "AWS::EC2::ClientVpnEndpoint"

    props = {
        'AuthenticationOptions': ([ClientAuthenticationRequest], True),
        'ClientCidrBlock': (str, True),
        'ClientConnectOptions': (ClientConnectOptions, False),
        'ConnectionLogOptions': (ConnectionLogOptions, True),
        'Description': (str, False),
        'DnsServers': ([str], False),
        'SecurityGroupIds': ([str], False),
        'SelfServicePortal': (
            validate_clientvpnendpoint_selfserviceportal, False
        ),
        'ServerCertificateArn': (str, True),
        'SplitTunnel': (boolean, False),
        'TagSpecifications': ([TagSpecifications], False),
        'TransportProtocol': (str, False),
        'VpcId': (str, False),
        'VpnPort': (validate_clientvpnendpoint_vpnport, False),
    }


class ClientVpnRoute(AWSObject):
    resource_type = "AWS::EC2::ClientVpnRoute"

    props = {
        'ClientVpnEndpointId': (str, True),
        'Description': (str, False),
        'DestinationCidrBlock': (str, True),
        'TargetVpcSubnetId': (str, True),
    }


class ClientVpnTargetNetworkAssociation(AWSObject):
    resource_type = "AWS::EC2::ClientVpnTargetNetworkAssociation"

    props = {
        'ClientVpnEndpointId': (str, True),
        'SubnetId': (str, True),
    }


class LocalGatewayRoute(AWSObject):
    resource_type = "AWS::EC2::LocalGatewayRoute"

    props = {
        'DestinationCidrBlock': (str, True),
        'LocalGatewayRouteTableId': (str, True),
        'LocalGatewayVirtualInterfaceGroupId': (str, True),
    }


class LocalGatewayRouteTableVPCAssociation(AWSObject):
    resource_type = "AWS::EC2::LocalGatewayRouteTableVPCAssociation"

    props = {
        'LocalGatewayRouteTableId': (str, True),
        'Tags': ((Tags, list), False),
        'VpcId': (str, True),
    }
