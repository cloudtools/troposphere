patches = [
    # backwards compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CodeCommit::Repository.RepositoryTrigger",
        "path": "/PropertyTypes/AWS::CodeCommit::Repository.Trigger",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::CodeCommit::Repository/Properties/Triggers/ItemType",
        "value": "Trigger",
    },
]
