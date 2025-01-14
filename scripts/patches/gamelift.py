patches = [
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::GameLift::Fleet/Properties/AnywhereConfiguration/Type",
        "value": "AnywhereConfiguration",
    },
    {
        # Prefer ContainerFleet.LocationConfiguration over GameLift::Fleet.LocationConfiguration
        "op": "remove",
        "path": "/PropertyTypes/AWS::GameLift::Fleet.LocationConfiguration",
    },
    {
        # Prefer GameLift::ContainerFleet.ScalingPolicy over GameLift::Fleet.ScalingPolicy
        "op": "remove",
        "path": "/PropertyTypes/AWS::GameLift::ContainerFleet.ScalingPolicy",
    },
]
