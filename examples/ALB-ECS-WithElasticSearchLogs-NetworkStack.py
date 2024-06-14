import troposphere.elasticloadbalancingv2 as elb
from troposphere.ecs import Cluster as ECSCluster
from troposphere.elasticsearch import Domain, ElasticsearchClusterConfig
from troposphere.elasticsearch import EBSOptions
from troposphere import Join, Select, GetAZs, Equals, GetAtt, Base64
from troposphere import FindInMap, Output, If, Or
from troposphere import Parameter, Ref, Tags, Template, autoscaling
from troposphere import cloudformation, Export
from troposphere.ec2 import InternetGateway
from troposphere.ec2 import VPCGatewayAttachment
from troposphere.ec2 import SubnetRouteTableAssociation, Subnet
from troposphere.ec2 import SecurityGroup, SecurityGroupRule
from troposphere.ec2 import RouteTable, Route
from troposphere.ec2 import VPC
from troposphere.ec2 import EIP
from troposphere.ec2 import NatGateway
from troposphere.autoscaling import LaunchConfiguration, AutoScalingGroup, Tag
from troposphere.policies import UpdatePolicy, AutoScalingRollingUpdate
from troposphere.policies import CreationPolicy, ResourceSignal
from troposphere.iam import Role, InstanceProfile

ref_region = Ref('AWS::Region')
ref_stack_id = Ref('AWS::StackId')
ref_stack_name = Ref('AWS::StackName')
no_value = Ref("AWS::NoValue")
ref_account = Ref("AWS::AccountId")


template = Template()
template.add_version("2010-09-09")

template.add_description(
    "ALB-ECS Network Template")

template.add_mapping(
    'AWSRegion2AMI4ECS', {
        "us-east-1": {"AMI": "ami-67a3a90d"},
        "us-west-2": {"AMI": "ami-c7a451a7"}
    })

template.add_description("""\
Parent VPC CloudFormation Template""")

# Set up parameters

vpc_cidr_prefix = template.add_parameter(Parameter(
    "VPCCIDRPrefix",
    Description="IP Address range for the VPN connected VPC",
    Default="172.31",
    Type="String",
))

env = template.add_parameter(Parameter(
    "Env",
    Type="String",
    Description="The environment being deployed into",
    Default="dev"
))

keypair = template.add_parameter(Parameter(
    "KeyPair",
    Type="String",
    Description="Name of an existing EC2 KeyPair to enable SSH access",
    MinLength="1",
    AllowedPattern="[\x20-\x7E]*",
    MaxLength="255",
    ConstraintDescription="can contain only ASCII characters.",
    Default="None"
))

template.add_condition(
    "NoKeyPair", Equals(Ref(keypair), "None")
)


template.add_condition(
    "ProdCheck", Or(Equals(Ref(env), "prod"),
                    Equals(Ref(env), "staging")
                    )
)

# Start resource creation

es_domain = template.add_resource(Domain(
    'GlobalElasticSearch',
    ElasticsearchClusterConfig=ElasticsearchClusterConfig(
        DedicatedMasterEnabled=True,
        InstanceCount=2,
        ZoneAwarenessEnabled=True,
        InstanceType="t2.micro.elasticsearch",
        DedicatedMasterType="t2.micro.elasticsearch",
        DedicatedMasterCount=2
    ),
    EBSOptions=EBSOptions(EBSEnabled=True,
                          Iops=0,
                          VolumeSize=20,
                          VolumeType="gp2"),
    AccessPolicies={
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "AWS": [
                        Join("", ["arn:aws:iam::", ref_account, ":root"])
                    ]
                },
                "Action": [
                    "es:*"
                ],
                "Resource": "*"
            }
        ]
    }
))


vpc = template.add_resource(VPC(
    "VPC",
    EnableDnsSupport="true",
    CidrBlock=Join('', [Ref(vpc_cidr_prefix), '.0.0/16']),
    EnableDnsHostnames="true",
    Tags=Tags(
        Application=Ref("AWS::StackName"),
        Network="VPC",
    )
))

