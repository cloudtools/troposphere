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
]
