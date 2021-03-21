from troposphere import GetAtt, Join, Output, Parameter, Ref, Template
from troposphere.ec2 import SecurityGroup
from troposphere.rds import (
    DBSubnetGroup,
    DBCluster,
    ScalingConfiguration
)
from troposphere.secretsmanager import (Secret, GenerateSecretString,
                                        SecretTargetAttachment)

t = Template()
t.set_version('2010-09-09')
t.set_description("""\
AWS CloudFormation Template to launch an Aurora Serverless Relational \
Database (RDS) Cluster.""")

vpcid = t.add_parameter(Parameter(
    "VpcId",
    Type="String",
    Description="VpcId of your existing Virtual Private Cloud (VPC)"
))

subnet = t.add_parameter(Parameter(
    "Subnets",
    Type="CommaDelimitedList",
    Description=(
        "The list of SubnetIds, for at least two Availability Zones in the "
        "region in your Virtual Private Cloud (VPC)")
))

dbuser = t.add_parameter(Parameter(
    "DBUser",
    NoEcho=True,
    Default="admin",
    Description="Database admin account username (Default: admin)",
    Type="String",
    MinLength="1",
    MaxLength="16",
    AllowedPattern="[a-zA-Z][a-zA-Z0-9]*",
    ConstraintDescription=("must begin with a letter and contain only"
                           " alphanumeric characters.")
))

clustermincapacity = t.add_parameter(Parameter(
    "ClusterMinCapacity",
    Type="Number",
    Default="1",
    Description="Minimum Capacity Units for an Aurora ServerLess Cluster \
            (Default: 1)",
    AllowedValues=["1", "2", "4", "8", "16", "32", "64", "128", "256"],
))

clustermaxcapacity = t.add_parameter(Parameter(
    "ClusterMaxCapacity",
    Type="Number",
    Default="2",
    Description="Maximum Capacity Units for an Aurora ServerLess Cluster \
            (Default: 2)",
    AllowedValues=["1", "2", "4", "8", "16", "32", "64", "128", "256"],
))

slclusterparametergroup = t.add_parameter(
    Parameter(
        "DatabaseClusterParameterGroupName",
        Type="String",
        Default="default.aurora5.6",
    )
)

DbSecret = t.add_resource(Secret(
    "DbSecret",
    Name="DbSecret",
    Description="RDS instance master password",
    GenerateSecretString=GenerateSecretString(
        SecretStringTemplate="{\"username\":\"admin\"}",
        GenerateStringKey="password",
        PasswordLength=30,
        ExcludeCharacters='/@" '
    ),
))

rdssubnetgroup = t.add_resource(DBSubnetGroup(
    "RDSSubnetGroup",
    DBSubnetGroupDescription="Subnets available for the RDS DB Instance",
    SubnetIds=Ref(subnet),
))

rdssecuritygroup = t.add_resource(SecurityGroup(
    "RDSSecurityGroup",
    GroupDescription="Security Group for the Aurora Serverless Cluster",
    VpcId=Ref(vpcid)
))

AuroraSLCluster = t.add_resource(DBCluster(
    "AuroraSLCluster",
    Engine="aurora",
    MasterUsername=Ref(dbuser),
    MasterUserPassword=Join("", [
        "{{resolve:secretsmanager:",
        {"Ref": "DbSecret"},
        ":SecretString:password}}"
    ]),
    DBClusterParameterGroupName=Ref(slclusterparametergroup),
    DBClusterIdentifier="aurora-sl-cluster",
    EngineMode="serverless",
    ScalingConfiguration=ScalingConfiguration(
        AutoPause=False,
        MaxCapacity=Ref(clustermaxcapacity),
        MinCapacity=Ref(clustermincapacity)),
    DBSubnetGroupName=Ref(rdssubnetgroup),
    VpcSecurityGroupIds=[Ref(rdssecuritygroup)],
    StorageEncrypted="true"
))

t.add_resource(SecretTargetAttachment(
    "SecretRDSInstanceAttachment",
    TargetType="AWS::RDS::DBCluster",
    SecretId=Ref(DbSecret),
    TargetId=Ref(AuroraSLCluster),
))

t.add_output(Output(
    "EndpointAddressandPort",
    Description="Endpoint Address and Port for the Aurora Serverless Cluster",
    Value=Join("", [
        GetAtt("AuroraSLCluster", "Endpoint.Address"),
        ":",
        GetAtt("AuroraSLCluster", "Endpoint.Port")
    ])
))

print(t.to_json())
