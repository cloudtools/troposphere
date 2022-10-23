import unittest

from troposphere import AWSHelperFn, Parameter, Template
from troposphere.sqs import Queue


class TestServerless(unittest.TestCase):
    def test_transform(self):
        t = Template()
        t.set_version("2010-09-09")
        t.set_transform("AWS::LanguageExtensions")

        self.assertEqual(
            t.to_dict(),
            {
                "AWSTemplateFormatVersion": "2010-09-09",
                "Transform": "AWS::LanguageExtensions",
                "Resources": {},
            },
        )

    def test_length_function(self):
        class Length(AWSHelperFn):
            def __init__(self, data: object) -> None:
                self.data = {"Fn::Length": data}

        t = Template()
        t.set_version("2010-09-09")
        t.set_transform("AWS::LanguageExtensions")

        queue_list = t.add_parameter(Parameter("QueueList", Type="CommaDelimitedList"))
        queue_name = t.add_parameter(
            Parameter(
                "QueueNameParam", Description="Name for your SQS queue", Type="String"
            )
        )

        t.add_resource(
            Queue(
                "Queue",
                QueueName=queue_name.ref(),
                DelaySeconds=Length(queue_list.ref()),
            )
        )

        self.assertEqual(
            t.to_dict(),
            {
                "AWSTemplateFormatVersion": "2010-09-09",
                "Transform": "AWS::LanguageExtensions",
                "Parameters": {
                    "QueueList": {"Type": "CommaDelimitedList"},
                    "QueueNameParam": {
                        "Description": "Name for your SQS queue",
                        "Type": "String",
                    },
                },
                "Resources": {
                    "Queue": {
                        "Type": "AWS::SQS::Queue",
                        "Properties": {
                            "QueueName": {"Ref": "QueueNameParam"},
                            "DelaySeconds": {"Fn::Length": {"Ref": "QueueList"}},
                        },
                    }
                },
            },
        )
