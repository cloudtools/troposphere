patches = [
    # Rename AWS::IoTSiteWise::AccessPolicy.Portal to AWS::IoTSiteWise::AccessPolicy.PortalProperty due to conflict with Portal resource name
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::IoTSiteWise::AccessPolicy.Portal",
        "path": "/PropertyTypes/AWS::IoTSiteWise::AccessPolicy.PortalProperty",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::IoTSiteWise::AccessPolicy.AccessPolicyResource/Properties/Portal/Type",
        "value": "PortalProperty",
    },
    # Rename AWS::IoTSiteWise::AccessPolicy.Project to AWS::IoTSiteWise::AccessPolicy.ProjectProperty due to conflict with Project resource name
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::IoTSiteWise::AccessPolicy.Project",
        "path": "/PropertyTypes/AWS::IoTSiteWise::AccessPolicy.ProjectProperty",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::IoTSiteWise::AccessPolicy.AccessPolicyResource/Properties/Project/Type",
        "value": "ProjectProperty",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::IoTSiteWise::ComputationModel.ComputationModelDataBindingValue/Properties/List/ItemType",
        "value": "object",
    },
]
