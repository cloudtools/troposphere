# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 25.0.0


from . import AWSObject
from . import AWSProperty
from troposphere import Tags


class Assignment(AWSObject):
    resource_type = "AWS::SSO::Assignment"

    props = {
        'InstanceArn': (basestring, True),
        'PermissionSetArn': (basestring, True),
        'PrincipalId': (basestring, True),
        'PrincipalType': (basestring, True),
        'TargetId': (basestring, True),
        'TargetType': (basestring, True),
    }


class AccessControlAttributeValueSourceList(AWSProperty):
    props = {
        'AccessControlAttributeValueSourceList': ([basestring], False),
    }


class AccessControlAttributeValue(AWSProperty):
    props = {
        'Source': (AccessControlAttributeValueSourceList, True),
    }


class AccessControlAttribute(AWSProperty):
    props = {
        'Key': (basestring, True),
        'Value': (AccessControlAttributeValue, True),
    }


class InstanceAccessControlAttributeConfiguration(AWSObject):
    resource_type = "AWS::SSO::InstanceAccessControlAttributeConfiguration"

    props = {
        'AccessControlAttributes': ([AccessControlAttribute], False),
        'InstanceAccessControlAttributeConfiguration': (dict, False),
        'InstanceArn': (basestring, True),
    }


class PermissionSet(AWSObject):
    resource_type = "AWS::SSO::PermissionSet"

    props = {
        'Description': (basestring, False),
        'InlinePolicy': (dict, False),
        'InstanceArn': (basestring, True),
        'ManagedPolicies': ([basestring], False),
        'Name': (basestring, True),
        'RelayStateType': (basestring, False),
        'SessionDuration': (basestring, False),
        'Tags': (Tags, False),
    }
