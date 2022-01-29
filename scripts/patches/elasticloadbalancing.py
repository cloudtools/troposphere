patches = [
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::ElasticLoadBalancing::LoadBalancer.Listeners",
        "path": "/PropertyTypes/AWS::ElasticLoadBalancing::LoadBalancer.Listener",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::ElasticLoadBalancing::LoadBalancer/Properties/Listeners/ItemType",
        "value": "Listener",
    },
    # Prevent mapping List of Json to Tags. Make it a List of dict instead.
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::ElasticLoadBalancing::LoadBalancer.Policies/Properties/Attributes/PrimitiveItemType",
        "value": "dict",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::ElasticLoadBalancing::LoadBalancer.Policies",
        "path": "/PropertyTypes/AWS::ElasticLoadBalancing::LoadBalancer.Policy",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::ElasticLoadBalancing::LoadBalancer/Properties/Policies/ItemType",
        "value": "Policy",
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::ElasticLoadBalancing::LoadBalancer/Properties/AppCookieStickinessPolicy/PrimitiveType",
        "value": "list",
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::ElasticLoadBalancing::LoadBalancer/Properties/AvailabilityZones/PrimitiveType",
        "value": "list",
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::ElasticLoadBalancing::LoadBalancer/Properties/LBCookieStickinessPolicy/PrimitiveType",
        "value": "list",
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::ElasticLoadBalancing::LoadBalancer/Properties/Listeners/PrimitiveType",
        "value": "list",
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::ElasticLoadBalancing::LoadBalancer/Properties/Policies/PrimitiveType",
        "value": "list",
    },
]
