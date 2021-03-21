from troposphere import Template, Join, Ref
from troposphere.secretsmanager import (Secret, GenerateSecretString,
                                        SecretTargetAttachment)
from troposphere.rds import DBInstance

t = Template()
t.add_version('2010-09-09')

DbSecret = t.add_resource(Secret(
    "DbSecret",
    Name="DbSecret",
    Description="This is the RDS instance master password",
    GenerateSecretString=GenerateSecretString(
        SecretStringTemplate="{\"username\":\"admin\"}",
        GenerateStringKey="password",
        PasswordLength=30,
    ),
))

Instance = t.add_resource(DBInstance(
    "Instance",
    AllocatedStorage="20",
    DBInstanceClass="db.t2.micro",
    Engine="mysql",
    DBInstanceIdentifier="TestInstance",
    MasterUsername=Join("", [
        "{{resolve:secretsmanager:",
        {"Ref": "DbSecret"},
        ":SecretString:username}}"
    ]),
    MasterUserPassword=Join("", [
        "{{resolve:secretsmanager:",
        {"Ref": "DbSecret"},
        ":SecretString:password}}"
    ])
))

t.add_resource(SecretTargetAttachment(
    "SecretRDSInstanceAttachment",
    TargetType="AWS::RDS::DBInstance",
    SecretId=Ref(DbSecret),
    TargetId=Ref(Instance),
))

print(t.to_json())
