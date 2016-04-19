from troposphere import Parameter, Ref, Template
from troposphere.apigateway import RestApi, Method, Integration, Deployment, Model, Resource, MethodResponse, IntegrationResponse
from troposphere.iam import Role, Policy
from troposphere.awslambda import Function, Code
from troposphere import FindInMap, GetAtt, Join, Output



t = Template()

# Create the Api Gateway
rest_api = t.add_resource(RestApi(
    "ExampleApi",
    Name="ExampleApi"
    # Body=swagger,
))

schema = """{
    "title": "Example Schema",
    "type": "object",
    "properties": {
        "firstName": {
            "type": "string"
        },
        "lastName": {
            "type": "string"
        },
        "age": {
            "description": "Age in years",
            "type": "integer",
            "minimum": 0
        }
    },
    "required": ["firstName", "lastName"]
}"""

# add a model
model = t.add_resource(Model(
    "CatModel",
    RestApiId=Ref(rest_api),
    ContentType="application/json",
    Schema=Join("", schema.split("\n"))
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
            },{
                "Action": ["lambda:*"],
                "Resource": "*",
                "Effect": "Allow"
            }]
        })],
    AssumeRolePolicyDocument={"Version": "2012-10-17", "Statement": [
        {"Action": ["sts:AssumeRole"], "Effect": "Allow",
         "Principal": {"Service": ["lambda.amazonaws.com", "apigateway.amazonaws.com"]}}]},
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

# create a resource to map the model to
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

print(t.to_json())
