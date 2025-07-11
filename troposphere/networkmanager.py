# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer


class ConnectAttachmentOptions(AWSProperty):
    """
    `ConnectAttachmentOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectattachment-connectattachmentoptions.html>`__
    """

    props: PropsDictType = {
        "Protocol": (str, False),
    }


class ProposedNetworkFunctionGroupChange(AWSProperty):
    """
    `ProposedNetworkFunctionGroupChange <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-proposednetworkfunctiongroupchange.html>`__
    """

    props: PropsDictType = {
        "AttachmentPolicyRuleNumber": (integer, False),
        "NetworkFunctionGroupName": (str, False),
        "Tags": (Tags, False),
    }


class ProposedSegmentChange(AWSProperty):
    """
    `ProposedSegmentChange <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-proposedsegmentchange.html>`__
    """

    props: PropsDictType = {
        "AttachmentPolicyRuleNumber": (integer, False),
        "SegmentName": (str, False),
        "Tags": (Tags, False),
    }


class ConnectAttachment(AWSObject):
    """
    `ConnectAttachment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html>`__
    """

    resource_type = "AWS::NetworkManager::ConnectAttachment"

    props: PropsDictType = {
        "CoreNetworkId": (str, True),
        "EdgeLocation": (str, True),
        "NetworkFunctionGroupName": (str, False),
        "Options": (ConnectAttachmentOptions, True),
        "ProposedNetworkFunctionGroupChange": (
            ProposedNetworkFunctionGroupChange,
            False,
        ),
        "ProposedSegmentChange": (ProposedSegmentChange, False),
        "Tags": (Tags, False),
        "TransportAttachmentId": (str, True),
    }


class BgpOptions(AWSProperty):
    """
    `BgpOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-bgpoptions.html>`__
    """

    props: PropsDictType = {
        "PeerAsn": (double, False),
    }


class ConnectPeer(AWSObject):
    """
    `ConnectPeer <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html>`__
    """

    resource_type = "AWS::NetworkManager::ConnectPeer"

    props: PropsDictType = {
        "BgpOptions": (BgpOptions, False),
        "ConnectAttachmentId": (str, True),
        "CoreNetworkAddress": (str, False),
        "InsideCidrBlocks": ([str], False),
        "PeerAddress": (str, True),
        "SubnetArn": (str, False),
        "Tags": (Tags, False),
    }


class CoreNetwork(AWSObject):
    """
    `CoreNetwork <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html>`__
    """

    resource_type = "AWS::NetworkManager::CoreNetwork"

    props: PropsDictType = {
        "Description": (str, False),
        "GlobalNetworkId": (str, True),
        "PolicyDocument": (dict, False),
        "Tags": (Tags, False),
    }


class CustomerGatewayAssociation(AWSObject):
    """
    `CustomerGatewayAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html>`__
    """

    resource_type = "AWS::NetworkManager::CustomerGatewayAssociation"

    props: PropsDictType = {
        "CustomerGatewayArn": (str, True),
        "DeviceId": (str, True),
        "GlobalNetworkId": (str, True),
        "LinkId": (str, False),
    }


class AWSLocation(AWSProperty):
    """
    `AWSLocation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-awslocation.html>`__
    """

    props: PropsDictType = {
        "SubnetArn": (str, False),
        "Zone": (str, False),
    }


class Location(AWSProperty):
    """
    `Location <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html>`__
    """

    props: PropsDictType = {
        "Address": (str, False),
        "Latitude": (str, False),
        "Longitude": (str, False),
    }


class Device(AWSObject):
    """
    `Device <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html>`__
    """

    resource_type = "AWS::NetworkManager::Device"

    props: PropsDictType = {
        "AWSLocation": (AWSLocation, False),
        "Description": (str, False),
        "GlobalNetworkId": (str, True),
        "Location": (Location, False),
        "Model": (str, False),
        "SerialNumber": (str, False),
        "SiteId": (str, False),
        "Tags": (Tags, False),
        "Type": (str, False),
        "Vendor": (str, False),
    }


class DirectConnectGatewayAttachment(AWSObject):
    """
    `DirectConnectGatewayAttachment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-directconnectgatewayattachment.html>`__
    """

    resource_type = "AWS::NetworkManager::DirectConnectGatewayAttachment"

    props: PropsDictType = {
        "CoreNetworkId": (str, True),
        "DirectConnectGatewayArn": (str, True),
        "EdgeLocations": ([str], True),
        "ProposedNetworkFunctionGroupChange": (
            ProposedNetworkFunctionGroupChange,
            False,
        ),
        "ProposedSegmentChange": (ProposedSegmentChange, False),
        "Tags": (Tags, False),
    }


class GlobalNetwork(AWSObject):
    """
    `GlobalNetwork <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html>`__
    """

    resource_type = "AWS::NetworkManager::GlobalNetwork"

    props: PropsDictType = {
        "CreatedAt": (str, False),
        "Description": (str, False),
        "State": (str, False),
        "Tags": (Tags, False),
    }


class Bandwidth(AWSProperty):
    """
    `Bandwidth <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html>`__
    """

    props: PropsDictType = {
        "DownloadSpeed": (integer, False),
        "UploadSpeed": (integer, False),
    }


