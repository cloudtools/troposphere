# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty, Ref
from .validators import boolean, integer, network_port


class Tag(AWSHelperFn):
    def __init__(self, key, value):
        self.data = {'Key': key, 'Value': value}

    def JSONrepr(self):
        return self.data


class CustomerGateway(AWSObject):
    props = {
        'BgpAsn': (int, True),
        'IpAddress': (basestring, True),
        'Type': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::CustomerGateway"
        sup = super(CustomerGateway, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class DHCPOptions(AWSObject):
    props = {
        'DomainName': (basestring, False),
        'DomainNameServers': (list, False),
        'NetbiosNameServers': (list, False),
        'NetbiosNodeType': (int, False),
        'NTPServers': (list, False),
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


class EBSBlockDevice(AWSProperty):
    props = {
        'DeleteOnTermination': (bool, False),
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


class Instance(AWSObject):
    props = {
        'AvailabilityZone': (basestring, False),
        'BlockDeviceMappings': (list, False),
        'DisableApiTermination': (bool, False),
        'EbsOptimized': (bool, False),
        'IamInstanceProfile': (basestring, False),
        'ImageId': (basestring, True),
        'InstanceType': (basestring, True),
        'KernelId': (basestring, False),
        'KeyName': (basestring, False),
        'Monitoring': (boolean, False),
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


class ICMP(AWSProperty):
    props = {
        'Code': (int, False),
        'Type': (int, False),
    }


class PortRange(AWSProperty):
    props = {
        'From': (int, False),
        'To': (int, False),
    }


class NetworkAclEntry(AWSObject):
    props = {
        'CidrBlock': (basestring, True),
        'Egress': (boolean, True),
        'Icmp': (ICMP, False),  # Conditional
        'NetworkAclId': (basestring, True),
        'PortRange': (PortRange, True),
        'Protocol': (int, True),
        'RuleAction': (basestring, True),
        'RuleNumber': (int, True),
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

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::SecurityGroupEgress"
        sup = super(SecurityGroupEgress, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class SecurityGroupIngress(AWSObject):
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

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::SecurityGroupIngress"
        sup = super(SecurityGroupIngress, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


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
        'DhcpOptionsId': (basestring, True),
        'VpcId': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::EC2::VPCDHCPOptionsAssociation"
        sup = super(VPCDHCPOptionsAssociation, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class VPCGatewayAttachment(AWSObject):
    props = {
        'InternetGatewayId': (basestring, False),
        'VpcId': (basestring, True),
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
