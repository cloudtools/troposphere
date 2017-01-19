# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty


class Target(AWSProperty):
    props = {
        'Arn': (basestring, True),
        'Id': (basestring, True),
        'Input': (basestring, False),
        'InputPath': (basestring, False)

    }


class Rule(AWSObject):
    resource_type = "AWS::Events::Rule"

    props = {

        'Description': (basestring, False),
        'EventPattern': (dict, False),
        'Name': (basestring, False),
        'RoleArn': (basestring, False),
        'ScheduleExpression': (basestring, False),
        'State': (basestring, False),
        'Targets': ([Target], False)

    }
