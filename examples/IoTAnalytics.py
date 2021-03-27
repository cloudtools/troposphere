from troposphere import Tags, Template
from troposphere.iotanalytics import (
    Action,
    Activity,
    ActivityChannel,
    ActivityDatastore,
    Channel,
    ChannelStorage,
    CustomerManagedS3,
    Dataset,
    DatasetContentDeliveryRule,
    DatasetContentDeliveryRuleDestination,
    Datastore,
    DatastoreStorage,
    Pipeline,
    RetentionPeriod,
    S3DestinationConfiguration,
    ServiceManagedS3,
    Trigger,
    TriggeringDataset,
    VersioningConfiguration,
)

t = Template()

channel = Channel(
    "TestChannel",
    ChannelName="testchannel",
    ChannelStorage=ChannelStorage(
        CustomerManagedS3=CustomerManagedS3(
            Bucket="customerbucket",
            KeyPrefix="bobdog",
            RoleArn="arn",
        )
    ),
    RetentionPeriod=RetentionPeriod(
        NumberOfDays=10,
    ),
    Tags=Tags(Manufacturer="AmazonWebServices"),
)

pipeline = Pipeline(
    "TestPipeline",
    PipelineActivities=[
        Activity(
            Channel=ActivityChannel(
                ChannelName="ChannelName",
                Name="testchannel",
                Next="DatastoreActivity",
            ),
        ),
        Activity(
            Datastore=ActivityDatastore(
                Name="DatastoreActivity",
                DatastoreName="testdatastore",
            ),
        ),
    ],
    PipelineName="testpipeline",
    Tags=Tags(Manufacturer="AmazonWebServices"),
)

datastore = Datastore(
    "TestDatastore",
    DatastoreName="testdatastore",
    DatastoreStorage=DatastoreStorage(
        ServiceManagedS3=ServiceManagedS3(),
    ),
    RetentionPeriod=RetentionPeriod(
        NumberOfDays=365,
    ),
    Tags=Tags(Manufacturer="AmazonWebServices"),
)

dataset = Dataset(
    "TestDataset",
    Actions=[
        Action(
            ActionName="actionname",
        ),
    ],
    ContentDeliveryRules=[
        DatasetContentDeliveryRule(
            Destination=DatasetContentDeliveryRuleDestination(
                S3DestinationConfiguration=S3DestinationConfiguration(
                    Bucket="testbucket",
                    Key="testkey",
                    RoleArn="arn",
                ),
            ),
            EntryName="entryname",
        )
    ],
    DatasetName="testdataset",
    RetentionPeriod=RetentionPeriod(
        Unlimited=True,
    ),
    Tags=Tags(Manufacturer="AmazonWebServices"),
    Triggers=[
        Trigger(
            TriggeringDataset=TriggeringDataset(DatasetName="testdataset"),
        ),
    ],
    VersioningConfiguration=VersioningConfiguration(
        Unlimited=True,
    ),
)

t.add_resource(channel)
t.add_resource(pipeline)
t.add_resource(datastore)
t.add_resource(dataset)

print(t.to_json())
