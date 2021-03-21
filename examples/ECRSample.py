from troposphere import Template
from troposphere.ecr import Repository
from awacs.aws import Allow, PolicyDocument, AWSPrincipal, Statement
import awacs.ecr as ecr
import awacs.iam as iam


t = Template()

t.add_resource(
    Repository(
        'MyRepository',
        RepositoryName='test-repository',
        RepositoryPolicyText=PolicyDocument(
            Version='2008-10-17',
            Statement=[
                Statement(
                    Sid='AllowPushPull',
                    Effect=Allow,
                    Principal=AWSPrincipal([
                        iam.ARN(account='123456789012', resource='user/Bob'),
                        iam.ARN(account='123456789012', resource='user/Alice'),
                    ]),
                    Action=[
                        ecr.GetDownloadUrlForLayer,
                        ecr.BatchGetImage,
                        ecr.BatchCheckLayerAvailability,
                        ecr.PutImage,
                        ecr.InitiateLayerUpload,
                        ecr.UploadLayerPart,
                        ecr.CompleteLayerUpload,
                    ],
                ),
            ]
        ),
    )
)

print(t.to_json())
