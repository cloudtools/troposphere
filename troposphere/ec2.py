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
VALID_CLIENTVPNENDPOINT_VPNPORT = (443, 1194)


def validate_elasticinferenceaccelerator_type(
        elasticinferenceaccelerator_type):
    """Validate ElasticInferenceAccelerator for Instance"""

    if elasticinferenceaccelerator_type not in VALID_ELASTICINFERENCEACCELERATOR_TYPES:  # NOQA
        raise ValueError("Elastic Inference Accelerator Type must be one of: %s" %  # NOQA
                         ", ".join(VALID_ELASTICINFERENCEACCELERATOR_TYPES))
    return elasticinferenceaccelerator_type


def validate_clientvpnendpoint_vpnport(vpnport):
    """Validate VpnPort for ClientVpnEndpoint"""

    if vpnport not in VALID_CLIENTVPNENDPOINT_VPNPORT:
        raise ValueError("ClientVpnEndpoint VpnPortmust be one of: %s" %  # NOQA
                         ", ".join(VALID_CLIENTVPNENDPOINT_VPNPORT))
    return vpnport


class Tag(AWSProperty):
    props = {
        'Key': (basestring, True),
        'Value': (basestring, True)
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
        'VpcId': (basestring, True),
    }


class CustomerGateway(AWSObject):
    resource_type = "AWS::EC2::CustomerGateway"

    props = {
        'BgpAsn': (integer, True),
        'IpAddress': (basestring, True),
        'Tags': ((Tags, list), False),
        'Type': (basestring, True),
    }


class DHCPOptions(AWSObject):
    resource_type = "AWS::EC2::DHCPOptions"

    props = {
        'DomainName': (basestring, False),
        'DomainNameServers': (list, False),
        'NetbiosNameServers': (list, False),
        'NetbiosNodeType': (integer, False),
        'NtpServers': (list, False),
        'Tags': ((Tags, list), False),
    }


class EgressOnlyInternetGateway(AWSObject):
    resource_type = "AWS::EC2::EgressOnlyInternetGateway"

    props = {
        'VpcId': (basestring, True),
    }


class EIP(AWSObject):
    resource_type = "AWS::EC2::EIP"

    props = {
        'InstanceId': (basestring, False),
        'Domain': (basestring, False),
        'PublicIpv4Pool': (basestring, False),
        'Tags': (Tags, False),
    }


class EIPAssociation(AWSObject):
    resource_type = "AWS::EC2::EIPAssociation"

    props = {
        'AllocationId': (basestring, False),
        'EIP': (basestring, False),
        'InstanceId': (basestring, False),
        'NetworkInterfaceId': (basestring, False),
        'PrivateIpAddress': (basestring, False),
    }


class FlowLog(AWSObject):
    resource_type = "AWS::EC2::FlowLog"

    props = {
        'DeliverLogsPermissionArn': (basestring, False),
        'LogDestination': (basestring, False),
        'LogDestinationType': (basestring, False),
        'LogFormat': (basestring, False),
        'LogGroupName': (basestring, False),
        'MaxAggregationInterval': (integer, False),
        'ResourceId': (basestring, True),
        'ResourceType': (basestring, True),
        'Tags': (Tags, False),
        'TrafficType': (basestring, True),
    }


class NatGateway(AWSObject):
    resource_type = "AWS::EC2::NatGateway"

    props = {
        'AllocationId': (basestring, True),
        'SubnetId': (basestring, True),
        'Tags': ((Tags, list), False),
    }


class EBSBlockDevice(AWSProperty):
    props = {
        'DeleteOnTermination': (boolean, False),
        'Encrypted': (boolean, False),
        'KmsKeyId': (basestring, False),
        'Iops': (integer, False),  # Conditional
        'SnapshotId': (basestring, False),  # Conditional
        'VolumeSize': (integer, False),  # Conditional
        'VolumeType': (basestring, False),
    }


NO_DEVICE = {}


class BlockDeviceMapping(AWSProperty):
    props = {
        'DeviceName': (basestring, True),
        'Ebs': (EBSBlockDevice, False),  # Conditional
        'VirtualName': (basestring, False),  # Conditional
        'NoDevice': (dict, False)
    }


class LaunchTemplateBlockDeviceMapping(AWSProperty):
    props = {
        'DeviceName': (basestring, True),
        'Ebs': (EBSBlockDevice, False),  # Conditional
        'VirtualName': (basestring, False),  # Conditional
        'NoDevice': (basestring, False)
    }


class MountPoint(AWSProperty):
    props = {
        'Device': (basestring, True),
        'VolumeId': (basestring, True),
    }


