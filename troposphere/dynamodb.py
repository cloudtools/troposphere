# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import warnings

from . import AWSHelperFn, AWSObject, AWSProperty

warnings.warn("This module is outdated and will be replaced with "
              "troposphere.dynamodb2. Please see the README for "
              "instructions on how to prepare for this change.")


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
    def __init__(self, ProjectionType, NonKeyAttributes=None):
        self.data = {
            'ProjectionType': ProjectionType
        }
        if NonKeyAttributes is not None:
            self.data['NonKeyAttributes'] = NonKeyAttributes

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


class StreamSpecification(AWSProperty):
        props = {
            'StreamViewType': (basestring, True),
        }


class Table(AWSObject):
    resource_type = "AWS::DynamoDB::Table"

    props = {
        'AttributeDefinitions': ([AttributeDefinition], True),
        'GlobalSecondaryIndexes': ([GlobalSecondaryIndex], False),
        'KeySchema': ([Key], True),
        'LocalSecondaryIndexes': ([LocalSecondaryIndex], False),
        'ProvisionedThroughput': (ProvisionedThroughput, True),
        'StreamSpecification': (StreamSpecification, False),
        'TableName': (basestring, False),
    }
