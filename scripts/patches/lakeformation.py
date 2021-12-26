patches = [
    # Rename AWS::LakeFormation::Permissions.Resource to AWS::LakeFormation::Permissions.ResourceProperty
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::LakeFormation::Permissions.Resource",
        "path": "/PropertyTypes/AWS::LakeFormation::Permissions.ResourceProperty",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::LakeFormation::Permissions/Properties/Resource/Type",
        "value": "ResourceProperty",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::LakeFormation::DataLakeSettings/Properties/Admins/Type",
        "value": "List",
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::LakeFormation::DataLakeSettings/Properties/Admins/ItemType",
        "value": "DataLakePrincipal",
    },
]
