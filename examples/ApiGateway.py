from troposphere import Parameter, Ref, Template
from troposphere.apigateway import RestApi, Method, Integration, Deployment, Model, Resource, MethodResponse
from troposphere.iam import Role, Policy
from troposphere.awslambda import Function, Code
from troposphere import FindInMap, GetAtt, Join, Output



t = Template()

swagger = """{
  "swagger": "2.0",
  "info": {
    "version": "1.0.0",
    "title": "Troposphere Example",
    "description": "A sample API",
    "termsOfService": "http://example.com/",
    "contact": {
      "name": "Troposphere Team"
    },
    "license": {
      "name": "MIT"
    }
  },
  "host": "foobar.example.com",
  "basePath": "/api",
  "schemes": [
    "http"
  ],
  "consumes": [
    "application/json"
  ],
  "produces": [
    "application/json"
  ],
  "paths": {
    "/armadillos": {
      "get": {
        "description": "Returns all armadillos from the system that the user has access to",
        "produces": [
          "application/json"
        ],
        "responses": {
          "200": {
            "description": "A list of armadillos.",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Armadillo"
              }
            }
          }
        }
      }
    }
  },
  "definitions": {
    "Armadillo": {
      "type": "object",
      "required": [
        "id",
        "name"
      ],
      "properties": {
        "id": {
          "type": "integer",
          "format": "int64"
        },
        "name": {
          "type": "string"
        },
        "tag": {
          "type": "string"
        }
      }
    }
  }
}"""

# Create the Api Gateway
rest_api = t.add_resource(RestApi(
    "ExampleApi",
    Body=swagger,
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

# create a resource to map the model to
resource = t.add_resource(Resource(
    "ExampleResource",
    RestApiId=Ref(rest_api),
    PathPart="cats"
))

# Create a mock API method for the Cat resource
method = t.add_resource(Method(
    "CatMethod",
    DependsOn='ExampleResource',
    ApiKeyRequired=False,
    RestApiId=Ref(rest_api),
    HttpMethod="GET",
    Integration=Integration(Type="MOCK"),
    ResourceId=Ref(resource),
    MethodResponses=[
        MethodResponse(
            "CatResponse",
            ResponseModels={
                "application/json": Ref(model)
            }
        )
    ]
))

# Create a Lambda function that will be mapped
code = [
    "var response = require('cfn-response');",
    "exports.handler = function(event, context) {",
    "   return 'foobar!';",
    "};",
]

# create a role for the lambda function
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
            }]
        })],
    AssumeRolePolicyDocument={"Version": "2012-10-17", "Statement": [
        {"Action": ["sts:AssumeRole"], "Effect": "Allow",
         "Principal": {"Service": ["lambda.amazonaws.com"]}}]},
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

# Create an API method for the lambda function
# method = t.add_resource(Method(
#     "FoobarMethod",
#     RestApiId=Ref(rest_api),
#     HttpMethod="GET",
#     Integration=Integration(
#         Type="LAMBDA",
#         Uri=Ref(foobar_function)
#     )
# ))
#
# deployment = t.add_resource(Deployment(
#     "TestDeployment",
#     RestApiId=Ref(rest_api),
#     StageName="Test"
# ))


print(t.to_json())
