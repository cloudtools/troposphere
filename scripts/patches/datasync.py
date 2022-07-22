patches = [
    # Rename AWS::DataSync::LocationFSxONTAP.Protocol to AWS::DataSync::LocationFSxONTAP.ONTAPProtocol
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::DataSync::LocationFSxONTAP.Protocol",
        "path": "/PropertyTypes/AWS::DataSync::LocationFSxONTAP.ONTAPProtocol",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::DataSync::LocationFSxONTAP/Properties/Protocol/Type",
        "value": "ONTAPProtocol",
    },
]
