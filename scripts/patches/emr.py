patches = [
    # backward compatibility - use KeyValue and MetricDimension from
    # the validation file rather than from the spec file.
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::EMR::Cluster.KeyValue",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::EMR::Cluster.MetricDimension",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::EMR::Step.KeyValue",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::EMR::InstanceGroupConfig.MetricDimension",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::EMR::Cluster.HadoopJarStepConfig/Properties/StepProperties/ItemType",
        "path": "/PropertyTypes/AWS::EMR::Cluster.HadoopJarStepConfig/Properties/StepProperties/PrimitiveItemType",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::EMR::Step.HadoopJarStepConfig/Properties/StepProperties/ItemType",
        "path": "/PropertyTypes/AWS::EMR::Step.HadoopJarStepConfig/Properties/StepProperties/PrimitiveItemType",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::EMR::Cluster.CloudWatchAlarmDefinition/Properties/Dimensions/ItemType",
        "path": "/PropertyTypes/AWS::EMR::Cluster.CloudWatchAlarmDefinition/Properties/Dimensions/PrimitiveItemType",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::EMR::InstanceGroupConfig.CloudWatchAlarmDefinition/Properties/Dimensions/ItemType",
        "path": "/PropertyTypes/AWS::EMR::InstanceGroupConfig.CloudWatchAlarmDefinition/Properties/Dimensions/PrimitiveItemType",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::EMR::Cluster.EbsBlockDeviceConfig",
        "path": "/PropertyTypes/AWS::EMR::Cluster.EbsBlockDeviceConfigs",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::EMR::Cluster.EbsConfiguration/Properties/EbsBlockDeviceConfigs/ItemType",
        "value": "EbsBlockDeviceConfigs",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::EMR::InstanceFleetConfig.EbsBlockDeviceConfig",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::EMR::InstanceFleetConfig.EbsConfiguration/Properties/EbsBlockDeviceConfigs/ItemType",
        "value": "EbsBlockDeviceConfigs",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::EMR::InstanceGroupConfig.EbsBlockDeviceConfig",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::EMR::InstanceGroupConfig.EbsConfiguration/Properties/EbsBlockDeviceConfigs/ItemType",
        "value": "EbsBlockDeviceConfigs",
    },
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::EMR::Cluster.JobFlowInstancesConfig/Properties/TaskInstanceFleets",
        "value": {
            "ItemType": "InstanceFleetConfigProperty",
            "Required": False,
            "Type": "List",
        },
    },
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::EMR::Cluster.JobFlowInstancesConfig/Properties/TaskInstanceGroup",
        "value": {
            "ItemType": "InstanceGroupConfigProperty",
            "Required": False,
            "Type": "List",
        },
    },
]
