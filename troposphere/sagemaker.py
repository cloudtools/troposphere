# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer


class Endpoint(AWSObject):
    resource_type = "AWS::SageMaker::Endpoint"

    props = {
        'EndpointName': (basestring, False),
        'EndpointConfigName': (basestring, True),
        'Tags': (Tags, False),
    }


class ProductionVariant(AWSProperty):
    props = {
        'ModelName': (boolean, True),
        'VariantName': (basestring, True),
        'InitialInstanceCount': (integer, True),
        'InstanceType': (basestring, True),
    }


class EndpointConfig(AWSObject):
    resource_type = "AWS::SageMaker::EndpointConfig"

    props = {
        'EndpointConfigName': (basestring, False),
        'ProductionVariants': ([ProductionVariant], True),
        'Tags': (Tags, False),
    }


class ContainerDefinition(AWSProperty):
    props = {
        'ContainerHostname': (basestring, False),
        'Environment': (dict, False),
        'ModelDataUrl': (basestring, False),
        'Image': (basestring, True),
    }


class Model(AWSObject):
    resource_type = "AWS::SageMaker::Model"

    props = {
        'ExecutionRoleArn': (basestring, True),
        'PrimaryContainer': (ContainerDefinition, True),
        'ModelName': (basestring, False),
        'VpcConfig': (basestring, False),
        'Tags': (Tags, False),
    }


class NotebookInstance(AWSObject):
    resource_type = "AWS::SageMaker::NotebookInstance"

    props = {
        'KmsKeyId': (basestring, False),
        'DirectInternetAccess': (basestring, True),
        'SubnetId': (basestring, False),
        'NotebookInstanceName': (basestring, False),
        'InstanceType': (basestring, True),
        'LifecycleConfigName': (basestring, False),
        'SecurityGroupIds': ([basestring], False),
        'RoleArn': (basestring, True),
        'Tags': (Tags, False),
    }


class NotebookInstanceLifecycleConfig (AWSProperty):
    props = {
        'Content': (basestring, False),
    }


class NotebookInstanceLifecycleConfig(AWSObject):
    resource_type = "AWS::SageMaker::NotebookInstanceLifecycleConfig"

    props = {
        'NotebookInstanceLifecycleConfigName': (basestring, False),
        'OnCreate': (NotebookInstanceLifecycleConfig, False),
        'OnStart': (NotebookInstanceLifecycleConfig, False),
    }
