patches = [
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::EFS::AccessPoint/Properties/AccessPointTags/ItemType",
        "value": "Tag",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::EFS::FileSystem/Properties/FileSystemTags/ItemType",
        "value": "Tag",
    },
]
