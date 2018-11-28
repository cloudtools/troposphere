# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean


class Spend(AWSProperty):
    props = {
        'Amount': (float, True),
        'Unit': (basestring, True),
    }


class CostTypes(AWSProperty):
    props = {
        'IncludeCredit': (boolean, False),
        'IncludeDiscount': (boolean, False),
        'IncludeOtherSubscription': (boolean, False),
        'IncludeRecurring': (boolean, False),
        'IncludeRefund': (boolean, False),
        'IncludeSubscription': (boolean, False),
        'IncludeSupport': (boolean, False),
        'IncludeTax': (boolean, False),
        'IncludeUpfront': (boolean, False),
        'UseAmortized': (boolean, False),
        'UseBlended': (boolean, False),
    }


class TimePeriod(AWSProperty):
    props = {
        'End': (basestring, False),
        'Start': (basestring, False),
    }


class BudgetData(AWSProperty):
    props = {
        'BudgetLimit': (Spend, False),
        'BudgetName': (basestring, False),
        'BudgetType': (basestring, True),
        'CostFilters': (dict, False),
        'CostTypes': (CostTypes, False),
        'TimePeriod': (TimePeriod, False),
        'TimeUnit': (basestring, True),
    }


class Notification(AWSProperty):
    props = {
        'ComparisonOperator': (basestring, True),
        'NotificationType': (basestring, True),
        'Threshold': (float, True),
        'ThresholdType': (basestring, False),
    }


class Subscriber(AWSProperty):
    props = {
        'Address': (basestring, True),
        'SubscriptionType': (basestring, True),
    }


class NotificationWithSubscribers(AWSProperty):
    props = {
        'Notification': (Notification, True),
        'Subscribers': ([Subscriber], True),
    }


class Budget(AWSObject):
    resource_type = "AWS::Budgets::Budget"

    props = {
        'Budget': (BudgetData, True),
        'NotificationsWithSubscribers':
            ([NotificationWithSubscribers], False),
    }
