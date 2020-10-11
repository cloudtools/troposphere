# Copyright (c) 2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import AWSObject, AWSProperty, Tags
from .validators import (
    double
)

VALID_GROWTH_TYPE = ('LINEAR')
VALID_REPLICATION_DESTINATION = ('NONE', 'SSM_DOCUMENT')
VALID_VALIDATOR_TYPE = ('JSON_SCHEMA', 'LAMBDA')


def validate_growth_type(growth_type):
    if growth_type not in VALID_GROWTH_TYPE:
        raise ValueError("DeploymentStrategy GrowthType must be one of: %s" %
                         ', '.join(VALID_GROWTH_TYPE))
    return growth_type


def validate_replicate_to(replicate_to):
    if replicate_to not in VALID_REPLICATION_DESTINATION:
        raise ValueError("DeploymentStrategy ReplicateTo must be one of: %s" %
                         ', '.join(VALID_REPLICATION_DESTINATION))
    return replicate_to


def validate_validator_type(validator_type):
    if validator_type not in VALID_VALIDATOR_TYPE:
        raise ValueError("ConfigurationProfile Validator Type must be one of: %s" %  # NOQA
                         ', '.join(VALID_VALIDATOR_TYPE))
    return validator_type


class DeploymentStrategy(AWSObject):
    resource_type = "AWS::AppConfig::DeploymentStrategy"

    props = {
        'DeploymentDurationInMinutes': (double, True),
        'Description': (basestring, False),
        'FinalBakeTimeInMinutes': (double, False),
        'GrowthFactor': (double, True),
        'GrowthType': (validate_growth_type, False),
        'Name': (basestring, True),
        'ReplicateTo': (validate_replicate_to, True),
        'Tags': (Tags, False),
    }


class Monitors(AWSProperty):
    props = {
        'AlarmArn': (basestring, False),
        'AlarmRoleArn': (basestring, False),
    }


class Environment(AWSObject):
    resource_type = "AWS::AppConfig::Environment"

    props = {
        'ApplicationId': (basestring, True),
        'Description': (basestring, False),
        'Monitors': ([Monitors], False),
        'Name': (basestring, True),
        'Tags': (Tags, False),
    }


class Deployment(AWSObject):
    resource_type = "AWS::AppConfig::Deployment"

    props = {
        'ApplicationId': (basestring, True),
        'ConfigurationProfileId': (basestring, True),
        'ConfigurationVersion': (basestring, True),
        'DeploymentStrategyId': (basestring, True),
        'Description': (basestring, False),
        'EnvironmentId': (basestring, True),
        'Tags': (Tags, False),
    }


class Validators(AWSProperty):
    props = {
        'Content': (basestring, False),
        'Type': (validate_validator_type, False),
    }


class ConfigurationProfile(AWSObject):
    resource_type = "AWS::AppConfig::ConfigurationProfile"

    props = {
        'ApplicationId': (basestring, True),
        'Description': (basestring, False),
        'LocationUri': (basestring, True),
        'Name': (basestring, True),
        'RetrievalRoleArn': (basestring, False),
        'Tags': (Tags, False),
        'Validators': ([Validators], False)
    }


class Application(AWSObject):
    resource_type = "AWS::AppConfig::Application"

    props = {
        'Description': (basestring, False),
        'Name': (basestring, True),
        'Tags': (Tags, False),
    }
