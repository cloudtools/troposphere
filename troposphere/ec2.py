# Copyright (c) 2011-2012, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import json

from . import AWSHelperFn, AWSObject, AWSProperty, Ref


class Tag(AWSHelperFn):
    def __init__(self, key, value):
        self.data = {'Key': key, 'Value': value}

    def JSONrepr(self):
        return self.data


class CustomGateway(AWSObject):
    props = {
        'BgpAsn': (int, True),
        'IpAddress': (basestring, True),
        'Type': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::CustomGateway"
        sup = super(CustomGateway, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class DHCPOptions(AWSObject):
    props = {
        'DomainName': (basestring, False),
        'DomainNameServers': (list, False),
        'NTPServers': (basestring, False),
        'NetbiosNameServers': (basestring, False),
        'NetbiosNodeType': (list, False),
        'Tags': (list, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::DHCPOptions"
        sup = super(DHCPOptions, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class EIP(AWSObject):
    props = {
        'InstanceId': (basestring, False),
        'Domain': (basestring, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::EIP"
        sup = super(EIP, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class EIPAssociation(AWSObject):
    props = {
        'AllocationId': (basestring, False),
        'EIP': (basestring, False),
        'InstanceId': (basestring, False),
        'NetworkInterfaceId': (basestring, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::EIPAssociation"
        sup = super(EIPAssociation, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class Instance(AWSObject):
    props = {
        'AvailabilityZone': (basestring, False),
        'DisableApiTermination': (bool, False),
        'EbsOptimized': (bool, False),
        'IamInstanceProfile': (basestring, False),
        'ImageId': (basestring, True),
        'InstanceType': (basestring, True),
        'KernelId': (basestring, False),
        'KeyName': (basestring, False),
        'Monitoring': (basestring, False),
        'NetworkInterfaces': (list, False),
        'PlacementGroupName': (basestring, False),
        'PrivateIpAddress': (basestring, False),
        'RamdiskId': (basestring, False),
        'SecurityGroupIds': (list, False),
        'SecurityGroups': (list, False),
        'SourceDestCheck': (bool, False),
        'SubnetId': (basestring, False),
        'Tags': (list, False),
        'Tenancy': (basestring, False),
        'UserData': (basestring, False),
        'Volumes': (list, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::Instance"
        sup = super(Instance, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class MountPoint(AWSProperty):
    props = {
        'Device': (basestring, True),
        'VolumeId': (basestring, True),
    }


class InternetGateway(AWSObject):
    props = {
        'Tags': (list, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::InternetGateway"
        sup = super(InternetGateway, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class NetworkAcl(AWSObject):
    props = {
        'Tags': (list, False),
        'VpcId': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::NetworkAcl"
        sup = super(NetworkAcl, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class ICMP(AWSObject):
    props = {
        'Code': (int, False),
        'Type': (int, False),
    }

    def __init__(self, **kwargs):
        sup = super(ICMP, self)
        sup.__init__(None, None, "ICMP", self.props, **kwargs)


class PortRange(AWSObject):
    props = {
        'From': (int, False),
        'To': (int, False),
    }

    def __init__(self, **kwargs):
        sup = super(PortRange, self)
        sup.__init__(None, None, "PortRange", self.props, **kwargs)


class NetworkAclEntry(AWSObject):
    props = {
        'NetworkAclId': (basestring, True),
        'RuleNumber': (int, True),
        'Protocol': (int, True),
        'RuleAction': (basestring, True),
        'Egress': (basestring, True),
        'CidrBlock': (basestring, True),
        'Icmp': (ICMP, True),
        'PortRange': (PortRange, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::NetworkAclEntry"
        sup = super(NetworkAclEntry, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class NetworkInterface(AWSObject):
    props = {
        'Description': (basestring, False),
        'GroupSet': (list, False),
        'PrivateIpAddress': (basestring, False),
        'SourceDestCheck': (bool, False),
        'SubnetId': (basestring, True),
        'Tags': (list, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::NetworkInterface"
        sup = super(NetworkInterface, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class Route(AWSObject):
    props = {
        'DestinationCidrBlock': (basestring, True),
        'GatewayId': (basestring, False),
        'InstanceId': (basestring, False),
        'NetworkInterfaceId': (basestring, False),
        'RouteTableId': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::Route"
        sup = super(Route, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class RouteTable(AWSObject):
    props = {
        'Tags': (list, False),
        'VpcId': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::RouteTable"
        sup = super(RouteTable, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class SecurityGroupEgress(AWSObject):
    props = {
        'GroupId': (basestring, True),
        'IpProtocol': (basestring, True),
        'CidrIp': (basestring, False),
        'DestinationSecurityGroupId': (basestring, False),
        'FromPort': (basestring, True),
        'ToPort': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::SecurityGroupEgress"
        sup = super(SecurityGroupEgress, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class SecurityGroupIngress(AWSObject):
    props = {
        'GroupName': (basestring, False),
        'GroupId': (basestring, False),
        'IpProtocol': (basestring, True),
        'CidrIp': (basestring, False),
        'SourceSecurityGroupName': (basestring, False),
        'SourceSecurityGroupId': (basestring, False),
        'SourceSecurityGroupOwnerId': (basestring, False),
        'FromPort': (basestring, False),
        'ToPort': (basestring, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::SecurityGroupIngress"
        sup = super(SecurityGroupIngress, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class SecurityGroupRule(AWSObject):
    props = {
        'IpProtocol': (basestring, True),
        'CidrIp': (basestring, False),
        'SourceSecurityGroupName': (basestring, False),
        'SourceSecurityGroupId': (basestring, False),
        'SourceSecurityGroupOwnerId': (basestring, False),
        'FromPort': (basestring, True),
        'ToPort': (basestring, True),
    }

    def __init__(self, **kwargs):
        sup = super(SecurityGroupRule, self)
        sup.__init__(None, props=self.props, **kwargs)


class SecurityGroup(AWSObject):
    props = {
        'GroupDescription': (basestring, True),
        'SecurityGroupEgress': (list, False),
        'SecurityGroupIngress': (list, False),
        'VpcId': (basestring, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::SecurityGroup"
        sup = super(SecurityGroup, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class Subnet(AWSObject):
    props = {
        'AvailabilityZone': (basestring, False),
        'CidrBlock': (basestring, True),
        'Tags': (list, False),
        'VpcId': (Ref, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::Subnet"
        sup = super(Subnet, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class SubnetNetworkAclAssociation(AWSObject):
    props = {
        'SubnetId': (basestring, True),
        'NetworkAclId': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::SubnetNetworkAclAssociation"
        sup = super(SubnetNetworkAclAssociation, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class SubnetRouteTableAssociation(AWSObject):
    props = {
        'RouteTableId': (basestring, True),
        'SubnetId': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::SubnetRouteTableAssociation"
        sup = super(SubnetRouteTableAssociation, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class Volume(AWSObject):
    props = {
        'AvailabilityZone': (basestring, True),
        'Iops': (int, False),
        'Size': (basestring, False),
        'SnapshotId': (basestring, False),
        'Tags': (list, False),
        'VolumeType': (basestring, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::Volume"
        sup = super(Volume, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class VolumeAttachment(AWSObject):
    props = {
        'Device': (basestring, True),
        'InstanceId': (basestring, True),
        'VolumeId': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::VolumeAttachment"
        sup = super(VolumeAttachment, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class VPC(AWSObject):
    props = {
        'CidrBlock': (basestring, True),
        'InstanceTenancy': (basestring, False),
        'Tags': (list, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::VPC"
        sup = super(VPC, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class VPCDHCPOptionsAssociation(AWSObject):
    props = {
        'VpcId': (basestring, True),
        'DhcpOptionsId': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::VPCDHCPOptionsAssociation"
        sup = super(VPCDHCPOptionsAssociation, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class VPCGatewayAttachment(AWSObject):
    props = {
        'VpcId': (basestring, True),
        'InternetGatewayId': (basestring, False),
        'VpnGatewayId': (basestring, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::VPCGatewayAttachment"
        sup = super(VPCGatewayAttachment, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class VPNConnection(AWSObject):
    props = {
        'Type': (basestring, True),
        'CustomerGatewayId': (basestring, True),
        'VpnGatewayId': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::VPNConnection"
        sup = super(VPNConnection, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class VPNGateway(AWSObject):
    props = {
        'Type': (basestring, True),
        'Tags': (list, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::VPNGateway"
        sup = super(VPNGateway, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)
