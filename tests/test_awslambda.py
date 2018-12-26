import unittest
from troposphere import GetAtt, Template, Join, Ref
from troposphere.awslambda import Code, Function, Environment


class TestAWSLambda(unittest.TestCase):
    def test_exclusive(self):
        lambda_func = Function(
            "AMIIDLookup",
            Handler="index.handler",
            Role=GetAtt("LambdaExecutionRole", "Arn"),
            Code=Code(
                S3Bucket="lambda-functions",
                S3Key="amilookup.zip",
            ),
            Runtime="nodejs",
            Timeout="25",
        )
        t = Template()
        t.add_resource(lambda_func)
        t.to_json()

    def test_zip_file(self):
        lambda_func = Function(
            "AMIIDLookup",
            Handler="index.handler",
            Role=GetAtt("LambdaExecutionRole", "Arn"),
            Code=Code(
                ZipFile=Join("", [
                    "var response = require('cfn-response');",
                    "exports.handler = function(event, context) {",
                    "  var input = parseInt(event.ResourceProperties.Input);",
                    "  var responseData = {Value: input * 5};",
                    "  response.send("
                    "    event, context, response.SUCCESS, responseData"
                    "  );",
                    "};"
                ]),
            ),
            Runtime="nodejs",
            Timeout="25",
        )
        t = Template()
        t.add_resource(lambda_func)
        t.to_json()

    def test_check_zip_file(self):
        positive_tests = [
            'a'*4096,
            Join('', ['a'*4096]),
            Join('', ['a', 10]),
            Join('', ['a'*4096, Ref('EmptyParameter')]),
            Join('ab', ['a'*2047, 'a'*2047]),
            GetAtt('foo', 'bar'),
        ]
        for z in positive_tests:
            Code.check_zip_file(z)
        negative_tests = [
            'a'*4097,
            Join('', ['a'*4097]),
            Join('', ['a'*4097, Ref('EmptyParameter')]),
            Join('abc', ['a'*2047, 'a'*2047]),
        ]
        for z in negative_tests:
            with self.assertRaises(ValueError):
                Code.check_zip_file(z)

    def test_environment_variable_invalid_name(self):
        for var in ['1', '2var', '_var', '/var']:
            with self.assertRaises(ValueError) as context:
                Environment(Variables={var: 'value'})

            self.assertTrue('Invalid environment variable name: %s' % var
                            in context.exception)


if __name__ == '__main__':
    unittest.main()
