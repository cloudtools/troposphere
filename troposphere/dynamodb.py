# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean


def attribute_type_validator(x):
    valid_types = ["S", "N", "B"]
    if x not in valid_types:
        raise ValueError("AttributeType must be one of: %s" %
                         ", ".join(valid_types))
    return x


def key_type_validator(x):
    valid_types = ["HASH", "RANGE"]
    if x not in valid_types:
        raise ValueError("KeyType must be one of: %s" % ", ".join(valid_types))
    return x


def projection_type_validator(x):
    valid_types = ["KEYS_ONLY", "INCLUDE", "ALL"]
    if x not in valid_types:
        raise ValueError("ProjectionType must be one of: %s" %
                         ", ".join(valid_types))
    return x


class AttributeDefinition(AWSProperty):
    props = {
        "AttributeName": (basestring, True),
        "AttributeType": (attribute_type_validator, True),
    }


class KeySchema(AWSProperty):
    props = {
        "AttributeName": (basestring, True),
        "KeyType": (key_type_validator, True)
    }


class Key(KeySchema):
    """ For backwards compatibility. """
    pass


class ProvisionedThroughput(AWSProperty):
    props = {
        "ReadCapacityUnits": (int, True),
        "WriteCapacityUnits": (int, True),
    }


class Projection(AWSProperty):
    props = {
        "NonKeyAttributes": ([basestring], False),
        "ProjectionType": (projection_type_validator, False)
    }


class SSESpecification(AWSProperty):
    props = {
        "SSEEnabled": (boolean, True),
    }


class GlobalSecondaryIndex(AWSProperty):
    props = {
        "IndexName": (basestring, True),
        "KeySchema": ([KeySchema], True),
        "Projection": (Projection, True),
        "ProvisionedThroughput": (ProvisionedThroughput, True)
    }


class LocalSecondaryIndex(AWSProperty):
    props = {
        "IndexName": (basestring, True),
        "KeySchema": ([KeySchema], True),
        "Projection": (Projection, True),
    }


class StreamSpecification(AWSProperty):
        props = {
            'StreamViewType': (basestring, True),
        }


class TimeToLiveSpecification(AWSProperty):
        props = {
            'AttributeName': (basestring, True),
            'Enabled': (boolean, True),
        }


class Table(AWSObject):
    resource_type = "AWS::DynamoDB::Table"

    props = {
        'AttributeDefinitions': ([AttributeDefinition], True),
        'GlobalSecondaryIndexes': ([GlobalSecondaryIndex], False),
        'KeySchema': ([KeySchema], True),
        'LocalSecondaryIndexes': ([LocalSecondaryIndex], False),
        'ProvisionedThroughput': (ProvisionedThroughput, True),
        'SSESpecification': (SSESpecification, False),
        'StreamSpecification': (StreamSpecification, False),
        'TableName': (basestring, False),
        'Tags': (Tags, False),
        'TimeToLiveSpecification': (TimeToLiveSpecification, False),
    }
