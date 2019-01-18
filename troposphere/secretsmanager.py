# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import integer, boolean

try:
    from awacs.aws import Policy
    policytypes = (dict, Policy)
except ImportError:
    policytypes = dict,


VALID_TARGET_TYPES = ('AWS::RDS::DBInstance', 'AWS::RDS::DBCluster')


def validate_target_types(target_type):
    """Target types validation rule."""

    if target_type not in VALID_TARGET_TYPES:
        raise ValueError("Target type must be one of : %s" %
                         ", ".join(VALID_TARGET_TYPES))
    return target_type


class ResourcePolicy(AWSObject):
    resource_type = "AWS::SecretsManager::ResourcePolicy"

    props = {
        'SecretId': (basestring, True),
        'ResourcePolicy': (policytypes, True),
    }


class RotationRules(AWSProperty):
    props = {
        'AutomaticallyAfterDays': (integer, False),
    }


class RotationSchedule(AWSObject):
    resource_type = "AWS::SecretsManager::RotationSchedule"

    props = {
        'SecretId': (basestring, True),
        'RotationLambdaARN': (basestring, True),
        'RotationRules': (RotationRules, False)
    }


class SecretTargetAttachment(AWSObject):
    resource_type = "AWS::SecretsManager::SecretTargetAttachment"

    props = {
        'SecretId': (basestring, True),
        'TargetId': (basestring, True),
        'TargetType': (validate_target_types, True),
    }


class GenerateSecretString(AWSProperty):
    props = {
        'ExcludeUppercase': (boolean, False),
        'RequireEachIncludedType': (boolean, False),
        'IncludeSpace': (boolean, False),
        'ExcludeCharacters': (basestring, False),
        'GenerateStringKey': (basestring, False),
        'PasswordLength': (integer, False),
        'ExcludePunctuation': (boolean, False),
        'ExcludeLowercase': (boolean, False),
        'SecretStringTemplate': (basestring, False),
        'ExcludeNumbers': (boolean, False),
    }


class Secret(AWSObject):
    resource_type = "AWS::SecretsManager::Secret"

    props = {
        'Description': (basestring, False),
        'KmsKeyId': (basestring, False),
        'SecretString': (basestring, False),
        'GenerateSecretString': (GenerateSecretString, False),
        'Name': (basestring, False),
        'Tags': ((Tags, list), False),
    }
