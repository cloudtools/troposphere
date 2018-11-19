# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import (boolean, double, integer, scalable_dimension_type,
                         service_namespace_type, statistic_type)


class TagFilter(AWSProperty):
    props = {
        'Values': ([basestring], False),
        'Key': (basestring, True)
    }


class ApplicationSource(AWSProperty):
    props = {
        'CloudFormationStackARN': (basestring, False),
        'TagFilters': ([TagFilter], False)
    }


class PredefinedScalingMetricSpecification(AWSProperty):
    props = {
        'ResourceLabel': (basestring, False),
        'PredefinedScalingMetricType': (basestring, True)
    }


class MetricDimension(AWSProperty):
    props = {
        'Value': (basestring, True),
        'Name': (basestring, True)
    }


class CustomizedScalingMetricSpecification(AWSProperty):
    props = {
        'MetricName': (basestring, True),
        'Statistic': (statistic_type, True),
        'Dimensions': ([MetricDimension], False),
        'Unit': (basestring, False),
        'Namespace': (basestring, True)
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


class ScalingInstruction(AWSProperty):
    props = {
        'ResourceId': (basestring, True),
        'ServiceNamespace': (service_namespace_type, True),
        'ScalableDimension': (scalable_dimension_type, True),
        'MinCapacity': (integer, True),
        'TargetTrackingConfigurations': (
            TargetTrackingConfiguration,
            True
        ),
        'MaxCapacity': (integer, True)
    }


class ScalingPlan(AWSObject):
    resource_type = "AWS::AutoScalingPlans::ScalingPlan"

    props = {
        'ApplicationSource': (ApplicationSource, True),
        'ScalingInstructions': ([ScalingInstruction], True)
    }
