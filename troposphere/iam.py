# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import integer, boolean, status
from .validators import iam_path, iam_role_name, iam_group_name

try:
    from awacs.aws import Policy
    policytypes = (dict, Policy)
except ImportError:
    policytypes = dict,


Active = "Active"
Inactive = "Inactive"


class AccessKey(AWSObject):
    resource_type = "AWS::IAM::AccessKey"

    props = {
        'Serial': (integer, False),
        # XXX - Is Status required? Docs say yes, examples say no
        'Status': (status, True),
        'UserName': (basestring, True),
    }


class PolicyType(AWSObject):
    resource_type = "AWS::IAM::Policy"

    props = {
        'Groups': ([basestring], False),
        'PolicyDocument': (policytypes, True),
        'PolicyName': (basestring, True),
        'Roles': ([basestring], False),
        'Users': ([basestring], False),
    }


class Policy(AWSProperty):
    props = {
        'PolicyDocument': (policytypes, True),
        'PolicyName': (basestring, True),
    }

PolicyProperty = Policy


class Group(AWSObject):
    def validate_title(self):
        iam_group_name(self.title)

    resource_type = "AWS::IAM::Group"

    props = {
        'ManagedPolicyArns': ([basestring], False),
        'Path': (iam_path, False),
        'Policies': ([Policy], False),
    }


class InstanceProfile(AWSObject):
    resource_type = "AWS::IAM::InstanceProfile"

    props = {
        'Path': (iam_path, False),
        'Roles': (list, True),
    }


class Role(AWSObject):
    def validate_title(self):
        iam_role_name(self.title)

    resource_type = "AWS::IAM::Role"

    props = {
        'AssumeRolePolicyDocument': (policytypes, True),
        'ManagedPolicyArns': ([basestring], False),
        'Path': (iam_path, False),
        'Policies': ([Policy], False),
    }


class LoginProfile(AWSProperty):
    props = {
        'Password': (basestring, True),
        'PasswordResetRequired': (boolean, False),
    }


class User(AWSObject):
    resource_type = "AWS::IAM::User"

    props = {
        'Path': (iam_path, False),
        'Groups': ([basestring], False),
        'ManagedPolicyArns': ([basestring], False),
        'LoginProfile': (LoginProfile, False),
        'Policies': ([Policy], False),
    }


class UserToGroupAddition(AWSObject):
    resource_type = "AWS::IAM::UserToGroupAddition"

    props = {
        'GroupName': (basestring, True),
        'Users': (list, True),
    }


class ManagedPolicy(AWSObject):
    resource_type = "AWS::IAM::ManagedPolicy"

    props = {
        'Description': (basestring, False),
        'Groups': ([basestring], False),
        'Path': (iam_path, False),
        'PolicyDocument': (policytypes, True),
        'Roles': ([basestring], False),
        'Users': ([basestring], False),
    }
