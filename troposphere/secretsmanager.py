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
        'BlockPublicPolicy': (boolean, False),
        'SecretId': (str, True),
        'ResourcePolicy': (policytypes, True),
    }


class HostedRotationLambda(AWSProperty):
    props = {
        'KmsKeyArn': (str, False),
        'MasterSecretArn': (str, False),
        'MasterSecretKmsKeyArn': (str, False),
        'RotationLambdaName': (str, False),
        'RotationType': (str, True),
        'VpcSecurityGroupIds': (str, False),
        'VpcSubnetIds': (str, False),
    }


class RotationRules(AWSProperty):
    props = {
        'AutomaticallyAfterDays': (integer, False),
    }


class RotationSchedule(AWSObject):
    resource_type = "AWS::SecretsManager::RotationSchedule"

    props = {
        'HostedRotationLambda': (HostedRotationLambda, False),
        'RotationLambdaARN': (str, False),
        'RotationRules': (RotationRules, False),
        'SecretId': (str, True),
    }


class GenerateSecretString(AWSProperty):
    props = {
        'ExcludeCharacters': (str, False),
        'ExcludeLowercase': (boolean, False),
        'ExcludeNumbers': (boolean, False),
        'ExcludePunctuation': (boolean, False),
        'ExcludeUppercase': (boolean, False),
        'GenerateStringKey': (str, False),
        'IncludeSpace': (boolean, False),
        'PasswordLength': (integer, False),
        'RequireEachIncludedType': (boolean, False),
        'SecretStringTemplate': (str, False),
    }


class ReplicaRegion(AWSProperty):
    props = {
        'KmsKeyId': (str, False),
        'Region': (str, True),
    }


class Secret(AWSObject):
    resource_type = "AWS::SecretsManager::Secret"

    props = {
        'Description': (str, False),
        'GenerateSecretString': (GenerateSecretString, False),
        'KmsKeyId': (str, False),
        'Name': (str, False),
        'ReplicaRegions': ([ReplicaRegion], False),
        'SecretString': (str, False),
        'Tags': ((Tags, list), False),
    }


class SecretTargetAttachment(AWSObject):
    resource_type = "AWS::SecretsManager::SecretTargetAttachment"

    props = {
        'SecretId': (str, True),
        'TargetId': (str, True),
        'TargetType': (validate_target_types, True),
    }
