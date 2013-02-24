# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty


class Element(AWSHelperFn):
    def __init__(self, name, type):
        self.data = {
            'AttributeName': name,
            'AttributeType': type,
        }

    def JSONrepr(self):
        return self.data


class PrimaryKey(AWSProperty):
    props = {
        'HashKeyElement': (Element, True),
        'RangeKeyElement': (Element, False),
    }


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
