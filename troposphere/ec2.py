# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty, Ref
from .validators import boolean, integer, integer_range, network_port


class Tag(AWSHelperFn):
    def __init__(self, key, value):
        self.data = {'Key': key, 'Value': value}

    def JSONrepr(self):
        return self.data


class CustomerGateway(AWSObject):
    type = "AWS::EC2::CustomerGateway"

    props = {
        'BgpAsn': (integer, True),
        'IpAddress': (basestring, True),
        'Tags': (list, False),
        'Type': (basestring, True),
    }


class DHCPOptions(AWSObject):
    type = "AWS::EC2::DHCPOptions"

    props = {
        'DomainName': (basestring, False),
        'DomainNameServers': (list, False),
        'NetbiosNameServers': (list, False),
        'NetbiosNodeType': (int, False),
        'NtpServers': (list, False),
        'Tags': (list, False),
    }


class EIP(AWSObject):
    type = "AWS::EC2::EIP"

    props = {
        'InstanceId': (basestring, False),
        'Domain': (basestring, False),
    }


class EIPAssociation(AWSObject):
    type = "AWS::EC2::EIPAssociation"

    props = {
        'AllocationId': (basestring, False),
        'EIP': (basestring, False),
        'InstanceId': (basestring, False),
        'NetworkInterfaceId': (basestring, False),
        'PrivateIpAddress': (basestring, False),
    }


class EBSBlockDevice(AWSProperty):
    props = {
        'DeleteOnTermination': (boolean, False),
        'Iops': (int, False),  # Conditional
        'SnapshotId': (basestring, False),  # Conditional
        'VolumeSize': (integer, False),  # Conditional
        'VolumeType': (basestring, False),
    }


class BlockDeviceMapping(AWSProperty):
    props = {
        'DeviceName': (basestring, True),
        'Ebs': (EBSBlockDevice, False),      # Conditional
        'NoDevice': (dict, False),
        'VirtualName': (basestring, False),  # Conditional
    }


class MountPoint(AWSProperty):
    props = {
        'Device': (basestring, True),
        'VolumeId': (basestring, True),
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
        'DeviceIndex': (basestring, True),
        'GroupSet': ([basestring, Ref], False),
        'NetworkInterfaceId': (basestring, False),
        'PrivateIpAddress': (basestring, False),
        'PrivateIpAddresses': ([PrivateIpAddressSpecification], False),
        'SecondaryPrivateIpAddressCount': (int, False),
        'SubnetId': (basestring, False),
    }


class Instance(AWSObject):
    type = "AWS::EC2::Instance"

    props = {
        'AvailabilityZone': (basestring, False),
        'BlockDeviceMappings': (list, False),
        'DisableApiTermination': (boolean, False),
        'EbsOptimized': (boolean, False),
        'IamInstanceProfile': (basestring, False),
        'ImageId': (basestring, True),
        'InstanceType': (basestring, False),
        'KernelId': (basestring, False),
        'KeyName': (basestring, False),
        'Monitoring': (boolean, False),
        'NetworkInterfaces': ([NetworkInterfaceProperty], False),
        'PlacementGroupName': (basestring, False),
        'PrivateIpAddress': (basestring, False),
        'RamdiskId': (basestring, False),
        'SecurityGroupIds': (list, False),
        'SecurityGroups': (list, False),
        'SourceDestCheck': (boolean, False),
        'SubnetId': (basestring, False),
        'Tags': (list, False),
        'Tenancy': (basestring, False),
        'UserData': (basestring, False),
        'Volumes': (list, False),
    }


class InternetGateway(AWSObject):
    type = "AWS::EC2::InternetGateway"

    props = {
        'Tags': (list, False),
    }


class NetworkAcl(AWSObject):
    type = "AWS::EC2::NetworkAcl"

    props = {
        'Tags': (list, False),
        'VpcId': (basestring, True),
    }


class ICMP(AWSProperty):
    props = {
        'Code': (int, False),
        'Type': (int, False),
    }


class PortRange(AWSProperty):
    props = {
        'From': (network_port, False),
        'To': (network_port, False),
    }


class NetworkAclEntry(AWSObject):
    type = "AWS::EC2::NetworkAclEntry"

    props = {
        'CidrBlock': (basestring, True),
        'Egress': (boolean, True),
        'Icmp': (ICMP, False),  # Conditional
        'NetworkAclId': (basestring, True),
        'PortRange': (PortRange, False),  # Conditional
        'Protocol': (network_port, True),
        'RuleAction': (basestring, True),
        'RuleNumber': (integer_range(1, 32766), True),
    }


class NetworkInterface(AWSObject):
    type = "AWS::EC2::NetworkInterface"

    props = {
        'Description': (basestring, False),
        'GroupSet': (list, False),
        'PrivateIpAddress': (basestring, False),
        'PrivateIpAddresses': ([PrivateIpAddressSpecification], False),
        'SecondaryPrivateIpAddressCount': (int, False),
        'SourceDestCheck': (boolean, False),
        'SubnetId': (basestring, True),
        'Tags': (list, False),
    }


class NetworkInterfaceAttachment(AWSObject):
    type = "AWS::EC2::NetworkInterfaceAttachment"

    props = {
        'DeleteOnTermination': (boolean, False),
        'DeviceIndex': (basestring, True),
        'InstanceId': (basestring, True),
        'NetworkInterfaceId': (basestring, True),
    }


