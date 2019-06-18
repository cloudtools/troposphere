# Converted from s3_processor located at:
# https://github.com/awslabs/serverless-application-model/blob/dbc54b5d0cd31bf5cebd16d765b74aee9eb34641/examples/2016-10-31/s3_processor/template.yaml

from troposphere import Template
from troposphere.serverless import Function, DeploymentPreference

t = Template()

t.set_description(
    "A function that uses the configured traffic shifting type "
    "for a canary deployment.")

t.add_transform('AWS::Serverless-2016-10-31')

t.add_resource(
    Function(
        "Function",
        Handler='index.handler',
        Runtime='nodejs6.10',
        CodeUri='s3://<bucket>/function.zip',
        AutoPublishAlias="live",
        DeploymentPreference=DeploymentPreference(
            Enabled=True,
            Type="Canary10Percent5Minutes"
        )
    )
)

print(t.to_json())
