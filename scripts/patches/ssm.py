patches = [
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::SSM::PatchBaseline.Rule/Properties/ApproveUntilDate/PrimitiveType",
        "value": "String",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::SSM::Association.Target",
        "path": "/PropertyTypes/AWS::SSM::Association.Targets",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::SSM::Association/Properties/Targets/ItemType",
        "value": "Targets",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::SSM::MaintenanceWindowTarget/Properties/Targets/ItemType",
        "value": "Targets",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::SSM::MaintenanceWindowTask/Properties/Targets/ItemType",
        "value": "Targets",
    },
    # backward compatibility
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::SSM::MaintenanceWindowTask.Target",
    },
]
