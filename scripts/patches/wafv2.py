patches = [
    # LoggingConfiguration FieldToMatch is different from WebACL or RuleGroup FieldToMatch
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAFv2::LoggingConfiguration.FieldToMatch",
        "path": "/PropertyTypes/AWS::WAFv2::LoggingConfiguration.LoggingConfigurationFieldToMatch",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::WAFv2::LoggingConfiguration/Properties/RedactedFields/ItemType",
        "value": "LoggingConfigurationFieldToMatch",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAFv2::WebACL.Rule",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.WebACLRule",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::WAFv2::WebACL/Properties/Rules/ItemType",
        "value": "WebACLRule",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAFv2::RuleGroup.Rule",
        "path": "/PropertyTypes/AWS::WAFv2::RuleGroup.RuleGroupRule",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::WAFv2::RuleGroup/Properties/Rules/ItemType",
        "value": "RuleGroupRule",
    },
    # Remove redundent RuleGroup properties
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::WAFv2::RuleGroup.AndStatement",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::WAFv2::RuleGroup.LabelSummary",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::WAFv2::RuleGroup.NotStatement",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::WAFv2::RuleGroup.OrStatement",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::WAFv2::RuleGroup.RateBasedStatement",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::WAFv2::RuleGroup.Statement",
    },
]
