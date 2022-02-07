patches = [
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::AutoScaling::AutoScalingGroup.NotificationConfiguration",
        "path": "/PropertyTypes/AWS::AutoScaling::AutoScalingGroup.NotificationConfigurations",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::AutoScaling::AutoScalingGroup/Properties/NotificationConfigurations/ItemType",
        "value": "NotificationConfigurations",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::AutoScaling::AutoScalingGroup.TagProperty",
    },
    {
        "op": "remove",
        "path": "/ResourceTypes/AWS::AutoScaling::AutoScalingGroup/Properties/Tags/ItemType",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::AutoScaling::ScalingPolicy.StepAdjustment",
        "path": "/PropertyTypes/AWS::AutoScaling::ScalingPolicy.StepAdjustments",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::AutoScaling::ScalingPolicy/Properties/StepAdjustments/ItemType",
        "value": "StepAdjustments",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::AutoScaling::LaunchConfiguration.BlockDevice",
        "path": "/PropertyTypes/AWS::AutoScaling::LaunchConfiguration.EBSBlockDevice",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::AutoScaling::LaunchConfiguration.BlockDeviceMapping/Properties/Ebs/Type",
        "value": "EBSBlockDevice",
    },
]
