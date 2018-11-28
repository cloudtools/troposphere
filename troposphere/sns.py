# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean
try:
    from awacs.aws import Policy
    policytypes = (dict, Policy)
except ImportError:
    policytypes = dict,


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
        'Subscription': ([Subscription], False),
        'TopicName': (basestring, False),
    }
