# Copyright (c) 2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags


class TransitGatewayRegistration(AWSObject):
    resource_type = "AWS::NetworkManager::TransitGatewayRegistration"

    props = {
        'GlobalNetworkId': (str, True),
        'TransitGatewayArn': (str, True),
    }


class Location(AWSProperty):
    props = {
        'Address': (str, False),
        'Latitude': (str, False),
        'Longitude': (str, False),
    }


class Site(AWSObject):
    resource_type = "AWS::NetworkManager::Site"

    props = {
        'Description': (str, False),
        'GlobalNetworkId': (str, True),
        'Location': (Location, False),
        'Tags': (Tags, False),
    }


class LinkAssociation(AWSObject):
    resource_type = "AWS::NetworkManager::LinkAssociation"

    props = {
        'DeviceId': (str, True),
        'GlobalNetworkId': (str, True),
        'LinkId': (str, True),
    }


class Bandwidth(AWSProperty):
    props = {
        'DownloadSpeed': (str, False),
        'UploadSpeed': (str, False),
    }


class Link(AWSObject):
    resource_type = "AWS::NetworkManager::Link"

    props = {
        'Bandwidth': (Bandwidth, True),
        'Description': (str, False),
        'GlobalNetworkId': (str, True),
        'Provider': (str, False),
        'SiteId': (str, True),
        'Tags': (Tags, False),
        'Type': (str, False),
    }


class GlobalNetwork(AWSObject):
    resource_type = "AWS::NetworkManager::GlobalNetwork"

    props = {
        'Description': (str, False),
        'Tags': (Tags, False),
    }


class Device(AWSObject):
    resource_type = "AWS::NetworkManager::Device"

    props = {
        'Description': (str, False),
        'GlobalNetworkId': (str, True),
        'Location': (str, False),
        'Model': (str, False),
        'SerialNumber': (str, False),
        'SiteId': (str, False),
        'Tags': (Tags, False),
        'Type': (str, False),
        'Vendor': (str, False),
    }


class CustomerGatewayAssociation(AWSObject):
    resource_type = "AWS::NetworkManager::CustomerGatewayAssociation"

    props = {
        'CustomerGatewayArn': (str, True),
        'DeviceId': (str, True),
        'GlobalNetworkId': (str, True),
        'LinkId': (str, False),
    }
