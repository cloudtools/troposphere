# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, Tags
from .compat import policytypes
from .validators import boolean, integer_range, key_usage_type


class Alias(AWSObject):
    resource_type = "AWS::KMS::Alias"

    props = {
        'AliasName': (basestring, True),
        'TargetKeyId': (basestring, True)
    }


class Key(AWSObject):
    resource_type = "AWS::KMS::Key"

    props = {
        'Description': (basestring, False),
        'Enabled': (boolean, False),
        'EnableKeyRotation': (boolean, False),
        'KeyPolicy': (policytypes, True),
        'KeyUsage': (key_usage_type, False),
        'PendingWindowInDays': (integer_range(7, 30), False),
        'Tags': ((Tags, list), False)
    }
