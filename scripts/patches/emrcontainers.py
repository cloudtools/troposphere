patches = [
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::EMRContainers::Endpoint.EMREKSConfiguration/Properties/Configurations/ItemType",
        "value": "object",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::EMRContainers::JobRun.Configuration/Properties/Configurations/ItemType",
        "value": "object",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::EMRContainers::JobRun.ConfigurationOverrides",
        "path": "/PropertyTypes/AWS::EMRContainers::JobRun.JobRunConfigurationOverrides",
    },
    {
        "op": "move",
        "from": "/ResourceTypes/AWS::EMRContainers::JobRun/Properties/ConfigurationOverrides",
        "path": "/ResourceTypes/AWS::EMRContainers::JobRun/Properties/JobRunConfigurationOverrides",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::EMRContainers::JobRun/Properties/JobRunConfigurationOverrides/Type",
        "value": "JobRunConfigurationOverrides",
    },
]
