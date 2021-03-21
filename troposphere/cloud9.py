# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import integer


class Repository(AWSProperty):
    props = {
        'PathComponent': (str, True),
        'RepositoryUrl': (str, True),
    }


class EnvironmentEC2(AWSObject):
    resource_type = "AWS::Cloud9::EnvironmentEC2"

    props = {
        'AutomaticStopTimeMinutes': (integer, False),
        'Description': (str, False),
        'InstanceType': (str, True),
        'Name': (str, False),
        'OwnerArn': (str, False),
        'Repositories': ([Repository], False),
        'SubnetId': (str, False),
    }
