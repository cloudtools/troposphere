patches = [
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Config::ConfigRule.SourceDetail",
        "path": "/PropertyTypes/AWS::Config::ConfigRule.SourceDetails",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Config::ConfigRule.Source/Properties/SourceDetails/ItemType",
        "value": "SourceDetails",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Config::ConfigurationAggregator.AccountAggregationSource",
        "path": "/PropertyTypes/AWS::Config::ConfigurationAggregator.AccountAggregationSources",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::Config::ConfigurationAggregator/Properties/AccountAggregationSources/ItemType",
        "value": "AccountAggregationSources",
    },
]
