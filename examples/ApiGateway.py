from troposphere import Ref, Template, Output
from troposphere.apigateway import RestApi, Method
from troposphere.apigateway import Resource, MethodResponse
from troposphere.apigateway import Integration, IntegrationResponse
from troposphere.apigateway import Deployment, Stage, ApiStage
from troposphere.apigateway import UsagePlan, QuotaSettings, ThrottleSettings
from troposphere.apigateway import ApiKey, StageKey, UsagePlanKey
from troposphere.iam import Role, Policy
from troposphere.awslambda import Function, Code
from troposphere import GetAtt, Join

t = Template()

# Create the Api Gateway
rest_api = t.add_resource(RestApi(
    "ExampleApi",
    Name="ExampleApi"
))

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
    Runtime="nodejs4.3",
))

# Create a resource to map the lambda function to
resource = t.add_resource(Resource(
    "FoobarResource",
    RestApiId=Ref(rest_api),
    PathPart="foobar",
    ParentId=GetAtt("ExampleApi", "RootResourceId"),
))

# Create a Lambda API method for the Lambda resource
method = t.add_resource(Method(
    "LambdaMethod",
    DependsOn='FoobarFunction',
    RestApiId=Ref(rest_api),
    AuthorizationType="NONE",
    ResourceId=Ref(resource),
    HttpMethod="GET",
    Integration=Integration(
        Credentials=GetAtt("LambdaExecutionRole", "Arn"),
        Type="AWS",
        IntegrationHttpMethod='POST',
        IntegrationResponses=[
            IntegrationResponse(
                StatusCode='200'
            )
        ],
        Uri=Join("", [
            "arn:aws:apigateway:eu-west-1:lambda:path/2015-03-31/functions/",
            GetAtt("FoobarFunction", "Arn"),
            "/invocations"
        ])
    ),
    MethodResponses=[
        MethodResponse(
            "CatResponse",
            StatusCode='200'
        )
    ]
))

# Create a deployment
stage_name = 'v1'

deployment = t.add_resource(Deployment(
    "%sDeployment" % stage_name,
    DependsOn="LambdaMethod",
    RestApiId=Ref(rest_api),
))

stage = t.add_resource(Stage(
    '%sStage' % stage_name,
    StageName=stage_name,
    RestApiId=Ref(rest_api),
    DeploymentId=Ref(deployment)
))

key = t.add_resource(ApiKey(
    "ApiKey",
    StageKeys=[StageKey(
        RestApiId=Ref(rest_api),
        StageName=Ref(stage)
    )]
))

# Create an API usage plan
usagePlan = t.add_resource(UsagePlan(
    "ExampleUsagePlan",
    UsagePlanName="ExampleUsagePlan",
    Description="Example usage plan",
    Quota=QuotaSettings(
        Limit=50000,
        Period="MONTH"
    ),
    Throttle=ThrottleSettings(
        BurstLimit=500,
        RateLimit=5000
    ),
    ApiStages=[
        ApiStage(
            ApiId=Ref(rest_api),
            Stage=Ref(stage),
            Throttle=({
                "/some/api/path/GET":
                    ThrottleSettings(
                        BurstLimit=500,
                        RateLimit=5000
                    )
            })
        )
    ]
))

# tie the usage plan and key together
usagePlanKey = t.add_resource(UsagePlanKey(
    "ExampleUsagePlanKey",
    KeyId=Ref(key),
    KeyType="API_KEY",
    UsagePlanId=Ref(usagePlan)
))

# Add the deployment endpoint as an output
t.add_output([
    Output(
        "ApiEndpoint",
        Value=Join("", [
            "https://",
            Ref(rest_api),
            ".execute-api.eu-west-1.amazonaws.com/",
            stage_name
        ]),
        Description="Endpoint for this stage of the api"
    ),
    Output(
        "ApiKey",
        Value=Ref(key),
        Description="API key"
    ),
])

print(t.to_json())
