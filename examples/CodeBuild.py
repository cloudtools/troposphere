from troposphere import Template
from troposphere.codebuild import Artifacts, Environment, Source, Project


template = Template()
template.add_version('2010-09-09')

artifacts = Artifacts(Type='NO_ARTIFACTS')

environment = Environment(
    ComputeType='BUILD_GENERAL1_SMALL',
    Image='aws/codebuild/java:openjdk-8',
    Type='LINUX_CONTAINER',
    EnvironmentVariables=[{'Name': 'APP_NAME', 'Value': 'demo'}],
)

source = Source(
    Location='codebuild-demo-test/0123ab9a371ebf0187b0fe5614fbb72c',
    Type='S3'
)

project = Project(
    "DemoProject",
    Artifacts=artifacts,
    Environment=environment,
    Name='DemoProject',
    ServiceRole='arn:aws:iam::0123456789:role/codebuild-role',
    Source=source,
)
template.add_resource(project)

print(template.to_json())
