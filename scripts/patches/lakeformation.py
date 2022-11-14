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
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::LakeFormation::PrincipalPermissions.Resource/Properties/Catalog/PrimitiveType",
        "value": "Json",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::LakeFormation::PrincipalPermissions.Resource/Properties/Catalog/Type",
    },
    # Rename AWS::LakeFormation::PrincipalPermissions.Resource to AWS::LakeFormation::PrincipalPermissions.PrincipalResource
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::LakeFormation::PrincipalPermissions.Resource",
        "path": "/PropertyTypes/AWS::LakeFormation::PrincipalPermissions.PrincipalResource",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::LakeFormation::PrincipalPermissions/Properties/Resource/Type",
        "value": "PrincipalResource",
    },
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::LakeFormation::TagAssociation.Resource/Properties/Catalog/PrimitiveType",
        "value": "Json",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::LakeFormation::TagAssociation.Resource/Properties/Catalog/Type",
    },
    # Rename AWS::LakeFormation::TagAssociation.Resource to AWS::LakeFormation::TagAssociation.TagAssociationResource
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::LakeFormation::TagAssociation.Resource",
        "path": "/PropertyTypes/AWS::LakeFormation::TagAssociation.TagAssociationResource",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::LakeFormation::TagAssociation/Properties/Resource/Type",
        "value": "TagAssociationResource",
    },
    # Rename AWS::LakeFormation::TagAssociation.TableWithColumns to AWS::LakeFormation::TagAssociation.TagAssociationTableWithColumns
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::LakeFormation::TagAssociation.TableWithColumnsResource",
        "path": "/PropertyTypes/AWS::LakeFormation::TagAssociation.TagAssociationTableWithColumnsResource",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::LakeFormation::TagAssociation.TagAssociationResource/Properties/TableWithColumns/Type",
        "value": "TagAssociationTableWithColumnsResource",
    },
    # Rename AWS::LakeFormation::Permissions.DataLocationResource to AWS::LakeFormation::Permissions.PermissionsDataLocationResource
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::LakeFormation::Permissions.DataLocationResource",
        "path": "/PropertyTypes/AWS::LakeFormation::Permissions.PermissionsDataLocationResource",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::LakeFormation::Permissions.ResourceProperty/Properties/DataLocationResource/Type",
        "value": "PermissionsDataLocationResource",
    },
]
