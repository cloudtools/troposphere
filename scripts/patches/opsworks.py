patches = [
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::OpsWorks::App.EnvironmentVariable",
        "path": "/PropertyTypes/AWS::OpsWorks::App.Environment",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::OpsWorks::App/Properties/Environment/ItemType",
        "value": "Environment",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::OpsWorks::Layer.LifecycleEventConfiguration",
        "path": "/PropertyTypes/AWS::OpsWorks::Layer.LifeCycleConfiguration",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::OpsWorks::Layer/Properties/LifecycleEventConfiguration/Type",
        "value": "LifeCycleConfiguration",
    },
]
