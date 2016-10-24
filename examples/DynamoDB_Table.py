# Converted from DynamoDB_Table.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/
#
# Note: This implementation is being phased out, you should instead look at
#       the DynamoDB2_* examples for the new implementation.
#

from troposphere import Output, Parameter, Ref, Template
from troposphere.dynamodb import (Key, AttributeDefinition,
                                  ProvisionedThroughput)
from troposphere.dynamodb import Table

t = Template()

t.add_description("AWS CloudFormation Sample Template: This template "
                  "demonstrates the creation of a DynamoDB table.")

hashkeyname = t.add_parameter(Parameter(
    "HaskKeyElementName",
    Description="HashType PrimaryKey Name",
    Type="String",
    AllowedPattern="[a-zA-Z0-9]*",
    MinLength="1",
    MaxLength="2048",
    ConstraintDescription="must contain only alphanumberic characters"
))

hashkeytype = t.add_parameter(Parameter(
    "HaskKeyElementType",
    Description="HashType PrimaryKey Type",
    Type="String",
    Default="S",
    AllowedPattern="[S|N]",
    MinLength="1",
    MaxLength="1",
    ConstraintDescription="must be either S or N"
))

readunits = t.add_parameter(Parameter(
    "ReadCapacityUnits",
    Description="Provisioned read throughput",
    Type="Number",
    Default="5",
    MinValue="5",
    MaxValue="10000",
    ConstraintDescription="should be between 5 and 10000"
))

writeunits = t.add_parameter(Parameter(
    "WriteCapacityUnits",
    Description="Provisioned write throughput",
    Type="Number",
    Default="10",
    MinValue="5",
    MaxValue="10000",
    ConstraintDescription="should be between 5 and 10000"
))

myDynamoDB = t.add_resource(Table(
    "myDynamoDBTable",
    AttributeDefinitions=[
        AttributeDefinition(Ref(hashkeyname), Ref(hashkeytype)),
    ],
    KeySchema=[
        Key(Ref(hashkeyname), "HASH")
    ],
    ProvisionedThroughput=ProvisionedThroughput(
        Ref(readunits),
        Ref(writeunits)
    )
))

t.add_output(Output(
    "TableName",
    Value=Ref(myDynamoDB),
    Description="Table name of the newly create DynamoDB table",
))

print(t.to_json())
