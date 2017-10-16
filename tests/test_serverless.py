import unittest
from troposphere import Tags, Template
from troposphere.serverless import (
    Api, DeadLetterQueue, Function, S3Location, SimpleTable
)


class TestServerless(unittest.TestCase):
    def test_s3_location(self):
        serverless_func = Function(
            "SomeHandler",
            Handler="index.handler",
            Runtime="nodejs",
            CodeUri=S3Location(
                Bucket="mybucket",
                Key="mykey",
            )
        )
        t = Template()
        t.add_resource(serverless_func)
        t.to_json()

    def test_tags(self):
        serverless_func = Function(
            "SomeHandler",
            Handler="index.handler",
            Runtime="nodejs",
            CodeUri="s3://bucket/handler.zip",
            Tags=Tags({
                'Tag1': 'TagValue1',
                'Tag2': 'TagValue2'
            })
        )
        t = Template()
        t.add_resource(serverless_func)
        t.to_json()

    def test_DLQ(self):
        serverless_func = Function(
            "SomeHandler",
            Handler="index.handler",
            Runtime="nodejs",
            CodeUri="s3://bucket/handler.zip",
            DeadLetterQueue=DeadLetterQueue(
                Type='SNS',
                TargetArn='arn:aws:sns:us-east-1:000000000000:SampleTopic'
            )
        )
        t = Template()
        t.add_resource(serverless_func)
        t.to_json()

    def test_required_function(self):
        serverless_func = Function(
            "SomeHandler",
            Handler="index.handler",
            Runtime="nodejs",
            CodeUri="s3://bucket/handler.zip"
        )
        t = Template()
        t.add_resource(serverless_func)
        t.to_json()

    def test_required_api_definitionuri(self):
        serverless_api = Api(
            "SomeApi",
            StageName='test',
            DefinitionUri='s3://bucket/swagger.yml',
        )
        t = Template()
        t.add_resource(serverless_api)
        t.to_json()

    swagger = {
        "swagger": "2.0",
        "info": {
            "title": "swagger test",
        },
        "paths": {
            "/test": {
                "get": {
                 },
            },
        },
    }

    def test_required_api_both(self):
        serverless_api = Api(
            "SomeApi",
            StageName='test',
            DefinitionUri='s3://bucket/swagger.yml',
            DefinitionBody=self.swagger,
        )
        t = Template()
        t.add_resource(serverless_api)
        with self.assertRaises(ValueError):
            t.to_json()

    def test_required_api_definitionbody(self):
        serverless_api = Api(
            "SomeApi",
            StageName='test',
            DefinitionBody=self.swagger,
        )
        t = Template()
        t.add_resource(serverless_api)
        t.to_json()

    def test_simple_table(self):
        serverless_table = SimpleTable(
            "SomeTable"
        )
        t = Template()
        t.add_resource(serverless_table)
        t.to_json()


if __name__ == '__main__':
    unittest.main()
