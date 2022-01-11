patches = [
    # Remove attribute property ClusterEndpoint
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Route53RecoveryControl::Cluster.ClusterEndpoint",
    },
]
