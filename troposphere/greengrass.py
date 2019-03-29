# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, integer


class Subscription(AWSProperty):
    props = {
        'Target': (basestring, True),
        'Id': (basestring, True),
        'Source': (basestring, True),
        'Subject': (basestring, True),
    }


class SubscriptionDefinitionVersion(AWSObject):
    resource_type = "AWS::Greengrass::SubscriptionDefinitionVersion"

    props = {
        'SubscriptionDefinitionId': (basestring, True),
        'Subscriptions': ([Subscription], True),
    }
