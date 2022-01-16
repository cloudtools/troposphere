patches = [
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAF::ByteMatchSet.ByteMatchTuple",
        "path": "/PropertyTypes/AWS::WAF::ByteMatchSet.ByteMatchTuples",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::WAF::ByteMatchSet/Properties/ByteMatchTuples/ItemType",
        "value": "ByteMatchTuples",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAF::IPSet.IPSetDescriptor",
        "path": "/PropertyTypes/AWS::WAF::IPSet.IPSetDescriptors",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::WAF::IPSet/Properties/IPSetDescriptors/ItemType",
        "value": "IPSetDescriptors",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAF::Rule.Predicate",
        "path": "/PropertyTypes/AWS::WAF::Rule.Predicates",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::WAF::Rule/Properties/Predicates/ItemType",
        "value": "Predicates",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAF::SqlInjectionMatchSet.SqlInjectionMatchTuple",
        "path": "/PropertyTypes/AWS::WAF::SqlInjectionMatchSet.SqlInjectionMatchTuples",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::WAF::SqlInjectionMatchSet/Properties/SqlInjectionMatchTuples/ItemType",
        "value": "SqlInjectionMatchTuples",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAF::WebACL.WafAction",
        "path": "/PropertyTypes/AWS::WAF::WebACL.Action",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::WAF::WebACL/Properties/DefaultAction/Type",
        "value": "Action",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::WAF::WebACL.ActivatedRule/Properties/Action/Type",
        "value": "Action",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAF::WebACL.ActivatedRule",
        "path": "/PropertyTypes/AWS::WAF::WebACL.Rules",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::WAF::WebACL/Properties/Rules/ItemType",
        "value": "Rules",
    },
]
