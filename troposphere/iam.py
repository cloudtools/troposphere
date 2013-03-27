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
    props = {
        'Serial': (integer, False),
        # XXX - Is Status required? Docs say yes, examples say no
        'Status': (basestring, False),
        'UserName': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::IAM::AccessKey"
        sup = super(AccessKey, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class BasePolicy(AWSObject):
    props = {
        'Groups': (list, False),
        'PolicyDocument': (policytypes, True),
        'PolicyName': (basestring, True),
        'Roles': (list, False),
        'User': (list, False),
    }

    def __init__(self, name, type, propname, **kwargs):
        sup = super(BasePolicy, self)
        sup.__init__(name, type, propname, self.props, **kwargs)


class PolicyType(BasePolicy):
    # This is a top-level resource
    def __init__(self, name, **kwargs):
        self.type = "AWS::IAM::Policy"
        sup = super(PolicyType, self)
        sup.__init__(name, self.type, "Properties", **kwargs)


class Policy(BasePolicy):
    # This is for use in a list with Group (below)
    def __init__(self, name, **kwargs):
        sup = super(Policy, self)
        sup.__init__(name, None, None, **kwargs)


class Group(AWSObject):
    props = {
        'Path': (basestring, False),
        'Policies': (list, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::IAM::Group"
        sup = super(Group, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class InstanceProfile(AWSObject):
    props = {
        'Path': (basestring, True),
        'Roles': (list, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::IAM::InstanceProfile"
        sup = super(InstanceProfile, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class Role(AWSObject):
    props = {
        'AssumeRolePolicyDocument': (policytypes, True),
        'Path': (basestring, True),
        'Policies': (list, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::IAM::Role"
        sup = super(Role, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class LoginProfile(AWSHelperFn):
    def __init__(self, data):
        self.data = {'Password': data}

    def JSONrepr(self):
        return self.data


class User(AWSObject):
    props = {
        'Path': (basestring, False),
        'Groups': (list, False),
        'LoginProfile': (LoginProfile, False),
        'Policies': (list, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::IAM::User"
        sup = super(User, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class UserToGroupAddition(AWSObject):
    props = {
        'GroupName': (basestring, True),
        'Users': (list, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::IAM::UserToGroupAddition"
        sup = super(UserToGroupAddition, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)
