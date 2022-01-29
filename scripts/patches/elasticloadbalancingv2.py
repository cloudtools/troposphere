patches = [
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::ElasticLoadBalancingV2::ListenerRule.RuleCondition",
        "path": "/PropertyTypes/AWS::ElasticLoadBalancingV2::ListenerRule.Condition",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::ElasticLoadBalancingV2::ListenerRule/Properties/Conditions/ItemType",
        "value": "Condition",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::ElasticLoadBalancingV2::LoadBalancer.LoadBalancerAttribute",
        "path": "/PropertyTypes/AWS::ElasticLoadBalancingV2::LoadBalancer.LoadBalancerAttributes",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::ElasticLoadBalancingV2::LoadBalancer/Properties/LoadBalancerAttributes/ItemType",
        "value": "LoadBalancerAttributes",
    },
    # duplicate AuthenticateOidcConfig
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::ElasticLoadBalancingV2::ListenerRule.AuthenticateOidcConfig",
        "path": "/PropertyTypes/AWS::ElasticLoadBalancingV2::ListenerRule.ListenerRuleAuthenticateOidcConfig",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::ElasticLoadBalancingV2::ListenerRule.Action/Properties/AuthenticateOidcConfig/Type",
        "value": "ListenerRuleAuthenticateOidcConfig",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::ElasticLoadBalancingV2::ListenerRule.Action",
        "path": "/PropertyTypes/AWS::ElasticLoadBalancingV2::ListenerRule.ListenerRuleAction",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::ElasticLoadBalancingV2::ListenerRule/Properties/Actions/ItemType",
        "value": "ListenerRuleAction",
    },
]
