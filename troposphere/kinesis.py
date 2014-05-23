# Copyright (c) 2014, Guillem Anguera <ganguera@gmail.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject
from .validators import integer


class Stream(AWSObject):
    type = "AWS::Kinesis::Stream"

    props = {
        'ShardCount': (integer, False),
    }
