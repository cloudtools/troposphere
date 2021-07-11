# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import (
    boolean,
    exactly_one,
    integer,
    mutually_exclusive,
    positive_integer,
)

KEY_ONLY = "KEY_ONLY"
VALUE_ONLY = "VALUE_ONLY"
KEY_AND_VALUE = "KEY_AND_VALUE"


class GitHubLocation(AWSProperty):
    props = {
        "CommitId": (str, True),
        "Repository": (str, True),
    }


class S3Location(AWSProperty):
    props = {
        "Bucket": (str, True),
        "BundleType": (str, True),
        "ETag": (str, False),
        "Key": (str, True),
        "Version": (str, False),
    }


class Revision(AWSProperty):
    props = {
        "GitHubLocation": (GitHubLocation, False),
        "RevisionType": (str, False),
        "S3Location": (S3Location, False),
    }


def deployment_option_validator(x):
    valid_values = ["WITH_TRAFFIC_CONTROL", "WITHOUT_TRAFFIC_CONTROL"]
    if x not in valid_values:
        raise ValueError(
            "Deployment Option value must be one of: %s" % ", ".join(valid_values)
        )
    return x


def deployment_type_validator(x):
    valid_values = ["IN_PLACE", "BLUE_GREEN"]
    if x not in valid_values:
        raise ValueError(
            "Deployment Type value must be one of: %s" % ", ".join(valid_values)
        )
    return x


class AutoRollbackConfiguration(AWSProperty):
    props = {"Enabled": (bool, False), "Events": ([str], False)}


class Deployment(AWSProperty):
    props = {
        "Description": (str, False),
        "IgnoreApplicationStopFailures": (bool, False),
        "Revision": (Revision, True),
    }


class DeploymentStyle(AWSProperty):
    props = {
        "DeploymentOption": (deployment_option_validator, False),
        "DeploymentType": (deployment_type_validator, False),
    }


class Ec2TagFilters(AWSProperty):
    props = {
        "Key": (str, False),
        "Type": (str, True),
        "Value": (str, False),
    }


class TagFilters(AWSProperty):
    props = {"Key": (str, False), "Type": (str, False), "Value": (str, False)}


class ElbInfoList(AWSProperty):
    props = {"Name": (str, False)}


class TargetGroupInfoList(AWSProperty):
    props = {"Name": (str, False)}


class LoadBalancerInfo(AWSProperty):
    props = {
        "ElbInfoList": ([ElbInfoList], False),
        "TargetGroupInfoList": ([TargetGroupInfoList], False),
    }

    def validate(self):
        conds = ["ElbInfoList", "TargetGroupInfoList"]
        exactly_one(self.__class__.__name__, self.properties, conds)


class OnPremisesInstanceTagFilters(AWSProperty):
    props = {
        "Key": (str, False),
        "Type": (str, False),
        "Value": (str, False),
    }


class Application(AWSObject):
    resource_type = "AWS::CodeDeploy::Application"

    props = {
        "ApplicationName": (str, False),
        "ComputePlatform": (str, False),
        "Tags": (Tags, False),
    }


class MinimumHealthyHosts(AWSProperty):
    props = {
        "Type": (str, True),
        "Value": (positive_integer, True),
    }


class TimeBasedCanary(AWSProperty):
    props = {
        "CanaryInterval": (integer, True),
        "CanaryPercentage": (integer, True),
    }


class TimeBasedLinear(AWSProperty):
    props = {
        "LinearInterval": (integer, True),
        "LinearPercentage": (integer, True),
    }


class TrafficRoutingConfig(AWSProperty):
    props = {
        "TimeBasedCanary": (TimeBasedCanary, False),
        "TimeBasedLinear": (TimeBasedLinear, False),
        "Type": (str, True),
    }


