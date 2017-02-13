# Copyright (c) 2017, Fernando Freire <fernando.freire@nike.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .awslambda import Environment, VPCConfig, validate_memory_size
from .dynamodb import ProvisionedThroughput
from .iam import policytypes
from .validators import positive_integer


def primary_key_type_validator(x):
    valid_types = ["String", "Number", "Binary"]
    if x not in valid_types:
        raise ValueError("KeyType must be one of: %s" % ", ".join(valid_types))
    return x


class Function(AWSObject):
    resource_type = "AWS::Serverless::Function"

    props = {
        'Handler': (basestring, True),
        'Runtime': (basestring, True),
        'CodeUri': (basestring, True),
        'Description': (basestring, False),
        'MemorySize': (validate_memory_size, False),
        'Timeout': (positive_integer, False),
        'Role': (basestring, False),
        'Policies': (policytypes, False),  # TODO not sure this is the righht approach
        'Environment': (Environment, False),
        'VpcConfig': (VPCConfig, False),
        'Events': (dict, False)  # TODO this is certainly not the right approach
    }


class Api(AWSObject):
    resource_type = "AWS::Serverless::Api"

    props = {
        'StageName': (basestring, True),
        'DefinitionUri': (basestring, True),
        'CacheClusterEnabled': (bool, False),
        'CacheClusterSize': (basestring, False),
        'Variables': (dict, False)
    }


class PrimaryKey(AWSProperty):
    props = {
        'Name': (basestring, False),
        'Type': (primary_key_type_validator, False)
    }


class SimpleTable(AWSObject):
    resource_type = "AWS::Serverless::SimpleTable"

    props = {
        'PrimaryKey': (PrimaryKey, False),
        'ProvisionedThroughput': (ProvisionedThroughput, False)
    }

class S3EventSource(AWSObject):
    resource_type = 'S3'

    props = {
        'Bucket': (basestring, True),
        'Events': (basestring, True),
        'Filter': (basestring, False)
    }
