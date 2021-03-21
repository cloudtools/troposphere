#!/usr/bin/python

from troposphere import Template, Ref, Output, Parameter
from troposphere.dynamodb import (
    KeySchema,
    AttributeDefinition,
    ProvisionedThroughput,
    Projection,
    Table,
    GlobalSecondaryIndex
)

template = Template()

template.set_description("Create a dynamodb table with a global secondary "
                         "index")
# N.B. If you remove the provisioning section this works for
# LocalSecondaryIndexes aswell.

readunits = template.add_parameter(Parameter(
    "ReadCapacityUnits",
    Description="Provisioned read throughput",
    Type="Number",
    Default="10",
    MinValue="5",
    MaxValue="10000",
    ConstraintDescription="should be between 5 and 10000"
))

writeunits = template.add_parameter(Parameter(
    "WriteCapacityUnits",
    Description="Provisioned write throughput",
    Type="Number",
    Default="5",
    MinValue="5",
    MaxValue="10000",
    ConstraintDescription="should be between 5 and 10000"
))

tableIndexName = template.add_parameter(Parameter(
    "TableIndexName",
    Description="Table: Primary Key Field",
    Type="String",
    Default="id",
    AllowedPattern="[a-zA-Z0-9]*",
    MinLength="1",
    MaxLength="2048",
    ConstraintDescription="must contain only alphanumberic characters"
))

tableIndexDataType = template.add_parameter(Parameter(
    "TableIndexDataType",
    Description=" Table: Primary Key Data Type",
    Type="String",
    Default="S",
    AllowedPattern="[S|N|B]",
    MinLength="1",
    MaxLength="1",
    ConstraintDescription="S for string data, N for numeric data, or B for "
                          "binary data"
))

secondaryIndexHashName = template.add_parameter(Parameter(
    "SecondaryIndexHashName",
    Description="Secondary Index: Primary Key Field",
    Type="String",
    Default="tokenType",
    AllowedPattern="[a-zA-Z0-9]*",
    MinLength="1",
    MaxLength="2048",
    ConstraintDescription="must contain only alphanumberic characters"
))

secondaryIndexHashDataType = template.add_parameter(Parameter(
    "SecondaryIndexHashDataType",
    Description="Secondary Index: Primary Key Data Type",
    Type="String",
    Default="S",
    AllowedPattern="[S|N|B]",
    MinLength="1",
    MaxLength="1",
    ConstraintDescription="S for string data, N for numeric data, or B for "
                          "binary data"
))

secondaryIndexRangeName = template.add_parameter(Parameter(
    "refreshSecondaryIndexRangeName",
    Description="Secondary Index: Range Key Field",
    Type="String",
    Default="tokenUpdatedTime",
    AllowedPattern="[a-zA-Z0-9]*",
    MinLength="1",
    MaxLength="2048",
    ConstraintDescription="must contain only alphanumberic characters"
))

secondaryIndexRangeDataType = template.add_parameter(Parameter(
    "SecondaryIndexRangeDataType",
    Description="Secondary Index: Range Key Data Type",
    Type="String",
    Default="S",
    AllowedPattern="[S|N|B]",
    MinLength="1",
    MaxLength="1",
    ConstraintDescription="S for string data, N for numeric data, or B for "
                          "binary data"
))


GSITable = template.add_resource(Table(
    "GSITable",
    AttributeDefinitions=[
        AttributeDefinition(
            AttributeName=Ref(tableIndexName),
            AttributeType=Ref(tableIndexDataType)
        ),
        AttributeDefinition(
            AttributeName=Ref(secondaryIndexHashName),
            AttributeType=Ref(secondaryIndexHashDataType)
        ),
        AttributeDefinition(
            AttributeName=Ref(secondaryIndexRangeName),
            AttributeType=Ref(secondaryIndexRangeDataType)
        )
    ],
    KeySchema=[
        KeySchema(
            AttributeName=Ref(tableIndexName),
            KeyType="HASH"
        )
    ],
    ProvisionedThroughput=ProvisionedThroughput(
        ReadCapacityUnits=Ref(readunits),
        WriteCapacityUnits=Ref(writeunits)
    ),
    GlobalSecondaryIndexes=[
        GlobalSecondaryIndex(
            IndexName="SecondaryIndex",
            KeySchema=[
                KeySchema(
                    AttributeName=Ref(secondaryIndexHashName),
                    KeyType="HASH"
                ),
                KeySchema(
                    AttributeName=Ref(secondaryIndexRangeName),
                    KeyType="RANGE"
                )
            ],
            Projection=Projection(ProjectionType="ALL"),
            ProvisionedThroughput=ProvisionedThroughput(
                ReadCapacityUnits=Ref(readunits),
                WriteCapacityUnits=Ref(writeunits)
            )
        )
    ]
))

template.add_output(Output(
    "GSITable",
    Value=Ref(GSITable),
    Description="Table with a Global Secondary Index",
))


print(template.to_json())
