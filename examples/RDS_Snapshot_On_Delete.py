# Converted from RDS_Snapshot_On_Delete.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import GetAtt, Join, Output
from troposphere import Template
from troposphere.rds import DBInstance


t = Template()

t.add_version("2010-09-09")

t.set_description(
    "AWS CloudFormation Sample Template RDS_Snapshot_On_Delete: Sample "
    "template showing how to create an RDS DBInstance that is snapshotted on "
    "stack deletion. **WARNING** This template creates an Amazon RDS database "
    "instance. When the stack is deleted a database snpshot will be left in "
    "your account. You will be billed for the AWS resources used if you "
    "create a stack from this template.")
MyDB = t.add_resource(DBInstance(
    "MyDB",
    Engine="MySQL",
    MasterUsername="myName",
    MasterUserPassword="myPassword",
    AllocatedStorage="5",
    DBInstanceClass="db.m1.small",
    DBName="MyDatabase",
))

JDBCConnectionString = t.add_output(Output(
    "JDBCConnectionString",
    Description="JDBC connection string for the database",
    Value=Join("", [
        "jdbc:mysql://",
        GetAtt(MyDB, "Endpoint.Address"),
        ":",
        GetAtt(MyDB, "Endpoint.Port"),
        "/MyDatabase"
    ]),
))

print(t.to_json())
