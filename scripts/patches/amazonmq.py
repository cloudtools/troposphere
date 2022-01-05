patches = [
    # Rename AWS::AmazonMQ::Broker.LogList to AWS::AmazonMQ::Broker.LogsConfiguration - backward compatibility
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::AmazonMQ::Broker.LogList",
        "path": "/PropertyTypes/AWS::AmazonMQ::Broker.LogsConfiguration",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::AmazonMQ::Broker/Properties/Logs/Type",
        "value": "LogsConfiguration",
    },
]
