patches = [
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Glue::SecurityConfiguration.EncryptionConfiguration/Properties/S3Encryptions/Type",
        "value": "List",
    },
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::Glue::SecurityConfiguration.EncryptionConfiguration/Properties/S3Encryptions/ItemType",
        "value": "S3Encryption",
    },
]
