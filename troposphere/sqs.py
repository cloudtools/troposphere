# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty
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
        'ContentBasedDeduplication': (bool, False),
        'DelaySeconds': (integer, False),
        'FifoQueue': (bool, False),
        'KmsMasterKeyId': (basestring, False),
        'KmsDataKeyReusePeriodSeconds': (integer, False),
        'MaximumMessageSize': (integer, False),
        'MessageRetentionPeriod': (integer, False),
        'QueueName': (basestring, False),
        'ReceiveMessageWaitTimeSeconds': (integer, False),
        'RedrivePolicy': (RedrivePolicy, False),
        'VisibilityTimeout': (integer, False),
    }

    def validate(self):
        if self.properties.get('FifoQueue'):
            queuename = self.properties.get('QueueName')
            if queuename is None or isinstance(queuename, AWSHelperFn):
                pass
            elif not queuename.endswith('.fifo'):
                raise ValueError("SQS: FIFO queues need to provide a "
                                 "QueueName that ends with '.fifo'")


class QueuePolicy(AWSObject):
    resource_type = "AWS::SQS::QueuePolicy"

    props = {
        'PolicyDocument': (policytypes, False),
        'Queues': (list, True),
    }
