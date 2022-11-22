# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
from typing import List

from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer

class ConfigParameter(AWSProperty):
    """
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-configparameter.html
    """
    props: PropsDictType = {
        "ParameterKey": (str, False),
        "ParameterValue": (str, False),
    }


class Namespace(AWSObject):
    """
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html
    """
    resource_type = "AWS::RedshiftServerless::Namespace"
    props: PropsDictType = {
        "AdminUsername": (str, False),
        "AdminUserPassword": (str, False),
        "DbName": (str, False),
        "DefaultIamRoleArn": (str, False),
        "FinalSnapshotName": (str, False),
        "FinalSnapshotRetentionPeriod": (integer, False),
        "IamRoles": ([str], False),
        "KmsKeyId": (str, False),
        "LogExports": ([str], False),
        "NamespaceName": (str, True),
        "Tags": ([Tags], False),
    }


class Workgroup(AWSObject):
    """
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html
    """
    resource_type = "AWS::RedshiftServerless::Workgroup"
    props: PropsDictType = {
        "BaseCapacity": (integer, False),
        "ConfigParameters": ([ConfigParameter], False),
        "EnhancedVpcRouting": (boolean, False),
        "NamespaceName": (str, False),
        "PubliclyAccessible": (boolean, False),
        "SecurityGroupIds": ([str], False),
        "SubnetIds": ([str], False),
        "Tags": ([Tags], False),
        "WorkgroupName": (str, True),
    }
