patches = [
    {
        "op": "move",
        "from": "/ResourceTypes/AWS::Transfer::Server/Properties/Protocols/ItemType",
        "path": "/ResourceTypes/AWS::Transfer::Server/Properties/Protocols/PrimitiveItemType",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::Transfer::Server/Properties/Protocols/PrimitiveItemType",
        "value": "String",
    },
    {
        "op": "move",
        "from": "/ResourceTypes/AWS::Transfer::User/Properties/SshPublicKeys/ItemType",
        "path": "/ResourceTypes/AWS::Transfer::User/Properties/SshPublicKeys/PrimitiveItemType",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::Transfer::User/Properties/SshPublicKeys/PrimitiveItemType",
        "value": "String",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Transfer::Server.ProtocolDetails/Properties/As2Transports/ItemType",
        "path": "/PropertyTypes/AWS::Transfer::Server.ProtocolDetails/Properties/As2Transports/PrimitiveItemType",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Transfer::Server.ProtocolDetails/Properties/As2Transports/PrimitiveItemType",
        "value": "String",
    },
]
