# Converted from AWS OpsWorks Snippets located at:
# http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-opsworks.html

from troposphere import GetAZs, Join
from troposphere import Parameter, Ref, Template
from troposphere.elasticloadbalancing import LoadBalancer, HealthCheck
from troposphere.opsworks import App, ElasticLoadBalancerAttachment, Instance
from troposphere.opsworks import Layer, Stack
from troposphere.opsworks import Source, Recipes, VolumeConfiguration


template = Template()

template.add_version("2010-09-09")

ServiceRole = template.add_parameter(Parameter(
    "ServiceRole",
    Default="aws-opsworks-service-role",
    Description="The OpsWorks service role",
    Type="String",
    MinLength="1",
    MaxLength="64",
    AllowedPattern="[a-zA-Z][a-zA-Z0-9-]*",
    ConstraintDescription="must begin with a letter and contain only " +
                          "alphanumeric characters.",
))

InstanceRole = template.add_parameter(Parameter(
    "InstanceRole",
    Default="aws-opsworks-ec2-role",
    Description="The OpsWorks instance role",
    Type="String",
    MinLength="1",
    MaxLength="64",
    AllowedPattern="[a-zA-Z][a-zA-Z0-9-]*",
    ConstraintDescription="must begin with a letter and contain only " +
                          "alphanumeric characters.",
))

AppName = template.add_parameter(Parameter(
    "AppName",
    Default="myapp",
    Description="The app name",
    Type="String",
    MinLength="1",
    MaxLength="64",
    AllowedPattern="[a-zA-Z][a-zA-Z0-9]*",
    ConstraintDescription="must begin with a letter and contain only " +
                          "alphanumeric characters.",
))

MysqlRootPassword = template.add_parameter(Parameter(
    "MysqlRootPassword",
    Description="MysqlRootPassword",
    NoEcho=True,
    Type="String",
))

myStack = template.add_resource(Stack(
    "myStack",
    Name=Ref("AWS::StackName"),
    ServiceRoleArn=Join(
        "",
        [
            "arn:aws:iam::",
            Ref("AWS::AccountId"),
            ":role/", Ref(ServiceRole)
        ]),
    DefaultInstanceProfileArn=Join(
        "",
        [
            "arn:aws:iam::",
            Ref("AWS::AccountId"),
            ":instance-profile/",
            Ref(InstanceRole)
        ]),
    UseCustomCookbooks=True,
    CustomCookbooksSource=Source(
        Type="git",
        Url="git://github.com/amazonwebservices/" +
            "opsworks-example-cookbooks.git",
    ),
))

myLayer = template.add_resource(Layer(
    "myLayer",
    StackId=Ref(myStack),
    Type="php-app",
    Shortname="php-app",
    EnableAutoHealing=True,
    AutoAssignElasticIps=False,
    AutoAssignPublicIps=True,
    Name="MyPHPApp",
    CustomRecipes=Recipes(
        Configure=["phpapp::appsetup"],
    ),
))

DBLayer = template.add_resource(Layer(
    "DBLayer",
    StackId=Ref(myStack),
    Type="db-master",
    Shortname="db-layer",
    EnableAutoHealing=True,
    AutoAssignElasticIps=False,
    AutoAssignPublicIps=True,
    Name="MyMySQL",
    CustomRecipes=Recipes(
        Setup=["phpapp::dbsetup"]
    ),
    Attributes={
        "MysqlRootPassword": Ref(MysqlRootPassword),
        "MysqlRootPasswordUbiquitous": "true",
    },
    VolumeConfigurations=[
        VolumeConfiguration(
            MountPoint="/vol/mysql",
            NumberOfDisks=1,
            Size=10,
        )
    ],
))

ELB = template.add_resource(LoadBalancer(
    "ELB",
    AvailabilityZones=GetAZs(""),
    Listeners=[{
        "LoadBalancerPort": "80",
        "InstancePort": "80",
        "Protocol": "HTTP",
        "InstanceProtocol": "HTTP",
    }],
    HealthCheck=HealthCheck(
        Target="HTTP:80/",
        HealthyThreshold="2",
        UnhealthyThreshold="10",
        Interval="30",
        Timeout="5",
    ),
))

ELBAttachment = template.add_resource(ElasticLoadBalancerAttachment(
    "ELBAttachment",
    ElasticLoadBalancerName=Ref(ELB),
    LayerId=Ref(myLayer),
))

myAppInstance1 = template.add_resource(Instance(
    "myAppInstance1",
    StackId=Ref(myStack),
    LayerIds=[Ref(myLayer)],
    InstanceType="m1.small",
))

myAppInstance2 = template.add_resource(Instance(
    "myAppInstance2",
    StackId=Ref(myStack),
    LayerIds=[Ref(myLayer)],
    InstanceType="m1.small",
))

myDBInstance = template.add_resource(Instance(
    "myDBInstance",
    StackId=Ref(myStack),
    LayerIds=[Ref(DBLayer)],
    InstanceType="m1.small",
))

myApp = template.add_resource(App(
    "myApp",
    StackId=Ref(myStack),
    Type="php",
    Name=Ref(AppName),
    AppSource=Source(
        Type="git",
        Url="git://github.com/amazonwebservices/" +
            "opsworks-demo-php-simple-app.git",
        Revision="version2",
    ),
    Attributes={
        "DocumentRoot": "web",
    },
))

print(template.to_json())
