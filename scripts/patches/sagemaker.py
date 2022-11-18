patches = [
    # Rename AWS::SageMaker::Device.Device to AWS::SageMaker::Device.DeviceProperty
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::SageMaker::Device.Device",
        "path": "/PropertyTypes/AWS::SageMaker::Device.DeviceProperty",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::SageMaker::Device/Properties/Device/Type",
        "value": "DeviceProperty",
    },
    # Rename AWS::SageMaker::ModelBiasJobDefinition.EndpointInput to AWS::SageMaker::ModelBiasJobDefinition.ModelBiasEndpointInput
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::SageMaker::ModelBiasJobDefinition.EndpointInput",
        "path": "/PropertyTypes/AWS::SageMaker::ModelBiasJobDefinition.ModelBiasEndpointInput",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobInput/Properties/EndpointInput/Type",
        "value": "ModelBiasEndpointInput",
    },
    # Rename AWS::SageMaker::ModelExplainabilityJobDefinition.EndpointInput to AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityEndpointInput
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::SageMaker::ModelExplainabilityJobDefinition.EndpointInput",
        "path": "/PropertyTypes/AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityEndpointInput",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobInput/Properties/EndpointInput/Type",
        "value": "ModelExplainabilityEndpointInput",
    },
    # Rename AWS::SageMaker::ModelQualityJobDefinition.EndpointInput to AWS::SageMaker::ModelQualityJobDefinition.ModelQualityEndpointInput
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::SageMaker::ModelQualityJobDefinition.EndpointInput",
        "path": "/PropertyTypes/AWS::SageMaker::ModelQualityJobDefinition.ModelQualityEndpointInput",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobInput/Properties/EndpointInput/Type",
        "value": "ModelQualityEndpointInput",
    },
    # CreatedBy, LastModifiedBy, and Tag are documented as "Not currently supported by AWS CloudFormation."
    {
        "op": "remove",
        "path": "/ResourceTypes/AWS::SageMaker::ModelPackage/Properties/CreatedBy",
    },
    {
        "op": "remove",
        "path": "/ResourceTypes/AWS::SageMaker::ModelPackage/Properties/LastModifiedBy",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::SageMaker::ModelPackage.ModelPackageContainerDefinition/Properties/Environment/Type",
    },
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::SageMaker::ModelPackage.ModelPackageContainerDefinition/Properties/Environment/PrimitiveType",
        "value": "Json",
    },
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::SageMaker::ModelPackage.TransformJobDefinition/Properties/Environment/PrimitiveType",
        "value": "Json",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::SageMaker::EndpointConfig.ClarifyFeatureType",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::SageMaker::EndpointConfig.ClarifyInferenceConfig/Properties/FeatureTypes/ItemType",
    },
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::SageMaker::EndpointConfig.ClarifyInferenceConfig/Properties/FeatureTypes/PrimitiveItemType",
        "value": "String",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::SageMaker::EndpointConfig.ClarifyHeader",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::SageMaker::EndpointConfig.ClarifyInferenceConfig/Properties/LabelHeaders/ItemType",
    },
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::SageMaker::EndpointConfig.ClarifyInferenceConfig/Properties/LabelHeaders/PrimitiveItemType",
        "value": "String",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::SageMaker::EndpointConfig.ClarifyInferenceConfig/Properties/FeatureHeaders/ItemType",
    },
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::SageMaker::EndpointConfig.ClarifyInferenceConfig/Properties/FeatureHeaders/PrimitiveItemType",
        "value": "String",
    },
]
