# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .. import AWSHelperFn, AWSProperty
from ..type_defs.compat import Final
from . import defer, double, integer, positive_integer

CHANGE_IN_CAPACITY: Final[str] = "CHANGE_IN_CAPACITY"
PERCENT_CHANGE_IN_CAPACITY: Final[str] = "PERCENT_CHANGE_IN_CAPACITY"
EXACT_CAPACITY: Final[str] = "EXACT_CAPACITY"


class KeyValueClass(AWSProperty):
    """
    Backward compatibility class
    """

    props = {"Key": (str, True), "Value": (str, True)}

    def __init__(self, key=None, value=None, **kwargs):
        # provided for backward compatibility
        if key is not None:
            kwargs["Key"] = key
        if value is not None:
            kwargs["Value"] = value
        super().__init__(**kwargs)


KeyValue = KeyValueClass
MetricDimension = KeyValueClass


def validate_defer(x):
    """
    Property: SimpleScalingPolicyConfiguration.ScalingAdjustment
    """
    return defer(x)


def validate_configurations(configurations):
    """
    Property: Configuration.Configurations
    """
    from ..emr import Configuration

    if not isinstance(configurations, list):
        raise TypeError("Configurations is not a list")

    for config in configurations:
        if not isinstance(config, (Configuration, dict)):
            raise TypeError(
                f"Configurations must be a list of {dict} or {Configuration}, found {config}"
            )
    return configurations


def validate_action_on_failure(action_on_failure):
    """
    Validate action on failure for EMR StepConfig
    """

    ACTIONS_ON_FAILURE = (
        "TERMINATE_CLUSTER",
        "CANCEL_AND_WAIT",
        "CONTINUE",
        "TERMINATE_JOB_FLOW",
    )
    if action_on_failure not in ACTIONS_ON_FAILURE:
        raise ValueError(
            "StepConfig ActionOnFailure  must be one of: %s"
            % ", ".join(ACTIONS_ON_FAILURE)
        )
    return action_on_failure


def additional_info_validator(xs):
    """
    Property: Application.AdditionalInfo
    """
    if not isinstance(xs, dict):
        raise ValueError("AdditionalInfo must be a dict of " "string to string pairs")
    for k, v in xs.items():
        if not isinstance(k, str):
            raise ValueError("AdditionalInfo keys must be strings")
        if not isinstance(v, str):
            raise ValueError("AdditionalInfo values must be strings")

    return xs


def properties_validator(xs):
    """
    Property: Configuration.ConfigurationProperties
    """
    if not isinstance(xs, dict):
        raise ValueError(
            "ConfigurationProperties must be a dict of " "string to string pairs"
        )
    for k, v in xs.items():
        if not isinstance(k, str):
            raise ValueError("ConfigurationProperties keys must be strings")
        if not isinstance(v, str) and not isinstance(v, AWSHelperFn):
            raise ValueError(
                "ConfigurationProperties values must be strings" " or helper functions"
            )

    return xs


def market_validator(x):
    """
    Property: InstanceGroupConfigProperty.Market
    Property: InstanceGroupConfig.Market
    Property: ScalingAction.Market
    """
    valid_values = ["ON_DEMAND", "SPOT"]
    if x not in valid_values:
        raise ValueError("Market must be one of: %s" % ", ".join(valid_values))
    return x


def volume_type_validator(x):
    """
    Property: VolumeSpecification.VolumeType
    """
    valid_values = ["gp2", "gp3", "io1", "sc1", "st1", "standard"]
    if x not in valid_values:
        raise ValueError("VolumeType must be one of: %s" % ", ".join(valid_values))
    return x


def validate_simple_scaling_policy_configuration(self):
    """
    Class: SimpleScalingPolicyConfiguration
    """

    if "AdjustmentType" in self.properties and "ScalingAdjustment" in self.properties:
        valid_values = [
            CHANGE_IN_CAPACITY,
            PERCENT_CHANGE_IN_CAPACITY,
            EXACT_CAPACITY,
        ]

        adjustment_type = self.properties.get("AdjustmentType", None)
        scaling_adjustment = self.properties.get("ScalingAdjustment", None)

        if adjustment_type not in valid_values:
            raise ValueError(
                "Only CHANGE_IN_CAPACITY, PERCENT_CHANGE_IN_CAPACITY, or"
                " EXACT_CAPACITY are valid AdjustmentTypes"
            )

        if adjustment_type == CHANGE_IN_CAPACITY:
            integer(scaling_adjustment)
        elif adjustment_type == PERCENT_CHANGE_IN_CAPACITY:
            double(scaling_adjustment)
            f = float(scaling_adjustment)
            if f < 0.0 or f > 1.0:
                raise ValueError(
                    "ScalingAdjustment value must be between 0.0 and 1.0"
                    " value was %0.2f" % f
                )
        elif adjustment_type == EXACT_CAPACITY:
            positive_integer(scaling_adjustment)
        else:
            raise ValueError("ScalingAdjustment value must be" " an integer or a float")


def validate_on_demand_provisioning_specification(self):
    """
    Class: OnDemandProvisioningSpecification
    """
    valid_values = ["lowest-price"]

    allocation_strategy = self.properties.get("AllocationStrategy", None)

    if allocation_strategy not in valid_values:
        raise ValueError(
            "AllocationStrategy %s is not valid. Valid options are %s"
            % (allocation_strategy, ", ".join(valid_values))
        )


def validate_spot_provisioning_specification(self):
    """
    Class: SpotProvisioningSpecification
    """
    if "AllocationStrategy" in self.properties:
        valid_values = ["capacity-optimized"]

        allocation_strategy = self.properties.get("AllocationStrategy", None)

        if allocation_strategy not in valid_values:
            raise ValueError(
                "AllocationStrategy %s is not valid. Valid options are %s"
                % (allocation_strategy, ", ".join(valid_values))
            )


def action_on_failure_validator(x):
    """
    Property: Step.ActionOnFailure
    """
    valid_values = ["CONTINUE", "CANCEL_AND_WAIT"]
    if x not in valid_values:
        raise ValueError("ActionOnFailure must be one of: %s" % ", ".join(valid_values))
    return x
