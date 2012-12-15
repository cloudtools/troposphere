# Copyright (c) 2011-2012, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import json
from . import AWSHelperFn, AWSObject


class Element(AWSHelperFn):
    def __init__(self, name, type):
        self.data = {
            'AttributeName': name,
            'AttributeType': type,
        }

    def JSONrepr(self):
        return self.data


class PrimaryKey(AWSObject):
    props = {
        'HashKeyElement': (Element, True),
        'RangeKeyElement': (Element, False),
    }

    def __init__(self, **kwargs):
        sup = super(PrimaryKey, self)
        sup.__init__(None, props=self.props, **kwargs)


class ProvisionedThroughput(AWSHelperFn):
    def __init__(self, ReadCapacityUnits, WriteCapacityUnits):
        self.data = {
            'ReadCapacityUnits': ReadCapacityUnits,
            'WriteCapacityUnits': WriteCapacityUnits,
        }

    def JSONrepr(self):
        return self.data


class Table(AWSObject):
    props = {
        'KeySchema': (PrimaryKey, True),
        'ProvisionedThroughput': (ProvisionedThroughput, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::DynamoDB::Table"
        sup = super(Table, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)
