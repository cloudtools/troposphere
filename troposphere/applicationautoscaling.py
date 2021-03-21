from . import AWSObject, AWSProperty
from .validators import boolean, double, integer, positive_integer


class ScalableTargetAction(AWSProperty):
    props = {
        'MaxCapacity': (integer, False),
        'MinCapacity': (integer, False),
    }


class ScheduledAction(AWSProperty):
    props = {
        'EndTime': (str, False),
        'ScalableTargetAction': (ScalableTargetAction, False),
        'Schedule': (str, True),
        'ScheduledActionName': (str, True),
        'StartTime': (str, False),
    }


class SuspendedState(AWSProperty):
    props = {
        'DynamicScalingInSuspended': (boolean, False),
        'DynamicScalingOutSuspended': (boolean, False),
        'ScheduledScalingSuspended': (boolean, False),
    }


class ScalableTarget(AWSObject):
    resource_type = "AWS::ApplicationAutoScaling::ScalableTarget"

    props = {
        'MaxCapacity': (integer, True),
        'MinCapacity': (integer, True),
        'ResourceId': (str, True),
        'RoleARN': (str, True),
        'ScalableDimension': (str, True),
        'ScheduledActions': ([ScheduledAction], False),
        'ServiceNamespace': (str, True),
        'SuspendedState': (SuspendedState, False),
    }


class StepAdjustment(AWSProperty):
    props = {
        'MetricIntervalLowerBound': (integer, False),
        'MetricIntervalUpperBound': (integer, False),
        'ScalingAdjustment': (integer, True),
    }


class StepScalingPolicyConfiguration(AWSProperty):
    props = {
        'AdjustmentType': (str, False),
        'Cooldown': (integer, False),
        'MetricAggregationType': (str, False),
        'MinAdjustmentMagnitude': (integer, False),
        'StepAdjustments': ([StepAdjustment], False),
    }


class MetricDimension(AWSProperty):
    props = {
        'Name': (str, True),
        'Value': (str, True),
    }


class CustomizedMetricSpecification(AWSProperty):
    props = {
        'Dimensions': ([MetricDimension], False),
        'MetricName': (str, False),
        'Namespace': (str, False),
        'Statistic': (str, False),
        'Unit': (str, True),
    }


class PredefinedMetricSpecification(AWSProperty):
    props = {
        'PredefinedMetricType': (str, True),
        'ResourceLabel': (str, False),
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
        'TargetValue': (double, True),
    }


class ScalingPolicy(AWSObject):
    resource_type = "AWS::ApplicationAutoScaling::ScalingPolicy"

    props = {
        'PolicyName': (str, True),
        'PolicyType': (str, False),
        'ResourceId': (str, False),
        'ScalableDimension': (str, False),
        'ServiceNamespace': (str, False),
        'ScalingTargetId': (str, False),
        'StepScalingPolicyConfiguration': (
            StepScalingPolicyConfiguration,
            False,
        ),
        'TargetTrackingScalingPolicyConfiguration': (
            TargetTrackingScalingPolicyConfiguration,
            False,
        ),
    }
