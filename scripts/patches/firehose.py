patches = [
    # backward compatibility
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::KinesisFirehose::DeliveryStream.ElasticsearchRetryOptions",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::KinesisFirehose::DeliveryStream.ElasticsearchDestinationConfiguration/Properties/RetryOptions/Type",
        "value": "RetryOptions",
    },
    # backward compatibility
    {
        "op": "copy",
        "from": "/PropertyTypes/AWS::KinesisFirehose::DeliveryStream.S3DestinationConfiguration",
        "path": "/PropertyTypes/AWS::KinesisFirehose::DeliveryStream.S3Configuration",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::KinesisFirehose::DeliveryStream.ElasticsearchDestinationConfiguration/Properties/S3Configuration/Type",
        "value": "S3Configuration",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::KinesisFirehose::DeliveryStream.RedshiftDestinationConfiguration/Properties/S3Configuration/Type",
        "value": "S3Configuration",
    },
    # backward compatibility
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::KinesisFirehose::DeliveryStream.ElasticsearchBufferingHints",
    },
    # backward compatibility
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::KinesisFirehose::DeliveryStream.ElasticsearchDestinationConfiguration/Properties/BufferingHints/Type",
        "value": "BufferingHints",
    },
]
