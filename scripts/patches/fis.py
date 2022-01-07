patches = [
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::FIS::ExperimentTemplate/Properties/Tags/PrimitiveType",
        "value": "Map",
    },
    {
        "op": "remove",
        "path": "/ResourceTypes/AWS::FIS::ExperimentTemplate/Properties/Tags/Type",
    },
]
