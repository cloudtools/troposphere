patches = [
    # Remove AWS::AuditManager::Assessment.Delegation as it emits a double but only used in the Attributes section
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::AuditManager::Assessment.Delegation",
    },
]