igw = template.add_resource(InternetGateway(
    "InternetGateway",
    Tags=[{"Key": "Network", "Value": "igw"}]
))
igw_attachment = template.add_resource(VPCGatewayAttachment(
    "AttachGateway",
    VpcId=Ref(vpc),
    InternetGatewayId=Ref("InternetGateway")
))
public_route_table = template.add_resource(RouteTable(
    "PublicRouteTable",
    VpcId=Ref(vpc),
    Tags=[{"Key": "Network", "Value": "public"}]
))
route_to_internet_for_public_subnets = template.add_resource(Route(
    "RouteToInternetForPublicSubnets",
    RouteTableId=Ref(public_route_table),
    DestinationCidrBlock="0.0.0.0/0",
    GatewayId=Ref(igw)
))
public_subnet_a = template.add_resource(Subnet(
    'PublicSubnetA',
    CidrBlock=Join('', [Ref(vpc_cidr_prefix), '.0.0/26']),
    VpcId=Ref(vpc),
    AvailabilityZone=Select("0", GetAZs(ref_region))
)
)
subnet_a_route_table_association = template.add_resource(
    SubnetRouteTableAssociation(
        'PublicSubnetRouteTableAssociationA',
        SubnetId=Ref(public_subnet_a),
        RouteTableId=Ref(public_route_table)))
public_subnet_b = template.add_resource(Subnet(
    'PublicSubnetB',
    CidrBlock=Join('', [Ref(vpc_cidr_prefix), '.0.64/26']),
    VpcId=Ref(vpc),
    AvailabilityZone=Select("1", GetAZs(ref_region))
))
subnet_b_route_table_association = template.add_resource(
    SubnetRouteTableAssociation(
        'PublicSubnetRouteTableAssociationB',
        SubnetId=Ref(public_subnet_b),
        RouteTableId=Ref(public_route_table)))
public_subnet_c = template.add_resource(Subnet(
    'PublicSubnetC',
    CidrBlock=Join('', [Ref(vpc_cidr_prefix), '.0.128/26']),
    VpcId=Ref(vpc),
    AvailabilityZone=Select("2", GetAZs(ref_region))
))
subnet_c_route_table_association = template.add_resource(
    SubnetRouteTableAssociation(
        'PublicSubnetRouteTableAssociationC',
        SubnetId=Ref(public_subnet_c),
        RouteTableId=Ref(public_route_table)))

nat_eip = template.add_resource(EIP(
    'NatEip',
    Domain="vpc"
))

nat_a = template.add_resource(NatGateway(
    'NATa',
    AllocationId=GetAtt(nat_eip, 'AllocationId'),
    SubnetId=Ref(public_subnet_a)
))

nat_b = template.add_resource(NatGateway(
    'NATb',
    AllocationId=GetAtt(nat_eip, 'AllocationId'),
    SubnetId=Ref(public_subnet_b),
    Condition="ProdCheck"
))

nat_c = template.add_resource(NatGateway(
    'NATc',
    AllocationId=GetAtt(nat_eip, 'AllocationId'),
    SubnetId=Ref(public_subnet_c),
    Condition="ProdCheck"
))


private_route_table_a = template.add_resource(RouteTable(
    "PrivateRouteTableA",
    VpcId=Ref(vpc),
    Tags=[{"Key": "Network", "Value": "private"}]
))

private_route_table_b = template.add_resource(RouteTable(
    "PrivateRouteTableB",
    VpcId=Ref(vpc),
    Tags=[{"Key": "Network", "Value": "private"}]
))

private_route_table_c = template.add_resource(RouteTable(
    "PrivateRouteTableC",
    VpcId=Ref(vpc),
    Tags=[{"Key": "Network", "Value": "private"}]
))

route_to_internet_for_private_subnet_a = template.add_resource(Route(
    "RouteToInternetForPrivateSubnetA",
    RouteTableId=Ref(private_route_table_a),
    DestinationCidrBlock="0.0.0.0/0",
    NatGatewayId=Ref(nat_a)
))

route_to_internet_for_private_subnet_b = template.add_resource(Route(
    "RouteToInternetForPrivateSubnetB",
    RouteTableId=Ref(private_route_table_b),
    DestinationCidrBlock="0.0.0.0/0",
    NatGatewayId=If("ProdCheck", Ref(nat_b), Ref(nat_a))
))

route_to_internet_for_private_subnet_c = template.add_resource(Route(
    "RouteToInternetForPrivateSubnetC",
    RouteTableId=Ref(private_route_table_c),
    DestinationCidrBlock="0.0.0.0/0",
    NatGatewayId=If("ProdCheck", Ref(nat_c), Ref(nat_a))
))

private_subnet_a = template.add_resource(Subnet(
    'PrivateSubnetA',
    CidrBlock=Join('', [Ref(vpc_cidr_prefix), '.1.0/26']),
    VpcId=Ref(vpc),
    AvailabilityZone=Select("0", GetAZs(ref_region))
))

private_subnet_a_route_table_association = template.add_resource(
    SubnetRouteTableAssociation(
        'PrivateSubnetRouteTableAssociationA',
        SubnetId=Ref(private_subnet_a),
        RouteTableId=Ref(private_route_table_a)))

