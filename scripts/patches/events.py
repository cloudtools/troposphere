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
]
