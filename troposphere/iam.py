# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .compat import policytypes
from .validators import integer, boolean, status
from .validators import iam_path, iam_role_name, iam_group_name, iam_user_name

Active = "Active"
Inactive = "Inactive"


class AccessKey(AWSObject):
    resource_type = "AWS::IAM::AccessKey"

    props = {
        'Serial': (integer, False),
        'Status': (status, False),
        'UserName': (str, True),
    }


class PolicyType(AWSObject):
    resource_type = "AWS::IAM::Policy"

    props = {
        'Groups': ([str], False),
        'PolicyDocument': (policytypes, True),
        'PolicyName': (str, True),
        'Roles': ([str], False),
        'Users': ([str], False),
    }


class Policy(AWSProperty):
    props = {
        'PolicyDocument': (policytypes, True),
        'PolicyName': (str, True),
    }


PolicyProperty = Policy


class Group(AWSObject):
    resource_type = "AWS::IAM::Group"

    props = {
        'GroupName': (iam_group_name, False),
        'ManagedPolicyArns': ([str], False),
        'Path': (iam_path, False),
        'Policies': ([Policy], False),
    }


class InstanceProfile(AWSObject):
    resource_type = "AWS::IAM::InstanceProfile"

    props = {
        'InstanceProfileName': (str, False),
        'Path': (iam_path, False),
        'Roles': (list, True),
    }


class ManagedPolicy(AWSObject):
    resource_type = "AWS::IAM::ManagedPolicy"

    props = {
        'Description': (str, False),
        'Groups': ([str], False),
        'ManagedPolicyName': (str, False),
        'Path': (iam_path, False),
        'PolicyDocument': (policytypes, True),
        'Roles': ([str], False),
        'Users': ([str], False),
    }


class OIDCProvider(AWSObject):
    resource_type = "AWS::IAM::OIDCProvider"

    props = {
        'ClientIdList': ([str], False),
        'Tags': (Tags, False),
        'ThumbprintList': ([str], True),
        'Url': (str, False),
    }


class Role(AWSObject):
    resource_type = "AWS::IAM::Role"

    props = {
        'AssumeRolePolicyDocument': (policytypes, True),
        'Description': (str, False),
        'ManagedPolicyArns': ([str], False),
        'MaxSessionDuration': (integer, False),
        'Path': (iam_path, False),
        'PermissionsBoundary': (str, False),
        'Policies': ([Policy], False),
        'RoleName': (iam_role_name, False),
        'Tags': ((Tags, list), False),
    }


class SAMLProvider(AWSObject):
    resource_type = "AWS::IAM::SAMLProvider"

    props = {
        'Name': (str, False),
        'SamlMetadataDocument': (str, True),
        'Tags': (Tags, False),
    }


class ServerCertificate(AWSObject):
    resource_type = "AWS::IAM::ServerCertificate"

    props = {
        'CertificateBody': (str, False),
        'CertificateChain': (str, False),
        'Path': (str, False),
        'PrivateKey': (str, False),
        'ServerCertificateName': (str, False),
        'Tags': (Tags, False),
    }


class ServiceLinkedRole(AWSObject):
    resource_type = "AWS::IAM::ServiceLinkedRole"

    props = {
        'AWSServiceName': (str, True),
        'CustomSuffix': (str, False),
        'Description': (str, False),
    }


class LoginProfile(AWSProperty):
    props = {
        'Password': (str, True),
        'PasswordResetRequired': (boolean, False),
    }


class User(AWSObject):
    resource_type = "AWS::IAM::User"

    props = {
        'Groups': ([str], False),
        'LoginProfile': (LoginProfile, False),
        'ManagedPolicyArns': ([str], False),
        'Path': (iam_path, False),
        'PermissionsBoundary': (str, False),
        'Policies': ([Policy], False),
        'Tags': (Tags, False),
        'UserName': (iam_user_name, False),
    }


class UserToGroupAddition(AWSObject):
    resource_type = "AWS::IAM::UserToGroupAddition"

    props = {
        'GroupName': (str, True),
        'Users': (list, True),
    }


class VirtualMFADevice(AWSObject):
    resource_type = "AWS::IAM::VirtualMFADevice"

    props = {
        'Path': (str, False),
        'Tags': (Tags, False),
        'Users': ([str], True),
        'VirtualMfaDeviceName': (str, False),
    }
