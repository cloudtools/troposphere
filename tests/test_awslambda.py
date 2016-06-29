import unittest
from troposphere import GetAtt, Template, Join
from troposphere.awslambda import Code, Function


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

if __name__ == '__main__':
    unittest.main()
