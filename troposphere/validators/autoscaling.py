# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from .. import AWSHelperFn, FindInMap, If, Ref, cloudformation
from ..type_defs.compat import Final
from . import boolean, exactly_one, mutually_exclusive

EC2_INSTANCE_LAUNCH: Final = "autoscaling:EC2_INSTANCE_LAUNCH"
EC2_INSTANCE_LAUNCH_ERROR: Final = "autoscaling:EC2_INSTANCE_LAUNCH_ERROR"
EC2_INSTANCE_TERMINATE: Final = "autoscaling:EC2_INSTANCE_TERMINATE"
EC2_INSTANCE_TERMINATE_ERROR: Final = "autoscaling:EC2_INSTANCE_TERMINATE_ERROR"
TEST_NOTIFICATION: Final = "autoscaling:TEST_NOTIFICATION"

# Termination Policy constants
Default: Final = "Default"
OldestInstance: Final = "OldestInstance"
NewestInstance: Final = "NewestInstance"
OldestLaunchConfiguration: Final = "OldestLaunchConfiguration"
OldestLaunchTemplate: Final = "OldestLaunchTemplate"
ClosestToNextInstanceHour: Final = "ClosestToNextInstanceHour"
AllocationStrategy: Final = "AllocationStrategy"


def validate_int_to_str(x):
    """
    Backward compatibility - field was int and now str.
    Property: AutoScalingGroup.MaxSize
    Property: AutoScalingGroup.MinSize
    """

    if isinstance(x, int):
        return str(x)
    if isinstance(x, str):
        return str(int(x))

    raise TypeError(f"Value {x} of type {type(x)} must be either int or str")


class Tag(AWSHelperFn):
    """
    Export:
    """

    def __init__(self, key, value, propogate):
        self.data = {
            "Key": key,
            "Value": value,
            "PropagateAtLaunch": propogate,
        }


class Tags(AWSHelperFn):
    """
    Export:
    """

    defaultPropagateAtLaunch = True
    manyType = [type([]), type(())]

    def __init__(self, **kwargs):
        self.tags = []
        for k, v in sorted(kwargs.items()):
            if type(v) in self.manyType:
                propagate = boolean(v[1])
                v = v[0]
            else:
                propagate = boolean(self.defaultPropagateAtLaunch)
            self.tags.append(
                {
                    "Key": k,
                    "Value": v,
                    "PropagateAtLaunch": propagate,
                }
            )

    # append tags to list
    def __add__(self, newtags):
        newtags.tags = self.tags + newtags.tags
        return newtags

    def to_dict(self):
        return self.tags


def validate_tags_or_list(x):
    """
    Duplicate this since Tags is different from the stock version

    Property: AutoScalingGroup.Tags
    """
    from .. import AWSHelperFn

    if isinstance(x, (AWSHelperFn, Tags, list)):
        return x

    raise ValueError(f"Value {x} of type {type(x)} must be either Tags or list")


class Metadata(AWSHelperFn):
    """
    Export:
    """

    def __init__(self, init, authentication=None):
        self.validate(init, authentication)
        # get keys and values from init and authentication

        # if there's only one data point, then we know its the default
        # cfn-init; where the key is 'config'
        if len(init.data) == 1:
            initKey, initValue = init.data.popitem()
            self.data = {initKey: initValue}
        else:
            self.data = init.data

        if authentication:
            authKey, authValue = authentication.data.popitem()
            self.data[authKey] = authValue

    def validate(self, init, authentication):
        if not isinstance(init, cloudformation.Init):
            raise ValueError("init must be of type cloudformation.Init")

        is_instance = isinstance(authentication, cloudformation.Authentication)
        if authentication and not is_instance:
            raise ValueError(
                "authentication must be of type cloudformation.Authentication"
            )


def validate_launch_template_specification(self):
    """
    Class: LaunchTemplateSpecification
    """
    template_ids = ["LaunchTemplateId", "LaunchTemplateName"]
    exactly_one(self.__class__.__name__, self.properties, template_ids)


def validate_auto_scaling_group(self):
    """
    Class: AutoScalingGroup
    """
    if "UpdatePolicy" in self.resource:
        update_policy = self.resource["UpdatePolicy"]

        if (
            not isinstance(update_policy, AWSHelperFn)
            and "AutoScalingRollingUpdate" in update_policy.properties
        ):
            if not isinstance(update_policy.AutoScalingRollingUpdate, AWSHelperFn):
                rolling_update = update_policy.AutoScalingRollingUpdate

                min_instances = rolling_update.properties.get(
                    "MinInstancesInService", "0"
                )
                is_min_no_check = isinstance(min_instances, (If, FindInMap, Ref))
                is_max_no_check = isinstance(self.MaxSize, (If, FindInMap, Ref))

                if not (is_min_no_check or is_max_no_check):
                    max_count = int(self.MaxSize)
                    min_count = int(min_instances)

                    if min_count >= max_count:
                        raise ValueError(
                            "The UpdatePolicy attribute "
                            "MinInstancesInService must be less than the "
                            "autoscaling group's MaxSize"
                        )

    instance_config_types = [
        "LaunchConfigurationName",
        "LaunchTemplate",
        "InstanceId",
    ]

    mutually_exclusive(self.__class__.__name__, self.properties, instance_config_types)

    availability_zones = self.properties.get("AvailabilityZones")
    vpc_zone_identifier = self.properties.get("VPCZoneIdentifier")
    if not availability_zones and not vpc_zone_identifier:
        raise ValueError(
            "Must specify AvailabilityZones and/or "
            "VPCZoneIdentifier: http://docs.aws.amazon.com/A"
            "WSCloudFormation/latest/TemplateReference/aws-propertie"
            "s-as-group.html#cfn-as-group-vpczoneidentifier"
        )
