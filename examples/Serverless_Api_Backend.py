# Converted from api_backend located at:
# https://github.com/awslabs/serverless-application-model/blob/dbc54b5d0cd31bf5cebd16d765b74aee9eb34641/examples/2016-10-31/api_backend/template.yaml

from troposphere import Template, Ref
from troposphere.awslambda import Environment
from troposphere.serverless import Function, ApiEvent, SimpleTable

t = Template()

t.set_description(
    "Simple CRUD webservice. State is stored in a SimpleTable (DynamoDB) "
    "resource.")

t.add_transform('AWS::Serverless-2016-10-31')

simple_table = t.add_resource(
    SimpleTable("Table")
)

t.add_resource(
    Function(
        "GetFunction",
        Handler='index.get',
        Runtime='nodejs4.3',
        CodeUri='s3://<bucket>/api_backend.zip',
        Policies='AmazonDynamoDBReadOnlyAccess',
        Environment=Environment(
            Variables={
                'TABLE_NAME': Ref(simple_table)
            }
        ),
        Events={
            'GetResource': ApiEvent(
                'GetResource',
                Path='/resource/{resourceId}',
                Method='get'
            )
        }
    )
)

t.add_resource(
    Function(
        "PutFunction",
        Handler='index.put',
        Runtime='nodejs4.3',
        CodeUri='s3://<bucket>/api_backend.zip',
        Policies='AmazonDynamoDBFullAccess',
        Environment=Environment(
            Variables={
                'TABLE_NAME': Ref(simple_table)
            }
        ),
        Events={
            'PutResource': ApiEvent(
                'PutResource',
                Path='/resource/{resourceId}',
                Method='put'
            )
        }
    )
)

t.add_resource(
    Function(
        "DeleteFunction",
        Handler='index.delete',
        Runtime='nodejs4.3',
        CodeUri='s3://<bucket>/api_backend.zip',
        Policies='AmazonDynamoDBFullAccess',
        Environment=Environment(
            Variables={
                'TABLE_NAME': Ref(simple_table)
            }
        ),
        Events={
            'DeleteResource': ApiEvent(
                'DeleteResource',
                Path='/resource/{resourceId}',
                Method='delete'
            )
        }
    )
)


print(t.to_json())
