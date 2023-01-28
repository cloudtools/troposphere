# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double


class FlexibleTimeWindow(AWSProperty):
    """
    `FlexibleTimeWindow <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-flexibletimewindow.html>`__
    """

    props: PropsDictType = {
        "MaximumWindowInMinutes": (double, False),
        "Mode": (str, True),
    }


class DeadLetterConfig(AWSProperty):
    """
    `DeadLetterConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-deadletterconfig.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, False),
    }


class CapacityProviderStrategyItem(AWSProperty):
    """
    `CapacityProviderStrategyItem <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-capacityproviderstrategyitem.html>`__
    """

    props: PropsDictType = {
        "Base": (double, False),
        "CapacityProvider": (str, True),
        "Weight": (double, False),
    }


class AwsVpcConfiguration(AWSProperty):
    """
    `AwsVpcConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-awsvpcconfiguration.html>`__
    """

    props: PropsDictType = {
        "AssignPublicIp": (str, False),
        "SecurityGroups": ([str], False),
        "Subnets": ([str], True),
    }


class NetworkConfiguration(AWSProperty):
    """
    `NetworkConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-networkconfiguration.html>`__
    """

    props: PropsDictType = {
        "AwsvpcConfiguration": (AwsVpcConfiguration, False),
    }


class PlacementConstraint(AWSProperty):
    """
    `PlacementConstraint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementconstraint.html>`__
    """

    props: PropsDictType = {
        "Expression": (str, False),
        "Type": (str, False),
    }


class PlacementStrategy(AWSProperty):
    """
    `PlacementStrategy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementstrategy.html>`__
    """

    props: PropsDictType = {
        "Field": (str, False),
        "Type": (str, False),
    }


class EcsParameters(AWSProperty):
    """
    `EcsParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html>`__
    """

    props: PropsDictType = {
        "CapacityProviderStrategy": ([CapacityProviderStrategyItem], False),
        "EnableECSManagedTags": (boolean, False),
        "EnableExecuteCommand": (boolean, False),
        "Group": (str, False),
        "LaunchType": (str, False),
        "NetworkConfiguration": (NetworkConfiguration, False),
        "PlacementConstraints": ([PlacementConstraint], False),
        "PlacementStrategy": ([PlacementStrategy], False),
        "PlatformVersion": (str, False),
        "PropagateTags": (str, False),
        "ReferenceId": (str, False),
        "Tags": (dict, False),
        "TaskCount": (double, False),
        "TaskDefinitionArn": (str, True),
    }


class EventBridgeParameters(AWSProperty):
    """
    `EventBridgeParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-eventbridgeparameters.html>`__
    """

    props: PropsDictType = {
        "DetailType": (str, True),
        "Source": (str, True),
    }


class KinesisParameters(AWSProperty):
    """
    `KinesisParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-kinesisparameters.html>`__
    """

    props: PropsDictType = {
        "PartitionKey": (str, True),
    }


class RetryPolicy(AWSProperty):
    """
    `RetryPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-retrypolicy.html>`__
    """

    props: PropsDictType = {
        "MaximumEventAgeInSeconds": (double, False),
        "MaximumRetryAttempts": (double, False),
    }


class SageMakerPipelineParameter(AWSProperty):
    """
    `SageMakerPipelineParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameter.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Value": (str, True),
    }


class SageMakerPipelineParameters(AWSProperty):
    """
    `SageMakerPipelineParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameters.html>`__
    """

    props: PropsDictType = {
        "PipelineParameterList": ([SageMakerPipelineParameter], False),
    }


class SqsParameters(AWSProperty):
    """
    `SqsParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sqsparameters.html>`__
    """

    props: PropsDictType = {
        "MessageGroupId": (str, False),
    }


class Target(AWSProperty):
    """
    `Target <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html>`__
    """

    props: PropsDictType = {
        "Arn": (str, True),
        "DeadLetterConfig": (DeadLetterConfig, False),
        "EcsParameters": (EcsParameters, False),
        "EventBridgeParameters": (EventBridgeParameters, False),
        "Input": (str, False),
        "KinesisParameters": (KinesisParameters, False),
        "RetryPolicy": (RetryPolicy, False),
        "RoleArn": (str, True),
        "SageMakerPipelineParameters": (SageMakerPipelineParameters, False),
        "SqsParameters": (SqsParameters, False),
    }


class Schedule(AWSObject):
    """
    `Schedule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html>`__
    """

    resource_type = "AWS::Scheduler::Schedule"

    props: PropsDictType = {
        "Description": (str, False),
        "EndDate": (str, False),
        "FlexibleTimeWindow": (FlexibleTimeWindow, True),
        "GroupName": (str, False),
        "KmsKeyArn": (str, False),
        "Name": (str, False),
        "ScheduleExpression": (str, True),
        "ScheduleExpressionTimezone": (str, False),
        "StartDate": (str, False),
        "State": (str, False),
        "Target": (Target, True),
    }


class ScheduleGroup(AWSObject):
    """
    `ScheduleGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedulegroup.html>`__
    """

    resource_type = "AWS::Scheduler::ScheduleGroup"

    props: PropsDictType = {
        "Name": (str, False),
        "Tags": (Tags, False),
    }
