patches = [
    # Rename AWS::ECR::ReplicationConfiguration.ReplicationConfiguration to AWS::ECR::ReplicationConfiguration.ReplicationConfigurationProperty
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::ECR::ReplicationConfiguration.ReplicationConfiguration",
        "path": "/PropertyTypes/AWS::ECR::ReplicationConfiguration.ReplicationConfigurationProperty",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::ECR::ReplicationConfiguration/Properties/ReplicationConfiguration/Type",
        "value": "ReplicationConfigurationProperty",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/ResourceTypes/AWS::ECR::ReplicationConfiguration/Properties/ReplicationConfiguration",
        "path": "/ResourceTypes/AWS::ECR::ReplicationConfiguration/Properties/ReplicationConfigurationProperty",
    },
]
