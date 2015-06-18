import unittest
from troposphere import GetAtt, Template
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

if __name__ == '__main__':
    unittest.main()
