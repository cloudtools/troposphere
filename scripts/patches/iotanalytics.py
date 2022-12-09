patches = [
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::IoTAnalytics::Dataset.Filter",
        "path": "/PropertyTypes/AWS::IoTAnalytics::Dataset.QueryActionFilter",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::IoTAnalytics::Dataset.QueryAction/Properties/Filters/ItemType",
        "value": "QueryActionFilter",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::IoTAnalytics::Pipeline.Channel",
        "path": "/PropertyTypes/AWS::IoTAnalytics::Pipeline.ActivityChannel",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::IoTAnalytics::Pipeline.Activity/Properties/Channel/Type",
        "value": "ActivityChannel",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::IoTAnalytics::Pipeline.Datastore",
        "path": "/PropertyTypes/AWS::IoTAnalytics::Pipeline.ActivityDatastore",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::IoTAnalytics::Pipeline.Activity/Properties/Datastore/Type",
        "value": "ActivityDatastore",
    },
]
