patches = [
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Transfer::WebApp.IdentityProviderDetails",
        "path": "/PropertyTypes/AWS::Transfer::WebApp.WebAppIdentityProviderDetails",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::Transfer::WebApp/Properties/IdentityProviderDetails/Type",
        "value": "WebAppIdentityProviderDetails",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Transfer::WebApp.EndpointDetails",
        "path": "/PropertyTypes/AWS::Transfer::WebApp.WebAppEndpointDetails",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::Transfer::WebApp/Properties/EndpointDetails/Type",
        "value": "WebAppEndpointDetails",
    },
]
