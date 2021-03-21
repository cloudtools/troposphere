from troposphere import Template, Ref
from troposphere.applicationautoscaling import (
    ScalableTarget,
    StepAdjustment,
    StepScalingPolicyConfiguration,
    ScalingPolicy,
)


t = Template()

scalable_target = ScalableTarget(
    'scalableTarget',
    MaxCapacity=2,
    MinCapacity=1,
    ResourceId='service/ecsStack',
    RoleARN='Access Management (IAM) role',
    ScalableDimension='ecs:service:DesiredCount',
    ServiceNamespace='ecs',
)

scaling_policy = ScalingPolicy(
    'scalingPolicy',
    PolicyName='AStepPolicy',
    PolicyType='StepScaling',
    ScalingTargetId=Ref(scalable_target),
    StepScalingPolicyConfiguration=StepScalingPolicyConfiguration(
        AdjustmentType='PercentChangeInCapacity',
        Cooldown=60,
        MetricAggregationType='Average',
        StepAdjustments=[
            StepAdjustment(
                MetricIntervalLowerBound=0,
                ScalingAdjustment=200,
            ),
        ],
    ),
)

t = Template()

t.add_resource(scalable_target)
t.add_resource(scaling_policy)

print(t.to_json())
