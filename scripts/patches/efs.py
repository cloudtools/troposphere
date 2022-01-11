patches = [
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::EFS::AccessPoint/Properties/AccessPointTags/ItemType",
        "value": "Tag",
    },
    # Remove unused AccessPointTag (remapped to troposphere Tags)
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::EFS::AccessPoint.AccessPointTag",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::EFS::FileSystem/Properties/FileSystemTags/ItemType",
        "value": "Tag",
    },
    # Remove unused ElasticFileSystemTag (remapped to troposphere Tags)
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::EFS::FileSystem.ElasticFileSystemTag",
    },
]
