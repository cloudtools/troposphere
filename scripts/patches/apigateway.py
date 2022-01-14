patches = [
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::ApiGateway::Stage.CanarySetting",
        "path": "/PropertyTypes/AWS::ApiGateway::Stage.StageCanarySetting",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::ApiGateway::Stage/Properties/CanarySetting/Type",
        "value": "StageCanarySetting",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::ApiGateway::Deployment.StageDescription/Properties/CanarySetting/Type",
        "value": "DeploymentCanarySettings",
    },
    # Technically there are two different EndpointConfiguration but keep using
    # this one for backward compatibility
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::ApiGateway::DomainName.EndpointConfiguration",
    },
]
