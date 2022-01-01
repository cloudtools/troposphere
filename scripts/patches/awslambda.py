patches = [
    # Remove AWS::Lambda::EventSourceMapping.DestinationConfig and prefer AWS::Lambda::EventInvokeConfig.DestinationConfig
    # which includes OnSuccess
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Lambda::EventSourceMapping.DestinationConfig",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Lambda::EventSourceMapping.OnFailure",
    },
    # Rename VpcConfig to VPCConfig - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Lambda::Function.VpcConfig",
        "path": "/PropertyTypes/AWS::Lambda::Function.VPCConfig",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::Lambda::Function/Properties/VpcConfig/Type",
        "value": "VPCConfig",
    },
]
