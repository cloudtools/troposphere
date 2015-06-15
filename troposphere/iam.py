# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Ref
from .validators import integer, boolean
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
        'Status': (basestring, False),
        'UserName': (basestring, True),
    }


class PolicyType(AWSObject):
    resource_type = "AWS::IAM::Policy"

    props = {
        'Groups': ([basestring, Ref], False),
        'PolicyDocument': (policytypes, True),
        'PolicyName': (basestring, True),
        'Roles': ([basestring, Ref], False),
        'Users': ([basestring, Ref], False),
    }


class Policy(AWSProperty):
    props = {
        'PolicyDocument': (policytypes, True),
        'PolicyName': (basestring, True),
    }

PolicyProperty = Policy


class Group(AWSObject):
    resource_type = "AWS::IAM::Group"

    props = {
        'Path': (basestring, False),
        'Policies': ([Policy], False),
    }


class InstanceProfile(AWSObject):
    resource_type = "AWS::IAM::InstanceProfile"

    props = {
        'Path': (basestring, True),
        'Roles': (list, True),
    }


class Role(AWSObject):
    resource_type = "AWS::IAM::Role"

    props = {
        'AssumeRolePolicyDocument': (policytypes, True),
        'Path': (basestring, True),
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
        'Path': (basestring, False),
        'Groups': ([basestring, Ref], False),
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
        'Groups': ([basestring, Ref], False),
        'Path': (basestring, False),
        'PolicyDocument': (policytypes, True),
        'Roles': ([basestring, Ref], False),
        'Users': ([basestring, Ref], False),
    }
