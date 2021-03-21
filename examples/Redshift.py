# Converted from Redshift.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import Template, Parameter, Ref, Equals
from troposphere import If, Output, Join, GetAtt
from troposphere.redshift import Cluster, ClusterParameterGroup
from troposphere.redshift import AmazonRedshiftParameter


t = Template()

t.add_version("2010-09-09")

t.set_description(
    "AWS CloudFormation Sample Template: Redshift cluster")

dbname = t.add_parameter(Parameter(
    "DatabaseName",
    Description="The name of the first database to be created when the "
    "redshift cluster is created",
    Type="String",
    Default="defaultdb",
    AllowedPattern="([a-z]|[0-9])+",
))

clustertype = t.add_parameter(Parameter(
    "ClusterType",
    Description="The type of the cluster",
    Type="String",
    Default="single-node",
    AllowedValues=[
        "single-node",
        "multi-node"
    ],
))

numberofnodes = t.add_parameter(Parameter(
    "NumberOfNodes",
    Description="The number of compute nodes in the redshift cluster. "
    "When cluster type is specified as: 1) single-node, the NumberOfNodes "
    "parameter should be specified as 1, 2) multi-node, the NumberOfNodes "
    "parameter should be greater than 1",
    Type="Number",
    Default="1",
))

nodetype = t.add_parameter(Parameter(
    "NodeType",
    Description="The node type to be provisioned for the redshift cluster",
    Type="String",
    Default="dw2.large",
))

masterusername = t.add_parameter(Parameter(
    "MasterUsername",
    Description="The user name associated with the master user account for "
    "the redshift cluster that is being created",
    Type="String",
    Default="defaultuser",
    AllowedPattern="([a-z])([a-z]|[0-9])*",
    NoEcho=True,
))

masteruserpassword = t.add_parameter(Parameter(
    "MasterUserPassword",
    Description="The password associated with the master user account for the "
    "redshift cluster that is being created.",
    Type="String",
    NoEcho=True,
))

conditions = {
    "IsMultiNodeCluster": Equals(
        Ref("ClusterType"),
        "multi-node"
    ),
}

for k in conditions:
    t.add_condition(k, conditions[k])

redshiftcluster = t.add_resource(Cluster(
    "RedshiftCluster",
    ClusterType=Ref("ClusterType"),
    NumberOfNodes=If("IsMultiNodeCluster",
                     Ref("NumberOfNodes"), Ref("AWS::NoValue")),
    NodeType=Ref("NodeType"),
    DBName=Ref("DatabaseName"),
    MasterUsername=Ref("MasterUsername"),
    MasterUserPassword=Ref("MasterUserPassword"),
    ClusterParameterGroupName=Ref("RedshiftClusterParameterGroup"),
    DeletionPolicy="Snapshot",
))

amazonredshiftparameter1 = AmazonRedshiftParameter(
    "AmazonRedshiftParameter1",
    ParameterName="enable_user_activity_logging",
    ParameterValue="true",
)

redshiftclusterparametergroup = t.add_resource(ClusterParameterGroup(
    "RedshiftClusterParameterGroup",
    Description="Cluster parameter group",
    ParameterGroupFamily="redshift-1.0",
    Parameters=[amazonredshiftparameter1],
))

t.add_output(Output(
    "ClusterEndpoint",
    Value=Join(":", [GetAtt(redshiftcluster, "Endpoint.Address"),
               GetAtt(redshiftcluster, "Endpoint.Port")]),
))

print(t.to_json())
