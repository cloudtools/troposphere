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
    ReleaseLabel='emr-4.4.0',
    BootstrapActions=[emr.BootstrapActionConfig(
        Name='Dummy bootstrap action',
        ScriptBootstrapAction=emr.ScriptBootstrapActionConfig(
            Path='/bin/sh',
            Args=['echo', 'Hello World']
        )
    )],
    Configurations=[
        emr.Configuration(
            Classification="core-site",
            ConfigurationProperties={
                'hadoop.security.groups.cache.secs': '250'
            }
        ),
        emr.Configuration(
            Classification="mapred-site",
            ConfigurationProperties={
                'mapred.tasktracker.map.tasks.maximum': '2',
                'mapreduce.map.sort.spill.percent': '90',
                'mapreduce.tasktracker.reduce.tasks.maximum': '5'
            }
        ),
        emr.Configuration(
            Classification="hadoop-env",
            Configurations=[
                emr.Configuration(
                    Classification="export",
                    ConfigurationProperties={
                        "HADOOP_DATANODE_HEAPSIZE": "2048",
                        "HADOOP_NAMENODE_OPTS": "-XX:GCTimeRatio=19"
                    }
                )
            ]
        )
    ],
    EbsConfiguration=emr.EbsConfiguration(
        EbsBlockDeviceConfig=[
            emr.EbsBlockDeviceConfig(
                VolumeSpecification=emr.VolumeSpecification(
                    SizeInGB="100",
                    VolumeType="standard"
                ),
                VolumesPerInstance="1"
            )
        ],
        EbsOptimized="true"
    ),
    JobFlowRole=Ref(emr_instance_profile),
    ServiceRole=Ref(emr_service_role),
    Instances=emr.JobFlowInstancesConfig(
        MasterInstanceGroup=emr.InstanceGroupConfigProperty(
            Name="Master Instance",
            InstanceCount="1",
            InstanceType="m3.xlarge",
            Market="ON_DEMAND"
        ),
        CoreInstanceGroup=emr.InstanceGroupConfigProperty(
            Name="Core Instance",
            BidPrice="20",
            InstanceCount="1",
            InstanceType="m3.xlarge",
            Market="SPOT"
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

step = template.add_resource(emr.Step(
    'TestStep',
    Name="TestStep",
    ActionOnFailure='CONTINUE',
    HadoopJarStep=emr.HadoopJarStepConfig(
        Args=["5", "10"],
        Jar="s3://emr-cfn-test/hadoop-mapreduce-examples-2.6.0.jar",
        MainClass="pi",
        StepProperties=[
            emr.KeyValue('my.custom.property', 'my.custom.value')
        ]
    ),
    JobFlowId=Ref(cluster)
))

print(template.to_json())
