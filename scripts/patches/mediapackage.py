patches = [
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.HlsEncryption",
        "path": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.OriginEndpointHlsEncryption",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.HlsPackage/Properties/Encryption/Type",
        "value": "OriginEndpointHlsEncryption",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.HlsPackage",
        "path": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.OriginEndpointHlsPackage",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::MediaPackage::OriginEndpoint/Properties/HlsPackage/Type",
        "value": "OriginEndpointHlsPackage",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.MssPackage",
        "path": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.OriginEndpointMssPackage",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::MediaPackage::OriginEndpoint/Properties/MssPackage/Type",
        "value": "OriginEndpointMssPackage",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.SpekeKeyProvider",
        "path": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.OriginEndpointSpekeKeyProvider",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.CmafEncryption/Properties/SpekeKeyProvider/Type",
        "value": "OriginEndpointSpekeKeyProvider",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.DashEncryption",
        "path": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.OriginEndpointDashEncryption",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.DashPackage/Properties/Encryption/Type",
        "value": "OriginEndpointDashEncryption",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.CmafEncryption",
        "path": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.OriginEndpointCmafEncryption",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.CmafPackage/Properties/Encryption/Type",
        "value": "OriginEndpointCmafEncryption",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.HlsManifest",
        "path": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.OriginEndpointHlsManifest",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.CmafPackage/Properties/HlsManifests/ItemType",
        "value": "OriginEndpointHlsManifest",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.CmafPackage",
        "path": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.OriginEndpointCmafPackage",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::MediaPackage::OriginEndpoint/Properties/CmafPackage/Type",
        "value": "OriginEndpointCmafPackage",
    },
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.DashPackage",
        "path": "/PropertyTypes/AWS::MediaPackage::OriginEndpoint.OriginEndpointDashPackage",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::MediaPackage::OriginEndpoint/Properties/DashPackage/Type",
        "value": "OriginEndpointDashPackage",
    },
]
