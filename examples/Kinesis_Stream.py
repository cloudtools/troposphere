# This is an example of a Kinesis Stream

import troposphere.kinesis as kinesis
from troposphere import Output, Ref, Template

template = Template()

kinesis_stream = template.add_resource(kinesis.Stream("TestStream", ShardCount=1))

template.add_output(
    [
        Output(
            "StreamName",
            Description="Stream Name (Physical ID)",
            Value=Ref(kinesis_stream),
        ),
    ]
)

print(template.to_json())
