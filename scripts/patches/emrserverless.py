patches = [
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::EMRServerless::Application.ConfigurationObject/Properties/Configurations",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::EMRServerless::JobRun.Configuration/Properties/Configurations/ItemType",
        "value": "object",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::EMRServerless::Session.Configuration/Properties/Configurations/ItemType",
        "value": "object",
    },
]
