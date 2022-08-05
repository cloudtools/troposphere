patches = [
    # duplicate GlobalSecondaryIndex
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::DynamoDB::GlobalTable.GlobalSecondaryIndex",
        "path": "/PropertyTypes/AWS::DynamoDB::GlobalTable.GlobalTableGlobalSecondaryIndex",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::DynamoDB::GlobalTable/Properties/GlobalSecondaryIndexes/ItemType",
        "value": "GlobalTableGlobalSecondaryIndex",
    },
    # duplicate SSESpecification
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::DynamoDB::GlobalTable.SSESpecification",
        "path": "/PropertyTypes/AWS::DynamoDB::GlobalTable.GlobalTableSSESpecification",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::DynamoDB::GlobalTable/Properties/SSESpecification/Type",
        "value": "GlobalTableSSESpecification",
    },
    # Fix issue in spec 82.0.0 that changed Type to Json
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::DynamoDB::Table/Properties/KeySchema/Type",
        "value": "List",
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::DynamoDB::Table/Properties/KeySchema/ItemType",
        "value": "KeySchema",
    },
]
