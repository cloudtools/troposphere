patches = [
    # Add AWS::MemoryDB::Cluster Endpoint
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::MemoryDB::Cluster/Properties/ClusterEndpoint",
        "value": {"Type": "Endpoint"},
    },
]
