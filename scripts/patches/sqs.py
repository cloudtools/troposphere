patches = [
    # Add RedrivePolicy for backward compatibility
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::SQS::Queue.RedrivePolicy",
        "value": {
            "Properties": {
                "deadLetterTargetArn": {"PrimitiveType": "String", "Required": False},
                "maxReceiveCount": {"PrimitiveType": "Integer", "Required": False},
            },
        },
    },
    {
        "op": "remove",
        "path": "/ResourceTypes/AWS::SQS::Queue/Properties/RedrivePolicy/PrimitiveType",
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::SQS::Queue/Properties/RedrivePolicy/Type",
        "value": "RedrivePolicy",
    },
]
