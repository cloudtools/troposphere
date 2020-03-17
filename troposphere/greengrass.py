# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject
from . import AWSProperty
from .validators import boolean
from .validators import integer


class Connector(AWSProperty):
    props = {
        'ConnectorArn': (basestring, True),
        'Id': (basestring, True),
        'Parameters': (dict, False),
    }


class ConnectorDefinitionVersion(AWSProperty):
    props = {
        'Connectors': ([Connector], True),
    }


class ConnectorDefinition(AWSObject):
    resource_type = "AWS::Greengrass::ConnectorDefinition"

    props = {
        'InitialVersion': (ConnectorDefinitionVersion, False),
        'Name': (basestring, True),
        'Tags': (dict, False),
    }


class ConnectorDefinitionVersion(AWSObject):
    resource_type = "AWS::Greengrass::ConnectorDefinitionVersion"

    props = {
        'ConnectorDefinitionId': (basestring, True),
        'Connectors': ([Connector], True),
    }


class Core(AWSProperty):
    props = {
        'CertificateArn': (basestring, True),
        'Id': (basestring, True),
        'SyncShadow': (boolean, False),
        'ThingArn': (basestring, True),
    }


class CoreDefinitionVersion(AWSProperty):
    props = {
        'Cores': ([Core], True),
    }


class CoreDefinition(AWSObject):
    resource_type = "AWS::Greengrass::CoreDefinition"

    props = {
        'InitialVersion': (CoreDefinitionVersion, False),
        'Name': (basestring, True),
        'Tags': (dict, False),
    }


class CoreDefinitionVersion(AWSObject):
    resource_type = "AWS::Greengrass::CoreDefinitionVersion"

    props = {
        'CoreDefinitionId': (basestring, True),
        'Cores': ([Core], True),
    }


class Device(AWSProperty):
    props = {
        'CertificateArn': (basestring, True),
        'Id': (basestring, True),
        'SyncShadow': (boolean, False),
        'ThingArn': (basestring, True),
    }


class DeviceDefinitionVersion(AWSProperty):
    props = {
        'Devices': ([Device], True),
    }


class DeviceDefinition(AWSObject):
    resource_type = "AWS::Greengrass::DeviceDefinition"

    props = {
        'InitialVersion': (DeviceDefinitionVersion, False),
        'Name': (basestring, True),
        'Tags': (dict, False),
    }


class DeviceDefinitionVersion(AWSObject):
    resource_type = "AWS::Greengrass::DeviceDefinitionVersion"

    props = {
        'DeviceDefinitionId': (basestring, True),
        'Devices': ([Device], True),
    }


class RunAs(AWSProperty):
    props = {
        'Gid': (integer, False),
        'Uid': (integer, False),
    }


class Execution(AWSProperty):
    props = {
        'IsolationMode': (basestring, False),
        'RunAs': (RunAs, False),
    }


class DefaultConfig(AWSProperty):
    props = {
        'Execution': (Execution, True),
    }


class ResourceAccessPolicy(AWSProperty):
    props = {
        'Permission': (basestring, False),
        'ResourceId': (basestring, True),
    }


class Environment(AWSProperty):
    props = {
        'AccessSysfs': (boolean, False),
        'Execution': (Execution, False),
        'ResourceAccessPolicies': ([ResourceAccessPolicy], False),
        'Variables': (dict, False),
    }


class FunctionConfiguration(AWSProperty):
    props = {
        'EncodingType': (basestring, False),
        'Environment': (Environment, False),
        'ExecArgs': (basestring, False),
        'Executable': (basestring, False),
        'MemorySize': (integer, False),
        'Pinned': (boolean, False),
        'Timeout': (integer, False),
    }


class Function(AWSProperty):
    props = {
        'FunctionArn': (basestring, True),
        'FunctionConfiguration': (FunctionConfiguration, True),
        'Id': (basestring, True),
    }


class FunctionDefinitionVersion(AWSProperty):
    props = {
        'DefaultConfig': (DefaultConfig, False),
        'Functions': ([Function], True),
    }


class FunctionDefinition(AWSObject):
    resource_type = "AWS::Greengrass::FunctionDefinition"

    props = {
        'InitialVersion': (FunctionDefinitionVersion, False),
        'Name': (basestring, True),
        'Tags': (dict, False),
    }


class FunctionDefinitionVersion(AWSObject):
    resource_type = "AWS::Greengrass::FunctionDefinitionVersion"

    props = {
        'DefaultConfig': (DefaultConfig, False),
        'FunctionDefinitionId': (basestring, True),
        'Functions': ([Function], True),
    }


class GroupVersion(AWSProperty):
    props = {
        'ConnectorDefinitionVersionArn': (basestring, False),
        'CoreDefinitionVersionArn': (basestring, False),
        'DeviceDefinitionVersionArn': (basestring, False),
        'FunctionDefinitionVersionArn': (basestring, False),
        'LoggerDefinitionVersionArn': (basestring, False),
        'ResourceDefinitionVersionArn': (basestring, False),
        'SubscriptionDefinitionVersionArn': (basestring, False),
    }


