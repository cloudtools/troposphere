patches = [
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::StepFunctions::StateMachine/Properties/Definition/PrimitiveType",
        "value": "Json",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::StepFunctions::Activity/Properties/Tags/ItemType",
        "value": "Tag",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::StepFunctions::Activity.TagsEntry",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::StepFunctions::StateMachine/Properties/Tags/ItemType",
        "value": "Tag",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::StepFunctions::StateMachine.TagsEntry",
    },
]
