# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject
from .validators import integer
try:
    from awacs.aws import Policy
    policytypes = (dict, Policy)
except ImportError:
    policytypes = dict,


class Queue(AWSObject):
    type = "AWS::SQS::Queue"

    props = {
        'VisibilityTimeout': (integer, False),
    }


class QueuePolicy(AWSObject):
    type = "AWS::SQS::QueuePolicy"

    props = {
        'PolicyDocument': (policytypes, False),
        'Queues': (list, True),
    }
