# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_predictivescalingmaxcapacitybehavior(predictivescalingmaxcapacitybehavior):
    """
    Validate PredictiveScalingMaxCapacityBehavior for ScalingInstruction
    Property: ScalingInstruction.PredictiveScalingMaxCapacityBehavior
    """

    VALID_PREDICTIVESCALINGMAXCAPACITYBEHAVIOR = (
        "SetForecastCapacityToMaxCapacity",
        "SetMaxCapacityToForecastCapacity",
        "SetMaxCapacityAboveForecastCapacity",
    )

    if (
        predictivescalingmaxcapacitybehavior
        not in VALID_PREDICTIVESCALINGMAXCAPACITYBEHAVIOR
    ):  # noqa
        raise ValueError(
            "ScalingInstruction PredictiveScalingMaxCapacityBehavior must be one of: %s"
            % ", ".join(VALID_PREDICTIVESCALINGMAXCAPACITYBEHAVIOR)  # noqa
        )
    return predictivescalingmaxcapacitybehavior


def validate_predictivescalingmode(predictivescalingmode):
    """
    Validate PredictiveScalingMode for ScalingInstruction
    Property: ScalingInstruction.PredictiveScalingMode
    """

    VALID_PREDICTIVESCALINGMODE = ("ForecastAndScale", "ForecastOnly")

    if predictivescalingmode not in VALID_PREDICTIVESCALINGMODE:
        raise ValueError(
            "ScalingInstruction PredictiveScalingMode must be one of: %s"
            % ", ".join(VALID_PREDICTIVESCALINGMODE)  # noqa
        )
    return predictivescalingmode


def validate_scalingpolicyupdatebehavior(scalingpolicyupdatebehavior):
    """
    Validate ScalingPolicyUpdateBehavior for ScalingInstruction
    Property: ScalingInstruction.ScalingPolicyUpdateBehavior
    """

    VALID_SCALINGPOLICYUPDATEBEHAVIOR = (
        "KeepExternalPolicies",
        "ReplaceExternalPolicies",
    )

    if scalingpolicyupdatebehavior not in VALID_SCALINGPOLICYUPDATEBEHAVIOR:
        raise ValueError(
            "ScalingInstruction ScalingPolicyUpdateBehavior must be one of: %s"
            % ", ".join(VALID_SCALINGPOLICYUPDATEBEHAVIOR)  # noqa
        )
    return scalingpolicyupdatebehavior


def scalable_dimension_type(scalable_dimension):
    """
    Property: ScalingInstruction.ScalableDimension
    """
    valid_values = [
        "autoscaling:autoScalingGroup:DesiredCapacity",
        "ecs:service:DesiredCount",
        "ec2:spot-fleet-request:TargetCapacity",
        "rds:cluster:ReadReplicaCount",
        "dynamodb:table:ReadCapacityUnits",
        "dynamodb:table:WriteCapacityUnits",
        "dynamodb:index:ReadCapacityUnits",
        "dynamodb:index:WriteCapacityUnits",
    ]
    if scalable_dimension not in valid_values:
        raise ValueError(
            'ScalableDimension must be one of: "%s"' % (", ".join(valid_values))
        )
    return scalable_dimension


def service_namespace_type(service_namespace):
    """
    Property: ScalingInstruction.ServiceNamespace
    """
    valid_values = ["autoscaling", "ecs", "ec2", "rds", "dynamodb"]
    if service_namespace not in valid_values:
        raise ValueError(
            'ServiceNamespace must be one of: "%s"' % (", ".join(valid_values))
        )
    return service_namespace


def statistic_type(statistic):
    """
    Property: CustomizedScalingMetricSpecification.Statistic
    """
    valid_values = ["Average", "Minimum", "Maximum", "SampleCount", "Sum"]
    if statistic not in valid_values:
        raise ValueError('Statistic must be one of: "%s"' % (", ".join(valid_values)))
    return statistic
