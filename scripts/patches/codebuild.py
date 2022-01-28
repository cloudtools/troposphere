patches = [
    # Fixup to account for FilterGroup
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::CodeBuild::Project.ProjectTriggers/Properties/FilterGroups/PrimitiveType",
        "value": "list",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CodeBuild::Project.CloudWatchLogsConfig",
        "path": "/PropertyTypes/AWS::CodeBuild::Project.CloudWatchLogs",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CodeBuild::Project.LogsConfig/Properties/CloudWatchLogs/Type",
        "value": "CloudWatchLogs",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CodeBuild::Project.S3LogsConfig",
        "path": "/PropertyTypes/AWS::CodeBuild::Project.S3Logs",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CodeBuild::Project.LogsConfig/Properties/S3Logs/Type",
        "value": "S3Logs",
    },
]
