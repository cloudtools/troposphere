# Converted from SQS_With_CloudWatch_Alarms.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import GetAtt, Output, Ref, Template
from troposphere.sqs import Queue, RedrivePolicy


t = Template()

t.set_description(
    "AWS CloudFormation Sample Template SQS: Sample template showing how to "
    "create an SQS queue with a dead letter queue. **WARNING** This template "
    "creates Amazon SQS Queues. You will be billed for the AWS resources used "
    "if you create a stack from this template.")

mysourcequeue = t.add_resource(Queue(
    "MySourceQueue",
    RedrivePolicy=RedrivePolicy(
        deadLetterTargetArn=GetAtt("MyDeadLetterQueue", "Arn"),
        maxReceiveCount="5",
    )
))

mydeadletterqueue = t.add_resource(Queue("MyDeadLetterQueue"))

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
    ),
    Output(
        "DeadLetterQueueURL",
        Description="URL of the dead letter queue",
        Value=Ref(mydeadletterqueue)
    ),
    Output(
        "DeadLetterQueueARN",
        Description="ARN of the dead letter queue",
        Value=GetAtt(mydeadletterqueue, "Arn")
    ),
])

print(t.to_json())