class Placement(AWSProperty):
    props = {
        'Affinity': (basestring, False),
        'AvailabilityZone': (basestring, False),
        'GroupName': (basestring, False),
        'HostId': (basestring, False),
        'HostResourceGroupArn': (basestring, False),
        'PartitionNumber': (integer, False),
        'Tenancy': (basestring, False)
    }


class CpuOptions(AWSProperty):
    props = {
        'CoreCount': (integer, False),
        'ThreadsPerCore': (integer, False),
    }


class CreditSpecification(AWSProperty):
    props = {
        'CPUCredits': (basestring, False),
    }


class ElasticGpuSpecification(AWSProperty):
    props = {
        'Type': (basestring, True),
    }


class Ipv6Addresses(AWSHelperFn):
    def __init__(self, address):
        self.data = {
            'Ipv6Address': address,
        }


class LaunchTemplateSpecification(AWSProperty):
    props = {
        'LaunchTemplateId': (basestring, False),
        'LaunchTemplateName': (basestring, False),
        'Version': (basestring, True),
    }


class PrivateIpAddressSpecification(AWSProperty):
    props = {
        'Primary': (boolean, True),
        'PrivateIpAddress': (basestring, True),
    }


class NetworkInterfaceProperty(AWSProperty):
    props = {
        'AssociatePublicIpAddress': (boolean, False),
        'DeleteOnTermination': (boolean, False),
        'Description': (basestring, False),
        'DeviceIndex': (integer, True),
        'GroupSet': ([basestring], False),
        'NetworkInterfaceId': (basestring, False),
        'Ipv6AddressCount': (integer, False),
        'Ipv6Addresses': ([Ipv6Addresses], False),
        'PrivateIpAddress': (basestring, False),
        'PrivateIpAddresses': ([PrivateIpAddressSpecification], False),
        'SecondaryPrivateIpAddressCount': (integer, False),
        'SubnetId': (basestring, False),
    }


class AssociationParameters(AWSProperty):
    props = {
        'Key': (basestring, True),
        'Value': ([basestring], True),
    }


class SsmAssociations(AWSProperty):
    props = {
        'AssociationParameters': ([AssociationParameters], False),
        'DocumentName': (basestring, True),
    }


class GatewayRouteTableAssociation(AWSObject):
    resource_type = "AWS::EC2::GatewayRouteTableAssociation"

    props = {
        'GatewayId': (basestring, True),
        'RouteTableId': (basestring, True),
    }


class Host(AWSObject):
    resource_type = "AWS::EC2::Host"

    props = {
        'AutoPlacement': (basestring, False),
        'AvailabilityZone': (basestring, True),
        'HostRecovery': (basestring, False),
        'InstanceType': (basestring, True),
    }


class ElasticInferenceAccelerator(AWSProperty):
    props = {
        'Count': (integer, False),
        'Type': (validate_elasticinferenceaccelerator_type, True),
    }


class LicenseSpecification(AWSProperty):
    props = {
        'LicenseConfigurationArn': (basestring, True),
    }


class HibernationOptions(AWSProperty):
    props = {
        'Configured': (boolean, False),
    }


class Instance(AWSObject):
    resource_type = "AWS::EC2::Instance"

    props = {
        'Affinity': (basestring, False),
        'AvailabilityZone': (basestring, False),
        'BlockDeviceMappings': (list, False),
        'CpuOptions': (CpuOptions, False),
        'CreditSpecification': (CreditSpecification, False),
        'DisableApiTermination': (boolean, False),
        'EbsOptimized': (boolean, False),
        'ElasticGpuSpecifications': ([ElasticGpuSpecification], False),
        'ElasticInferenceAccelerators': ([ElasticInferenceAccelerator], False),
        'HibernationOptions': (HibernationOptions, False),
        'HostId': (basestring, False),
        'HostResourceGroupArn': (basestring, False),
        'IamInstanceProfile': (basestring, False),
        'ImageId': (basestring, False),
        'InstanceInitiatedShutdownBehavior': (basestring, False),
        'InstanceType': (basestring, False),
        'Ipv6AddressCount': (integer, False),
        'Ipv6Addresses': ([Ipv6Addresses], False),
        'KernelId': (basestring, False),
        'KeyName': (basestring, False),
        'LaunchTemplate': (LaunchTemplateSpecification, False),
        'LicenseSpecifications': ([LicenseSpecification], False),
        'Monitoring': (boolean, False),
        'NetworkInterfaces': ([NetworkInterfaceProperty], False),
        'PlacementGroupName': (basestring, False),
        'PrivateIpAddress': (basestring, False),
        'RamdiskId': (basestring, False),
        'SecurityGroupIds': (list, False),
        'SecurityGroups': (list, False),
        'SsmAssociations': ([SsmAssociations], False),
        'SourceDestCheck': (boolean, False),
        'SubnetId': (basestring, False),
        'Tags': ((Tags, list), False),
        'Tenancy': (basestring, False),
        'UserData': (basestring, False),
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
        'VpcId': (basestring, True),
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
        'CidrBlock': (basestring, False),
        'Egress': (boolean, False),
        'Icmp': (ICMP, False),  # Conditional
        'Ipv6CidrBlock': (basestring, False),
        'NetworkAclId': (basestring, True),
        'PortRange': (PortRange, False),  # Conditional
        'Protocol': (network_port, True),
        'RuleAction': (basestring, True),
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
        'Description': (basestring, False),
        'GroupSet': (list, False),
        'Ipv6AddressCount': (integer, False),
        'Ipv6Addresses': ([Ipv6Addresses], False),
        'PrivateIpAddress': (basestring, False),
        'PrivateIpAddresses': ([PrivateIpAddressSpecification], False),
        'SecondaryPrivateIpAddressCount': (integer, False),
        'SourceDestCheck': (boolean, False),
        'SubnetId': (basestring, True),
        'Tags': ((Tags, list), False),
    }


