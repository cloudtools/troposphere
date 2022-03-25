patches = [
    # Rename AWS::FSx::Volume.OntapConfiguration to AWS::FSx::Volume.VolumeOntapConfiguration - duplicate property name
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::FSx::Volume.OntapConfiguration",
        "path": "/PropertyTypes/AWS::FSx::Volume.VolumeOntapConfiguration",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::FSx::Volume/Properties/OntapConfiguration/Type",
        "value": "VolumeOntapConfiguration",
    },
    # Rename AWS::FSx::Volume.OpenZFSConfiguration to AWS::FSx::Volume.VolumeOpenZFSConfiguration - duplicate property name
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::FSx::Volume.OpenZFSConfiguration",
        "path": "/PropertyTypes/AWS::FSx::Volume.VolumeOpenZFSConfiguration",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::FSx::Volume/Properties/OpenZFSConfiguration/Type",
        "value": "VolumeOpenZFSConfiguration",
    },
]
