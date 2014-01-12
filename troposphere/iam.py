# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty, Ref
from .validators import integer
try:
    from awacs.aws import Policy
    policytypes = (dict, Policy)
except ImportError:
    policytypes = dict,


Active = "Active"
Inactive = "Inactive"


class AccessKey(AWSObject):
    type = "AWS::IAM::AccessKey"

    props = {
        'Serial': (integer, False),
        # XXX - Is Status required? Docs say yes, examples say no
        'Status': (basestring, False),
        'UserName': (basestring, True),
    }


class PolicyProps():
    props = {
        'Groups': ([basestring, Ref], False),
        'PolicyDocument': (policytypes, True),
        'PolicyName': (basestring, True),
        'Roles': ([basestring, Ref], False),
        'Users': ([basestring, Ref], False),
    }


class PolicyType(AWSObject, PolicyProps):
    # This is a top-level resource
    type = "AWS::IAM::Policy"


class Policy(AWSProperty, PolicyProps):
    # This is for use in a list with Group (below)
    pass


class Group(AWSObject):
    type = "AWS::IAM::Group"

    props = {
        'Path': (basestring, False),
        'Policies': ([Policy], False),
    }


class InstanceProfile(AWSObject):
    type = "AWS::IAM::InstanceProfile"

    props = {
        'Path': (basestring, True),
        'Roles': (list, True),
    }


class Role(AWSObject):
    type = "AWS::IAM::Role"

    props = {
        'AssumeRolePolicyDocument': (policytypes, True),
        'Path': (basestring, True),
        'Policies': ([Policy], False),
    }


class LoginProfile(AWSHelperFn):
    def __init__(self, data):
        self.data = {'Password': data}

    def JSONrepr(self):
        return self.data


class User(AWSObject):
    type = "AWS::IAM::User"

    props = {
        'Path': (basestring, False),
        'Groups': ([Group], False),
        'LoginProfile': (LoginProfile, False),
        'Policies': ([Policy], False),
    }


class UserToGroupAddition(AWSObject):
    type = "AWS::IAM::UserToGroupAddition"

    props = {
        'GroupName': (basestring, True),
        'Users': (list, True),
    }
