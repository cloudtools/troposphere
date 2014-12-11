# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty, Ref
from .validators import integer, boolean


valid_encodings = ['plain', 'base64']


class Stack(AWSObject):
    type = "AWS::CloudFormation::Stack"

    props = {
        'TemplateURL': (basestring, True),
        'TimeoutInMinutes': (integer, False),
        'Parameters': (dict, False),
    }


class WaitCondition(AWSObject):
    type = "AWS::CloudFormation::WaitCondition"

    props = {
        'Count': (integer, False),
        'Handle': (Ref, True),
        'Timeout': (integer, True),
    }


class WaitConditionHandle(AWSObject):
    type = "AWS::CloudFormation::WaitConditionHandle"

    props = {}


class InitFileContext(AWSHelperFn):
    def __init__(self, data):
        self.data = data

    def JSONrepr(self):
        return self.data


def validate_encoding(encoding):
    if encoding not in valid_encodings:
        raise ValueError('Encoding needs to be one of %r' % valid_encodings)
    return encoding


class InitFile(AWSProperty):
    props = {
        'content': (basestring, False),
        'mode': (basestring, False),
        'owner': (basestring, False),
        'encoding': (validate_encoding, False),
        'group': (basestring, False),
        'source': (basestring, False),
        'authentication': (basestring, False),
        'context': (InitFileContext, False)
    }


class InitFiles(AWSHelperFn):
    def __init__(self, data):
        self.validate(data)
        self.data = data

    def validate(self, data):
        for k in data:
            if not isinstance(data[k], InitFile):
                raise ValueError("File '" + k + "' must be of type InitFile")

    def JSONrepr(self):
        return self.data


class InitService(AWSProperty):
    props = {
        'ensureRunning': (boolean, False),
        'enabled': (boolean, False),
        'files': (list, False),
        'sources': (list, False),
        'commands': (list, False)
    }


class InitServices(AWSHelperFn):
    def __init__(self, data):
        self.validate(data)
        self.data = data

    def validate(self, data):
        for k in data:
            if not isinstance(data[k], InitService):
                raise ValueError(
                    "Service '" + k + "' must be of type InitService"
                )

    def JSONrepr(self):
        return self.data


class InitConfig(AWSProperty):
    props = {
        'groups': (dict, False),
        'users': (dict, False),
        'sources': (dict, False),
        'packages': (dict, False),
        'files': (dict, False),
        'commands': (dict, False),
        'services': (dict, False)
    }


class Init(AWSHelperFn):
    def __init__(self, data):
        self.validate(data)
        self.data = {"AWS::CloudFormation::Init": data}

    def validate(self, data):
        if 'config' not in data:
            raise ValueError('config property is required')
        if not isinstance(data['config'], InitConfig):
            raise ValueError(
                'config property must be of type cloudformation.InitConfig'
            )

    def JSONrepr(self):
        return self.data