private_subnet_b = template.add_resource(Subnet(
    'PrivateSubnetB',
    CidrBlock=Join('', [Ref(vpc_cidr_prefix), '.1.64/26']),
    VpcId=Ref(vpc),
    AvailabilityZone=Select("1", GetAZs(ref_region))
))

private_subnet_b_route_table_association = template.add_resource(
    SubnetRouteTableAssociation(
        'PrivateSubnetRouteTableAssociationB',
        SubnetId=Ref(private_subnet_b),
        RouteTableId=Ref(private_route_table_b)))

private_subnet_c = template.add_resource(Subnet(
    'PrivateSubnetC',
    CidrBlock=Join('', [Ref(vpc_cidr_prefix), '.1.128/26']),
    VpcId=Ref(vpc),
    AvailabilityZone=Select("2", GetAZs(ref_region))
))

private_subnet_c_route_table_association = template.add_resource(
    SubnetRouteTableAssociation(
        'PrivateSubnetRouteTableAssociationC',
        SubnetId=Ref(private_subnet_c),
        RouteTableId=Ref(private_route_table_c)))

app_role = template.add_resource(Role(
    "AppInstanceRole",
    ManagedPolicyArns=["arn:aws:iam::aws:policy/service-role/"
                       "AmazonEC2ContainerServiceforEC2Role"],
    AssumeRolePolicyDocument={
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": [
                        "ec2.amazonaws.com"
                    ]
                },
                "Action": [
                    "sts:AssumeRole"
                ]
            }
        ]
    },
    Path="/"
))

service_instance_profile = template.add_resource(InstanceProfile(
    "ServiceInstanceProfile",
    Path="/",
    Roles=[Ref(app_role)]
))


elb_security_group = template.add_resource(SecurityGroup(
    "ELBSecurityGroup",
    GroupDescription="ELB Security Group",
    SecurityGroupIngress=[
        SecurityGroupRule(
            IpProtocol='tcp',
            FromPort='80',
            ToPort='80',
            CidrIp='0.0.0.0/0')
    ],
    VpcId=Ref(vpc)
))

instance_security_group = template.add_resource(SecurityGroup(
    "InstanceSG",
    GroupDescription="Instance_SG",
    SecurityGroupIngress=[
        SecurityGroupRule(
            IpProtocol='TCP',
            FromPort='443',
            ToPort='443',
            SourceSecurityGroupId=Ref(elb_security_group)
        ),
        SecurityGroupRule(
            IpProtocol='-1',
            FromPort="-1",
            ToPort="-1",
            SourceSecurityGroupId=Ref(elb_security_group)
        ),
        SecurityGroupRule(
            IpProtocol='-1',
            FromPort='-1',
            ToPort='-1',
            CidrIp=Join('', [Ref(vpc_cidr_prefix), '.0.0/0'])
        )
    ],
    VpcId=Ref(vpc)
))

ecs_cluster = template.add_resource(ECSCluster(
    "ECSServiceCluster"
))

# Add the application ELB
app_load_balancer = template.add_resource(elb.LoadBalancer(
    "ApplicationElasticLB",
    Name="ApplicationElasticLB",
    Scheme="internet-facing",
    Subnets=[Ref(public_subnet_a), Ref(public_subnet_b), Ref(public_subnet_c)],
    SecurityGroups=[Ref(elb_security_group)]
))

default_target_group = template.add_resource(elb.TargetGroup(
    "DefaultTargetGroup",
    HealthCheckIntervalSeconds="30",
    HealthCheckProtocol="HTTP",
    HealthCheckTimeoutSeconds="10",
    HealthyThresholdCount="4",
    Matcher=elb.Matcher(
        HttpCode="200"),
    Name="DefaultRedirect",
    Port="80",
    Protocol="HTTP",
    UnhealthyThresholdCount="3",
    VpcId=Ref(vpc)
))

http_listener = template.add_resource(elb.Listener(
    "HTTPListener",
    Port="80",
    Protocol="HTTP",
    LoadBalancerArn=Ref(app_load_balancer),
    DefaultActions=[elb.Action(
        Type="forward",
        TargetGroupArn=Ref(default_target_group)
    )]
))