class NetworkInterfaceAttachment(AWSObject):
    resource_type = "AWS::EC2::NetworkInterfaceAttachment"

    props = {
        'DeleteOnTermination': (boolean, False),
        'DeviceIndex': (integer, True),
        'InstanceId': (basestring, True),
        'NetworkInterfaceId': (basestring, True),
    }


PERMISSION_INSTANCE_ATTACH = 'INSTANCE-ATTACH'
PERMISSION_EIP_ASSOCIATE = 'EIP-ASSOCIATE'


class NetworkInterfacePermission(AWSObject):
    resource_type = "AWS::EC2::NetworkInterfacePermission"

    props = {
        'AwsAccountId': (basestring, True),
        'NetworkInterfaceId': (basestring, True),
        'Permission': (basestring, True),
    }


class Entry(AWSProperty):
    props = {
        'Cidr': (basestring, True),
        'Description': (basestring, False),
    }


class PrefixList(AWSObject):
    resource_type = "AWS::EC2::PrefixList"

    props = {
        'AddressFamily': (basestring, True),
        'Entries': ([Entry], False),
        'MaxEntries': (integer, True),
        'PrefixListName': (basestring, True),
        'Tags': (Tags, False),
    }


class Route(AWSObject):
    resource_type = "AWS::EC2::Route"

    props = {
        'DestinationCidrBlock': (basestring, False),
        'DestinationIpv6CidrBlock': (basestring, False),
        'EgressOnlyInternetGatewayId': (basestring, False),
        'GatewayId': (basestring, False),
        'InstanceId': (basestring, False),
        'NatGatewayId': (basestring, False),
        'NetworkInterfaceId': (basestring, False),
        'RouteTableId': (basestring, True),
        'TransitGatewayId': (basestring, False),
        'VpcPeeringConnectionId': (basestring, False),
    }

    def validate(self):
        cidr_conds = [
            'DestinationCidrBlock',
            'DestinationIpv6CidrBlock',
        ]
        gateway_conds = [
            'EgressOnlyInternetGatewayId',
            'GatewayId',
            'InstanceId',
            'NatGatewayId',
            'NetworkInterfaceId',
            'TransitGatewayId',
            'VpcPeeringConnectionId'
        ]
        exactly_one(self.__class__.__name__, self.properties, cidr_conds)
        exactly_one(self.__class__.__name__, self.properties, gateway_conds)


class RouteTable(AWSObject):
    resource_type = "AWS::EC2::RouteTable"

    props = {
        'Tags': ((Tags, list), False),
        'VpcId': (basestring, True),
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
        'CidrIp': (basestring, False),
        'CidrIpv6': (basestring, False),
        'Description': (basestring, False),
        'DestinationPrefixListId': (basestring, False),
        'DestinationSecurityGroupId': (basestring, False),
        'FromPort': (network_port, False),
        'GroupId': (basestring, True),
        'IpProtocol': (basestring, True),
        'ToPort': (network_port, False),
        #
        # Workaround for a bug in CloudFormation and EC2 where the
        # DestinationSecurityGroupId property is ignored causing
        # egress rules targeting a security group to be ignored.
        # Using SourceSecurityGroupId instead works fine even in
        # egress rules. AWS have known about this bug for a while.
        #
        'SourceSecurityGroupId': (basestring, False),
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
        'CidrIp': (basestring, False),
        'CidrIpv6': (basestring, False),
        'Description': (basestring, False),
        'FromPort': (network_port, False),
        'GroupName': (basestring, False),
        'GroupId': (basestring, False),
        'IpProtocol': (basestring, True),
        'SourcePrefixListId': (basestring, False),
        'SourceSecurityGroupName': (basestring, False),
        'SourceSecurityGroupId': (basestring, False),
        'SourceSecurityGroupOwnerId': (basestring, False),
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
        'CidrIp': (basestring, False),
        'CidrIpv6': (basestring, False),
        'Description': (basestring, False),
        'DestinationPrefixListId': (basestring, False),
        'DestinationSecurityGroupId': (basestring, False),
        'FromPort': (network_port, False),
        'IpProtocol': (basestring, True),
        'SourcePrefixListId': (basestring, False),
        'SourceSecurityGroupId': (basestring, False),
        'SourceSecurityGroupName': (basestring, False),
        'SourceSecurityGroupOwnerId': (basestring, False),
        'ToPort': (network_port, False),
    }


