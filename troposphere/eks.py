# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty


class ResourcesVpcConfig(AWSProperty):
    props = {
        'SecurityGroupIds': ([basestring], False),
        'SubnetIds': ([basestring], True),
    }


class Cluster(AWSObject):
    resource_type = "AWS::EKS::Cluster"

    props = {
        'Name': (basestring, False),
        'ResourcesVpcConfig': (ResourcesVpcConfig, True),
        'RoleArn': (basestring, True),
        'Version': (basestring, False),
    }
