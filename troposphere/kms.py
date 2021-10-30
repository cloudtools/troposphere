# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, Tags
from .compat import policytypes
from .validators import boolean, integer, integer_range, key_usage_type


class Alias(AWSObject):
    resource_type = "AWS::KMS::Alias"

    props = {"AliasName": (str, True), "TargetKeyId": (str, True)}


class Key(AWSObject):
    resource_type = "AWS::KMS::Key"

    props = {
        "Description": (str, False),
        "EnableKeyRotation": (boolean, False),
        "Enabled": (boolean, False),
        "KeyPolicy": (policytypes, True),
        "KeySpec": (str, False),
        "KeyUsage": (key_usage_type, False),
        "MultiRegion": (boolean, False),
        "PendingWindowInDays": (integer_range(7, 30), False),
        "Tags": ((Tags, list), False),
    }


class ReplicaKey(AWSObject):
    resource_type = "AWS::KMS::ReplicaKey"

    props = {
        "Description": (str, False),
        "Enabled": (boolean, False),
        "KeyPolicy": (dict, True),
        "PendingWindowInDays": (integer, False),
        "PrimaryKeyArn": (str, True),
        "Tags": (Tags, False),
    }
