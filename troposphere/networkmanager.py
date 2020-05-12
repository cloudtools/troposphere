# Copyright (c) 2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags


class TransitGatewayRegistration(AWSObject):
    resource_type = "AWS::NetworkManager::TransitGatewayRegistration"

    props = {
        'GlobalNetworkId': (basestring, True),
        'TransitGatewayArn': (basestring, True),
    }


class Location(AWSProperty):
    props = {
        'Address': (basestring, False),
        'Latitude': (basestring, False),
        'Longitude': (basestring, False),
    }


class Site(AWSObject):
    resource_type = "AWS::NetworkManager::Site"

    props = {
        'Description': (basestring, False),
        'GlobalNetworkId': (basestring, True),
        'Location': (Location, False),
        'Tags': (Tags, False),
    }


class LinkAssociation(AWSObject):
    resource_type = "AWS::NetworkManager::LinkAssociation"

    props = {
        'DeviceId': (basestring, True),
        'GlobalNetworkId': (basestring, True),
        'LinkId': (basestring, True),
    }


class Bandwidth(AWSProperty):
    props = {
        'DownloadSpeed': (basestring, False),
        'UploadSpeed': (basestring, False),
    }


class Link(AWSObject):
    resource_type = "AWS::NetworkManager::Link"

    props = {
        'Bandwidth': (Bandwidth, True),
        'Description': (basestring, False),
        'GlobalNetworkId': (basestring, True),
        'Provider': (basestring, False),
        'SiteId': (basestring, True),
        'Tags': (Tags, False),
        'Type': (basestring, False),
    }


class GlobalNetwork(AWSObject):
    resource_type = "AWS::NetworkManager::GlobalNetwork"

    props = {
        'Description': (basestring, False),
        'Tags': (Tags, False),
    }


class Device(AWSObject):
    resource_type = "AWS::NetworkManager::Device"

    props = {
        'Description': (basestring, False),
        'GlobalNetworkId': (basestring, True),
        'Location': (basestring, False),
        'Model': (basestring, False),
        'SerialNumber': (basestring, False),
        'SiteId': (basestring, False),
        'Tags': (Tags, False),
        'Type': (basestring, False),
        'Vendor': (basestring, False),
    }


class CustomerGatewayAssociation(AWSObject):
    resource_type = "AWS::NetworkManager::CustomerGatewayAssociation"

    props = {
        'CustomerGatewayArn': (basestring, True),
        'DeviceId': (basestring, True),
        'GlobalNetworkId': (basestring, True),
        'LinkId': (basestring, False),
    }
