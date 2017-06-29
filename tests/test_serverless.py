import unittest
from troposphere import Template
from troposphere.serverless import Function, Api, SimpleTable


class TestServerless(unittest.TestCase):
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

    def test_required_api(self):
        serverless_api = Api(
            "SomeApi",
            StageName='test',
            DefinitionUri='s3://bucket/swagger.yml',
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
