from troposphere import Template
from troposphere.firehose import (
    BufferingHints,
    CloudWatchLoggingOptions,
    CopyCommand,
    DeliveryStream,
    EncryptionConfiguration,
    KMSEncryptionConfig,
    RedshiftDestinationConfiguration,
    S3Configuration,
)

t = Template()
t.add_version('2010-09-09')
t.set_description('Sample Kinesis Firehose Delivery Stream')

t.add_resource(DeliveryStream(
    'MyDeliveryStream',
    DeliveryStreamName='MyDeliveryStream',
    RedshiftDestinationConfiguration=RedshiftDestinationConfiguration(
        CloudWatchLoggingOptions=CloudWatchLoggingOptions(
            Enabled=True,
            LogGroupName='my-log-group',
            LogStreamName='my-log-stream',
        ),
        ClusterJDBCURL='jdbc:redshift://my-redshift-db.asdf.us-west-2.redshift.amazonaws.com:5432/mydb',  # noqa
        CopyCommand=CopyCommand(
            CopyOptions="JSON 'auto'",
            DataTableColumns='mycol',
            DataTableName='mytable',
        ),
        Password='hooli-suxx',
        RoleARN='arn:aws:iam::12345:role/my-role',
        S3Configuration=S3Configuration(
            BucketARN='arn:aws:s3:::muh-bucket',
            BufferingHints=BufferingHints(
                IntervalInSeconds=5,
                SizeInMBs=60,
            ),
            CloudWatchLoggingOptions=CloudWatchLoggingOptions(
                Enabled=True,
                LogGroupName='my-other-log-group',
                LogStreamName='my-other-log-stream',
            ),
            CompressionFormat='UNCOMPRESSED',
            EncryptionConfiguration=EncryptionConfiguration(
                KMSEncryptionConfig=KMSEncryptionConfig(
                    AWSKMSKeyARN='aws-kms-key-arn'
                ),
                NoEncryptionConfig='NoEncryption',
            ),
            Prefix='my-prefix',
            RoleARN='arn:aws:iam::12345:role/my-role',
        ),
        Username='erlich_bachman',
    )
))

print(t.to_json())
