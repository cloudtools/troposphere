# Copyright (c) 2017, Fernando Freire <fernando.freire@nike.com>
# All rights reserved.
#
# See LICENSE file for full license.

import types

from . import AWSObject, AWSProperty
from .awslambda import Environment, VPCConfig, validate_memory_size
from .dynamodb import ProvisionedThroughput
from .validators import positive_integer


def primary_key_type_validator(x):
    valid_types = ["String", "Number", "Binary"]
    if x not in valid_types:
        raise ValueError("KeyType must be one of: %s" % ", ".join(valid_types))
    return x

def policy_validator(x):
    if isinstance(x, types.StringTypes):
        return x
    elif isinstance(x, types.ListType):
        return x
    else:
        raise ValueError("Policies must refer to a managed policy, a list of "
                         + "policies, an IAM policy document, or a list of IAM"
                         + " policy documents")


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
        'Policies': (policy_validator, False),
        'Environment': (Environment, False),
        'VpcConfig': (VPCConfig, False),
        'Events': (dict, False)
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

class EventSource(AWSProperty):
    resource_type = 'S3'

    props = {
        'Type': (basestring, True),
        'Bucket': (basestring, True),
        'Events': (list, True),
        'Filter': (basestring, False)
    }
