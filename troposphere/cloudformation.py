# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, Ref
from .validators import integer


class Stack(AWSObject):
    props = {
        'TemplateURL': (basestring, True),
        'TimeoutInMinutes': (integer, False),
        'Parameters': (dict, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::CloudFormation::Stack"
        sup = super(Stack, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class WaitCondition(AWSObject):
    props = {
        'Count': (integer, False),
        'Handle': (Ref, True),
        'Timeout': (integer, True),
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
