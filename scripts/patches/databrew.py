patches = [
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::DataBrew::Recipe.Action/Properties/Parameters/Type",
        "value": "RecipeParameters",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::DataBrew::Job.StatisticOverride/Properties/Parameters/Type",
        "value": "Map",
    },
    # Rename AWS::DataBrew::Job.Recipe to AWS::DataBrew::Job.JobRecipe due to conflict with Recipe resource name
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::DataBrew::Job.Recipe",
        "path": "/PropertyTypes/AWS::DataBrew::Job.JobRecipe",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::DataBrew::Job/Properties/Recipe/Type",
        "value": "JobRecipe",
    },
    # Rename AWS::DataBrew::Job.S3Location to AWS::DataBrew::Job.JobS3Location
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::DataBrew::Job.S3Location",
        "path": "/PropertyTypes/AWS::DataBrew::Job.JobS3Location",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::DataBrew::Job.S3TableOutputOptions/Properties/Location/Type",
        "value": "JobS3Location",
    },
]
