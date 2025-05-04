patches = [
    # Fix different Subscriber properties
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Budgets::BudgetsAction.Subscriber",
        "path": "/PropertyTypes/AWS::Budgets::BudgetsAction.ActionSubscriber",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::Budgets::BudgetsAction/Properties/Subscribers/ItemType",
        "value": "ActionSubscriber",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Budgets::Budget.Expression/Properties/And/ItemType",
        "value": "object",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Budgets::Budget.Expression/Properties/Not/Type",
        "value": "object",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Budgets::Budget.Expression/Properties/Or/ItemType",
        "value": "object",
    },
]
