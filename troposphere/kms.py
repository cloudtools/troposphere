# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject
from .validators import boolean
try:
    from awacs.aws import Policy
    policytypes = (dict, Policy)
except ImportError:
    policytypes = dict,


class Key(AWSObject):
    resource_type = "AWS::KMS::Key"

    props = {
        'Description': (basestring, False),
        'Enabled': (boolean, False),
        'EnableKeyRotation': (boolean, False),
        'KeyPolicy': (policytypes, True),
    }
