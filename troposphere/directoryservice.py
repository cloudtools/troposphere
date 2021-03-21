# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean


class VpcSettings(AWSProperty):
    props = {
        'SubnetIds': ([str], True),
        'VpcId': (str, True),
    }


class MicrosoftAD(AWSObject):
    resource_type = "AWS::DirectoryService::MicrosoftAD"

    props = {
        'CreateAlias': (boolean, False),
        'Edition': (str, False),
        'EnableSso': (boolean, False),
        'Name': (str, True),
        'Password': (str, True),
        'ShortName': (str, False),
        'VpcSettings': (VpcSettings, True)
    }


class SimpleAD(AWSObject):
    resource_type = "AWS::DirectoryService::SimpleAD"

    props = {
        'CreateAlias': (boolean, False),
        'Description': (str, False),
        'EnableSso': (boolean, False),
        'Name': (str, True),
        'Password': (str, True),
        'ShortName': (str, False),
        'Size': (str, True),
        'VpcSettings': (VpcSettings, True),
    }