class Group(AWSObject):
    resource_type = "AWS::Greengrass::Group"

    props = {
        'InitialVersion': (GroupVersion, False),
        'Name': (basestring, True),
        'RoleArn': (basestring, False),
        'Tags': (dict, False),
    }


class GroupVersion(AWSObject):
    resource_type = "AWS::Greengrass::GroupVersion"

    props = {
        'ConnectorDefinitionVersionArn': (basestring, False),
        'CoreDefinitionVersionArn': (basestring, False),
        'DeviceDefinitionVersionArn': (basestring, False),
        'FunctionDefinitionVersionArn': (basestring, False),
        'GroupId': (basestring, True),
        'LoggerDefinitionVersionArn': (basestring, False),
        'ResourceDefinitionVersionArn': (basestring, False),
        'SubscriptionDefinitionVersionArn': (basestring, False),
    }


class Logger(AWSProperty):
    props = {
        'Component': (basestring, True),
        'Id': (basestring, True),
        'Level': (basestring, True),
        'Space': (integer, False),
        'Type': (basestring, True),
    }


class LoggerDefinitionVersion(AWSProperty):
    props = {
        'Loggers': ([Logger], True),
    }


class LoggerDefinition(AWSObject):
    resource_type = "AWS::Greengrass::LoggerDefinition"

    props = {
        'InitialVersion': (LoggerDefinitionVersion, False),
        'Name': (basestring, True),
        'Tags': (dict, False),
    }


class LoggerDefinitionVersion(AWSObject):
    resource_type = "AWS::Greengrass::LoggerDefinitionVersion"

    props = {
        'LoggerDefinitionId': (basestring, True),
        'Loggers': ([Logger], True),
    }


class GroupOwnerSetting(AWSProperty):
    props = {
        'AutoAddGroupOwner': (boolean, True),
        'GroupOwner': (basestring, False),
    }


class LocalDeviceResourceData(AWSProperty):
    props = {
        'GroupOwnerSetting': (GroupOwnerSetting, False),
        'SourcePath': (basestring, True),
    }


class LocalVolumeResourceData(AWSProperty):
    props = {
        'DestinationPath': (basestring, True),
        'GroupOwnerSetting': (GroupOwnerSetting, False),
        'SourcePath': (basestring, True),
    }


class ResourceDownloadOwnerSetting(AWSProperty):
    props = {
        'GroupOwner': (basestring, True),
        'GroupPermission': (basestring, True),
    }


class S3MachineLearningModelResourceData(AWSProperty):
    props = {
        'DestinationPath': (basestring, True),
        'OwnerSetting': (ResourceDownloadOwnerSetting, False),
        'S3Uri': (basestring, True),
    }


class SageMakerMachineLearningModelResourceData(AWSProperty):
    props = {
        'DestinationPath': (basestring, True),
        'OwnerSetting': (ResourceDownloadOwnerSetting, False),
        'SageMakerJobArn': (basestring, True),
    }


class SecretsManagerSecretResourceData(AWSProperty):
    props = {
        'ARN': (basestring, True),
        'AdditionalStagingLabelsToDownload': ([basestring], False),
    }


class ResourceDataContainer(AWSProperty):
    props = {
        'LocalDeviceResourceData': (LocalDeviceResourceData, False),
        'LocalVolumeResourceData': (LocalVolumeResourceData, False),
        'S3MachineLearningModelResourceData':
            (S3MachineLearningModelResourceData, False),
        'SageMakerMachineLearningModelResourceData':
            (SageMakerMachineLearningModelResourceData, False),
        'SecretsManagerSecretResourceData':
            (SecretsManagerSecretResourceData, False),
    }


class ResourceInstance(AWSProperty):
    props = {
        'Id': (basestring, True),
        'Name': (basestring, True),
        'ResourceDataContainer': (ResourceDataContainer, True),
    }


class ResourceDefinitionVersion(AWSProperty):
    props = {
        'Resources': ([ResourceInstance], True),
    }


class ResourceDefinition(AWSObject):
    resource_type = "AWS::Greengrass::ResourceDefinition"

    props = {
        'InitialVersion': (ResourceDefinitionVersion, False),
        'Name': (basestring, True),
        'Tags': (dict, False),
    }


class ResourceDefinitionVersion(AWSObject):
    resource_type = "AWS::Greengrass::ResourceDefinitionVersion"

    props = {
        'ResourceDefinitionId': (basestring, True),
        'Resources': ([ResourceInstance], True),
    }


class Subscription(AWSProperty):
    props = {
        'Id': (basestring, True),
        'Source': (basestring, True),
        'Subject': (basestring, True),
        'Target': (basestring, True),
    }


class SubscriptionDefinitionVersionProperty(AWSProperty):
    props = {
        'Subscriptions': ([Subscription], True),
    }


class SubscriptionDefinition(AWSObject):
    resource_type = "AWS::Greengrass::SubscriptionDefinition"

    props = {
        'InitialVersion': (SubscriptionDefinitionVersionProperty, False),
        'Name': (basestring, True),
        'Tags': (dict, False),
    }


class SubscriptionDefinitionVersion(AWSObject):
    resource_type = "AWS::Greengrass::SubscriptionDefinitionVersion"

    props = {
        'SubscriptionDefinitionId': (basestring, True),
        'Subscriptions': ([Subscription], True),
    }
