patches = [
    # Rename ElasticBeanstalk::ConfigurationTemplate ConfigurationOptionSetting to OptionSetting - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::ElasticBeanstalk::ConfigurationTemplate.ConfigurationOptionSetting",
        "path": "/PropertyTypes/AWS::ElasticBeanstalk::ConfigurationTemplate.OptionSetting",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::ElasticBeanstalk::ConfigurationTemplate/Properties/OptionSettings/ItemType",
        "value": "OptionSetting",
    },
]
