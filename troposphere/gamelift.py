# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer


class RoutingStrategy(AWSProperty):
    """
    `RoutingStrategy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-alias-routingstrategy.html>`__
    """

    props: PropsDictType = {
        "FleetId": (str, False),
        "Message": (str, False),
        "Type": (str, True),
    }


class Alias(AWSObject):
    """
    `Alias <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html>`__
    """

    resource_type = "AWS::GameLift::Alias"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "RoutingStrategy": (RoutingStrategy, True),
    }


class StorageLocation(AWSProperty):
    """
    `StorageLocation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, True),
        "Key": (str, True),
        "ObjectVersion": (str, False),
        "RoleArn": (str, True),
    }


class Build(AWSObject):
    """
    `Build <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html>`__
    """

    resource_type = "AWS::GameLift::Build"

    props: PropsDictType = {
        "Name": (str, False),
        "OperatingSystem": (str, False),
        "ServerSdkVersion": (str, False),
        "StorageLocation": (StorageLocation, False),
        "Version": (str, False),
    }


class AnywhereConfiguration(AWSProperty):
    """
    `AnywhereConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-anywhereconfiguration.html>`__
    """

    props: PropsDictType = {
        "Cost": (str, True),
    }


class CertificateConfiguration(AWSProperty):
    """
    `CertificateConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-certificateconfiguration.html>`__
    """

    props: PropsDictType = {
        "CertificateType": (str, True),
    }


class IpPermission(AWSProperty):
    """
    `IpPermission <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ippermission.html>`__
    """

    props: PropsDictType = {
        "FromPort": (integer, True),
        "IpRange": (str, True),
        "Protocol": (str, True),
        "ToPort": (integer, True),
    }


class LocationCapacity(AWSProperty):
    """
    `LocationCapacity <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationcapacity.html>`__
    """

    props: PropsDictType = {
        "DesiredEC2Instances": (integer, True),
        "MaxSize": (integer, True),
        "MinSize": (integer, True),
    }


class LocationConfiguration(AWSProperty):
    """
    `LocationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationconfiguration.html>`__
    """

    props: PropsDictType = {
        "Location": (str, True),
        "LocationCapacity": (LocationCapacity, False),
    }


class ResourceCreationLimitPolicy(AWSProperty):
    """
    `ResourceCreationLimitPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-resourcecreationlimitpolicy.html>`__
    """

    props: PropsDictType = {
        "NewGameSessionsPerCreator": (integer, False),
        "PolicyPeriodInMinutes": (integer, False),
    }


class ServerProcess(AWSProperty):
    """
    `ServerProcess <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html>`__
    """

    props: PropsDictType = {
        "ConcurrentExecutions": (integer, True),
        "LaunchPath": (str, True),
        "Parameters": (str, False),
    }


class RuntimeConfiguration(AWSProperty):
    """
    `RuntimeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-runtimeconfiguration.html>`__
    """

    props: PropsDictType = {
        "GameSessionActivationTimeoutSeconds": (integer, False),
        "MaxConcurrentGameSessionActivations": (integer, False),
        "ServerProcesses": ([ServerProcess], False),
    }


class Fleet(AWSObject):
    """
    `Fleet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html>`__
    """

    resource_type = "AWS::GameLift::Fleet"

    props: PropsDictType = {
        "AnywhereConfiguration": (AnywhereConfiguration, False),
        "BuildId": (str, False),
        "CertificateConfiguration": (CertificateConfiguration, False),
        "ComputeType": (str, False),
        "Description": (str, False),
        "DesiredEC2Instances": (integer, False),
        "EC2InboundPermissions": ([IpPermission], False),
        "EC2InstanceType": (str, False),
        "FleetType": (str, False),
        "InstanceRoleARN": (str, False),
        "Locations": ([LocationConfiguration], False),
        "MaxSize": (integer, False),
        "MetricGroups": ([str], False),
        "MinSize": (integer, False),
        "Name": (str, True),
        "NewGameSessionProtectionPolicy": (str, False),
        "PeerVpcAwsAccountId": (str, False),
        "PeerVpcId": (str, False),
        "ResourceCreationLimitPolicy": (ResourceCreationLimitPolicy, False),
        "RuntimeConfiguration": (RuntimeConfiguration, False),
        "ScriptId": (str, False),
    }


class TargetTrackingConfiguration(AWSProperty):
    """
    `TargetTrackingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-targettrackingconfiguration.html>`__
    """

    props: PropsDictType = {
        "TargetValue": (double, True),
    }


class AutoScalingPolicy(AWSProperty):
    """
    `AutoScalingPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-autoscalingpolicy.html>`__
    """

    props: PropsDictType = {
        "EstimatedInstanceWarmup": (double, False),
        "TargetTrackingConfiguration": (TargetTrackingConfiguration, True),
    }


class InstanceDefinition(AWSProperty):
    """
    `InstanceDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-instancedefinition.html>`__
    """

    props: PropsDictType = {
        "InstanceType": (str, True),
        "WeightedCapacity": (str, False),
    }


class LaunchTemplate(AWSProperty):
    """
    `LaunchTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-launchtemplate.html>`__
    """

    props: PropsDictType = {
        "LaunchTemplateId": (str, False),
        "LaunchTemplateName": (str, False),
        "Version": (str, False),
    }


class GameServerGroup(AWSObject):
    """
    `GameServerGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html>`__
    """

    resource_type = "AWS::GameLift::GameServerGroup"

    props: PropsDictType = {
        "AutoScalingPolicy": (AutoScalingPolicy, False),
        "BalancingStrategy": (str, False),
        "DeleteOption": (str, False),
        "GameServerGroupName": (str, True),
        "GameServerProtectionPolicy": (str, False),
        "InstanceDefinitions": ([InstanceDefinition], True),
        "LaunchTemplate": (LaunchTemplate, False),
        "MaxSize": (double, False),
        "MinSize": (double, False),
        "RoleArn": (str, True),
        "Tags": (Tags, False),
        "VpcSubnets": ([str], False),
    }


class Destination(AWSProperty):
    """
    `Destination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-destination.html>`__
    """

    props: PropsDictType = {
        "DestinationArn": (str, False),
    }


class FilterConfiguration(AWSProperty):
    """
    `FilterConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-filterconfiguration.html>`__
    """

    props: PropsDictType = {
        "AllowedLocations": ([str], False),
    }


class PlayerLatencyPolicy(AWSProperty):
    """
    `PlayerLatencyPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-playerlatencypolicy.html>`__
    """

    props: PropsDictType = {
        "MaximumIndividualPlayerLatencyMilliseconds": (integer, False),
        "PolicyDurationSeconds": (integer, False),
    }


class PriorityConfiguration(AWSProperty):
    """
    `PriorityConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-priorityconfiguration.html>`__
    """

    props: PropsDictType = {
        "LocationOrder": ([str], False),
        "PriorityOrder": ([str], False),
    }


class GameSessionQueue(AWSObject):
    """
    `GameSessionQueue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html>`__
    """

    resource_type = "AWS::GameLift::GameSessionQueue"

    props: PropsDictType = {
        "CustomEventData": (str, False),
        "Destinations": ([Destination], False),
        "FilterConfiguration": (FilterConfiguration, False),
        "Name": (str, True),
        "NotificationTarget": (str, False),
        "PlayerLatencyPolicies": ([PlayerLatencyPolicy], False),
        "PriorityConfiguration": (PriorityConfiguration, False),
        "Tags": (Tags, False),
        "TimeoutInSeconds": (integer, False),
    }


class Location(AWSObject):
    """
    `Location <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-location.html>`__
    """

    resource_type = "AWS::GameLift::Location"

    props: PropsDictType = {
        "LocationName": (str, True),
        "Tags": (Tags, False),
    }


class GameProperty(AWSProperty):
    """
    `GameProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-matchmakingconfiguration-gameproperty.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Value": (str, True),
    }


class MatchmakingConfiguration(AWSObject):
    """
    `MatchmakingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html>`__
    """

    resource_type = "AWS::GameLift::MatchmakingConfiguration"

    props: PropsDictType = {
        "AcceptanceRequired": (boolean, True),
        "AcceptanceTimeoutSeconds": (integer, False),
        "AdditionalPlayerCount": (integer, False),
        "BackfillMode": (str, False),
        "CustomEventData": (str, False),
        "Description": (str, False),
        "FlexMatchMode": (str, False),
        "GameProperties": ([GameProperty], False),
        "GameSessionData": (str, False),
        "GameSessionQueueArns": ([str], False),
        "Name": (str, True),
        "NotificationTarget": (str, False),
        "RequestTimeoutSeconds": (integer, True),
        "RuleSetName": (str, True),
        "Tags": (Tags, False),
    }


class MatchmakingRuleSet(AWSObject):
    """
    `MatchmakingRuleSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html>`__
    """

    resource_type = "AWS::GameLift::MatchmakingRuleSet"

    props: PropsDictType = {
        "Name": (str, True),
        "RuleSetBody": (str, True),
        "Tags": (Tags, False),
    }


class S3Location(AWSProperty):
    """
    `S3Location <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, True),
        "Key": (str, True),
        "ObjectVersion": (str, False),
        "RoleArn": (str, True),
    }


class Script(AWSObject):
    """
    `Script <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html>`__
    """

    resource_type = "AWS::GameLift::Script"

    props: PropsDictType = {
        "Name": (str, False),
        "StorageLocation": (S3Location, True),
        "Tags": (Tags, False),
        "Version": (str, False),
    }
