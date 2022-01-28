patches = [
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::MediaConnect::FlowOutput.Encryption",
        "path": "/PropertyTypes/AWS::MediaConnect::FlowOutput.FlowOutputEncryption",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::MediaConnect::FlowOutput/Properties/Encryption/Type",
        "value": "FlowOutputEncryption",
    },
]
