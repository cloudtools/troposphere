# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, AWSHelperFn
from iam import PolicyDocument

# SQS policy action constants.
AddPermission = "sqs:AddPermission"
ChangeMessageVisibility = "sqs:ChangeMessageVisibility"
ChangeMessageVisibilityBatch = "sqs:ChangeMessageVisibilityBatch"
CreateQueue = "sqs:CreateQueue"
DeleteMessage = "sqs:DeleteMessage"
DeleteMessageBatch = "sqs:DeleteMessageBatch"
DeleteQueue = "sqs:DeleteQueue"
GetQueueAttributes = "sqs:GetQueueAttributes"
GetQueueUrl = "sqs:GetQueueUrl"
ListQueues = "sqs:ListQueues"
ReceiveMessage = "sqs:ReceiveMessage"
RemovePermission = "sqs:RemovePermission"
SendMessage = "sqs:SendMessage"
SendMessageBatch = "sqs:SendMessageBatch"
SetQueueAttributes = "sqs:SetQueueAttributes"


class Queue(AWSObject):
    props = {
        'VisibilityTimeout': (int, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::SQS::Queue"
        sup = super(Queue, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class QueuePolicy(AWSObject):
    props = {
        'PolicyDocument': (PolicyDocument, False),
        'Queues': (list, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::SQS::QueuePolicy"
        sup = super(QueuePolicy, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)
