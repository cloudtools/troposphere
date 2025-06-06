# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double


class CRL(AWSObject):
    """
    `CRL <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-crl.html>`__
    """

    resource_type = "AWS::RolesAnywhere::CRL"

    props: PropsDictType = {
        "CrlData": (str, True),
        "Enabled": (boolean, False),
        "Name": (str, True),
        "Tags": (Tags, False),
        "TrustAnchorArn": (str, False),
    }


class MappingRule(AWSProperty):
    """
    `MappingRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-profile-mappingrule.html>`__
    """

    props: PropsDictType = {
        "Specifier": (str, True),
    }


class AttributeMapping(AWSProperty):
    """
    `AttributeMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-profile-attributemapping.html>`__
    """

    props: PropsDictType = {
        "CertificateField": (str, True),
        "MappingRules": ([MappingRule], True),
    }


class Profile(AWSObject):
    """
    `Profile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html>`__
    """

    resource_type = "AWS::RolesAnywhere::Profile"

    props: PropsDictType = {
        "AcceptRoleSessionName": (boolean, False),
        "AttributeMappings": ([AttributeMapping], False),
        "DurationSeconds": (double, False),
        "Enabled": (boolean, False),
        "ManagedPolicyArns": ([str], False),
        "Name": (str, True),
        "RequireInstanceProperties": (boolean, False),
        "RoleArns": ([str], True),
        "SessionPolicy": (str, False),
        "Tags": (Tags, False),
    }


class NotificationSetting(AWSProperty):
    """
    `NotificationSetting <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-notificationsetting.html>`__
    """

    props: PropsDictType = {
        "Channel": (str, False),
        "Enabled": (boolean, True),
        "Event": (str, True),
        "Threshold": (double, False),
    }


class SourceData(AWSProperty):
    """
    `SourceData <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-sourcedata.html>`__
    """

    props: PropsDictType = {
        "AcmPcaArn": (str, False),
        "X509CertificateData": (str, False),
    }


class Source(AWSProperty):
    """
    `Source <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-source.html>`__
    """

    props: PropsDictType = {
        "SourceData": (SourceData, True),
        "SourceType": (str, True),
    }


class TrustAnchor(AWSObject):
    """
    `TrustAnchor <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-trustanchor.html>`__
    """

    resource_type = "AWS::RolesAnywhere::TrustAnchor"

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "Name": (str, True),
        "NotificationSettings": ([NotificationSetting], False),
        "Source": (Source, True),
        "Tags": (Tags, False),
    }
