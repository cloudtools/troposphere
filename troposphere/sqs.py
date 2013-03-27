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
    props = {
        'VisibilityTimeout': (integer, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::SQS::Queue"
        sup = super(Queue, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class QueuePolicy(AWSObject):
    props = {
        'PolicyDocument': (policytypes, False),
        'Queues': (list, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::SQS::QueuePolicy"
        sup = super(QueuePolicy, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)