class SecurityGroup(AWSObject):
    resource_type = "AWS::EC2::SecurityGroup"

    props = {
        'GroupName': (basestring, False),
        'GroupDescription': (basestring, True),
        'SecurityGroupEgress': (list, False),
        'SecurityGroupIngress': (list, False),
        'VpcId': (basestring, False),
        'Tags': ((Tags, list), False),
    }


class Subnet(AWSObject):
    resource_type = "AWS::EC2::Subnet"

    props = {
        'AssignIpv6AddressOnCreation': (boolean, False),
        'AvailabilityZone': (basestring, False),
        'CidrBlock': (basestring, True),
        'Ipv6CidrBlock': (basestring, False),
        'MapPublicIpOnLaunch': (boolean, False),
        'Tags': ((Tags, list), False),
        'VpcId': (basestring, True),
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
        'SubnetId': (basestring, True),
        'NetworkAclId': (basestring, True),
    }


class SubnetRouteTableAssociation(AWSObject):
    resource_type = "AWS::EC2::SubnetRouteTableAssociation"

    props = {
        'RouteTableId': (basestring, True),
        'SubnetId': (basestring, True),
    }


class Volume(AWSObject):
    resource_type = "AWS::EC2::Volume"

    props = {
        'AutoEnableIO': (boolean, False),
        'AvailabilityZone': (basestring, True),
        'Encrypted': (boolean, False),
        'Iops': (positive_integer, False),
        'KmsKeyId': (basestring, False),
        'MultiAttachEnabled': (boolean, False),
        'OutpostArn': (basestring, False),
        'Size': (positive_integer, False),
        'SnapshotId': (basestring, False),
        'Tags': ((Tags, list), False),
        'VolumeType': (basestring, False),
    }


class VolumeAttachment(AWSObject):
    resource_type = "AWS::EC2::VolumeAttachment"

    props = {
        'Device': (basestring, True),
        'InstanceId': (basestring, True),
        'VolumeId': (basestring, True),
    }


def instance_tenancy(value):
    valid = ['default', 'dedicated']
    if value not in valid:
        raise ValueError('InstanceTenancy needs to be one of %r' % valid)
    return value


class VPC(AWSObject):
    resource_type = "AWS::EC2::VPC"

    props = {
        'CidrBlock': (basestring, True),
        'EnableDnsSupport': (boolean, False),
        'EnableDnsHostnames': (boolean, False),
        'InstanceTenancy': (instance_tenancy, False),
        'Tags': ((Tags, list), False),
    }


class VPCDHCPOptionsAssociation(AWSObject):
    resource_type = "AWS::EC2::VPCDHCPOptionsAssociation"

    props = {
        'DhcpOptionsId': (basestring, True),
        'VpcId': (basestring, True),
    }


class VPCEndpoint(AWSObject):
    resource_type = "AWS::EC2::VPCEndpoint"

    props = {
        'PolicyDocument': (policytypes, False),
        'PrivateDnsEnabled': (boolean, False),
        'RouteTableIds': ([basestring], False),
        'SecurityGroupIds': ([basestring], False),
        'ServiceName': (basestring, True),
        'SubnetIds': ([basestring], False),
        'VpcEndpointType': (vpc_endpoint_type, False),
        'VpcId': (basestring, True),
    }


class VPCEndpointConnectionNotification(AWSObject):
    resource_type = "AWS::EC2::VPCEndpointConnectionNotification"

    props = {
        'ConnectionEvents': ([basestring], True),
        'ConnectionNotificationArn': (basestring, True),
        'ServiceId': (basestring, False),
        'VPCEndpointId': (basestring, False),
    }


class VPCEndpointService(AWSObject):
    resource_type = "AWS::EC2::VPCEndpointService"

    props = {
        'AcceptanceRequired': (boolean, False),
        'NetworkLoadBalancerArns': ([basestring], True),
    }


