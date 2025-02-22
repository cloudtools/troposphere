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
]
