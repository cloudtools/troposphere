# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import integer
try:
    from awacs.aws import Policy
    policytypes = (dict, Policy)
except ImportError:
    policytypes = dict,


class RedrivePolicy(AWSProperty):
    props = {
        'deadLetterTargetArn': (basestring, False),
        'maxReceiveCount': (integer, False),
    }


class Queue(AWSObject):
    resource_type = "AWS::SQS::Queue"

    props = {
        'DelaySeconds': (integer, False),
        'MaximumMessageSize': (integer, False),
        'MessageRetentionPeriod': (integer, False),
        'QueueName': (basestring, False),
        'ReceiveMessageWaitTimeSeconds': (integer, False),
        'RedrivePolicy': (RedrivePolicy, False),
        'VisibilityTimeout': (integer, False),
    }


class QueuePolicy(AWSObject):
    resource_type = "AWS::SQS::QueuePolicy"

    props = {
        'PolicyDocument': (policytypes, False),
        'Queues': (list, True),
    }
