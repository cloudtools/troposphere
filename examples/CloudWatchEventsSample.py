from troposphere import Template
from troposphere.events import Rule, Target
from troposphere.iam import Role, Policy
from troposphere.awslambda import Function, Code
from troposphere import GetAtt, Join


t = Template()


# Create a Lambda function that will be mapped
code = [
    "var response = require('cfn-response');",
    "exports.handler = function(event, context) {",
    "   context.succeed('foobar!');",
    "   return 'foobar!';",
    "};",
]

# Create a role for the lambda function
t.add_resource(Role(
    "LambdaExecutionRole",
    Path="/",
    Policies=[Policy(
        PolicyName="root",
        PolicyDocument={
            "Version": "2012-10-17",
            "Statement": [{
                "Action": ["logs:*"],
                "Resource": "arn:aws:logs:*:*:*",
                "Effect": "Allow"
            }, {
                "Action": ["lambda:*"],
                "Resource": "*",
                "Effect": "Allow"
            }]
        })],
    AssumeRolePolicyDocument={"Version": "2012-10-17", "Statement": [
        {
            "Action": ["sts:AssumeRole"],
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "lambda.amazonaws.com",
                    "apigateway.amazonaws.com"
                ]
            }
        }
    ]},
))

# Create the Lambda function
foobar_function = t.add_resource(Function(
    "FoobarFunction",
    Code=Code(
        ZipFile=Join("", code)
    ),
    Handler="index.handler",
    Role=GetAtt("LambdaExecutionRole", "Arn"),
    Runtime="nodejs",
))

# Create the Event Target
foobar_target = Target(
    "FoobarTarget",
    Arn=GetAtt('FoobarFunction', 'Arn'),
    Id="FooBarFunction1"
)

# Create the Event Rule
rule = Rule(
    "FoobarRule",
    EventPattern={
        "source": [
            "aws.ec2"
        ],
        "detail-type": [
            "EC2 Instance State-change Notification"
        ],
        "detail": {
            "state": [
                "stopping"
            ]
        }
    },
    Description="Foobar CloudWatch Event",
    State="ENABLED",
    Targets=[foobar_target]
)

print(t.to_json())
