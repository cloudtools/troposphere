# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, exactly_one, positive_integer


KEY_ONLY = "KEY_ONLY"
VALUE_ONLY = "VALUE_ONLY"
KEY_AND_VALUE = "KEY_AND_VALUE"


class GitHubLocation(AWSProperty):
    props = {
        'CommitId': (basestring, True),
        'Repository': (basestring, True),
    }


class S3Location(AWSProperty):
    props = {
        'Bucket': (basestring, True),
        'BundleType': (basestring, True),
        'ETag': (basestring, False),
        'Key': (basestring, True),
        'Version': (basestring, False),
    }


class Revision(AWSProperty):
    props = {
        'GitHubLocation': (GitHubLocation, False),
        'RevisionType': (basestring, False),
        'S3Location': (S3Location, False),
    }


def deployment_option_validator(x):
    valid_values = ['WITH_TRAFFIC_CONTROL', 'WITHOUT_TRAFFIC_CONTROL']
    if x not in valid_values:
        raise ValueError("Deployment Option value must be one of: %s" %
                         ', '.join(valid_values))
    return x


def deployment_type_validator(x):
    valid_values = ['IN_PLACE', 'BLUE_GREEN']
    if x not in valid_values:
        raise ValueError("Deployment Type value must be one of: %s" %
                         ', '.join(valid_values))
    return x


class AutoRollbackConfiguration(AWSProperty):
    props = {
        'Enabled': (bool, False),
        'Events': ([basestring], False)
    }


class Deployment(AWSProperty):
    props = {
        'Description': (basestring, False),
        'IgnoreApplicationStopFailures': (bool, False),
        'Revision': (Revision, True),
    }


class DeploymentStyle(AWSProperty):
    props = {
        'DeploymentOption': (deployment_option_validator, False),
        'DeploymentType': (deployment_type_validator, False),
    }


class Ec2TagFilters(AWSProperty):
    props = {
        'Key': (basestring, False),
        'Type': (basestring, False),
        'Value': (basestring, False),
    }


class ElbInfoList(AWSProperty):
    props = {
        'Name': (basestring, False)
    }


class TargetGroupInfoList(AWSProperty):
    props = {
        'Name': (basestring, False)
    }


class LoadBalancerInfo(AWSProperty):
    props = {
        'ElbInfoList': ([ElbInfoList], False),
        'TargetGroupInfoList': ([TargetGroupInfoList], False),
    }

    def validate(self):
        conds = [
            'ElbInfoList',
            'TargetGroupInfoList',
        ]
        exactly_one(self.__class__.__name__, self.properties, conds)


class OnPremisesInstanceTagFilters(AWSProperty):
    props = {
        'Key': (basestring, False),
        'Type': (basestring, False),
        'Value': (basestring, False),
    }


class MinimumHealthyHosts(AWSProperty):
    props = {
        'Type': (basestring, False),
        'Value': (positive_integer, False),
    }


class Application(AWSObject):
    resource_type = "AWS::CodeDeploy::Application"

    props = {
        'ApplicationName': (basestring, False),
        'ComputePlatform': (basestring, False),
    }


class DeploymentConfig(AWSObject):
    resource_type = "AWS::CodeDeploy::DeploymentConfig"

    props = {
        'DeploymentConfigName': (basestring, False),
        'MinimumHealthyHosts': (MinimumHealthyHosts, False),
    }


class Alarm(AWSProperty):
    props = {
        'Name': (basestring, False),
    }


class AlarmConfiguration(AWSProperty):
    props = {
        'Alarms': ([Alarm], False),
        'Enabled': (boolean, False),
        'IgnorePollAlarmFailure': (boolean, False),
    }


class TriggerConfig(AWSProperty):
    props = {
        'TriggerEvents': ([basestring], False),
        'TriggerName': (basestring, False),
        'TriggerTargetArn': (basestring, False),
    }


class DeploymentGroup(AWSObject):
    resource_type = "AWS::CodeDeploy::DeploymentGroup"

    props = {
        'AlarmConfiguration': (AlarmConfiguration, False),
        'ApplicationName': (basestring, True),
        'AutoRollbackConfiguration': (AutoRollbackConfiguration, False),
        'AutoScalingGroups': ([basestring], False),
        'Deployment': (Deployment, False),
        'DeploymentConfigName': (basestring, False),
        'DeploymentGroupName': (basestring, False),
        'DeploymentStyle': (DeploymentStyle, False),
        'Ec2TagFilters': ([Ec2TagFilters], False),
        'LoadBalancerInfo': (LoadBalancerInfo, False),
        'OnPremisesInstanceTagFilters': (OnPremisesInstanceTagFilters, False),
        'ServiceRoleArn': (basestring, True),
        'TriggerConfigurations': ([TriggerConfig], False),
    }
