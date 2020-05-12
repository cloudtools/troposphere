# Copyright (c) 2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject


class CostCategory(AWSObject):
    resource_type = "AWS::CE::CostCategory"

    props = {
        'Name': (basestring, True),
        'Rules': (basestring, True),
        'RuleVersion': (basestring, True),
    }