class VPCEndpointServicePermissions(AWSObject):
    resource_type = "AWS::EC2::VPCEndpointServicePermissions"

    props = {
        'AllowedPrincipals': ([basestring], False),
        'ServiceId': (basestring, True),
    }


class VPCGatewayAttachment(AWSObject):
    resource_type = "AWS::EC2::VPCGatewayAttachment"

    props = {
        'InternetGatewayId': (basestring, False),
        'VpcId': (basestring, True),
        'VpnGatewayId': (basestring, False),
    }


class VpnTunnelOptionsSpecification(AWSProperty):
    props = {
        'PreSharedKey': (vpn_pre_shared_key, False),
        'TunnelInsideCidr': (vpn_tunnel_inside_cidr, False),
    }


class VPNConnection(AWSObject):
    resource_type = "AWS::EC2::VPNConnection"

    props = {
        'CustomerGatewayId': (basestring, True),
        'StaticRoutesOnly': (boolean, False),
        'Tags': ((Tags, list), False),
        'TransitGatewayId': (basestring, False),
        'Type': (basestring, True),
        'VpnGatewayId': (basestring, False),
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
        'DestinationCidrBlock': (basestring, True),
        'VpnConnectionId': (basestring, True),
    }


class VPNGateway(AWSObject):
    resource_type = "AWS::EC2::VPNGateway"

    props = {
        'AmazonSideAsn': (positive_integer, False),
        'Type': (basestring, True),
        'Tags': ((Tags, list), False),
    }


class VPNGatewayRoutePropagation(AWSObject):
    resource_type = "AWS::EC2::VPNGatewayRoutePropagation"

    props = {
        'RouteTableIds': ([basestring], True),
        'VpnGatewayId': (basestring, True),
    }


class VPCPeeringConnection(AWSObject):
    resource_type = "AWS::EC2::VPCPeeringConnection"

    props = {
        'PeerVpcId': (basestring, True),
        'VpcId': (basestring, True),
        'Tags': ((Tags, list), False),
        'PeerRegion': (basestring, False),
        'PeerOwnerId': (basestring, False),
        'PeerRoleArn': (basestring, False),
    }


class Monitoring(AWSProperty):
    props = {
        'Enabled': (boolean, False),
    }


class NetworkInterfaces(AWSProperty):
    props = {
        'AssociatePublicIpAddress': (boolean, False),
        'DeleteOnTermination': (boolean, False),
        'Description': (basestring, False),
        'DeviceIndex': (integer, True),
        'Groups': ([basestring], False),
        'InterfaceType': (basestring, False),
        'Ipv6AddressCount': (integer, False),
        'Ipv6Addresses': ([Ipv6Addresses], False),
        'NetworkInterfaceId': (basestring, False),
        'PrivateIpAddresses': ([PrivateIpAddressSpecification], False),
        'SecondaryPrivateIpAddressCount': (integer, False),
        'SubnetId': (basestring, False),
    }


class SecurityGroups(AWSProperty):
    props = {
        'GroupId': (basestring, False),
    }


class IamInstanceProfile(AWSProperty):
    props = {
        'Arn': (basestring, False),
    }


class SpotFleetTagSpecification(AWSProperty):
    props = {
        'ResourceType': (basestring, True),
        'Tags': ((Tags, list), False),
    }


class LaunchSpecifications(AWSProperty):
    props = {
        'BlockDeviceMappings': ([BlockDeviceMapping], False),
        'EbsOptimized': (boolean, False),
        'IamInstanceProfile': (IamInstanceProfile, False),
        'ImageId': (basestring, True),
        'InstanceType': (basestring, True),
        'KernelId': (basestring, False),
        'KeyName': (basestring, False),
        'Monitoring': (Monitoring, False),
        'NetworkInterfaces': ([NetworkInterfaces], False),
        'Placement': (Placement, False),
        'RamdiskId': (basestring, False),
        'SecurityGroups': ([SecurityGroups], False),
        'SpotPrice': (basestring, False),
        'SubnetId': (basestring, False),
        'TagSpecifications': ([SpotFleetTagSpecification], False),
        'UserData': (basestring, False),
        'WeightedCapacity': (positive_integer, False),
    }


class LaunchTemplateOverrides(AWSProperty):
    props = {
        'AvailabilityZone': (basestring, False),
        'InstanceType': (basestring, False),
        'SpotPrice': (basestring, False),
        'SubnetId': (basestring, False),
        'WeightedCapacity': (double, False)
    }


class LaunchTemplateConfigs(AWSProperty):
    props = {
        'LaunchTemplateSpecification': (LaunchTemplateSpecification, True),
        'Overrides': ([LaunchTemplateOverrides], False)
    }


