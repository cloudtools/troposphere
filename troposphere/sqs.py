# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject


class Queue(AWSObject):
    props = {
        'VisibilityTimeout': (basestring, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::SQS::Queue"
        sup = super(Queue, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class QueuePolicy(AWSObject):
    props = {
        'PolicyDocument': (dict, False),
        'Queues': (list, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::SQS::QueuePolicy"
        sup = super(QueuePolicy, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)
