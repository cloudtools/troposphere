patches = [
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Batch::JobDefinition.JobTimeout",
        "path": "/PropertyTypes/AWS::Batch::JobDefinition.Timeout",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::Batch::JobDefinition/Properties/Timeout/Type",
        "value": "Timeout",
    },
]
