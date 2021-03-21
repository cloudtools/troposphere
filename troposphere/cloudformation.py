# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty, BaseAWSObject, Tags
from . import encode_to_dict
from .validators import boolean, check_required, encoding, integer


class ModuleDefaultVersion(AWSObject):
    resource_type = "AWS::CloudFormation::ModuleDefaultVersion"

    props = {
        'Arn': (str, False),
        'ModuleName': (str, False),
        'VersionId': (str, False),
    }


class ModuleVersion(AWSObject):
    resource_type = "AWS::CloudFormation::ModuleVersion"

    props = {
        'ModuleName': (str, True),
        'ModulePackage': (str, True),
    }


class ResourceDefaultVersion(AWSObject):
    resource_type = "AWS::CloudFormation::ResourceDefaultVersion"

    props = {
        'TypeName': (str, False),
        'TypeVersionArn': (str, False),
        'VersionId': (str, False),
    }


class LoggingConfig(AWSProperty):
    props = {
        'LogGroupName': (str, False),
        'LogRoleArn': (str, False),
    }


class ResourceVersion(AWSObject):
    resource_type = "AWS::CloudFormation::ResourceVersion"

    props = {
        'ExecutionRoleArn': (str, False),
        'LoggingConfig': (LoggingConfig, False),
        'SchemaHandlerPackage': (str, True),
        'TypeName': (str, True),
    }


class Stack(AWSObject):
    resource_type = "AWS::CloudFormation::Stack"

    props = {
        'NotificationARNs': ([str], False),
        'Parameters': (dict, False),
        'Tags': ((Tags, list), False),
        'TemplateURL': (str, True),
        'TimeoutInMinutes': (integer, False),
    }


class AWSCustomObject(BaseAWSObject):
    dictname = 'Properties'


class CustomResource(AWSCustomObject):
    resource_type = "AWS::CloudFormation::CustomResource"

    props = {
        'ServiceToken': (str, True)
    }


class AutoDeployment(AWSProperty):
    props = {
        'Enabled': (boolean, False),
        'RetainStacksOnAccountRemoval': (boolean, False),
    }


class OperationPreferences(AWSProperty):
    props = {
        'FailureToleranceCount': (integer, False),
        'FailureTolerancePercentage': (integer, False),
        'MaxConcurrentCount': (integer, False),
        'MaxConcurrentPercentage': (integer, False),
        'RegionOrder': ([str], False),
    }


class Parameter(AWSProperty):
    props = {
        'ParameterKey': (str, True),
        'ParameterValue': (str, True),
    }


class DeploymentTargets(AWSProperty):
    props = {
        'Accounts': ([str], False),
        'OrganizationalUnitIds': ([str], False),
    }


class StackInstances(AWSProperty):
    props = {
        'DeploymentTargets': (DeploymentTargets, True),
        'ParameterOverrides': ([Parameter], False),
        'Regions': ([str], True),
    }


class StackSet(AWSObject):
    resource_type = "AWS::CloudFormation::StackSet"

    props = {
        'AdministrationRoleARN': (str, False),
        'AutoDeployment': (AutoDeployment, False),
        'Capabilities': ([str], False),
        'Description': (str, False),
        'ExecutionRoleName': (str, False),
        'OperationPreferences': (OperationPreferences, False),
        'Parameters': ([Parameter], False),
        'PermissionModel': (str, False),
        'StackInstancesGroup': ([StackInstances], False),
        'StackSetName': (str, False),
        'Tags': (Tags, False),
        'TemplateBody': (str, False),
        'TemplateURL': (str, False),
    }


class WaitCondition(AWSObject):
    resource_type = "AWS::CloudFormation::WaitCondition"

    props = {
        'Count': (integer, False),
        'Handle': (str, False),
        'Timeout': (integer, False),
    }

    def validate(self):
        if 'CreationPolicy' in self.resource:
            for k in list(self.props.keys()):
                if k in self.properties:
                    raise ValueError(
                        "Property %s cannot be specified with CreationPolicy" %
                        k
                    )
        else:
            required = ['Handle', 'Timeout']
            check_required(self.__class__.__name__, self.properties, required)


class WaitConditionHandle(AWSObject):
    resource_type = "AWS::CloudFormation::WaitConditionHandle"

    props = {}


class Metadata(AWSHelperFn):
    def __init__(self, *args):
        self.data = args

    def to_dict(self):
        t = []
        for i in self.data:
            t += list(encode_to_dict(i).items())
        return dict(t)


class InitFileContext(AWSHelperFn):
    def __init__(self, data):
        self.data = data


class InitFile(AWSProperty):
    props = {
        'content': (str, False),
        'mode': (str, False),
        'owner': (str, False),
        'encoding': (encoding, False),
        'group': (str, False),
        'source': (str, False),
        'authentication': (str, False),
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


class InitService(AWSProperty):
    props = {
        'ensureRunning': (boolean, False),
        'enabled': (boolean, False),
        'files': (list, False),
        'packages': (dict, False),
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


class InitConfigSets(AWSHelperFn):
    def __init__(self, **kwargs):
        self.validate(dict(kwargs))
        self.data = kwargs

    def validate(self, config_sets):
        for k, v in config_sets.items():
            if not isinstance(v, list):
                raise ValueError('configSets values must be of type list')


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


def validate_authentication_type(auth_type):
    valid_types = ['S3', 'basic']
    if auth_type not in valid_types:
        raise ValueError('Type needs to be one of %r' % valid_types)
    return auth_type


class AuthenticationBlock(AWSProperty):
    props = {
        "accessKeyId": (str, False),
        "buckets": ([str], False),
        "password": (str, False),
        "secretKey": (str, False),
        "type": (validate_authentication_type, False),
        "uris": ([str], False),
        "username": (str, False),
        "roleName": (str, False)
    }


class Authentication(AWSHelperFn):
    def __init__(self, data):
        self.validate(data)
        self.data = {"AWS::CloudFormation::Authentication": data}

    def validate(self, data):
        for k, v in data.items():
            if not isinstance(v, AuthenticationBlock):
                raise ValueError(
                    'authentication block must be of type'
                    ' cloudformation.AuthenticationBlock'
                )


class Init(AWSHelperFn):
    def __init__(self, data, **kwargs):
        self.validate(data, dict(kwargs))

        if isinstance(data, InitConfigSets):
            self.data = {
                'AWS::CloudFormation::Init': dict({'configSets': data},
                                                  **kwargs)
            }
        else:
            self.data = {'AWS::CloudFormation::Init': data}

    def validate(self, data, config_sets):
        if isinstance(data, InitConfigSets):
            for k, v in sorted(config_sets.items()):
                if not isinstance(v, InitConfig):
                    raise ValueError(
                        'init configs must of type ',
                        'cloudformation.InitConfigSet'
                    )
        else:
            if 'config' not in data:
                raise ValueError('config property is required')
            if not isinstance(data['config'], InitConfig):
                raise ValueError(
                    'config property must be of type cloudformation.InitConfig'
                )


class Macro(AWSCustomObject):
    resource_type = "AWS::CloudFormation::Macro"

    props = {
        'Description': (str, False),
        'FunctionName': (str, True),
        'LogGroupName': (str, False),
        'LogRoleARN': (str, False),
        'Name': (str, True),
    }
