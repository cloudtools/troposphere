patches = [
    # Replace AWS::Lex::ResourcePolicy.Policy from Type "Policy" to Map
    # Note: a policy validator will replace this as well.
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
