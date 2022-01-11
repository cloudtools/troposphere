patches = [
    # Rename AWS::Lightsail::Instance.Disk to AWS::Lightsail::Instance.DiskProperty
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Lightsail::Instance.Disk",
        "path": "/PropertyTypes/AWS::Lightsail::Instance.DiskProperty",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Lightsail::Instance.Hardware/Properties/Disks/ItemType",
        "value": "DiskProperty",
    },
    # Remove Location and State attribute properties
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Lightsail::Instance.Location",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Lightsail::Instance.State",
    },
]
