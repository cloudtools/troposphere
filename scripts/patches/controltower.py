patches = [
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::ControlTower::EnabledBaseline.Parameter/Properties/Value/PrimitiveType",
        "value": "String",
    },
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::ControlTower::EnabledControl.EnabledControlParameter/Properties/Value/Type",
        "value": "object",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::ControlTower::EnabledControl.EnabledControlParameter/Properties/Value/PrimitiveType",
    },
]
