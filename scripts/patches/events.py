patches = [
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::Events::EventBus/Properties/Tags/ItemType",
        "value": "Tags",
    },
    # Remove unused Tag and TagEntry (remapped to troposphere Tags)
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Events::Rule.Tag",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Events::EventBus.TagEntry",
    },
]
