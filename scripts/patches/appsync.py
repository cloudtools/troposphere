patches = [
    # Rename AWS::SageMaker::Device.Device to AWS::SageMaker::Device.DeviceProperty
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::AppSync::GraphQLApi/Properties/AdditionalAuthenticationProviders/Type",
        "value": "List",
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::AppSync::GraphQLApi/Properties/AdditionalAuthenticationProviders/ItemType",
        "value": "AdditionalAuthenticationProvider",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::AppSync::GraphQLApi/Properties/Tags/Type",
        "value": "List",
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::AppSync::GraphQLApi/Properties/Tags/ItemType",
        "value": "Tag",
    },
]
