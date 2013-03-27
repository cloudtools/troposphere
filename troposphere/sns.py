# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
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


class TopicPolicy(AWSObject):
    props = {
        'PolicyDocument': (policytypes, True),
        'Topics': (list, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::SNS::TopicPolicy"
        sup = super(TopicPolicy, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class Topic(AWSObject):
    props = {
        'DisplayName': (basestring, False),
        'Subscription': ([Subscription], True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::SNS::Topic"
        sup = super(Topic, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)
