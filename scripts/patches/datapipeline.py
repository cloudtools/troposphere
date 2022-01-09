patches = [
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::DataPipeline::Pipeline.ParameterAttribute",
        "path": "/PropertyTypes/AWS::DataPipeline::Pipeline.ParameterObjectAttribute",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::DataPipeline::Pipeline.ParameterObject/Properties/Attributes/ItemType",
        "value": "ParameterObjectAttribute",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::DataPipeline::Pipeline.Field",
        "path": "/PropertyTypes/AWS::DataPipeline::Pipeline.ObjectField",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::DataPipeline::Pipeline.PipelineObject/Properties/Fields/ItemType",
        "value": "ObjectField",
    },
]
