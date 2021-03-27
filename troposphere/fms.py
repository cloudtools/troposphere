# Copyright (c) 2012-2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import AWSObject, AWSProperty, Tags
from .validators import boolean, json_checker


class IEMap(AWSProperty):
    props = {
        "ACCOUNT": ([str], False),
        "ORGUNIT": ([str], False),
    }


class Policy(AWSObject):
    resource_type = "AWS::FMS::Policy"

    props = {
        "DeleteAllPolicyResources": (boolean, False),
        "ExcludeMap": (IEMap, False),
        "ExcludeResourceTags": (boolean, True),
        "IncludeMap": (IEMap, False),
        "PolicyName": (str, True),
        "RemediationEnabled": (boolean, True),
        "ResourceTags": (Tags, False),
        "ResourceType": (str, True),
        "ResourceTypeList": ([str], True),
        "SecurityServicePolicyData": (json_checker, True),
        "Tags": (Tags, False),
    }


class NotificationChannel(AWSObject):
    resource_type = "AWS::FMS::NotificationChannel"

    props = {
        "SnsRoleName": (str, True),
        "SnsTopicArn": (str, True),
    }
