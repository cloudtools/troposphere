# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject


class Activity(AWSObject):
    resource_type = "AWS::StepFunctions::Activity"
    props = {
        'Name': (basestring, True),
    }


class StateMachine(AWSObject):
    resource_type = "AWS::StepFunctions::StateMachine"
    props = {
        'StateMachineName': (basestring, False),
        'DefinitionString': (basestring, True),
        'RoleArn': (basestring, True),

    }
