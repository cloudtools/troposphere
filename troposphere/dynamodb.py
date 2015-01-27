# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import re

from . import AWSHelperFn, AWSObject, AWSProperty


class AttributeDefinition(AWSHelperFn):
    def __init__(self, name, type):
        self.data = {
            'AttributeName': name,
            'AttributeType': type,
        }

    def JSONrepr(self):
        return self.data


class Key(AWSProperty):
    def __init__(self, AttributeName, KeyType):
        self.data = {
            'AttributeName': AttributeName,
            'KeyType': KeyType,
        }

    def JSONrepr(self):
        return self.data


class ProvisionedThroughput(AWSHelperFn):
    def __init__(self, ReadCapacityUnits, WriteCapacityUnits):
        self.data = {
            'ReadCapacityUnits': ReadCapacityUnits,
            'WriteCapacityUnits': WriteCapacityUnits,
        }

    def JSONrepr(self):
        return self.data


class Projection(AWSHelperFn):
    def __init__(self, ProjectionType):
        self.data = {
            'ProjectionType': ProjectionType,
        }

    def JSONrepr(self):
        return self.data


class GlobalSecondaryIndex(AWSHelperFn):
    def __init__(self, IndexName, KeySchema, Projection,
                 ProvisionedThroughput):
        self.data = {
            'IndexName': IndexName,
            'KeySchema': KeySchema,
            'Projection': Projection,
            'ProvisionedThroughput': ProvisionedThroughput,
        }

    def JSONrepr(self):
        return self.data


class LocalSecondaryIndex(AWSHelperFn):
    def __init__(self, IndexName, KeySchema, Projection,
                 ProvisionedThroughput):
        self.data = {
            'IndexName': IndexName,
            'KeySchema': KeySchema,
            'Projection': Projection,
        }

    def JSONrepr(self):
        return self.data


class Table(AWSObject):
    resource_type = "AWS::DynamoDB::Table"

    valid_names = re.compile(r'^[a-zA-Z0-9._-]+$')

    props = {
        'KeySchema': ([Key], True),
        'ProvisionedThroughput': (ProvisionedThroughput, True),
        'AttributeDefinitions': ([AttributeDefinition], False),
        'TableName': (basestring, False),
        'GlobalSecondaryIndexes': ([GlobalSecondaryIndex], False),
        'LocalSecondaryIndexes': ([LocalSecondaryIndex], False),
    }
