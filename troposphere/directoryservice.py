# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean


class VpcSettings(AWSProperty):
    props = {
        'SubnetIds': ([basestring], True),
        'VpcId': (basestring, True),
    }


class MicrosoftAD(AWSObject):
    resource_type = "AWS::DirectoryService::MicrosoftAD"

    props = {
        'CreateAlias': (boolean, False),
        'EnableSso': (boolean, False),
        'Name': (basestring, True),
        'Password': (basestring, True),
        'ShortName': (basestring, False),
        'VpcSettings': (VpcSettings, True)
    }


class SimpleAD(AWSObject):
    resource_type = "AWS::DirectoryService::SimpleAD"

    props = {
        'CreateAlias': (boolean, False),
        'Description': (basestring, False),
        'EnableSso': (boolean, False),
        'Name': (basestring, True),
        'Password': (basestring, True),
        'ShortName': (basestring, False),
        'Size': (basestring, True),
        'VpcSettings': (VpcSettings, True),
    }
