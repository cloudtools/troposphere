from . import AWSObject, AWSProperty
from .validators import integer


class ScalableTarget(AWSObject):
    resource_type = "AWS::ApplicationAutoScaling::ScalableTarget"

    props = {
        'MaxCapacity': (integer, True),
        'MinCapacity': (integer, True),
        'ResourceId': (basestring, True),
        'RoleARN': (basestring, True),
        'ScalableDimension': (basestring, True),
        'ServiceNamespace': (basestring, True),
    }


class StepAdjustment(AWSProperty):
    props = {
        'MetricIntervalLowerBound': (integer, False),
        'MetricIntervalUpperBound': (integer, False),
        'ScalingAdjustment': (integer, True),
    }


class StepScalingPolicyConfiguration(AWSProperty):
    props = {
        'AdjustmentType': (basestring, False),
        'Cooldown': (integer, False),
        'MetricAggregationType': (basestring, False),
        'MinAdjustmentMagnitude': (integer, False),
        'StepAdjustments': ([StepAdjustment], False),
    }


class ScalingPolicy(AWSObject):
    resource_type = "AWS::ApplicationAutoScaling::ScalingPolicy"

    props = {
        'PolicyName': (basestring, True),
        'PolicyType': (basestring, False),
        'ResourceId': (basestring, False),
        'ScalableDimension': (basestring, False),
        'ServiceNamespace': (basestring, False),
        'ScalingTargetId': (basestring, False),
        'StepScalingPolicyConfiguration': (
            StepScalingPolicyConfiguration,
            False,
        ),
    }
