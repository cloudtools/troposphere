# Converted from RDS_with_DBParameterGroup.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import Parameter, Ref, Template
from troposphere.rds import DBInstance, DBParameterGroup


t = Template()

t.set_description(
    "AWS CloudFormation Sample Template RDS_with_DBParameterGroup: Sample "
    "template showing how to create an Amazon RDS Database Instance with "
    "a DBParameterGroup.**WARNING** This template creates an Amazon "
    "Relational Database Service database instance. You will be billed for "
    "the AWS resources used if you create a stack from this template.")

dbuser = t.add_parameter(Parameter(
    "DBUser",
    NoEcho=True,
    Description="The database admin account username",
    Type="String",
    MinLength="1",
    MaxLength="16",
    AllowedPattern="[a-zA-Z][a-zA-Z0-9]*",
    ConstraintDescription=("must begin with a letter and contain only"
                           " alphanumeric characters.")
))

dbpassword = t.add_parameter(Parameter(
    "DBPassword",
    NoEcho=True,
    Description="The database admin account password",
    Type="String",
    MinLength="1",
    MaxLength="41",
    AllowedPattern="[a-zA-Z0-9]*",
    ConstraintDescription="must contain only alphanumeric characters."
))


myrdsparamgroup = t.add_resource(DBParameterGroup(
    "MyRDSParamGroup",
    Family="MySQL5.5",
    Description="CloudFormation Sample Database Parameter Group",
    Parameters={
        "autocommit": "1",
        "general_log": "1",
        "old_passwords": "0"
    }
))

mydb = t.add_resource(DBInstance(
    "MyDB",
    AllocatedStorage="5",
    DBInstanceClass="db.m1.small",
    Engine="MySQL",
    EngineVersion="5.5",
    MasterUsername=Ref(dbuser),
    MasterUserPassword=Ref(dbpassword),
    DBParameterGroupName=Ref(myrdsparamgroup),
))

print(t.to_json())
