patches = [
    # Rename AWS::SageMaker::Device.Device to AWS::SageMaker::Device.DeviceProperty
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::SageMaker::Device.Device",
        "path": "/PropertyTypes/AWS::SageMaker::Device.DeviceProperty",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::SageMaker::Device/Properties/Device/Type",
        "value": "DeviceProperty",
    },
    {
        "op": "remove",
        "path": "/ResourceTypes/AWS::SageMaker::Device/Properties/Device/PrimitiveType",
        "value": "DeviceProperty",
    },
]
