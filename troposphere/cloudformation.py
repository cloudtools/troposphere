# Copyright (c) 2011-2012, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import json
from . import AWSHelperFn, AWSObject, Ref


class Stack(AWSObject):
    props = {
        'TemplateURL': (basestring, True),
        'TimeoutInMinutes': (basestring, False),
        'Parameters': (dict, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::CloudFormation::Stack"
        sup = super(Stack, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class WaitCondition(AWSObject):
    props = {
        'Handle': (Ref, True),
        'Timeout': (basestring, True),
        'Count': (basestring, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::CloudFormation::WaitCondition"
        sup = super(WaitCondition, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class WaitConditionHandle(AWSObject):
    props = {}

    def __init__(self, name, **kwargs):
        self.type = "AWS::CloudFormation::WaitConditionHandle"
        sup = super(WaitConditionHandle, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)
