# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty


class VpcSettings(AWSProperty):
    props = {
        'SubnetIds': ([basestring], True),
        'VpcId': (basestring, True),
    }


class SimpleAD(AWSObject):
    resource_type = "AWS::DirectoryService::SimpleAD"

    props = {
        'CreateAlias': (bool, False),
        'Description': (basestring, False),
        'EnableSso': (bool, False),
        'Name': (basestring, True),
        'Password': (basestring, True),
        'ShortName': (basestring, False),
        'Size': (basestring, True),
        'VpcSettings': (VpcSettings, True),
    }
