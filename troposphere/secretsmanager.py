# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .compat import policytypes
from .validators import integer, boolean

VALID_TARGET_TYPES = ('AWS::RDS::DBInstance', 'AWS::RDS::DBCluster',
                      'AWS::Redshift::Cluster', 'AWS::DocDB::DBInstance',
                      'AWS::DocDB::DBCluster')


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


class HostedRotationLambda(AWSProperty):
    props = {
        'KmsKeyArn': (basestring, False),
        'MasterSecretArn': (basestring, False),
        'MasterSecretKmsKeyArn': (basestring, False),
        'RotationLambdaName': (basestring, False),
        'RotationType': (basestring, True),
        'VpcSecurityGroupIds': (basestring, False),
        'VpcSubnetIds': (basestring, False),
    }


class RotationRules(AWSProperty):
    props = {
        'AutomaticallyAfterDays': (integer, False),
    }


class RotationSchedule(AWSObject):
    resource_type = "AWS::SecretsManager::RotationSchedule"

    props = {
        'HostedRotationLambda': (HostedRotationLambda, False),
        'RotationLambdaARN': (basestring, False),
        'RotationRules': (RotationRules, False),
        'SecretId': (basestring, True),
    }


class GenerateSecretString(AWSProperty):
    props = {
        'ExcludeCharacters': (basestring, False),
        'ExcludeLowercase': (boolean, False),
        'ExcludeNumbers': (boolean, False),
        'ExcludePunctuation': (boolean, False),
        'ExcludeUppercase': (boolean, False),
        'GenerateStringKey': (basestring, False),
        'IncludeSpace': (boolean, False),
        'PasswordLength': (integer, False),
        'RequireEachIncludedType': (boolean, False),
        'SecretStringTemplate': (basestring, False),
    }


class Secret(AWSObject):
    resource_type = "AWS::SecretsManager::Secret"

    props = {
        'Description': (basestring, False),
        'GenerateSecretString': (GenerateSecretString, False),
        'KmsKeyId': (basestring, False),
        'Name': (basestring, False),
        'SecretString': (basestring, False),
        'Tags': ((Tags, list), False),
    }


class SecretTargetAttachment(AWSObject):
    resource_type = "AWS::SecretsManager::SecretTargetAttachment"

    props = {
        'SecretId': (basestring, True),
        'TargetId': (basestring, True),
        'TargetType': (validate_target_types, True),
    }
