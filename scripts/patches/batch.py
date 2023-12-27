patches = [
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Batch::JobDefinition.JobTimeout",
        "path": "/PropertyTypes/AWS::Batch::JobDefinition.Timeout",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::Batch::JobDefinition/Properties/Timeout/Type",
        "value": "Timeout",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Batch::JobDefinition.EksMetadata",
        "path": "/PropertyTypes/AWS::Batch::JobDefinition.Metadata",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Batch::JobDefinition.EksPodProperties/Properties/Metadata/Type",
        "value": "Metadata",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Batch::JobDefinition.EksPodProperties",
        "path": "/PropertyTypes/AWS::Batch::JobDefinition.PodProperties",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Batch::JobDefinition.EksProperties/Properties/PodProperties/Type",
        "value": "PodProperties",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Batch::JobDefinition.EFSAuthorizationConfig",
        "path": "/PropertyTypes/AWS::Batch::JobDefinition.AuthorizationConfig",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Batch::JobDefinition.EFSVolumeConfiguration/Properties/AuthorizationConfig/Type",
        "value": "AuthorizationConfig",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Batch::JobDefinition.EFSVolumeConfiguration",
        "path": "/PropertyTypes/AWS::Batch::JobDefinition.EfsVolumeConfiguration",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Batch::JobDefinition.Volume/Properties/EfsVolumeConfiguration/Type",
        "value": "EfsVolumeConfiguration",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Batch::JobDefinition.Host",
        "path": "/PropertyTypes/AWS::Batch::JobDefinition.VolumesHost",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Batch::JobDefinition.Volume/Properties/Host/Type",
        "value": "VolumesHost",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Batch::JobDefinition.MountPoint",
        "path": "/PropertyTypes/AWS::Batch::JobDefinition.MountPoints",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Batch::JobDefinition.ContainerProperties/Properties/MountPoints/ItemType",
        "value": "MountPoints",
    },
    # backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::Batch::JobDefinition.Volume",
        "path": "/PropertyTypes/AWS::Batch::JobDefinition.Volumes",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::Batch::JobDefinition.ContainerProperties/Properties/Volumes/ItemType",
        "value": "Volumes",
    },
]
