patches = [
    # Remove attribute property EventIntegrationAssociation and Metadata
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::AppIntegrations::EventIntegration.EventIntegrationAssociation",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::AppIntegrations::EventIntegration.Metadata",
    },
]