ecs_launch_configuration = template.add_resource(LaunchConfiguration(
    "ECSLaunchConfiguration",
    Metadata=autoscaling.Metadata(
        cloudformation.Init(
            cloudformation.InitConfigSets(
                default=['ecs']
            ),
            ecs=cloudformation.InitConfig(
                commands={
                    "RegisterWithECS": {
                        "command": Join("", [
                            "echo ECS_CLUSTER=", Ref(ecs_cluster),
                            " >> /etc/ecs/ecs.config"
                        ])
                    }
                }
            )
        )
    ),
    UserData=Base64(Join('', [
        "#cloud-config\n",
        "repo_upgrade: all\n",
        "runcmd:\n",
        "  - echo '05-22-2016-1652'\n",
        "  - yum install -y aws-cfn-bootstrap aws-cli\n",
        "  - /opt/aws/bin/cfn-init -v",
        " --resource 'ECSLaunchConfiguration'",
        "  -c 'default'"
        " --stack ", ref_stack_name,
        " --region ", ref_region, "\n",
        "  - /opt/aws/bin/cfn-signal -e $?",
        " --resource ECSServiceASG",
        " --stack ", ref_stack_name,
        " --region ", ref_region, "\n"
    ])),
    ImageId=FindInMap("AWSRegion2AMI4ECS", ref_region, "AMI"),
    KeyName=If("ProdCheck", no_value, If("NoKeyPair", no_value, Ref(keypair))),
    IamInstanceProfile=Ref(service_instance_profile),
    SecurityGroups=[Ref(instance_security_group)],
    InstanceType=If("ProdCheck", "m4.large", "t2.medium")
))

ecs_service_asg = template.add_resource(AutoScalingGroup(
    "ECSServiceASG",
    CreationPolicy=CreationPolicy(
        ResourceSignal=ResourceSignal(
            Count="1",
            Timeout='PT10M'
        )
    ),
    DesiredCapacity=If("ProdCheck", "3", "2"),
    Tags=[
        Tag("Environment", Ref(env), True),
        Tag("Name", "ECS Cluster", True)
    ],
    LaunchConfigurationName=Ref(ecs_launch_configuration),
    MinSize="2",
    MaxSize="10",
    VPCZoneIdentifier=[Ref(private_subnet_a), Ref(private_subnet_b),
                       Ref(private_subnet_c)],
    AvailabilityZones=[
        GetAtt(private_subnet_a, "AvailabilityZone"),
        GetAtt(private_subnet_b, "AvailabilityZone"),
        GetAtt(private_subnet_c, "AvailabilityZone")
    ],
    HealthCheckType="EC2",
    UpdatePolicy=UpdatePolicy(
        AutoScalingRollingUpdate=AutoScalingRollingUpdate(
            PauseTime='PT5M',
            MinInstancesInService="1",
            MaxBatchSize='1',
            WaitOnResourceSignals=True
        )
    )
))

template.add_output(Output(
    "VPCId",
    Description="VPC ID",
    Value=Ref(vpc),
    Export=Export(Join("", ["ECSClusterVPC-", Ref(env)]))
))

template.add_output(Output(
    "ECSClusterID",
    Description="ECS Cluster ID",
    Value=Ref(ecs_cluster),
    Export=Export(Join("", ["ECSClusterID-", Ref(env)]))
))

template.add_output(Output(
    "HTTPListener",
    Description="ALB HTTP Listener",
    Value=Ref(http_listener),
    Export=Export(Join("", ["ALBHttpListener-", Ref(env)]))
))

template.add_output(Output(
    "ECSClusterALB",
    Description="ALB for ECS Cluster",
    Value=Ref(app_load_balancer),
    Export=Export(Join("", ["ECSALB-", Ref(env)]))
))

template.add_output(Output(
    "GlobalESClusterEndpoint",
    Description="Global ElasticSearch Cluster Endpoint",
    Value=GetAtt(es_domain, "DomainEndpoint"),
    Export=Export(Join("", ["GlobalESClusterEndpoint-", Ref(env)]))
))

template.add_output(Output(
    "ESClusterARN",
    Description="Global ElasticSearch Cluster ARN",
    Value=GetAtt(es_domain, "DomainArn"),
    Export=Export(Join("", ["GlobalESClusterARN-", Ref(env)]))
))

template.add_output(Output(
    "VPCCidrPrefix",
    Description="VPC Cidr Prefix",
    Value=Ref(vpc_cidr_prefix),
    Export=Export(Join("", ["VPCCidrPrefix-", Ref(env)]))
))

template.add_output(Output(
    "NATa",
    Description="NAT A",
    Value=Ref(nat_a),
    Export=Export(Join("", ["NATa-", Ref(env)]))
))

template.add_output(Output(
    "NATb",
    Description="NAT B",
    Value=Ref(nat_b),
    Export=Export(Join("", ["NATb-", Ref(env)]))
))

template.add_output(Output(
    "NATc",
    Description="NAT C",
    Value=Ref(nat_c),
    Export=Export(Join("", ["NATc-", Ref(env)]))
))

template.add_output(Output(
    "URL",
    Description="URL of the ELB",
    Value=Join("", ["http://", GetAtt(app_load_balancer, "DNSName")])
))

print(template.to_json())
