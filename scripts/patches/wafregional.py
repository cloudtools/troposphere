patches = [
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAFRegional::WebACL.Rule",
        "path": "/PropertyTypes/AWS::WAFRegional::WebACL.Rules",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::WAFRegional::WebACL/Properties/Rules/ItemType",
        "value": "Rules",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAFRegional::ByteMatchSet.ByteMatchTuple",
        "path": "/PropertyTypes/AWS::WAFRegional::ByteMatchSet.ByteMatchTuples",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::WAFRegional::ByteMatchSet/Properties/ByteMatchTuples/ItemType",
        "value": "ByteMatchTuples",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAFRegional::IPSet.IPSetDescriptor",
        "path": "/PropertyTypes/AWS::WAFRegional::IPSet.IPSetDescriptors",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::WAFRegional::IPSet/Properties/IPSetDescriptors/ItemType",
        "value": "IPSetDescriptors",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAFRegional::GeoMatchSet.GeoMatchConstraint",
        "path": "/PropertyTypes/AWS::WAFRegional::GeoMatchSet.GeoMatchConstraints",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::WAFRegional::GeoMatchSet/Properties/GeoMatchConstraints/ItemType",
        "value": "GeoMatchConstraints",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAFRegional::RateBasedRule.Predicate",
        "path": "/PropertyTypes/AWS::WAFRegional::RateBasedRule.Predicates",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::WAFRegional::RateBasedRule/Properties/MatchPredicates/ItemType",
        "value": "Predicates",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::WAFRegional::Rule.Predicate",
        "value": "Predicates",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::WAFRegional::Rule/Properties/Predicates/ItemType",
        "value": "Predicates",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::WAFRegional::SqlInjectionMatchSet.SqlInjectionMatchTuple",
        "path": "/PropertyTypes/AWS::WAFRegional::SqlInjectionMatchSet.SqlInjectionMatchTuples",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::WAFRegional::SqlInjectionMatchSet/Properties/SqlInjectionMatchTuples/ItemType",
        "value": "SqlInjectionMatchTuples",
    },
]
