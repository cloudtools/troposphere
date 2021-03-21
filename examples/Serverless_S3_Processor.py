# Converted from s3_processor located at:
# https://github.com/awslabs/serverless-application-model/blob/dbc54b5d0cd31bf5cebd16d765b74aee9eb34641/examples/2016-10-31/s3_processor/template.yaml

from troposphere import Template, Ref
from troposphere.s3 import Bucket
from troposphere.serverless import Function, S3Event

t = Template()

t.set_description(
    "A function is triggered off an upload to a bucket. It logs the content "
    "type of the uploaded object.")

t.add_transform('AWS::Serverless-2016-10-31')


s3_bucket = t.add_resource(
    Bucket("Bucket")
)

t.add_resource(
    Function(
        "ProcessorFunction",
        Handler='index.handler',
        Runtime='nodejs4.3',
        CodeUri='s3://<bucket>/s3_processor.zip',
        Policies='AmazonS3ReadOnlyAccess',
        Events={
            'PhotoUpload': S3Event(
                'PhotoUpload',
                Bucket=Ref(s3_bucket),
                Events=['s3:ObjectCreated:*']
            )
        }
    )
)

print(t.to_json())
