# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, Tags
from .validators import boolean
try:
    from awacs.aws import Policy
    policytypes = (dict, Policy)
except ImportError:
    policytypes = dict,


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
        'Tags': ((Tags, list), False)
    }