class Route(AWSObject):
    type = "AWS::EC2::Route"

    props = {
        'DestinationCidrBlock': (basestring, True),
        'GatewayId': (basestring, False),
        'InstanceId': (basestring, False),
        'NetworkInterfaceId': (basestring, False),
        'RouteTableId': (basestring, True),
    }


class RouteTable(AWSObject):
    type = "AWS::EC2::RouteTable"

    props = {
        'Tags': (list, False),
        'VpcId': (basestring, True),
    }


class SecurityGroupEgress(AWSObject):
    type = "AWS::EC2::SecurityGroupEgress"

    props = {
        'CidrIp': (basestring, False),
        'DestinationSecurityGroupId': (basestring, False),
        'FromPort': (network_port, True),
        'GroupId': (basestring, False),
        'IpProtocol': (basestring, True),
        'ToPort': (network_port, True),
        #
        # Workaround for a bug in CloudFormation and EC2 where the
        # DestinationSecurityGroupId property is ignored causing
        # egress rules targeting a security group to be ignored.
        # Using SourceSecurityGroupId instead works fine even in
        # egress rules. AWS have known about this bug for a while.
        #
        'SourceSecurityGroupId': (basestring, False),
    }


class SecurityGroupIngress(AWSObject):
    type = "AWS::EC2::SecurityGroupIngress"

    props = {
        'CidrIp': (basestring, False),
        'FromPort': (network_port, False),
        'GroupName': (basestring, False),
        'GroupId': (basestring, False),
        'IpProtocol': (basestring, True),
        'SourceSecurityGroupName': (basestring, False),
        'SourceSecurityGroupId': (basestring, False),
        'SourceSecurityGroupOwnerId': (basestring, False),
        'ToPort': (network_port, False),
    }


class SecurityGroupRule(AWSProperty):
    props = {
        'CidrIp': (basestring, False),
        'FromPort': (network_port, True),
        'IpProtocol': (basestring, True),
        'SourceSecurityGroupId': (basestring, False),
        'SourceSecurityGroupName': (basestring, False),
        'SourceSecurityGroupOwnerId': (basestring, False),
        'ToPort': (network_port, True),
    }


class SecurityGroup(AWSObject):
    type = "AWS::EC2::SecurityGroup"

    props = {
        'GroupDescription': (basestring, True),
        'SecurityGroupEgress': (list, False),
        'SecurityGroupIngress': (list, False),
        'VpcId': (basestring, False),
        'Tags': (list, False),
    }


class Subnet(AWSObject):
    type = "AWS::EC2::Subnet"

    props = {
        'AvailabilityZone': (basestring, False),
        'CidrBlock': (basestring, True),
        'Tags': (list, False),
        'VpcId': (basestring, True),
    }


class SubnetNetworkAclAssociation(AWSObject):
    type = "AWS::EC2::SubnetNetworkAclAssociation"

    props = {
        'SubnetId': (basestring, True),
        'NetworkAclId': (basestring, True),
    }


class SubnetRouteTableAssociation(AWSObject):
    type = "AWS::EC2::SubnetRouteTableAssociation"

    props = {
        'RouteTableId': (basestring, True),
        'SubnetId': (basestring, True),
    }


class Volume(AWSObject):
    type = "AWS::EC2::Volume"

    props = {
        'AvailabilityZone': (basestring, True),
        'Iops': (int, False),
        'Size': (basestring, False),
        'SnapshotId': (basestring, False),
        'Tags': (list, False),
        'VolumeType': (basestring, False),
    }


class VolumeAttachment(AWSObject):
    type = "AWS::EC2::VolumeAttachment"

    props = {
        'Device': (basestring, True),
        'InstanceId': (basestring, True),
        'VolumeId': (basestring, True),
    }


class VPC(AWSObject):
    type = "AWS::EC2::VPC"

    props = {
        'CidrBlock': (basestring, True),
        'EnableDnsSupport': (boolean, False),
        'EnableDnsHostnames': (boolean, False),
        'InstanceTenancy': (basestring, False),
        'Tags': (list, False),
    }


class VPCDHCPOptionsAssociation(AWSObject):
    type = "AWS::EC2::VPCDHCPOptionsAssociation"

    props = {
        'DhcpOptionsId': (basestring, True),
        'VpcId': (basestring, True),
    }


class VPCGatewayAttachment(AWSObject):
    type = "AWS::EC2::VPCGatewayAttachment"

    props = {
        'InternetGatewayId': (basestring, False),
        'VpcId': (basestring, True),
        'VpnGatewayId': (basestring, False),
    }


class VPNConnection(AWSObject):
    type = "AWS::EC2::VPNConnection"

    props = {
        'Type': (basestring, True),
        'CustomerGatewayId': (basestring, True),
        'StaticRoutesOnly': (boolean, False),
        'Tags': (list, False),
        'VpnGatewayId': (basestring, True),
    }


class VPNConnectionRoute(AWSObject):
    type = "AWS::EC2::VPNConnectionRoute"

    props = {
        'DestinationCidrBlock': (basestring, True),
        'VpnConnectionId': (basestring, True),
    }


class VPNGateway(AWSObject):
    type = "AWS::EC2::VPNGateway"

    props = {
        'Type': (basestring, True),
        'Tags': (list, False),
    }


class VPNGatewayRoutePropagation(AWSObject):
    type = "AWS::EC2::VPNGatewayRoutePropagation"

    props = {
        'RouteTableIds': ([basestring], False),
        'VpnGatewayId': (basestring, True),
    }
