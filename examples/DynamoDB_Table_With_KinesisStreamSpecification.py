# Converted from DynamoDB_Table.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import Output, Parameter, Ref, Template
from troposphere.dynamodb import (
    AttributeDefinition,
    KeySchema,
    KinesisStreamSpecification,
    ProvisionedThroughput,
    Table,
)

t = Template()

t.set_description("Create a DynamoDB Table with a Kinesis Stream Specification.")

hashkeyname = t.add_parameter(
    Parameter(
        "HashKeyElementName",
        Description="HashType PrimaryKey Name",
        Type="String",
        AllowedPattern="[a-zA-Z0-9]*",
        MinLength="1",
        MaxLength="2048",
        ConstraintDescription="must contain only alphanumberic characters",
    )
)

hashkeytype = t.add_parameter(
    Parameter(
        "HashKeyElementType",
        Description="HashType PrimaryKey Type",
        Type="String",
        Default="S",
        AllowedPattern="[S|N]",
        MinLength="1",
        MaxLength="1",
        ConstraintDescription="must be either S or N",
    )
)

readunits = t.add_parameter(
    Parameter(
        "ReadCapacityUnits",
        Description="Provisioned read throughput",
        Type="Number",
        Default="10",
        MinValue="5",
        MaxValue="10000",
        ConstraintDescription="should be between 5 and 10000",
    )
)

writeunits = t.add_parameter(
    Parameter(
        "WriteCapacityUnits",
        Description="Provisioned write throughput",
        Type="Number",
        Default="5",
        MinValue="5",
        MaxValue="10000",
        ConstraintDescription="should be between 5 and 10000",
    )
)

streamarn = t.add_parameter(
    Parameter(
        "StreamArn",
        AllowedPattern="arn:aws[-a-z]*:\\S+:\\S+:\\d+:.*",
        Description="Kinesis StreamArn",
        Type="String",
        MinLength="37",
        MaxLength="1024",
        ConstraintDescription="must be a valid arn",
    )
)

DynamoDBTableWithKinesis = t.add_resource(
    Table(
        "DynamoDBTableWithKinesis",
        AttributeDefinitions=[
            AttributeDefinition(
                AttributeName=Ref(hashkeyname), AttributeType=Ref(hashkeytype)
            ),
        ],
        KeySchema=[KeySchema(AttributeName=Ref(hashkeyname), KeyType="HASH")],
        KinesisStreamSpecification=KinesisStreamSpecification(StreamArn=Ref(streamarn)),
        ProvisionedThroughput=ProvisionedThroughput(
            ReadCapacityUnits=Ref(readunits), WriteCapacityUnits=Ref(writeunits)
        ),
    )
)

t.add_output(
    Output(
        "TableName",
        Value=Ref(DynamoDBTableWithKinesis),
        Description="Table with Kinesis Stream Specification",
    )
)

print(t.to_json())
