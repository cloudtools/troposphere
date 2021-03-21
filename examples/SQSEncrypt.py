# Converted from SQS_With_CloudWatch_Alarms.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import GetAtt, Output, Ref, Template
from troposphere.sqs import Queue


t = Template()

t.set_description(
    "AWS CloudFormation Sample Template SQS: Sample template showing how to "
    "create an SQS queue with Server Side Encryption. **WARNING** This "
    "template creates Amazon SQS Queues. You will be billed for the AWS "
    "resources used if you create a stack from this template.")

mysourcequeue = t.add_resource(Queue(
    "MySourceQueue",
    KmsMasterKeyId='testing',
    KmsDataKeyReusePeriodSeconds=60
    )
)

t.add_output([
    Output(
        "SourceQueueURL",
        Description="URL of the source queue",
        Value=Ref(mysourcequeue)
    ),
    Output(
        "SourceQueueARN",
        Description="ARN of the source queue",
        Value=GetAtt(mysourcequeue, "Arn")
    )
])

print(t.to_json())
