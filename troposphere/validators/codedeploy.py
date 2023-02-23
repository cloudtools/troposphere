# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from ..type_defs.compat import Final
from . import exactly_one, mutually_exclusive

KEY_ONLY: Final = "KEY_ONLY"
VALUE_ONLY: Final = "VALUE_ONLY"
KEY_AND_VALUE: Final = "KEY_AND_VALUE"


def deployment_option_validator(x):
    """
    Property: DeploymentStyle.DeploymentOption
    """
    valid_values = ["WITH_TRAFFIC_CONTROL", "WITHOUT_TRAFFIC_CONTROL"]
    if x not in valid_values:
        raise ValueError(
            "Deployment Option value must be one of: %s" % ", ".join(valid_values)
        )
    return x


def deployment_type_validator(x):
    """
    Property: DeploymentStyle.DeploymentType
    """
    valid_values = ["IN_PLACE", "BLUE_GREEN"]
    if x not in valid_values:
        raise ValueError(
            "Deployment Type value must be one of: %s" % ", ".join(valid_values)
        )
    return x


def validate_load_balancer_info(self):
    """
    Class: LoadBalancerInfo
    """
    conds = ["ElbInfoList", "TargetGroupInfoList", "TargetGroupPairInfoList"]
    exactly_one(self.__class__.__name__, self.properties, conds)


def validate_deployment_group(self):
    """
    Class: DeploymentGroup
    """
    ec2_conds = ["EC2TagFilters", "Ec2TagSet"]
    onPremises_conds = ["OnPremisesInstanceTagFilters", "OnPremisesTagSet"]
    mutually_exclusive(self.__class__.__name__, self.properties, ec2_conds)
    mutually_exclusive(self.__class__.__name__, self.properties, onPremises_conds)
