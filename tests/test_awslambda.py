import unittest
from troposphere import GetAtt, Template, Join, Ref
from troposphere.awslambda import Code, Function, VpcConfig
from troposphere.ec2 import SecurityGroup, Subnet


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

    def test_vpc_config(self):
        security_group = SecurityGroup(
            'LambdaVpcSecurityGroup',
            GroupDescription='Lambda VPC Security Group',
            VpcId='vpc-123456',
        )
        subnet = Subnet(
            'LambdaVpcSubnet',
            CidrBlock='10.0.0.0/24',
            VpcId='vpc-123456',
        )
        lambda_func = Function(
            "LambdaVpcAMIIDLookup",
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
            VpcConfig=VpcConfig(
                SecurityGroupIds=[
                    'sg-123456',
                    Ref(security_group),
                ],
                SubnetIds=[
                    'subnet-123456',
                    Ref(subnet),
                ]
            ),
        )
        t = Template()
        t.add_resource(security_group)
        t.add_resource(subnet)
        t.add_resource(lambda_func)
        t.to_json()

if __name__ == '__main__':
    unittest.main()
