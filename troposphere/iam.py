# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject
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


class BasePolicy(AWSObject):
    props = {
        'Groups': (list, False),
        'PolicyDocument': (policytypes, True),
        'PolicyName': (basestring, True),
        'Roles': (list, False),
        'User': (list, False),
    }


class PolicyType(BasePolicy):
    # This is a top-level resource
    type = "AWS::IAM::Policy"


class Policy(BasePolicy):
    # This is for use in a list with Group (below)
    pass


class Group(AWSObject):
    type = "AWS::IAM::Group"

    props = {
        'Path': (basestring, False),
        'Policies': (list, False),
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
        'Policies': (list, False),
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
        'Groups': (list, False),
        'LoginProfile': (LoginProfile, False),
        'Policies': (list, False),
    }


class UserToGroupAddition(AWSObject):
    type = "AWS::IAM::UserToGroupAddition"

    props = {
        'GroupName': (basestring, True),
        'Users': (list, True),
    }
