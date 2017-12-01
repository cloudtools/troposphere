# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import integer


class Repository(AWSProperty):
    props = {
        'PathComponent': (basestring, True),
        'RepositoryUrl': (basestring, True),
    }


class EnvironmentEC2(AWSObject):
    resource_type = "AWS::Cloud9::EnvironmentEC2"

    props = {
        'AutomaticStopTimeMinutes': (integer, False),
        'Description': (basestring, False),
        'InstanceType': (basestring, True),
        'Name': (basestring, False),
        'OwnerArn': (basestring, False),
        'Repositories': ([Repository], False),
        'SubnetId': (basestring, False),
    }
