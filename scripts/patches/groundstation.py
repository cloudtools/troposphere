patches = [
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::GroundStation::Config.FrequencyBandwidth",
        "path": "/PropertyTypes/AWS::GroundStation::Config.Bandwidth",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::GroundStation::Config.SpectrumConfig/Properties/Bandwidth/Type",
        "value": "Bandwidth",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::GroundStation::Config.AntennaUplinkConfig/Properties/SpectrumConfig/Type",
        "value": "SpectrumConfig",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::GroundStation::Config.UplinkSpectrumConfig",
    },
]
