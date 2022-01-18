patches = [
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Redshift::ClusterParameterGroup.Parameter",
        "path": "/PropertyTypes/AWS::Redshift::ClusterParameterGroup.AmazonRedshiftParameter",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::Redshift::ClusterParameterGroup/Properties/Parameters/ItemType",
        "value": "AmazonRedshiftParameter",
    },
]
