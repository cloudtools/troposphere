# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import positive_integer


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


class Deployment(AWSProperty):
    props = {
        'Description': (basestring, False),
        'IgnoreApplicationStopFailures': (bool, False),
        'Revision': (Revision, True),
    }


class Ec2TagFilters(AWSProperty):
    props = {
        'Key': (basestring, False),
        'Type': (basestring, False),
        'Value': (basestring, False),
    }


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
    }


class DeploymentConfig(AWSObject):
    resource_type = "AWS::CodeDeploy::DeploymentConfig"

    props = {
        'DeploymentConfigName': (basestring, False),
        'MinimumHealthyHosts': (MinimumHealthyHosts, False),
    }


class DeploymentGroup(AWSObject):
    resource_type = "AWS::CodeDeploy::DeploymentGroup"

    props = {
        'ApplicationName': (basestring, True),
        'AutoScalingGroups': ([basestring], False),
        'Deployment': (Deployment, False),
        'DeploymentConfigName': (basestring, False),
        'DeploymentGroupName': (basestring, False),
        'Ec2TagFilters': ([Ec2TagFilters], False),
        'OnPremisesInstanceTagFilters': (OnPremisesInstanceTagFilters, False),
        'ServiceRoleArn': (basestring, True),
    }
