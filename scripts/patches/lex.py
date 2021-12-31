patches = [
    # Replace AWS::Lex::ResourcePolicy.Policy from Type "Policy" to Map
    # Note: a policy validator will replace this as well.
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::Lex::ResourcePolicy/Properties/Policy/Type",
        "value": "Map",
    },
    # Fix missing Type for AWS::Lex::BotAlias TextLogDestination
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::Lex::BotAlias.TextLogDestination/Properties/CloudWatch/Type",
        "value": "CloudWatchLogGroupLogDestination",
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::Lex::Bot/Properties/BotTags/PrimitiveType",
        "value": "Tags",
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::Lex::Bot/Properties/TestBotAliasTags/PrimitiveType",
        "value": "Tags",
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::Lex::BotAlias/Properties/BotAliasTags/PrimitiveType",
        "value": "Tags",
    },
]
