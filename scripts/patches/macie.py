patches = [
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Macie::FindingsFilter.FindingCriteria/Properties/Criterion/Type",
        "value": "Map",
    },
    # Remove FindingsFilterListItem attribute property
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Macie::FindingsFilter.FindingsFilterListItem",
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::Macie::AllowList/Properties/Criteria/PrimitiveType",
        "value": "Json",
    },
]
