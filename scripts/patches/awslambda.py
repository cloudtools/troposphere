patches = [
    # Keep EventSourceMapping.ScalingConfig backward compatible while giving the
    # WebFunctionEndpoint property type a unique name.
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Lambda::WebFunctionEndpoint.ScalingConfig",
        "path": "/PropertyTypes/AWS::Lambda::WebFunctionEndpoint.WebFunctionEndpointScalingConfig",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Lambda::WebFunctionEndpoint.RegionalEndpoint/Properties/ScalingConfig/Type",
        "value": "WebFunctionEndpointScalingConfig",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::Lambda::WebFunctionEndpoint/Properties/ScalingConfig/Type",
        "value": "WebFunctionEndpointScalingConfig",
    },
    # Keep Function.LoggingConfig backward compatible while giving the
    # WebFunctionRevision property type a unique name.
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Lambda::WebFunctionRevision.LoggingConfig",
        "path": "/PropertyTypes/AWS::Lambda::WebFunctionRevision.WebFunctionRevisionLoggingConfig",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Lambda::WebFunctionRevision.TelemetryConfig/Properties/LoggingConfig/Type",
        "value": "WebFunctionRevisionLoggingConfig",
    },
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
