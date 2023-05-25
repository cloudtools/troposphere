patches = [
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::Events::EventBus/Properties/Tags/ItemType",
        "value": "Tags",
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::Events::Rule/Properties/Tags",
        "value": {
            "Type": "List",
            "ItemType": "Tags",
            "Required": False,
        },
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
