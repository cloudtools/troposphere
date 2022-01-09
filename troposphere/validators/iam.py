# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import re

from ..compat import validate_policytype
from . import tags_or_list

Active = "Active"
Inactive = "Inactive"


def iam_group_name(group_name):
    """
    Property: Group.GroupName
    """
    if len(group_name) > 128:
        raise ValueError("IAM Role Name may not exceed 128 characters")
    iam_names(group_name)
    return group_name


def iam_names(b):
    iam_name_re = re.compile(r"^[a-zA-Z0-9_\.\+\=\@\-\,]+$")
    if iam_name_re.match(b):
        return b
    else:
        raise ValueError("%s is not a valid iam name" % b)


def iam_path(path):
    """
    Property: Group.Path
    Property: InstanceProfile.Path
    Property: ManagedPolicy.Path
    Property: Role.Path
    Property: User.Path
    """
    if len(path) > 512:
        raise ValueError("IAM path %s may not exceed 512 characters", path)

    iam_path_re = re.compile(r"^\/.*\/$|^\/$")
    if not iam_path_re.match(path):
        raise ValueError("%s is not a valid iam path name" % path)
    return path


def iam_role_name(role_name):
    """
    Property: Role.RoleName
    """
    if len(role_name) > 64:
        raise ValueError("IAM Role Name may not exceed 64 characters")
    iam_names(role_name)
    return role_name


def iam_user_name(user_name):
    """
    Property: User.UserName
    """
    if not user_name:
        raise ValueError("AWS::IAM::User property 'UserName' may not be empty")

    if len(user_name) > 64:
        raise ValueError(
            "AWS::IAM::User property 'UserName' may not exceed 64 characters"
        )

    iam_user_name_re = re.compile(r"^[\w+=,.@-]+$")
    if iam_user_name_re.match(user_name):
        return user_name
    else:
        raise ValueError(
            "%s is not a valid value for AWS::IAM::User property 'UserName'", user_name
        )


def policytypes(policy):
    """
    Property: ManagedPolicy.PolicyDocument
    Property: Policy.PolicyDocument
    Property: PolicyType.PolicyDocument
    Property: Role.AssumeRolePolicyDocument
    """
    return validate_policytype(policy)


def status(status):
    """
    Property: AccessKey.Status
    """

    valid_statuses = [Active, Inactive]

    if status not in valid_statuses:
        raise ValueError("Status needs to be one of %r" % valid_statuses)
    return status


def validate_tags_or_list(x):
    """
    Property: Role.Tags
    """
    return tags_or_list(x)
