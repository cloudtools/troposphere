patches = [
    # backward compatibility - these fake out the template generator for the
    # examples. Need to find a better long term fix.
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::RDS::DBInstance/Properties/DBSecurityGroups/PrimitiveType",
        "value": "list",
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::RDS::DBSubnetGroup/Properties/SubnetIds/PrimitiveType",
        "value": "list",
    },
    # Spec 193.0.0 removed these properties, so add them back in
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::RDS::DBInstance/Properties/CertificateDetails",
        "value": {
            "Type": "CertificateDetails",
            "Required": False,
        },
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::RDS::DBInstance/Properties/Endpoint",
        "value": {
            "Type": "Endpoint",
            "Required": False,
        },
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::RDS::GlobalCluster/Properties/GlobalEndpoint",
        "value": {
            "Type": "GlobalEndpoint",
            "Required": False,
        },
    },
]
