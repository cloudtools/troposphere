# Converted from ElasticBeanstalk_Python_Sample.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import GetAtt, Join, Output
from troposphere import Parameter, Ref, Template
from troposphere.elasticbeanstalk import Application, Environment
from troposphere.elasticbeanstalk import ApplicationVersion, OptionSettings
from troposphere.elasticbeanstalk import SourceBundle


t = Template()

t.add_description(
    "AWS CloudFormation Sample Template ElasticBeanstalk_Python_Sample: "
    "Configure and launch the AWS Elastic Beanstalk Python sample "
    "application. **WARNING** This template creates one or more Amazon EC2 "
    "instances. You will be billed for the AWS resources used if you create "
    "a stack from this template.")

keyname = t.add_parameter(Parameter(
    "KeyName",
    Description="Name of an existing EC2 KeyPair to enable SSH access "
                "to the AWS Elastic Beanstalk instance",
    Type="String",
))

sampleApp = t.add_resource(Application(
    "sampleApplication",
    Description="AWS Elastic Beanstalk Python Sample Application",
    ApplicationVersions=[
        ApplicationVersion(
            VersionLabel="Initial Version",
            Description="Version 1.0",
            SourceBundle=SourceBundle(
                S3Bucket=Join(
                    '-', ["elasticbeanstalk-samples", Ref("AWS::Region")]),
                S3Key="python-sample.zip"
            )
        )
    ]
))

sampleEnv = t.add_resource(Environment(
    "sampleEnvironment",
    ApplicationName=Ref(sampleApp),
    Description=
    "AWS Elastic Beanstalk Environment running Python Sample Application",
    SolutionStackName="64bit Amazon Linux running Python",
    OptionSettings=[
        OptionSettings(
            Namespace="aws:autoscaling:launchconfiguration",
            OptionName="EC2KeyName",
            Value=Ref(keyname),
        ),
    ],
    VersionLabel="Initial Version",
))

t.add_output([
    Output(
        "URL",
        Description="URL of the AWS Elastic Beanstalk Environment",
        Value=Join("", ["http://", GetAtt(sampleEnv, "EndpointURL")]),
    )
])

print(t.to_json())
