from troposphere import Join, GetAtt, ImportValue
from troposphere import Parameter, Ref, Template
from troposphere.ecs import Service as ECSService
from troposphere.ecs import LoadBalancer as ECSLoadBalancer
from troposphere.ecs import TaskDefinition, ContainerDefinition
from troposphere.ecs import Environment, PortMapping, LogConfiguration
from troposphere.ecs import Volume as ECSVolume
from troposphere.iam import Role, PolicyType
import troposphere.elasticloadbalancingv2 as elb
from troposphere.logs import LogGroup

template = Template()
template.add_version("2010-09-09")

template.add_description(
    "ALB-ECS App Template")

ref_region = Ref('AWS::Region')
ref_stack_id = Ref('AWS::StackId')
ref_stack_name = Ref('AWS::StackName')
no_value = Ref("AWS::NoValue")
ref_account = Ref("AWS::AccountId")

# Parameters

docker_image = template.add_parameter(Parameter(
    "DockerImage",
    Type="String",
    Description="Docker image to deploy"
))

priority = template.add_parameter(Parameter(
    "Priority",
    Type="String",
    Description="ALB Listener Rule Priority. Can't conflict with another rule"
))

service_name = template.add_parameter(Parameter(
    "ServiceName",
    Type="String",
    Description="Service Name"
))

number_of_containers = template.add_parameter(Parameter(
    "NumberOfContainers",
    Type="String",
    Description="Optionally specify the number of containers of your "
                "service you want to run",
    Default="1"
))

health_check_path = template.add_parameter(Parameter(
    "HealthCheckPath",
    Type="String",
    Description="Health Check Path. Don't include the base path of your "
                "service name. For example, just write: '/ping"
))

container_port = template.add_parameter(Parameter(
    "ContainerPort",
    Type="String",
    Description="This is the port specified in the Dockerfile"
))

env = template.add_parameter(Parameter(
    "Environment",
    Type="String",
    Description="Deployment Environment"
))

database_endpoint = template.add_parameter(Parameter(
    "DatabaseEndpoint",
    Type="String",
    Description="Customer database endpoint"
))
# Imports

vpc = ImportValue(Join("", ["ECSClusterVPC-", Ref(env)]))
ecs_cluster = ImportValue(Join("", ["ECSClusterID-", Ref(env)]))
http_listener = ImportValue(Join("", ["ALBHttpListener-", Ref(env)]))
app_load_balancer = ImportValue(Join("", ["ECSALB-", Ref(env)]))
global_es_cluster_endpoint = ImportValue(Join("",
                                         ["GlobalESClusterEndpoint-",
                                          Ref(env)]))
global_es_cluster_arn = ImportValue(Join("", ["GlobalESClusterARN-",
                                              Ref(env)]))

# Resources

app_log_group = template.add_resource(LogGroup(
    "AppLogGroup",
    RetentionInDays=7
))


service_ecs_role = template.add_resource(Role(
    "ECSServiceRole",
    AssumeRolePolicyDocument={
        "Version": "2008-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": [
                        "ecs.amazonaws.com"
                    ]
                },
                "Action": [
                    "sts:AssumeRole"
                ]
            }
        ]
    },
    ManagedPolicyArns=["arn:aws:iam::aws:policy/service-role/"
                       "AmazonEC2ContainerServiceRole"],
    Path="/"
))

ecs_task_role = template.add_resource(Role(
    "ECSTaskRole",
    AssumeRolePolicyDocument={
        "Version": "2008-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": [
                        "ecs-tasks.amazonaws.com"
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

basic_app_permissions = template.add_resource(PolicyType(
    "BasicAppPermissions",
    PolicyName="BasicAppPermissions",
    PolicyDocument={
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "logs:Create*",
                    "logs:PutLogEvents"
                ],
                "Resource": [
                    Join("", [
                        "arn:aws:logs:", ref_region, ":",
                        ref_account, ":log-group:",
                        Ref(app_log_group), ":*"]),
                    "*"
                ]
            },
            {
                "Effect": "Allow",
                "Action": [
                    "cloudwatch:PutMetricData"
                ],
                "Resource": [
                    "*"
                ]
            }
        ]
    },
    Roles=[Ref(ecs_task_role)]
))

docker_containers = [ContainerDefinition(
    Cpu=512,
    Essential=True,
    Image=Ref(docker_image),
    Memory=512,
    Name=Join("", [Ref(service_name), "-api"]),
    Environment=[
        Environment(
            Name="DB_ENDPOINT",
            Value=Ref(database_endpoint)
        ),
        Environment(
            Name="CW_LOGS_GROUP",
            Value=Ref(app_log_group)
        ),
        Environment(
            Name="REGION",
            Value=ref_region
        )
    ],
    PortMappings=[
        PortMapping(
            ContainerPort=Ref(container_port)
        )
    ],
    LogConfiguration=LogConfiguration(
        LogDriver="awslogs",
        Options={
            "awslogs-group": Ref(app_log_group),
            "awslogs-region": ref_region
        }
    )
)]

service_task = template.add_resource(TaskDefinition(
    "ServiceTask",
    ContainerDefinitions=docker_containers,
    Volumes=[
        ECSVolume(
            Name="default"
        )
    ],
    TaskRoleArn=GetAtt(ecs_task_role, "Arn")
))

target_group_api = template.add_resource(elb.TargetGroup(
    "APITargetGroup",
    HealthCheckIntervalSeconds="10",
    HealthCheckProtocol="HTTP",
    HealthCheckTimeoutSeconds="9",
    HealthyThresholdCount="2",
    HealthCheckPath=Join("", ["/api/", Ref(service_name),
                              Ref(health_check_path)]),
    Matcher=elb.Matcher(
        HttpCode="200"),
    Name=Join("", [Ref(service_name), "-TargetGroup"]),
    Port=Ref(container_port),
    Protocol="HTTP",
    UnhealthyThresholdCount="2",
    VpcId=vpc
))

ecs_service = template.add_resource(ECSService(
    "ECSService",
    Cluster=ecs_cluster,
    DesiredCount=Ref(number_of_containers),
    LoadBalancers=[(ECSLoadBalancer(
        ContainerName=Join("", [Ref(service_name), "-api"]),
        ContainerPort=Ref(container_port),
        TargetGroupArn=Ref(target_group_api)
    ))],
    TaskDefinition=Ref(service_task),
    Role=Ref(service_ecs_role)
))

template.add_resource(elb.ListenerRule(
    "ListenerRuleApi",
    ListenerArn=http_listener,
    Conditions=[elb.Condition(
        Field="path-pattern",
        Values=[Join("", ["/api/", Ref(service_name), "/*"])]
    )],
    Actions=[elb.Action(
        Type="forward",
        TargetGroupArn=Ref(target_group_api)
    )],
    Priority=Ref(priority)
))

cw_lambda_role = template.add_resource(Role(
    "CWLogsRole",
    AssumeRolePolicyDocument={
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": [
                        "lambda.amazonaws.com"
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

es_pemissions = template.add_resource(PolicyType(
    "ESPostingPermissions",
    PolicyName="ESPostingPermissions",
    PolicyDocument={
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": ["es:ESHttpPost", "es:ESHttpPut"],
                "Resource": [global_es_cluster_arn,
                             Join("", [global_es_cluster_arn, "/*"])]
            }
        ]
    },
    Roles=[Ref(cw_lambda_role)]
))

print(template.to_json())
