patches = [
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::FMS::Policy/Properties/ResourceTags/ItemType",
        "value": "Tag",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::FMS::Policy.ResourceTag",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::FMS::Policy/Properties/Tags/ItemType",
        "value": "Tag",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::FMS::Policy.PolicyTag",
    },
]
