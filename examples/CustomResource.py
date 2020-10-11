from troposphere import Join, Ref, Template
from troposphere.cloudformation import AWSCustomObject


class CustomPlacementGroup(AWSCustomObject):
    resource_type = "Custom::PlacementGroup"

    props = {
        'ServiceToken': (basestring, True),
        'PlacementGroupName': (basestring, True)
    }


t = Template()

t.set_description(
    "Example template showing how a Lambda Function CustomResource might look"
    "For information on AWS Lambda-backed Custom Resources see:"
    "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/"
    "template-custom-resources-lambda.html"
)

placementgroup_a = t.add_resource(CustomPlacementGroup(
    "ClusterGroup",
    ServiceToken=Join("", ["arn:aws:lambda:", Ref("AWS::Region"), ":",
                           Ref("AWS::AccountId"),
                           ":function:cfnPlacementGroup"]),
    PlacementGroupName="ExampleClusterGroup",
))

print(t.to_json())
