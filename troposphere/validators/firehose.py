# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def processor_type_validator(x):
    """
    Property: Processor.Type
    """
    valid_types = [
        "Lambda",
        "MetadataExtraction",
        "RecordDeAggregation",
        "AppendDelimiterToRecord",
    ]
    if x not in valid_types:
        raise ValueError("Type must be one of: %s" % ", ".join(valid_types))
    return x


def delivery_stream_type_validator(x):
    """
    Property: DeliveryStream.DeliveryStreamType
    """
    valid_types = ["DirectPut", "KinesisStreamAsSource"]
    if x not in valid_types:
        raise ValueError(
            "DeliveryStreamType must be one of: %s" % ", ".join(valid_types)
        )
    return x


def index_rotation_period_validator(x):
    """
    Property: ElasticsearchDestinationConfiguration.IndexRotationPeriod
    """
    valid_types = ["NoRotation", "OneHour", "OneDay", "OneWeek", "OneMonth"]
    if x not in valid_types:
        raise ValueError(
            "IndexRotationPeriod must be one of: %s" % ", ".join(valid_types)
        )
    return x


def s3_backup_mode_elastic_search_validator(x):
    """
    Property: ElasticsearchDestinationConfiguration.S3BackupMode
    """
    valid_types = ["FailedDocumentsOnly", "AllDocuments"]
    if x not in valid_types:
        raise ValueError("S3BackupMode must be one of: %s" % ", ".join(valid_types))
    return x


def s3_backup_mode_extended_s3_validator(x):
    """
    Property: ExtendedS3DestinationConfiguration.S3BackupMode
    """
    valid_types = ["Disabled", "Enabled"]
    if x not in valid_types:
        raise ValueError("S3BackupMode must be one of: %s" % ", ".join(valid_types))
    return x
