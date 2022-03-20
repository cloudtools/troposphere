patches = [
    # Rename AWS::ImageBuilder::ContainerRecipe.ComponentConfiguration to AWS::ImageBuilder::ContainerRecipe.ContainerComponentConfiguration
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::ImageBuilder::ContainerRecipe.ComponentConfiguration",
        "path": "/PropertyTypes/AWS::ImageBuilder::ContainerRecipe.ContainerComponentConfiguration",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::ImageBuilder::ContainerRecipe/Properties/Components/ItemType",
        "value": "ContainerComponentConfiguration",
    },
]
