patches = [
    # Rename AWS::S3::StorageLens.DataExport to AWS::S3::StorageLens.StorageLensDataExport due to conflict with AWS::S3::Bucket.DataExport
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::S3::StorageLens.DataExport",
        "path": "/PropertyTypes/AWS::S3::StorageLens.StorageLensDataExport",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::S3::StorageLens.StorageLensConfiguration/Properties/DataExport/Type",
        "value": "StorageLensDataExport",
    },
    # Rename AWS::S3::StorageLensGroup.Filter to AWS::S3::StorageLensGroup.StorageLensFilter due to conflict with AWS::S3::Bucket.Filter
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::S3::StorageLensGroup.Filter",
        "path": "/PropertyTypes/AWS::S3::StorageLensGroup.StorageLensFilter",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::S3::StorageLensGroup/Properties/Filter/Type",
        "value": "StorageLensFilter",
    },
    # Rename AWS::S3::LifecycleConfiguration.Rule to AWS::S3::LifecycleConfiguration.LifecycleRule - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::S3::Bucket.Rule",
        "path": "/PropertyTypes/AWS::S3::Bucket.LifecycleRule",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::S3::Bucket.LifecycleConfiguration/Properties/Rules/ItemType",
        "value": "LifecycleRule",
    },
    # Rename AWS::S3::Bucket.Transition to AWS::S3::Bucket.LifecycleRuleTransition - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::S3::Bucket.Transition",
        "path": "/PropertyTypes/AWS::S3::Bucket.LifecycleRuleTransition",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::S3::Bucket.LifecycleRule/Properties/Transition/Type",
        "value": "LifecycleRuleTransition",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::S3::Bucket.LifecycleRule/Properties/Transitions/ItemType",
        "value": "LifecycleRuleTransition",
    },
    # Rename AWS::S3::Bucket.CorsRule to AWS::S3::Bucket.CorsRule - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::S3::Bucket.CorsRule",
        "path": "/PropertyTypes/AWS::S3::Bucket.CorsRules",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::S3::Bucket.CorsConfiguration/Properties/CorsRules/ItemType",
        "value": "CorsRules",
    },
    # Rename AWS::S3::Bucket.FilterRule to AWS::S3::Bucket.Rules - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::S3::Bucket.FilterRule",
        "path": "/PropertyTypes/AWS::S3::Bucket.Rules",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::S3::Bucket.S3KeyFilter/Properties/Rules/ItemType",
        "value": "Rules",
    },
    # Rename AWS::S3::Bucket.S3KeyFilter to AWS::S3::Bucket.S3Key - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::S3::Bucket.S3KeyFilter",
        "path": "/PropertyTypes/AWS::S3::Bucket.S3Key",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::S3::Bucket.NotificationFilter/Properties/S3Key/Type",
        "value": "S3Key",
    },
    # Rename AWS::S3::Bucket.NotificationFilter to AWS::S3::Bucket.Filter - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::S3::Bucket.NotificationFilter",
        "path": "/PropertyTypes/AWS::S3::Bucket.Filter",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::S3::Bucket.LambdaConfiguration/Properties/Filter/Type",
        "value": "Filter",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::S3::Bucket.QueueConfiguration/Properties/Filter/Type",
        "value": "Filter",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::S3::Bucket.TopicConfiguration/Properties/Filter/Type",
        "value": "Filter",
    },
    # Rename AWS::S3::Bucket.LambdaConfiguration to AWS::S3::Bucket.LambdaConfigurations - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::S3::Bucket.LambdaConfiguration",
        "path": "/PropertyTypes/AWS::S3::Bucket.LambdaConfigurations",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::S3::Bucket.NotificationConfiguration/Properties/LambdaConfigurations/ItemType",
        "value": "LambdaConfigurations",
    },
    # Rename AWS::S3::Bucket.QueueConfigurations to AWS::S3::Bucket.QueueConfigurations - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::S3::Bucket.QueueConfiguration",
        "path": "/PropertyTypes/AWS::S3::Bucket.QueueConfigurations",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::S3::Bucket.NotificationConfiguration/Properties/QueueConfigurations/ItemType",
        "value": "QueueConfigurations",
    },
    # Rename AWS::S3::Bucket.TopicConfiguration to AWS::S3::Bucket.TopicConfigurations - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::S3::Bucket.TopicConfiguration",
        "path": "/PropertyTypes/AWS::S3::Bucket.TopicConfigurations",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::S3::Bucket.NotificationConfiguration/Properties/TopicConfigurations/ItemType",
        "value": "TopicConfigurations",
    },
    # Rename AWS::S3::Bucket.ReplicationDestination to AWS::S3::Bucket.ReplicationConfigurationRulesDestination - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::S3::Bucket.ReplicationDestination",
        "path": "/PropertyTypes/AWS::S3::Bucket.ReplicationConfigurationRulesDestination",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::S3::Bucket.ReplicationRule/Properties/Destination/Type",
        "value": "ReplicationConfigurationRulesDestination",
    },
    # Rename AWS::S3::Bucket.ReplicationRule to AWS::S3::Bucket.ReplicationConfigurationRules - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::S3::Bucket.ReplicationRule",
        "path": "/PropertyTypes/AWS::S3::Bucket.ReplicationConfigurationRules",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::S3::Bucket.ReplicationConfiguration/Properties/Rules/ItemType",
        "value": "ReplicationConfigurationRules",
    },
]
