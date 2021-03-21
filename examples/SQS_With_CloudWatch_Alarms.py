# Converted from SQS_With_CloudWatch_Alarms.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import GetAtt, Output, Parameter, Ref, Template
from troposphere.cloudwatch import Alarm, MetricDimension
from troposphere.sns import Subscription, Topic
from troposphere.sqs import Queue


t = Template()

t.set_description(
    "AWS CloudFormation Sample Template SQS_With_CloudWatch_Alarms: Sample "
    "template showing how to create an SQS queue with AWS CloudWatch alarms "
    "on queue depth. **WARNING** This template creates an Amazon SQS Queue "
    "and one or more Amazon CloudWatch alarms. You will be billed for the "
    "AWS resources used if you create a stack from this template.")

alarmemail = t.add_parameter(
    Parameter(
        "AlarmEmail",
        Default="nobody@amazon.com",
        Description="Email address to notify if there are any "
                    "operational issues",
        Type="String",
    )
)

myqueue = t.add_resource(Queue("MyQueue"))

alarmtopic = t.add_resource(
    Topic(
        "AlarmTopic",
        Subscription=[
            Subscription(
                Endpoint=Ref(alarmemail),
                Protocol="email"
            ),
        ],
    )
)

queuedepthalarm = t.add_resource(
    Alarm(
        "QueueDepthAlarm",
        AlarmDescription="Alarm if queue depth grows beyond 10 messages",
        Namespace="AWS/SQS",
        MetricName="ApproximateNumberOfMessagesVisible",
        Dimensions=[
            MetricDimension(
                Name="QueueName",
                Value=GetAtt(myqueue, "QueueName")
            ),
        ],
        Statistic="Sum",
        Period="300",
        EvaluationPeriods="1",
        Threshold="10",
        ComparisonOperator="GreaterThanThreshold",
        AlarmActions=[Ref(alarmtopic), ],
        InsufficientDataActions=[Ref(alarmtopic), ],
    )
)

t.add_output([
    Output(
        "QueueURL",
        Description="URL of newly created SQS Queue",
        Value=Ref(myqueue)
    ),
    Output(
        "QueueARN",
        Description="ARN of newly created SQS Queue",
        Value=GetAtt(myqueue, "Arn")
    ),
    Output(
        "QueueName",
        Description="Name newly created SQS Queue",
        Value=GetAtt(myqueue, "QueueName")
    ),
])

print(t.to_json())
