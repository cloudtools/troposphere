patches = [
    # Rename AWS::ECS::Cluster.ClusterSettings to AWS::ECS::Cluster.ClusterSetting - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::ECS::Cluster.ClusterSettings",
        "path": "/PropertyTypes/AWS::ECS::Cluster.ClusterSetting",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::ECS::Cluster/Properties/ClusterSettings/ItemType",
        "value": "ClusterSetting",
    },
    # Rename AWS::ECS::TaskDefinition.KeyValuePair to AWS::ECS::TaskDefinition.Environment - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::ECS::TaskDefinition.KeyValuePair",
        "path": "/PropertyTypes/AWS::ECS::TaskDefinition.Environment",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::ECS::TaskDefinition.ContainerDefinition/Properties/Environment/ItemType",
        "value": "Environment",
    },
    # Rename AWS::ECS::TaskDefinition.VolumeFrom to AWS::ECS::TaskDefinition.VolumesFrom - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::ECS::TaskDefinition.VolumeFrom",
        "path": "/PropertyTypes/AWS::ECS::TaskDefinition.VolumesFrom",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::ECS::TaskDefinition.ContainerDefinition/Properties/VolumesFrom/ItemType",
        "value": "VolumesFrom",
    },
    # backward compatibility
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::ECS::TaskDefinition.ProxyConfiguration/Properties/ProxyConfigurationProperties/PrimitiveType",
        "value": "list",
    },
    # Rename AWS::ECS::TaskDefinition.TaskDefinitionPlacementConstraint to AWS::ECS::TaskDefinition.PlacementConstraint - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::ECS::TaskDefinition.TaskDefinitionPlacementConstraint",
        "path": "/PropertyTypes/AWS::ECS::TaskDefinition.PlacementConstraint",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::ECS::TaskDefinition/Properties/PlacementConstraints/ItemType",
        "value": "PlacementConstraint",
    },
    # backward compatibility - prefer AWS::ECS::Service.NetworkConfiguration "AwsvpcConfiguration" over AWS::ECS::TaskSet.NetworkConfiguration "AwsVpcConfiguration"
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::ECS::TaskSet.NetworkConfiguration",
    },
    # backward compatibility
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::ECS::TaskSet.AwsVpcConfiguration",
    },
    # backward compatibility
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::ECS::TaskSet.LoadBalancer",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::ECS::Service.AwsVpcConfiguration",
        "path": "/PropertyTypes/AWS::ECS::Service.AwsvpcConfiguration",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::ECS::Service.NetworkConfiguration/Properties/AwsvpcConfiguration/Type",
        "value": "AwsvpcConfiguration",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::ECS::TaskDefinition.HostVolumeProperties",
        "path": "/PropertyTypes/AWS::ECS::TaskDefinition.Host",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::ECS::TaskDefinition.Volume/Properties/Host/Type",
        "value": "Host",
    },
    # Likely a temporary removal awaiting spec updates from AWS
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::ECS::ExpressGatewayService.ExpressGatewayServiceConfiguration",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::ECS::ExpressGatewayService.ECSManagedResourceArns",
    },
]
