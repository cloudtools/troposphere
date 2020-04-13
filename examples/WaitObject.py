# Converted from WaitObject.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import GetAtt, Output, Ref, Template
from troposphere.cloudformation import WaitCondition, WaitConditionHandle


t = Template()

t.set_description(
    "Example template showing how the WaitCondition and WaitConditionHandle "
    "are configured. With this template, the stack will not complete until "
    "either the WaitCondition timeout occurs, or you manually signal the "
    "WaitCondition object using the URL created by the WaitConditionHandle. "
    "You can use CURL or some other equivalent mechanism to signal the "
    "WaitCondition. To find the URL, use cfn-describe-stack-resources or "
    "the AWS Management Console to display the PhysicalResourceId of the "
    "WaitConditionHandle - this is the URL to use to signal. For details of "
    "the signal request see the AWS CloudFormation User Guide at "
    "http://docs.amazonwebservices.com/AWSCloudFormation/latest/UserGuide/"
)

mywaithandle = t.add_resource(WaitConditionHandle("myWaitHandle"))

mywaitcondition = t.add_resource(
    WaitCondition(
        "myWaitCondition",
        Handle=Ref(mywaithandle),
        Timeout="300",
    )
)

t.add_output([
    Output(
        "ApplicationData",
        Value=GetAtt(mywaitcondition, "Data"),
        Description="The data passed back as part of signalling the "
                    "WaitCondition"
    )
])

print(t.to_json())
