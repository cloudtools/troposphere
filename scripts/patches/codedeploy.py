patches = [
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CodeDeploy::DeploymentGroup.EC2TagFilter",
        "path": "/PropertyTypes/AWS::CodeDeploy::DeploymentGroup.Ec2TagFilters",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::CodeDeploy::DeploymentGroup/Properties/Ec2TagFilters/ItemType",
        "value": "Ec2TagFilters",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CodeDeploy::DeploymentGroup.EC2TagSetListObject/Properties/Ec2TagGroup/ItemType",
        "value": "Ec2TagFilters",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CodeDeploy::DeploymentGroup.EC2TagSet",
        "path": "/PropertyTypes/AWS::CodeDeploy::DeploymentGroup.Ec2TagSet",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::CodeDeploy::DeploymentGroup/Properties/Ec2TagSet/Type",
        "value": "Ec2TagSet",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CodeDeploy::DeploymentGroup.EC2TagSetListObject",
        "path": "/PropertyTypes/AWS::CodeDeploy::DeploymentGroup.Ec2TagSetListObject",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CodeDeploy::DeploymentGroup.Ec2TagSet/Properties/Ec2TagSetList/ItemType",
        "value": "Ec2TagSetListObject",
    },
    # backward compatibility
    {
        "op": "copy",
        "from": "/PropertyTypes/AWS::CodeDeploy::DeploymentGroup.TagFilter",
        "path": "/PropertyTypes/AWS::CodeDeploy::DeploymentGroup.OnPremisesInstanceTagFilters",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::CodeDeploy::DeploymentGroup/Properties/OnPremisesInstanceTagFilters/ItemType",
        "value": "OnPremisesInstanceTagFilters",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CodeDeploy::DeploymentGroup.ELBInfo",
        "path": "/PropertyTypes/AWS::CodeDeploy::DeploymentGroup.ElbInfoList",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CodeDeploy::DeploymentGroup.LoadBalancerInfo/Properties/ElbInfoList/ItemType",
        "value": "ElbInfoList",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CodeDeploy::DeploymentGroup.RevisionLocation",
        "path": "/PropertyTypes/AWS::CodeDeploy::DeploymentGroup.Revision",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CodeDeploy::DeploymentGroup.Deployment/Properties/Revision/Type",
        "value": "Revision",
    },
]
