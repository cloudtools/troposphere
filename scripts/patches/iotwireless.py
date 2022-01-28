patches = [
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::IoTWireless::FuotaTask.LoRaWAN",
        "path": "/PropertyTypes/AWS::IoTWireless::FuotaTask.FuotaTaskLoRaWAN",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::IoTWireless::FuotaTask/Properties/LoRaWAN/Type",
        "value": "FuotaTaskLoRaWAN",
    },
]
