#!/usr/bin/python
#
# Note: This implementation is being phased out, you should instead look at
#       the DynamoDB2_* examples for the new implementation.
#

from troposphere import Template, Ref, Output, Parameter
from troposphere.dynamodb import (Key, AttributeDefinition,
                                  ProvisionedThroughput, Projection)
from troposphere.dynamodb import Table, GlobalSecondaryIndex

template = Template()

template.add_description("Create a dynamodb table with a global secondary "
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
        AttributeDefinition(Ref(tableIndexName), Ref(tableIndexDataType)),
        AttributeDefinition(Ref(secondaryIndexHashName),
                            Ref(secondaryIndexHashDataType)),
        AttributeDefinition(Ref(secondaryIndexRangeName),
                            Ref(secondaryIndexRangeDataType))
    ],
    KeySchema=[
        Key(Ref(tableIndexName), "HASH")
    ],
    ProvisionedThroughput=ProvisionedThroughput(
        Ref(readunits),
        Ref(writeunits)
    ),
    GlobalSecondaryIndexes=[
        GlobalSecondaryIndex(
            "SecondaryIndex",
            [
                Key(Ref(secondaryIndexHashName), "HASH"),
                Key(Ref(secondaryIndexRangeName), "RANGE")
            ],
            Projection("ALL"),
            ProvisionedThroughput(
                Ref(readunits),
                Ref(writeunits)
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
