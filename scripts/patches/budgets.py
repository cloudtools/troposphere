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
]
