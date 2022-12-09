patches = [
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::Route53::HealthCheck/Properties/HealthCheckTags/Type",
        "value": "Tags",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Route53::HealthCheck.HealthCheckTag",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::Route53::HostedZone/Properties/HostedZoneTags/Type",
        "value": "Tags",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Route53::HostedZone.HostedZoneTag",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Route53::HostedZone.HostedZoneConfig",
        "path": "/PropertyTypes/AWS::Route53::HostedZone.HostedZoneConfiguration",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::Route53::HostedZone/Properties/HostedZoneConfig/Type",
        "value": "HostedZoneConfiguration",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Route53::HostedZone.VPC",
        "path": "/PropertyTypes/AWS::Route53::HostedZone.HostedZoneVPCs",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::Route53::HostedZone/Properties/VPCs/ItemType",
        "value": "HostedZoneVPCs",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Route53::RecordSet.AliasTarget",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Route53::RecordSetGroup.AliasTarget",
    },
    {
        "op": "add",
        "path": "/ResourceTypes/AWS::Route53::RecordSet/Properties/AliasTarget/PrimitiveType",
        "value": "AliasTarget",
    },
    {
        "op": "add",
        "path": "/PropertyTypes/AWS::Route53::RecordSetGroup.RecordSet/Properties/AliasTarget/PrimitiveType",
        "value": "AliasTarget",
    },
    {
        "op": "move",
        "from": "/ResourceTypes/AWS::Route53::RecordSet",
        "path": "/ResourceTypes/AWS::Route53::RecordSetType::RecordSet",
    },
]
