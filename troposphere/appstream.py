# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, integer


class ServiceAccountCredentials(AWSProperty):
    props = {
        'AccountName': (basestring, True),
        'AccountPassword': (basestring, True),
    }


class DirectoryConfig(AWSObject):
    resource_type = "AWS::AppStream::DirectoryConfig"

    props = {
        'DirectoryName': (basestring, True),
        'OrganizationalUnitDistinguishedNames': ([basestring], True),
        'ServiceAccountCredentials': (ServiceAccountCredentials, True),
    }


class ComputeCapacity(AWSProperty):
    props = {
        'DesiredInstances': (integer, True),
    }


class VpcConfig(AWSProperty):
    props = {
        'SecurityGroupIds': ([basestring], False),
        'SubnetIds': ([basestring], False),
    }


class DomainJoinInfo(AWSProperty):
    props = {
        'DirectoryName': (basestring, False),
        'OrganizationalUnitDistinguishedName': (basestring, False),
    }


class Fleet(AWSObject):
    resource_type = "AWS::AppStream::Fleet"

    props = {
        'ComputeCapacity': (ComputeCapacity, True),
        'Description': (basestring, False),
        'DisconnectTimeoutInSeconds': (integer, False),
        'DisplayName': (basestring, False),
        'DomainJoinInfo': (DomainJoinInfo, False),
        'EnableDefaultInternetAccess': (boolean, False),
        'FleetType': (basestring, False),
        'ImageArn': (basestring, False),
        'ImageName': (basestring, False),
        'InstanceType': (basestring, True),
        'MaxUserDurationInSeconds': (integer, False),
        'Name': (basestring, False),
        'VpcConfig': (VpcConfig, False),
    }


class ImageBuilder(AWSObject):
    resource_type = "AWS::AppStream::ImageBuilder"

    props = {
        'AppstreamAgentVersion': (basestring, False),
        'Description': (basestring, False),
        'DisplayName': (basestring, False),
        'DomainJoinInfo': (DomainJoinInfo, False),
        'EnableDefaultInternetAccess': (boolean, False),
        'ImageArn': (basestring, False),
        'ImageName': (basestring, False),
        'InstanceType': (basestring, True),
        'Name': (basestring, False),
        'VpcConfig': (VpcConfig, False),
    }


class StackFleetAssociation(AWSObject):
    resource_type = "AWS::AppStream::StackFleetAssociation"

    props = {
        'FleetName': (basestring, True),
        'StackName': (basestring, True),
    }


class StorageConnector(AWSProperty):
    props = {
        'ConnectorType': (basestring, True),
        'Domains': ([basestring], False),
        'ResourceIdentifier': (basestring, False),
    }


class UserSetting(AWSProperty):
    props = {
        'Action': (basestring, True),
        'Permission': (basestring, True),
    }


class ApplicationSettings(AWSProperty):
    props = {
        'Enabled': (boolean, True),
        'SettingsGroup': (basestring, False),
    }


class Stack(AWSObject):
    resource_type = "AWS::AppStream::Stack"

    props = {
        'ApplicationSettings': (ApplicationSettings, False),
        'AttributesToDelete': ([basestring], False),
        'DeleteStorageConnectors': (boolean, False),
        'Description': (basestring, False),
        'DisplayName': (basestring, False),
        'FeedbackURL': (basestring, False),
        'Name': (basestring, False),
        'RedirectURL': (basestring, False),
        'StorageConnectors': ([StorageConnector], False),
        'UserSettings': ([UserSetting], False),
    }


class StackUserAssociation(AWSObject):
    resource_type = "AWS::AppStream::StackUserAssociation"

    props = {
        'AuthenticationType': (basestring, True),
        'SendEmailNotification': (boolean, False),
        'StackName': (basestring, True),
        'UserName': (basestring, True),
    }


class User(AWSObject):
    resource_type = "AWS::AppStream::User"

    props = {
        'AuthenticationType': (basestring, True),
        'FirstName': (basestring, False),
        'LastName': (basestring, False),
        'MessageAction': (basestring, False),
        'UserName': (basestring, True),
    }
