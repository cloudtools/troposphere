# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import (boolean, double, integer, scalable_dimension_type,
                         service_namespace_type, statistic_type)


VALID_PREDICTIVESCALINGMAXCAPACITYBEHAVIOR = (
    'SetForecastCapacityToMaxCapacity',
    'SetMaxCapacityToForecastCapacity',
    'SetMaxCapacityAboveForecastCapacity',
)
VALID_PREDICTIVESCALINGMODE = ('ForecastAndScale', 'ForecastOnly')
VALID_SCALINGPOLICYUPDATEBEHAVIOR = ('KeepExternalPolicies',
                                     'ReplaceExternalPolicies')


def validate_predictivescalingmaxcapacitybehavior(
        predictivescalingmaxcapacitybehavior):
    """Validate PredictiveScalingMaxCapacityBehavior for ScalingInstruction"""  # noqa

    if predictivescalingmaxcapacitybehavior not in VALID_PREDICTIVESCALINGMAXCAPACITYBEHAVIOR:  # noqa
        raise ValueError("ScalingInstruction PredictiveScalingMaxCapacityBehavior must be one of: %s" %  # noqa
                         ", ".join(VALID_PREDICTIVESCALINGMAXCAPACITYBEHAVIOR))
    return predictivescalingmaxcapacitybehavior


def validate_predictivescalingmode(predictivescalingmode):
    """Validate PredictiveScalingMode for ScalingInstruction"""

    if predictivescalingmode not in VALID_PREDICTIVESCALINGMODE:
        raise ValueError("ScalingInstruction PredictiveScalingMode must be one of: %s" %  # noqa
                         ", ".join(VALID_PREDICTIVESCALINGMODE))
    return predictivescalingmode


def validate_scalingpolicyupdatebehavior(scalingpolicyupdatebehavior):
    """Validate ScalingPolicyUpdateBehavior for ScalingInstruction"""

    if scalingpolicyupdatebehavior not in VALID_SCALINGPOLICYUPDATEBEHAVIOR:
        raise ValueError("ScalingInstruction ScalingPolicyUpdateBehavior must be one of: %s" %  # noqa
                         ", ".join(VALID_SCALINGPOLICYUPDATEBEHAVIOR))
    return scalingpolicyupdatebehavior


class TagFilter(AWSProperty):
    props = {
        'Values': ([str], False),
        'Key': (str, True)
    }


class ApplicationSource(AWSProperty):
    props = {
        'CloudFormationStackARN': (str, False),
        'TagFilters': ([TagFilter], False)
    }


class PredefinedScalingMetricSpecification(AWSProperty):
    props = {
        'ResourceLabel': (str, False),
        'PredefinedScalingMetricType': (str, True)
    }


class MetricDimension(AWSProperty):
    props = {
        'Value': (str, True),
        'Name': (str, True)
    }


class CustomizedScalingMetricSpecification(AWSProperty):
    props = {
        'MetricName': (str, True),
        'Statistic': (statistic_type, True),
        'Dimensions': ([MetricDimension], False),
        'Unit': (str, False),
        'Namespace': (str, True)
    }


class TargetTrackingConfiguration(AWSProperty):
    props = {
        'ScaleOutCooldown': (integer, False),
        'TargetValue': (double, True),
        'PredefinedScalingMetricSpecification': (
            PredefinedScalingMetricSpecification,
            False
        ),
        'DisableScaleIn': (boolean, False),
        'ScaleInCooldown': (integer, False),
        'EstimatedInstanceWarmup': (integer, False),
        'CustomizedScalingMetricSpecification': (
            CustomizedScalingMetricSpecification,
            False
        )
    }


class CustomizedLoadMetricSpecification(AWSObject):
    props = {
        'Dimensions': ([MetricDimension], False),
        'MetricName': (str, True),
        'Namespace': (str, True),
        'Statistic': (str, True),
        'Unit': (str, False),
    }


class PredefinedLoadMetricSpecification(AWSProperty):
    props = {
        'PredefinedLoadMetricType': (str, True),
        'ResourceLabel': (str, False),
    }


class ScalingInstruction(AWSProperty):
    props = {
        'CustomizedLoadMetricSpecification': (CustomizedLoadMetricSpecification, False),  # NOQA
        'DisableDynamicScaling': (boolean, False),
        'MaxCapacity': (integer, True),
        'MinCapacity': (integer, True),
        'PredefinedLoadMetricSpecification': (PredefinedLoadMetricSpecification, False),  # NOQA
        'PredictiveScalingMaxCapacityBehavior': (validate_predictivescalingmaxcapacitybehavior, False),  # NOQA
        'PredictiveScalingMaxCapacityBuffer': (integer, False),
        'PredictiveScalingMode': (validate_predictivescalingmode, False),
        'ResourceId': (str, True),
        'ScalableDimension': (scalable_dimension_type, True),
        'ScalingPolicyUpdateBehavior': (validate_scalingpolicyupdatebehavior, False),  # NOQA
        'ScheduledActionBufferTime': (integer, False),
        'ServiceNamespace': (service_namespace_type, True),
        'TargetTrackingConfigurations': (
            [TargetTrackingConfiguration],
            True
        ),
    }


class ScalingPlan(AWSObject):
    resource_type = "AWS::AutoScalingPlans::ScalingPlan"

    props = {
        'ApplicationSource': (ApplicationSource, True),
        'ScalingInstructions': ([ScalingInstruction], True)
    }