class ClassicLoadBalancer(AWSProperty):
    props = {
        'Name': (basestring, True)
    }


class ClassicLoadBalancersConfig(AWSProperty):
    props = {
        'ClassicLoadBalancers': ([ClassicLoadBalancer], True)
    }


class TargetGroup(AWSProperty):
    props = {
        'Arn': (basestring, True)
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


class SpotFleetRequestConfigData(AWSProperty):

    props = {
        'AllocationStrategy': (basestring, False),
        'ExcessCapacityTerminationPolicy': (basestring, False),
        'IamFleetRole': (basestring, True),
        'InstanceInterruptionBehavior': (basestring, False),
        'LaunchSpecifications': ([LaunchSpecifications], False),
        'LaunchTemplateConfigs': ([LaunchTemplateConfigs], False),
        'LoadBalancersConfig': (LoadBalancersConfig, False),
        'ReplaceUnhealthyInstances': (boolean, False),
        'SpotPrice': (basestring, False),
        'TargetCapacity': (positive_integer, True),
        'TerminateInstancesWithExpiration': (boolean, False),
        'Type': (basestring, False),
        'ValidFrom': (basestring, False),
        'ValidUntil': (basestring, False),
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
        'Strategy': (basestring, False),
    }


class SubnetCidrBlock(AWSObject):
    resource_type = "AWS::EC2::SubnetCidrBlock"

    props = {
        'Ipv6CidrBlock': (basestring, True),
        'SubnetId': (basestring, True),
    }


class VPCCidrBlock(AWSObject):
    resource_type = "AWS::EC2::VPCCidrBlock"

    props = {
        'AmazonProvidedIpv6CidrBlock': (boolean, False),
        'CidrBlock': (basestring, False),
        'VpcId': (basestring, True),
    }


class TagSpecifications(AWSProperty):
    props = {
        'ResourceType': (basestring, False),
        'Tags': ((Tags, list), False)
    }


class SpotOptions(AWSProperty):
    props = {
        'BlockDurationMinutes': (integer, False),
        'InstanceInterruptionBehavior': (basestring, False),
        'MaxPrice': (basestring, False),
        'SpotInstanceType': (basestring, False),
        'ValidUntil': (basestring, False),
    }


class InstanceMarketOptions(AWSProperty):
    props = {
        'MarketType': (basestring, False),
        'SpotOptions': (SpotOptions, False)
    }


class LaunchTemplateCreditSpecification(AWSProperty):
    props = {
        'CpuCredits': (basestring, False),
    }


class MetadataOptions(AWSProperty):
    props = {
        'HttpEndpoint': (basestring, False),
        'HttpPutResponseHopLimit': (integer, False),
        'HttpTokens': (basestring, False),
    }


class LaunchTemplateElasticInferenceAccelerator(AWSProperty):
    props = {
        'Count': (integer, False),
        'Type': (validate_elasticinferenceaccelerator_type, False),
    }


class LaunchTemplateData(AWSProperty):
    props = {
        'BlockDeviceMappings': ([LaunchTemplateBlockDeviceMapping], False),
        'CpuOptions': (CpuOptions, False),
        'CreditSpecification': (LaunchTemplateCreditSpecification, False),
        'DisableApiTermination': (boolean, False),
        'EbsOptimized': (boolean, False),
        'ElasticGpuSpecifications': ([ElasticGpuSpecification], False),
        'ElasticInferenceAccelerators': ([LaunchTemplateElasticInferenceAccelerator], False),  # NOQA
        'HibernationOptions': (HibernationOptions, False),
        'IamInstanceProfile': (IamInstanceProfile, False),
        'ImageId': (basestring, False),
        'InstanceInitiatedShutdownBehavior': (basestring, False),
        'InstanceMarketOptions': (InstanceMarketOptions, False),
        'InstanceType': (basestring, False),
        'KernelId': (basestring, False),
        'KeyName': (basestring, False),
        'LicenseSpecifications': ([LicenseSpecification], False),
        'MetadataOptions': (MetadataOptions, False),
        'Monitoring': (Monitoring, False),
        'NetworkInterfaces': ([NetworkInterfaces], False),
        'Placement': (Placement, False),
        'RamDiskId': (basestring, False),
        'SecurityGroups': (list, False),
        'SecurityGroupIds': (list, False),
        'TagSpecifications': ([TagSpecifications], False),
        'UserData': (basestring, False)
    }


class LaunchTemplate(AWSObject):
    resource_type = "AWS::EC2::LaunchTemplate"
    props = {
        'LaunchTemplateData': (LaunchTemplateData, False),
        'LaunchTemplateName': (basestring, False),
    }


class TrafficMirrorFilter(AWSObject):
    resource_type = "AWS::EC2::TrafficMirrorFilter"

    props = {
        'Description': (basestring, False),
        'NetworkServices': ([basestring], False),
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
        'Description': (basestring, False),
        'DestinationCidrBlock': (basestring, True),
        'DestinationPortRange': (TrafficMirrorPortRange, False),
        'Protocol': (integer, False),
        'RuleAction': (basestring, True),
        'RuleNumber': (integer, True),
        'SourceCidrBlock': (basestring, True),
        'SourcePortRange': (TrafficMirrorPortRange, False),
        'TrafficDirection': (basestring, True),
        'TrafficMirrorFilterId': (basestring, True),
    }


class TrafficMirrorSession(AWSObject):
    resource_type = "AWS::EC2::TrafficMirrorSession"

    props = {
        'Description': (basestring, False),
        'NetworkInterfaceId': (basestring, True),
        'PacketLength': (integer, False),
        'SessionNumber': (integer, True),
        'Tags': (Tags, False),
        'TrafficMirrorFilterId': (basestring, True),
        'TrafficMirrorTargetId': (basestring, True),
        'VirtualNetworkId': (integer, False),
    }


class TrafficMirrorTarget(AWSObject):
    resource_type = "AWS::EC2::TrafficMirrorTarget"

    props = {
        'Description': (basestring, False),
        'NetworkInterfaceId': (basestring, False),
        'NetworkLoadBalancerArn': (basestring, False),
        'Tags': (Tags, False),
    }


class TransitGateway(AWSObject):
    resource_type = "AWS::EC2::TransitGateway"
    props = {
        'AmazonSideAsn': (integer, False),
        'AutoAcceptSharedAttachments': (basestring, False),
        'DefaultRouteTableAssociation': (basestring, False),
        'DefaultRouteTablePropagation': (basestring, False),
        'Description': (basestring, False),
        'DnsSupport': (basestring, False),
        'Tags': ((Tags, list), False),
        'VpnEcmpSupport': (basestring, False),
    }


class TransitGatewayAttachment(AWSObject):
    resource_type = "AWS::EC2::TransitGatewayAttachment"
    props = {
        'SubnetIds': ([basestring], True),
        'Tags': ((Tags, list), False),
        'TransitGatewayId': (basestring, True),
        'VpcId': (basestring, True),
    }


class TransitGatewayRoute(AWSObject):
    resource_type = "AWS::EC2::TransitGatewayRoute"
    props = {
        'Blackhole': (boolean, False),
        'DestinationCidrBlock': (basestring, False),
        'TransitGatewayAttachmentId': (basestring, False),
        'TransitGatewayRouteTableId': (basestring, True),
    }


class TransitGatewayRouteTable(AWSObject):
    resource_type = "AWS::EC2::TransitGatewayRouteTable"
    props = {
        'Tags': ((Tags, list), False),
        'TransitGatewayId': (basestring, True),
    }


class TransitGatewayRouteTableAssociation(AWSObject):
    resource_type = "AWS::EC2::TransitGatewayRouteTableAssociation"
    props = {
        'TransitGatewayAttachmentId': (basestring, True),
        'TransitGatewayRouteTableId': (basestring, True),
    }


class TransitGatewayRouteTablePropagation(AWSObject):
    resource_type = "AWS::EC2::TransitGatewayRouteTablePropagation"
    props = {
        'TransitGatewayAttachmentId': (basestring, True),
        'TransitGatewayRouteTableId': (basestring, True),
    }


class FleetLaunchTemplateSpecificationRequest(AWSProperty):
    props = {
        'LaunchTemplateId': (basestring, False),
        'LaunchTemplateName': (basestring, False),
        'Version': (basestring, False),
    }


class FleetLaunchTemplateOverridesRequest(AWSProperty):
    props = {
        'AvailabilityZone': (basestring, False),
        'InstanceType': (basestring, False),
        'MaxPrice': (basestring, False),
        'Priority': (double, False),
        'SubnetId': (basestring, False),
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
        'AllocationStrategy': (basestring, False),
    }


class SpotOptionsRequest(AWSProperty):
    props = {
        'AllocationStrategy': (basestring, False),
        'InstanceInterruptionBehavior': (basestring, False),
        'InstancePoolsToUseCount': (integer, False),
    }


class TargetCapacitySpecificationRequest(AWSProperty):
    props = {
        'DefaultTargetCapacityType': (basestring, False),
        'OnDemandTargetCapacity': (integer, False),
        'SpotTargetCapacity': (integer, False),
        'TotalTargetCapacity': (integer, False),
    }


class EC2Fleet(AWSObject):
    resource_type = "AWS::EC2::EC2Fleet"
    props = {
        'ExcessCapacityTerminationPolicy': (basestring, False),
        'LaunchTemplateConfigs': ([FleetLaunchTemplateConfigRequest], True),
        'OnDemandOptions': (OnDemandOptionsRequest, False),
        'ReplaceUnhealthyInstances': (boolean, False),
        'SpotOptions': (SpotOptionsRequest, False),
        'TagSpecifications': ([TagSpecifications], False),
        'TargetCapacitySpecification': (TargetCapacitySpecificationRequest,
                                        False),
        'TerminateInstancesWithExpiration': (boolean, False),
        'Type': (basestring, False),
        'ValidFrom': (str, False),
        'ValidUntil': (str, False),
    }


class CapacityReservation(AWSObject):
    resource_type = "AWS::EC2::CapacityReservation"
    props = {
        'AvailabilityZone': (basestring, True),
        'EbsOptimized': (boolean, False),
        'EndDate': (basestring, False),
        'EndDateType': (basestring, False),
        'EphemeralStorage': (boolean, False),
        'InstanceCount': (integer, True),
        'InstanceMatchCriteria': (basestring, False),
        'InstancePlatform': (basestring, True),
        'InstanceType': (basestring, True),
        'TagSpecifications': ([TagSpecifications], False),
        'Tenancy': (basestring, False),
    }


class ClientVpnAuthorizationRule(AWSObject):
    resource_type = "AWS::EC2::ClientVpnAuthorizationRule"

    props = {
        'AccessGroupId': (basestring, False),
        'AuthorizeAllGroups': (boolean, False),
        'ClientVpnEndpointId': (basestring, True),
        'Description': (basestring, False),
        'TargetNetworkCidr': (basestring, True),
    }


class CertificateAuthenticationRequest(AWSProperty):
    props = {
        'ClientRootCertificateChainArn': (basestring, True),
    }


class DirectoryServiceAuthenticationRequest(AWSProperty):
    props = {
        'DirectoryId': (basestring, True),
    }


class FederatedAuthenticationRequest(AWSProperty):
    props = {
        'SAMLProviderArn': (basestring, True),
    }


class ClientAuthenticationRequest(AWSProperty):
    props = {
        'ActiveDirectory': (DirectoryServiceAuthenticationRequest, False),
        'FederatedAuthentication': (FederatedAuthenticationRequest, False),
        'MutualAuthentication': (CertificateAuthenticationRequest, False),
        'Type': (basestring, True),
    }


class ConnectionLogOptions(AWSProperty):
    props = {
        'CloudwatchLogGroup': (basestring, False),
        'CloudwatchLogStream': (basestring, False),
        'Enabled': (boolean, True),
    }


class ClientVpnEndpoint(AWSObject):
    resource_type = "AWS::EC2::ClientVpnEndpoint"

    props = {
        'AuthenticationOptions': ([ClientAuthenticationRequest], True),
        'ClientCidrBlock': (basestring, True),
        'ConnectionLogOptions': (ConnectionLogOptions, True),
        'Description': (basestring, False),
        'DnsServers': ([basestring], False),
        'SecurityGroupIds': ([basestring], False),
        'ServerCertificateArn': (basestring, True),
        'SplitTunnel': (boolean, False),
        'TagSpecifications': ([TagSpecifications], False),
        'TransportProtocol': (basestring, False),
        'VpcId': (basestring, False),
        'VpnPort': (validate_clientvpnendpoint_vpnport, False),
    }


class ClientVpnRoute(AWSObject):
    resource_type = "AWS::EC2::ClientVpnRoute"

    props = {
        'ClientVpnEndpointId': (basestring, True),
        'Description': (basestring, False),
        'DestinationCidrBlock': (basestring, True),
        'TargetVpcSubnetId': (basestring, True),
    }


class ClientVpnTargetNetworkAssociation(AWSObject):
    resource_type = "AWS::EC2::ClientVpnTargetNetworkAssociation"

    props = {
        'ClientVpnEndpointId': (basestring, True),
        'SubnetId': (basestring, True),
    }


class LocalGatewayRoute(AWSObject):
    resource_type = "AWS::EC2::LocalGatewayRoute"

    props = {
        'DestinationCidrBlock': (basestring, True),
        'LocalGatewayRouteTableId': (basestring, True),
        'LocalGatewayVirtualInterfaceGroupId': (basestring, True),
    }


class LocalGatewayRouteTableVPCAssociation(AWSObject):
    resource_type = "AWS::EC2::LocalGatewayRouteTableVPCAssociation"

    props = {
        'LocalGatewayRouteTableId': (basestring, True),
        'Tags': ((Tags, list), False),
        'VpcId': (basestring, True),
    }
