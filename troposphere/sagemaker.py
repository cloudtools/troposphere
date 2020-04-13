# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import integer


class GitConfig(AWSProperty):
    props = {
        'Branch': (basestring, False),
        'RepositoryUrl': (basestring, True),
        'SecretArn': (basestring, False),
    }


class CodeRepository(AWSObject):
    resource_type = "AWS::SageMaker::CodeRepository"

    props = {
        'CodeRepositoryName': (basestring, False),
        'GitConfig': (GitConfig, True)
    }


class Endpoint(AWSObject):
    resource_type = "AWS::SageMaker::Endpoint"

    props = {
        'EndpointName': (basestring, False),
        'EndpointConfigName': (basestring, True),
        'Tags': (Tags, True)
    }


class ProductionVariant(AWSProperty):
    props = {
        'ModelName': (basestring, True),
        'VariantName': (basestring, True),
        'InitialInstanceCount': (integer, True),
        'InstanceType': (basestring, True),
        'InitialVariantWeight': (float, True)
    }


class EndpointConfig(AWSObject):
    resource_type = "AWS::SageMaker::EndpointConfig"

    props = {
        'EndpointConfigName': (basestring, False),
        'ProductionVariants': ([ProductionVariant], True),
        'KmsKeyId': (basestring, False),
        'Tags': (Tags, True)
    }


class ContainerDefinition(AWSProperty):
    props = {
        'ContainerHostname': (basestring, False),
        'Environment': (dict, False),
        'ModelDataUrl': (basestring, False),
        'Image': (basestring, True)
    }


class VpcConfig(AWSProperty):
    props = {
        'Subnets': ([basestring], True),
        'SecurityGroupIds': ([basestring], True)
    }


class Model(AWSObject):
    resource_type = "AWS::SageMaker::Model"

    props = {
        'ExecutionRoleArn': (basestring, True),
        'PrimaryContainer': (ContainerDefinition, True),
        'Containers': ([ContainerDefinition], False),
        'ModelName': (basestring, False),
        'VpcConfig': (VpcConfig, False),
        'Tags': (Tags, False)
    }


class NotebookInstanceLifecycleHook(AWSProperty):
    props = {
        'Content': (basestring, False)
    }


class NotebookInstanceLifecycleConfig(AWSObject):
    resource_type = "AWS::SageMaker::NotebookInstanceLifecycleConfig"

    props = {
        'NotebookInstanceLifecycleConfigName': (basestring, False),
        'OnCreate': ([NotebookInstanceLifecycleHook], False),
        'OnStart': ([NotebookInstanceLifecycleHook], False)
    }


class NotebookInstance(AWSObject):
    resource_type = "AWS::SageMaker::NotebookInstance"

    props = {
        'AcceleratorTypes': ([basestring], False),
        'AdditionalCodeRepositories': ([basestring], False),
        'DefaultCodeRepository': (basestring, False),
        'DirectInternetAccess': (basestring, False),
        'InstanceType': (basestring, True),
        'KmsKeyId': (basestring, False),
        'LifecycleConfigName': (basestring, False),
        'NotebookInstanceName': (basestring, False),
        'RoleArn': (basestring, True),
        'RootAccess': (basestring, False),
        'SecurityGroupIds': ([basestring], False),
        'SubnetId': (basestring, False),
        'Tags': (Tags, False),
        'VolumeSizeInGB': (integer, False),
    }


class CognitoMemberDefinition(AWSProperty):
    props = {
        'CognitoClientId': (basestring, True),
        'CognitoUserGroup': (basestring, True),
        'CognitoUserPool': (basestring, True),
    }


class MemberDefinition(AWSProperty):
    props = {
        'CognitoMemberDefinition': (CognitoMemberDefinition, True),
    }


class NotificationConfiguration(AWSProperty):
    props = {
        'NotificationTopicArn': (basestring, True),
    }


class Workteam(AWSObject):
    resource_type = "AWS::SageMaker::Workteam"

    props = {
        'Description': (basestring, False),
        'MemberDefinitions': ([MemberDefinition], False),
        'NotificationConfiguration': (NotificationConfiguration, False),
        'Tags': (Tags, False),
        'WorkteamName': (basestring, False),
    }
