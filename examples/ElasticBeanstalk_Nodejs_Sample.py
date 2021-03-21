# Converted from ElasticBeanstalk_Nodejs.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import (
    GetAtt, Join, Output,
    Parameter, Ref, Template, FindInMap
)

from troposphere.elasticbeanstalk import (
    Application, ApplicationVersion, ConfigurationTemplate, Environment,
    SourceBundle, OptionSettings
)

from troposphere.iam import Role, InstanceProfile
from troposphere.iam import PolicyType as IAMPolicy

from awacs.aws import Allow, Statement, Action, Principal, PolicyDocument
from awacs.sts import AssumeRole


t = Template()

t.add_version()

t.set_description(
    "AWS CloudFormation Sample Template ElasticBeanstalk_Nodejs_Sample: "
    "Configure and launch the AWS Elastic Beanstalk sample application. "
    "**WARNING** This template creates one or more Amazon EC2 instances. You "
    "will be billed for the AWS resources used if you create a stack from "
    "this template.")

keyname = t.add_parameter(Parameter(
    "KeyName",
    Description="Name of an existing EC2 KeyPair to enable SSH access to "
                "the AWS Elastic Beanstalk instance",
    Type="AWS::EC2::KeyPair::KeyName",
    ConstraintDescription="must be the name of an existing EC2 KeyPair."
))

t.add_mapping("Region2Principal", {
    'ap-northeast-1': {
        'EC2Principal': 'ec2.amazonaws.com',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
    'ap-southeast-1': {
        'EC2Principal': 'ec2.amazonaws.com',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
    'ap-southeast-2': {
        'EC2Principal': 'ec2.amazonaws.com',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
    'cn-north-1': {
        'EC2Principal': 'ec2.amazonaws.com.cn',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com.cn'},
    'eu-central-1': {
        'EC2Principal': 'ec2.amazonaws.com',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
    'eu-west-1': {
        'EC2Principal': 'ec2.amazonaws.com',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
    'sa-east-1': {
        'EC2Principal': 'ec2.amazonaws.com',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
    'us-east-1': {
        'EC2Principal': 'ec2.amazonaws.com',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
    'us-west-1': {
        'EC2Principal': 'ec2.amazonaws.com',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com'},
    'us-west-2': {
        'EC2Principal': 'ec2.amazonaws.com',
        'OpsWorksPrincipal': 'opsworks.amazonaws.com'}
    }
)

t.add_resource(Role(
    "WebServerRole",
    AssumeRolePolicyDocument=PolicyDocument(
        Statement=[
            Statement(
                Effect=Allow, Action=[AssumeRole],
                Principal=Principal(
                    "Service", [
                        FindInMap(
                            "Region2Principal",
                            Ref("AWS::Region"), "EC2Principal")
                    ]
                )
            )
        ]
    ),
    Path="/"
))

t.add_resource(IAMPolicy(
    "WebServerRolePolicy",
    PolicyName="WebServerRole",
    PolicyDocument=PolicyDocument(
        Statement=[
            Statement(Effect=Allow, NotAction=Action("iam", "*"),
                      Resource=["*"])
        ]
    ),
    Roles=[Ref("WebServerRole")]
))

t.add_resource(InstanceProfile(
    "WebServerInstanceProfile",
    Path="/",
    Roles=[Ref("WebServerRole")]
))

t.add_resource(Application(
    "SampleApplication",
    Description="AWS Elastic Beanstalk Sample Node.js Application"
))

t.add_resource(ApplicationVersion(
    "SampleApplicationVersion",
    Description="Version 1.0",
    ApplicationName=Ref("SampleApplication"),
    SourceBundle=SourceBundle(
        S3Bucket=Join("-", ["elasticbeanstalk-samples", Ref("AWS::Region")]),
        S3Key="nodejs-sample.zip"
    )
))

t.add_resource(ConfigurationTemplate(
    "SampleConfigurationTemplate",
    ApplicationName=Ref("SampleApplication"),
    Description="SSH access to Node.JS Application",
    SolutionStackName="64bit Amazon Linux 2014.03 v1.0.9 running Node.js",
    OptionSettings=[
        OptionSettings(
            Namespace="aws:autoscaling:launchconfiguration",
            OptionName="EC2KeyName",
            Value=Ref("KeyName")
        ),
        OptionSettings(
            Namespace="aws:autoscaling:launchconfiguration",
            OptionName="IamInstanceProfile",
            Value=Ref("WebServerInstanceProfile")
        )
    ]
))

t.add_resource(Environment(
    "SampleEnvironment",
    Description="AWS Elastic Beanstalk Environment running Sample Node.js "
                "Application",
    ApplicationName=Ref("SampleApplication"),
    TemplateName=Ref("SampleConfigurationTemplate"),
    VersionLabel=Ref("SampleApplicationVersion")
))

t.add_output(
    Output(
        "URL",
        Description="URL of the AWS Elastic Beanstalk Environment",
        Value=Join("", ["http://", GetAtt("SampleEnvironment", "EndpointURL")])
    )
)

print(t.to_json())
