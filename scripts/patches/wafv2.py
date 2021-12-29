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
    # backward compatibility - StatementOne
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAFv2::WebACL.Statement",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.StatementOne",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.StatementOne/Properties/AndStatement/Type",
        "value": "AndStatementOne",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.StatementOne/Properties/NotStatement/Type",
        "value": "NotStatementOne",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.StatementOne/Properties/OrStatement/Type",
        "value": "OrStatementOne",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.StatementOne/Properties/RateBasedStatement/Type",
        "value": "RateBasedStatementOne",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAFv2::WebACL.AndStatement",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.AndStatementOne",
    },
    {
        "op": "copy",
        "from": "/PropertyTypes/AWS::WAFv2::WebACL.AndStatementOne",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.AndStatementTwo",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAFv2::WebACL.NotStatement",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.NotStatementOne",
    },
    {
        "op": "copy",
        "from": "/PropertyTypes/AWS::WAFv2::WebACL.NotStatementOne",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.NotStatementTwo",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAFv2::WebACL.OrStatement",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.OrStatementOne",
    },
    {
        "op": "copy",
        "from": "/PropertyTypes/AWS::WAFv2::WebACL.OrStatementOne",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.OrStatementTwo",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAFv2::WebACL.RateBasedStatement",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.RateBasedStatementOne",
    },
    {
        "op": "copy",
        "from": "/PropertyTypes/AWS::WAFv2::WebACL.RateBasedStatementOne",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.RateBasedStatementTwo",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.AndStatementOne/Properties/Statements/ItemType",
        "value": "StatementTwo",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.NotStatementOne/Properties/Statement/Type",
        "value": "StatementTwo",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.OrStatementOne/Properties/Statements/ItemType",
        "value": "StatementTwo",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.RateBasedStatementOne/Properties/ScopeDownStatement/Type",
        "value": "StatementTwo",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.AndStatementTwo/Properties/Statements/ItemType",
        "value": "StatementThree",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.NotStatementTwo/Properties/Statement/Type",
        "value": "StatementThree",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.OrStatementTwo/Properties/Statements/ItemType",
        "value": "StatementThree",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.RateBasedStatementTwo/Properties/ScopeDownStatement/Type",
        "value": "StatementThree",
    },
    # backward compatibility - StatementTwo
    {
        "op": "copy",
        "from": "/PropertyTypes/AWS::WAFv2::WebACL.StatementOne",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.StatementTwo",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.StatementTwo/Properties/AndStatement/Type",
        "value": "AndStatementTwo",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.StatementTwo/Properties/NotStatement/Type",
        "value": "NotStatementTwo",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.StatementTwo/Properties/OrStatement/Type",
        "value": "OrStatementTwo",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.StatementTwo/Properties/RateBasedStatement/Type",
        "value": "RateBasedStatementTwo",
    },
    # backward compatibility - StatementThree
    {
        "op": "copy",
        "from": "/PropertyTypes/AWS::WAFv2::WebACL.StatementOne",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.StatementThree",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.StatementThree/Properties/AndStatement",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.StatementThree/Properties/NotStatement",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.StatementThree/Properties/OrStatement",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.StatementThree/Properties/RateBasedStatement",
    },
    # Insert StatementOne into RuleGroupRule and WebACLRule
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAFv2::RuleGroup.RuleGroupRule/Properties/Statement/Type",
        "value": "StatementOne",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.WebACLRule/Properties/Statement/Type",
        "value": "StatementOne",
    },
    # backward compatibility - remove ManagedRuleGroupStatement ScopeDownStatement
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::WAFv2::WebACL.ManagedRuleGroupStatement/Properties/ScopeDownStatement",
    },
]
