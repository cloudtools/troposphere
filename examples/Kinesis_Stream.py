# This is an example of a Kinesis Stream

from troposphere import Output
from troposphere import Ref, Template
import troposphere.kinesis as kinesis


template = Template()

kinesis_stream = template.add_resource(kinesis.Stream(
    "TestStream",
    ShardCount=1
))

template.add_output([
    Output(
        "StreamName",
        Description="Stream Name (Physical ID)",
        Value=Ref(kinesis_stream),
    ),
])

print(template.to_json())
