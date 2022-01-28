# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from .. import AWSHelperFn, AWSProperty, BaseAWSObject, encode_to_dict
from . import boolean, check_required, encoding


def validate_int_to_str(x):
    """
    Backward compatibility - field was int and now str.
    Property: WaitCondition.Timeout
    """

    if isinstance(x, int):
        return str(x)
    if isinstance(x, str):
        return str(int(x))

    raise TypeError(f"Value {x} of type {type(x)} must be either int or str")


class AWSCustomObject(BaseAWSObject):
    """
    Export:
    """

    dictname = "Properties"


def validate_wait_condition(self):
    """
    Class: WaitCondition
    """
    if "CreationPolicy" in self.resource:
        for k in self.props.keys():
            if k in self.properties:
                raise ValueError(
                    "Property %s cannot be specified with CreationPolicy" % k
                )
    else:
        required = ["Handle", "Timeout"]
        check_required(self.__class__.__name__, self.properties, required)


class Metadata(AWSHelperFn):
    """
    Export:
    """

    def __init__(self, *args):
        self.data = args

    def to_dict(self):
        t = []
        for i in self.data:
            t += list(encode_to_dict(i).items())
        return dict(t)


class InitFileContext(AWSHelperFn):
    """
    Export:
    """

    def __init__(self, data):
        self.data = data


class InitFile(AWSProperty):
    """
    Export:
    """

    props = {
        "content": (str, False),
        "mode": (str, False),
        "owner": (str, False),
        "encoding": (encoding, False),
        "group": (str, False),
        "source": (str, False),
        "authentication": (str, False),
        "context": (InitFileContext, False),
    }


class InitFiles(AWSHelperFn):
    """
    Export:
    """

    def __init__(self, data):
        self.validate(data)
        self.data = data

    def validate(self, data):
        for k in data:
            if not isinstance(data[k], InitFile):
                raise ValueError("File '" + k + "' must be of type InitFile")


class InitService(AWSProperty):
    """
    Export:
    """

    props = {
        "ensureRunning": (boolean, False),
        "enabled": (boolean, False),
        "files": (list, False),
        "packages": (dict, False),
        "sources": (list, False),
        "commands": (list, False),
    }


class InitServices(AWSHelperFn):
    """
    Export:
    """

    def __init__(self, data):
        self.validate(data)
        self.data = data

    def validate(self, data):
        for k in data:
            if not isinstance(data[k], InitService):
                raise ValueError("Service '" + k + "' must be of type InitService")


class InitConfigSets(AWSHelperFn):
    """
    Export:
    """

    def __init__(self, **kwargs):
        self.validate(dict(kwargs))
        self.data = kwargs

    def validate(self, config_sets):
        for k, v in config_sets.items():
            if not isinstance(v, list):
                raise ValueError("configSets values must be of type list")


class InitConfig(AWSProperty):
    """
    Export:
    """

    props = {
        "groups": (dict, False),
        "users": (dict, False),
        "sources": (dict, False),
        "packages": (dict, False),
        "files": (dict, False),
        "commands": (dict, False),
        "services": (dict, False),
    }


def validate_authentication_type(auth_type):
    valid_types = ["S3", "basic"]
    if auth_type not in valid_types:
        raise ValueError("Type needs to be one of %r" % valid_types)
    return auth_type


class AuthenticationBlock(AWSProperty):
    """
    Export:
    """

    props = {
        "accessKeyId": (str, False),
        "buckets": ([str], False),
        "password": (str, False),
        "secretKey": (str, False),
        "type": (validate_authentication_type, False),
        "uris": ([str], False),
        "username": (str, False),
        "roleName": (str, False),
    }


class Authentication(AWSHelperFn):
    """
    Export:
    """

    def __init__(self, data):
        self.validate(data)
        self.data = {"AWS::CloudFormation::Authentication": data}

    def validate(self, data):
        for k, v in data.items():
            if not isinstance(v, AuthenticationBlock):
                raise ValueError(
                    "authentication block must be of type"
                    " cloudformation.AuthenticationBlock"
                )


class Init(AWSHelperFn):
    """
    Export:
    """

    def __init__(self, data, **kwargs):
        self.validate(data, dict(kwargs))

        if isinstance(data, InitConfigSets):
            self.data = {
                "AWS::CloudFormation::Init": dict({"configSets": data}, **kwargs)
            }
        else:
            self.data = {"AWS::CloudFormation::Init": data}

    def validate(self, data, config_sets):
        if isinstance(data, InitConfigSets):
            for k, v in sorted(config_sets.items()):
                if not isinstance(v, InitConfig):
                    raise ValueError(
                        "init configs must of type ", "cloudformation.InitConfigSet"
                    )
        else:
            if "config" not in data:
                raise ValueError("config property is required")
            if not isinstance(data["config"], InitConfig):
                raise ValueError(
                    "config property must be of type cloudformation.InitConfig"
                )
