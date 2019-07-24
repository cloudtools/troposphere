from troposphere import Template
from troposphere.events import Rule, Target
from troposphere.awslambda import Function, Code, Permission
from troposphere import GetAtt, Join, Ref


t = Template()


# Create a Lambda function that will be mapped
code = [
    "var response = require('cfn-response');",
    "exports.handler = function(event, context) {",
    "   context.succeed('foobar!');",
    "   return 'foobar!';",
    "};",
]

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
rule = t.add_resource(Rule(
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
))

# Create Lambda Permission
permission = t.add_resource(Permission(
    'FoobarPermission',
    Action='lambda:invokeFunction',
    Principal='events.amazonaws.com',
    FunctionName=Ref(foobar_function),
    SourceArn=GetAtt(rule, 'Arn')
))

print(t.to_json())
