from . import AWSObject, AWSProperty
from .validators import boolean, floatingpoint, integer, positive_integer


class ScalableTargetAction(AWSProperty):
    props = {
        'MaxCapacity': (integer, False),
        'MinCapacity': (integer, False),
    }


class ScheduledAction(AWSProperty):
    props = {
        'EndTime': (basestring, False),
        'ScalableTargetAction': (ScalableTargetAction, False),
        'Schedule': (basestring, True),
        'ScheduledActionName': (basestring, True),
        'StartTime': (basestring, False),
    }


class ScalableTarget(AWSObject):
    resource_type = "AWS::ApplicationAutoScaling::ScalableTarget"

    props = {
        'MaxCapacity': (integer, True),
        'MinCapacity': (integer, True),
        'ResourceId': (basestring, True),
        'RoleARN': (basestring, True),
        'ScalableDimension': (basestring, True),
        'ScheduledActions': ([ScheduledAction], False),
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


class MetricDimension(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Value': (basestring, True),
    }


class CustomizedMetricSpecification(AWSProperty):
    props = {
        'Dimensions': ([MetricDimension], False),
        'MetricName': (basestring, False),
        'Namespace': (basestring, False),
        'Statistic': (basestring, False),
        'Unit': (basestring, True),
    }


class PredefinedMetricSpecification(AWSProperty):
    props = {
        'PredefinedMetricType': (basestring, True),
        'ResourceLabel': (basestring, False),
    }


class TargetTrackingScalingPolicyConfiguration(AWSProperty):
    props = {
        'CustomizedMetricSpecification':
            (CustomizedMetricSpecification, False),
        'DisableScaleIn': (boolean, False),
        'PredefinedMetricSpecification':
            (PredefinedMetricSpecification, False),
        'ScaleInCooldown': (positive_integer, False),
        'ScaleOutCooldown': (positive_integer, False),
        'TargetValue': (floatingpoint, True),
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
        'TargetTrackingScalingPolicyConfiguration': (
            TargetTrackingScalingPolicyConfiguration,
            False,
        ),
    }
