patches = [
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::AppFlow::ConnectorProfile.CustomAuthCredentials/Properties/CredentialsMap/PrimitiveType",
        "value": "Json",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::AppFlow::ConnectorProfile.CustomAuthCredentials/Properties/CredentialsMap/Type",
    },
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::AppFlow::ConnectorProfile.OAuth2Properties/Properties/TokenUrlCustomProperties/PrimitiveType",
        "value": "Json",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::AppFlow::ConnectorProfile.OAuth2Properties/Properties/TokenUrlCustomProperties/Type",
    },
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::AppFlow::ConnectorProfile.CustomConnectorProfileProperties/Properties/ProfileProperties/PrimitiveType",
        "value": "Json",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::AppFlow::ConnectorProfile.CustomConnectorProfileProperties/Properties/ProfileProperties/Type",
    },
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::AppFlow::Flow.CustomConnectorSourceProperties/Properties/CustomProperties/PrimitiveType",
        "value": "Json",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::AppFlow::Flow.CustomConnectorSourceProperties/Properties/CustomProperties/Type",
    },
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::AppFlow::Flow.CustomConnectorDestinationProperties/Properties/CustomProperties/PrimitiveType",
        "value": "Json",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::AppFlow::Flow.CustomConnectorDestinationProperties/Properties/CustomProperties/Type",
    },
]
