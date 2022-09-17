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
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::Redshift::ScheduledAction/Properties/TargetAction/PrimitiveType",
        "value": "Json",
    },
]
