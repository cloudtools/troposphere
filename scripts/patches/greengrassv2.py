patches = [
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::GreengrassV2::Deployment.IoTJobRateIncreaseCriteria",
    },
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::GreengrassV2::Deployment.IoTJobRateIncreaseCriteria",
        "value": {
            "Properties": {
                "NumberOfNotifiedThings": {
                    "PrimitiveType": "Integer",
                    "Required": False,
                },
                "NumberOfSucceededThings": {
                    "PrimitiveType": "Integer",
                    "Required": False,
                },
            },
        },
    },
]
