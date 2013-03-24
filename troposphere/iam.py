# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty


Active = "Active"
Inactive = "Inactive"

# Policy effect constants.
Allow = "Allow"
Deny = "Deny"

# Policy principal constants.
Everybody = "*"

# Policy condition key constants.
CurrentTime = "aws:CurrentTime"
EpochTime = "aws:EpochTime"
MultiFactorAuthAge = "aws:MultiFactorAuthAge"
Referer = "aws:Referer"
SecureTransport = "aws:SecureTransport"
SourceArn = "aws:SourceArn"
SourceIp = "aws:SourceIp"
UserAgent = "aws:UserAgent"

# Policy condition operator constants.
ArnEquals = "ArnEquals"
ArnNotEquals = "ArnNotEquals"
ArnLike = "ArnLike"
ArnNotLike = "ArnNotLike"
Bool = "Bool"
DateEquals = "DateEquals"
DateNotEquals = "DateNotEquals"
DateLessThan = "DateLessThan"
DateLessThanEquals = "DateLessThanEquals"
DateGreaterThan = "DateGreaterThan"
DateGreaterThanEquals = "DateGreaterThanEquals"
IpAddress = "IpAddress"
NotIpAddress = "NotIpAddress"
NumericEquals = "NumericEquals"
NumericNotEquals = "NumericNotEquals"
NumericLessThan = "NumericLessThan"
NumericLessThanEquals = "NumericLessThanEquals"
NumericGreaterThan = "NumericGreaterThan"
NumericGreaterThanEquals = "NumericGreaterThanEquals"
StringEquals = "StringEquals"
StringNotEquals = "StringNotEquals"
StringEqualsIgnoresCase = "StringEqualsIgnoresCase"
StringLike = "StringLike"
StringNotLike = "StringNotLike"


class AccessKey(AWSObject):
    props = {
        'Serial': (int, False),
        # XXX - Is Status required? Docs say yes, examples say no
        'Status': (basestring, False),
        'UserName': (basestring, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::IAM::AccessKey"
        sup = super(AccessKey, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class Principal(AWSHelperFn):
    def __init__(self, principals):
        self.data = {'AWS': [principals]}

    def JSONrepr(self):
        return self.data


class Statement(AWSProperty):
    props = {
        'Action': (list, False),
        'Condition': (dict, False),
        'Effect': (basestring, True),
        'NotAction': (list, False),
        'NotPrincipal': (list, False),
        'Principal': (Principal, False),
        'Resource': (list, False),
        'NotResource': (list, False),
        'Sid': (basestring, False),
    }


class PolicyDocument(AWSProperty):
    props = {
        'Id': (basestring, False),
        'Statement': (list, True),
        'Version': (basestring, False),
    }


class BasePolicy(AWSObject):
    props = {
        'Groups': (list, False),
        'PolicyDocument': (PolicyDocument, True),
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
        'AssumeRolePolicyDocument': (dict, True),
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
