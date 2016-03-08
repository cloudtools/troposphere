from troposphere import Parameter, Ref, Template, Tags
import troposphere.iam as iam
import troposphere.emr as emr

template = Template()
template.add_description(
    "Sample CloudFormation template for creating an EMR cluster"
)

keyname = template.add_parameter(Parameter(
    "KeyName",
    Description="Name of an existing EC2 KeyPair to enable SSH "
                "to the instances",
    Type="AWS::EC2::KeyPair::KeyName"
))

subnet = template.add_parameter(Parameter(
    "Subnet",
    Description="Subnet ID for creating the EMR cluster",
    Type="AWS::EC2::Subnet::Id"
))

service_access_sg = template.add_parameter(Parameter(
    "ServiceAccessSecurityGroup",
    Description="Security Group providing service access to EMR",
    Type="AWS::EC2::SecurityGroup::Id"
))

managed_master_sg = template.add_parameter(Parameter(
    "ManagedMasterSecurityGroup",
    Description="Security Group (managed by EMR) for master instances",
    Type="AWS::EC2::SecurityGroup::Id"
))

managed_slave_sq = template.add_parameter(Parameter(
    "ManagedSlaveSecurityGroup",
    Description="Security Group (managed by EMR) for slave instances",
    Type="AWS::EC2::SecurityGroup::Id"
))

# IAM roles required by EMR

emr_service_role = template.add_resource(iam.Role(
    'EMRServiceRole',
    AssumeRolePolicyDocument={
        "Statement": [{
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "elasticmapreduce.amazonaws.com"
                ]
            },
            "Action": ["sts:AssumeRole"]
        }]
    },
    ManagedPolicyArns=[
        'arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole'
    ]
))

emr_job_flow_role = template.add_resource(iam.Role(
    "EMRJobFlowRole",
    AssumeRolePolicyDocument={
        "Statement": [{
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "ec2.amazonaws.com"
                ]
            },
            "Action": ["sts:AssumeRole"]
        }]
    },
    ManagedPolicyArns=[
        'arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role'
    ]
))

emr_instance_profile = template.add_resource(iam.InstanceProfile(
    "EMRInstanceProfile",
    Roles=[Ref(emr_job_flow_role)]
))

# EMR Cluster Resource

cluster = template.add_resource(emr.Cluster(
    "EMRSampleCluster",
    Name="EMR Sample Cluster",
    ReleaseLabel='emr-4.3.0',
    BootstrapActions=[emr.BootstrapActionConfig(
        Name='Dummy bootstrap action',
        ScriptBootstrapAction=emr.ScriptBootstrapActionConfig(
            Path='/bin/sh',
            Args=['echo', 'Hello World']
        )
    )],
    JobFlowRole=Ref(emr_instance_profile),
    ServiceRole=Ref(emr_service_role),
    Instances=emr.JobFlowInstancesConfig(
        MasterInstanceGroup=emr.InstanceGroupConfigProperty(
            Name="Master Instance",
            InstanceCount="1",
            InstanceType="m3.xlarge"
        ),
        CoreInstanceGroup=emr.InstanceGroupConfigProperty(
            Name="Core Instance",
            InstanceCount="1",
            InstanceType="m3.xlarge"
        )
    ),
    Applications=[
        emr.Application(Name="Hadoop"),
        emr.Application(Name="Hive"),
        emr.Application(Name="Mahout"),
        emr.Application(Name="Pig"),
        emr.Application(Name="Spark")
    ],
    VisibleToAllUsers="true",
    Tags=Tags(
        Name="EMR Sample Cluster"
    )
))

print(template.to_json())
