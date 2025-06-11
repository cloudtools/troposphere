patches = [
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Bedrock::Flow.PromptTemplateConfiguration",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Bedrock::FlowVersion.PromptTemplateConfiguration",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Bedrock::PromptVersion.PromptTemplateConfiguration",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Bedrock::FlowVersion.LoopFlowNodeConfiguration",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Bedrock::FlowVersion.TextPromptTemplateConfiguration",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Bedrock::FlowVersion.FlowNodeInput",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Bedrock::Flow.TextPromptTemplateConfiguration",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Bedrock::PromptVersion.TextPromptTemplateConfiguration",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Bedrock::Flow.LoopFlowNodeConfiguration/Properties/Definition/Type",
        "value": "object",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Bedrock::DataSource.S3Location",
        "path": "/PropertyTypes/AWS::Bedrock::DataSource.DataSourceS3Location",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Bedrock::DataSource.IntermediateStorage/Properties/S3Location/Type",
        "value": "DataSourceS3Location",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Bedrock::KnowledgeBase.S3Location",
        "path": "/PropertyTypes/AWS::Bedrock::KnowledgeBase.KnowledgeBaseS3Location",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Bedrock::KnowledgeBase.SupplementalDataStorageLocation/Properties/S3Location/Type",
        "value": "KnowledgeBaseS3Location",
    },
]
