# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .compat import policytypes
from .validators import boolean


class Subscription(AWSProperty):
    props = {
        'Endpoint': (basestring, True),
        'Protocol': (basestring, True),
    }


class SubscriptionResource(AWSObject):
    resource_type = "AWS::SNS::Subscription"

    props = {
        'DeliveryPolicy': (dict, False),
        'Endpoint': (basestring, False),
        'FilterPolicy': (dict, False),
        'Protocol': (basestring, True),
        'RawMessageDelivery': (boolean, False),
        'RedrivePolicy': (dict, False),
        'Region': (basestring, False),
        'TopicArn': (basestring, True),
    }


class TopicPolicy(AWSObject):
    resource_type = "AWS::SNS::TopicPolicy"

    props = {
        'PolicyDocument': (policytypes, True),
        'Topics': (list, True),
    }


class Topic(AWSObject):
    resource_type = "AWS::SNS::Topic"

    props = {
        'DisplayName': (basestring, False),
        'KmsMasterKeyId': (basestring, False),
        'Subscription': ([Subscription], False),
        'Tags': (Tags, False),
        'TopicName': (basestring, False),
    }