class Link(AWSObject):
    """
    `Link <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html>`__
    """

    resource_type = "AWS::NetworkManager::Link"

    props: PropsDictType = {
        "Bandwidth": (Bandwidth, True),
        "Description": (str, False),
        "GlobalNetworkId": (str, True),
        "Provider": (str, False),
        "SiteId": (str, True),
        "Tags": (Tags, False),
        "Type": (str, False),
    }


class LinkAssociation(AWSObject):
    """
    `LinkAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html>`__
    """

    resource_type = "AWS::NetworkManager::LinkAssociation"

    props: PropsDictType = {
        "DeviceId": (str, True),
        "GlobalNetworkId": (str, True),
        "LinkId": (str, True),
    }


class Site(AWSObject):
    """
    `Site <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html>`__
    """

    resource_type = "AWS::NetworkManager::Site"

    props: PropsDictType = {
        "Description": (str, False),
        "GlobalNetworkId": (str, True),
        "Location": (Location, False),
        "Tags": (Tags, False),
    }


class SiteToSiteVpnAttachment(AWSObject):
    """
    `SiteToSiteVpnAttachment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html>`__
    """

    resource_type = "AWS::NetworkManager::SiteToSiteVpnAttachment"

    props: PropsDictType = {
        "CoreNetworkId": (str, True),
        "NetworkFunctionGroupName": (str, False),
        "ProposedNetworkFunctionGroupChange": (
            ProposedNetworkFunctionGroupChange,
            False,
        ),
        "ProposedSegmentChange": (ProposedSegmentChange, False),
        "Tags": (Tags, False),
        "VpnConnectionArn": (str, True),
    }


class TransitGatewayPeering(AWSObject):
    """
    `TransitGatewayPeering <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewaypeering.html>`__
    """

    resource_type = "AWS::NetworkManager::TransitGatewayPeering"

    props: PropsDictType = {
        "CoreNetworkId": (str, True),
        "Tags": (Tags, False),
        "TransitGatewayArn": (str, True),
    }


class TransitGatewayRegistration(AWSObject):
    """
    `TransitGatewayRegistration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html>`__
    """

    resource_type = "AWS::NetworkManager::TransitGatewayRegistration"

    props: PropsDictType = {
        "GlobalNetworkId": (str, True),
        "TransitGatewayArn": (str, True),
    }


class TransitGatewayRouteTableAttachment(AWSObject):
    """
    `TransitGatewayRouteTableAttachment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayroutetableattachment.html>`__
    """

    resource_type = "AWS::NetworkManager::TransitGatewayRouteTableAttachment"

    props: PropsDictType = {
        "NetworkFunctionGroupName": (str, False),
        "PeeringId": (str, True),
        "ProposedNetworkFunctionGroupChange": (
            ProposedNetworkFunctionGroupChange,
            False,
        ),
        "ProposedSegmentChange": (ProposedSegmentChange, False),
        "Tags": (Tags, False),
        "TransitGatewayRouteTableArn": (str, True),
    }


class VpcOptions(AWSProperty):
    """
    `VpcOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-vpcoptions.html>`__
    """

    props: PropsDictType = {
        "ApplianceModeSupport": (boolean, False),
        "DnsSupport": (boolean, False),
        "Ipv6Support": (boolean, False),
        "SecurityGroupReferencingSupport": (boolean, False),
    }


class VpcAttachment(AWSObject):
    """
    `VpcAttachment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html>`__
    """

    resource_type = "AWS::NetworkManager::VpcAttachment"

    props: PropsDictType = {
        "CoreNetworkId": (str, True),
        "Options": (VpcOptions, False),
        "ProposedNetworkFunctionGroupChange": (
            ProposedNetworkFunctionGroupChange,
            False,
        ),
        "ProposedSegmentChange": (ProposedSegmentChange, False),
        "SubnetArns": ([str], True),
        "Tags": (Tags, False),
        "VpcArn": (str, True),
    }


class ConnectPeerBgpConfiguration(AWSProperty):
    """
    `ConnectPeerBgpConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerbgpconfiguration.html>`__
    """

    props: PropsDictType = {
        "CoreNetworkAddress": (str, False),
        "CoreNetworkAsn": (double, False),
        "PeerAddress": (str, False),
        "PeerAsn": (double, False),
    }


class ConnectPeerConfiguration(AWSProperty):
    """
    `ConnectPeerConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerconfiguration.html>`__
    """

    props: PropsDictType = {
        "BgpConfigurations": ([ConnectPeerBgpConfiguration], False),
        "CoreNetworkAddress": (str, False),
        "InsideCidrBlocks": ([str], False),
        "PeerAddress": (str, False),
        "Protocol": (str, False),
    }


class CoreNetworkEdge(AWSProperty):
    """
    `CoreNetworkEdge <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworkedge.html>`__
    """

    props: PropsDictType = {
        "Asn": (double, False),
        "EdgeLocation": (str, False),
        "InsideCidrBlocks": ([str], False),
    }


class CoreNetworkSegment(AWSProperty):
    """
    `CoreNetworkSegment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworksegment.html>`__
    """

    props: PropsDictType = {
        "EdgeLocations": ([str], False),
        "Name": (str, False),
        "SharedSegments": ([str], False),
    }


class Segments(AWSProperty):
    """
    `Segments <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-segments.html>`__
    """

    props: PropsDictType = {
        "SendTo": ([str], False),
        "SendVia": ([str], False),
    }
