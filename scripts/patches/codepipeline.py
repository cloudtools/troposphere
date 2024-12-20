patches = [
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CodePipeline::Pipeline.StageTransition",
        "path": "/PropertyTypes/AWS::CodePipeline::Pipeline.DisableInboundStageTransitions",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::CodePipeline::Pipeline/Properties/DisableInboundStageTransitions/ItemType",
        "value": "DisableInboundStageTransitions",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CodePipeline::Pipeline.StageDeclaration",
        "path": "/PropertyTypes/AWS::CodePipeline::Pipeline.Stages",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::CodePipeline::Pipeline/Properties/Stages/ItemType",
        "value": "Stages",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CodePipeline::Pipeline.InputArtifact",
        "path": "/PropertyTypes/AWS::CodePipeline::Pipeline.InputArtifacts",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CodePipeline::Pipeline.ActionDeclaration/Properties/InputArtifacts/ItemType",
        "value": "InputArtifacts",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CodePipeline::Pipeline.RuleDeclaration/Properties/InputArtifacts/ItemType",
        "value": "InputArtifacts",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CodePipeline::Pipeline.OutputArtifact",
        "path": "/PropertyTypes/AWS::CodePipeline::Pipeline.OutputArtifacts",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CodePipeline::Pipeline.ActionDeclaration/Properties/OutputArtifacts/ItemType",
        "value": "OutputArtifacts",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CodePipeline::Pipeline.ActionDeclaration",
        "path": "/PropertyTypes/AWS::CodePipeline::Pipeline.Actions",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CodePipeline::Pipeline.Stages/Properties/Actions/ItemType",
        "value": "Actions",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CodePipeline::Pipeline.BlockerDeclaration",
        "path": "/PropertyTypes/AWS::CodePipeline::Pipeline.Blockers",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CodePipeline::Pipeline.Stages/Properties/Blockers/ItemType",
        "value": "Blockers",
    },
    # Add missing OutputArtifact.Files
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::CodePipeline::Pipeline.OutputArtifacts/Properties/Files",
        "value": {
            "PrimitiveItemType": "String",
            "Required": False,
            "Type": "List",
        },
    },
]