class DeploymentConfig(AWSObject):
    resource_type = "AWS::CodeDeploy::DeploymentConfig"

    props = {
        "ComputePlatform": (str, False),
        "DeploymentConfigName": (str, False),
        "MinimumHealthyHosts": (MinimumHealthyHosts, False),
        "TrafficRoutingConfig": (TrafficRoutingConfig, False),
    }


class Alarm(AWSProperty):
    props = {
        "Name": (str, False),
    }


class AlarmConfiguration(AWSProperty):
    props = {
        "Alarms": ([Alarm], False),
        "Enabled": (boolean, False),
        "IgnorePollAlarmFailure": (boolean, False),
    }


class BlueInstanceTerminationOption(AWSProperty):
    props = {
        "Action": (str, False),
        "TerminationWaitTimeInMinutes": (integer, False),
    }


class DeploymentReadyOption(AWSProperty):
    props = {
        "ActionOnTimeout": (str, False),
        "WaitTimeInMinutes": (integer, False),
    }


class GreenFleetProvisioningOption(AWSProperty):
    props = {
        "Action": (str, False),
    }


class BlueGreenDeploymentConfiguration(AWSProperty):
    props = {
        "DeploymentReadyOption": (DeploymentReadyOption, False),
        "GreenFleetProvisioningOption": (GreenFleetProvisioningOption, False),
        "TerminateBlueInstancesOnDeploymentSuccess": (
            BlueInstanceTerminationOption,
            False,
        ),
    }


class TriggerConfig(AWSProperty):
    props = {
        "TriggerEvents": ([str], False),
        "TriggerName": (str, False),
        "TriggerTargetArn": (str, False),
    }


class Ec2TagSetListObject(AWSProperty):
    props = {"Ec2TagGroup": ([Ec2TagFilters], False)}


class Ec2TagSet(AWSProperty):
    props = {"Ec2TagSetList": ([Ec2TagSetListObject], False)}


class ECSService(AWSProperty):
    props = {
        "ClusterName": (str, True),
        "ServiceName": (str, True),
    }


class OnPremisesTagSetObject(AWSProperty):
    props = {"OnPremisesTagGroup": ([TagFilters], False)}


class OnPremisesTagSetList(AWSProperty):
    props = {"OnPremisesTagSetList": ([OnPremisesTagSetObject], False)}


class OnPremisesTagSet(AWSProperty):
    props = {"OnPremisesTagSetList": (OnPremisesTagSetList, False)}


class DeploymentGroup(AWSObject):
    resource_type = "AWS::CodeDeploy::DeploymentGroup"

    props = {
        "AlarmConfiguration": (AlarmConfiguration, False),
        "ApplicationName": (str, True),
        "AutoRollbackConfiguration": (AutoRollbackConfiguration, False),
        "AutoScalingGroups": ([str], False),
        "BlueGreenDeploymentConfiguration": (BlueGreenDeploymentConfiguration, False),
        "Deployment": (Deployment, False),
        "DeploymentConfigName": (str, False),
        "DeploymentGroupName": (str, False),
        "DeploymentStyle": (DeploymentStyle, False),
        "ECSServices": ([ECSService], False),
        "Ec2TagFilters": ([Ec2TagFilters], False),
        "Ec2TagSet": (Ec2TagSet, False),
        "LoadBalancerInfo": (LoadBalancerInfo, False),
        "OnPremisesInstanceTagFilters": ([OnPremisesInstanceTagFilters], False),
        "OnPremisesInstanceTagSet": (OnPremisesTagSet, False),
        "ServiceRoleArn": (str, True),
        "TriggerConfigurations": ([TriggerConfig], False),
    }

    def validate(self):
        ec2_conds = ["EC2TagFilters", "Ec2TagSet"]
        onPremises_conds = ["OnPremisesInstanceTagFilters", "OnPremisesInstanceTagSet"]
        mutually_exclusive(self.__class__.__name__, self.properties, ec2_conds)
        mutually_exclusive(self.__class__.__name__, self.properties, onPremises_conds)
