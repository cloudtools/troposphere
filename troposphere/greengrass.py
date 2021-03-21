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
        'ConnectorArn': (str, True),
        'Id': (str, True),
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
        'Name': (str, True),
        'Tags': (dict, False),
    }


class ConnectorDefinitionVersion(AWSObject):
    resource_type = "AWS::Greengrass::ConnectorDefinitionVersion"

    props = {
        'ConnectorDefinitionId': (str, True),
        'Connectors': ([Connector], True),
    }


class Core(AWSProperty):
    props = {
        'CertificateArn': (str, True),
        'Id': (str, True),
        'SyncShadow': (boolean, False),
        'ThingArn': (str, True),
    }


class CoreDefinitionVersion(AWSProperty):
    props = {
        'Cores': ([Core], True),
    }


class CoreDefinition(AWSObject):
    resource_type = "AWS::Greengrass::CoreDefinition"

    props = {
        'InitialVersion': (CoreDefinitionVersion, False),
        'Name': (str, True),
        'Tags': (dict, False),
    }


class CoreDefinitionVersion(AWSObject):
    resource_type = "AWS::Greengrass::CoreDefinitionVersion"

    props = {
        'CoreDefinitionId': (str, True),
        'Cores': ([Core], True),
    }


class Device(AWSProperty):
    props = {
        'CertificateArn': (str, True),
        'Id': (str, True),
        'SyncShadow': (boolean, False),
        'ThingArn': (str, True),
    }


class DeviceDefinitionVersion(AWSProperty):
    props = {
        'Devices': ([Device], True),
    }


class DeviceDefinition(AWSObject):
    resource_type = "AWS::Greengrass::DeviceDefinition"

    props = {
        'InitialVersion': (DeviceDefinitionVersion, False),
        'Name': (str, True),
        'Tags': (dict, False),
    }


class DeviceDefinitionVersion(AWSObject):
    resource_type = "AWS::Greengrass::DeviceDefinitionVersion"

    props = {
        'DeviceDefinitionId': (str, True),
        'Devices': ([Device], True),
    }


class RunAs(AWSProperty):
    props = {
        'Gid': (integer, False),
        'Uid': (integer, False),
    }


class Execution(AWSProperty):
    props = {
        'IsolationMode': (str, False),
        'RunAs': (RunAs, False),
    }


class DefaultConfig(AWSProperty):
    props = {
        'Execution': (Execution, True),
    }


class ResourceAccessPolicy(AWSProperty):
    props = {
        'Permission': (str, False),
        'ResourceId': (str, True),
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
        'EncodingType': (str, False),
        'Environment': (Environment, False),
        'ExecArgs': (str, False),
        'Executable': (str, False),
        'MemorySize': (integer, False),
        'Pinned': (boolean, False),
        'Timeout': (integer, False),
    }


class Function(AWSProperty):
    props = {
        'FunctionArn': (str, True),
        'FunctionConfiguration': (FunctionConfiguration, True),
        'Id': (str, True),
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
        'Name': (str, True),
        'Tags': (dict, False),
    }


class FunctionDefinitionVersion(AWSObject):
    resource_type = "AWS::Greengrass::FunctionDefinitionVersion"

    props = {
        'DefaultConfig': (DefaultConfig, False),
        'FunctionDefinitionId': (str, True),
        'Functions': ([Function], True),
    }


class GroupVersion(AWSProperty):
    props = {
        'ConnectorDefinitionVersionArn': (str, False),
        'CoreDefinitionVersionArn': (str, False),
        'DeviceDefinitionVersionArn': (str, False),
        'FunctionDefinitionVersionArn': (str, False),
        'LoggerDefinitionVersionArn': (str, False),
        'ResourceDefinitionVersionArn': (str, False),
        'SubscriptionDefinitionVersionArn': (str, False),
    }


class Group(AWSObject):
    resource_type = "AWS::Greengrass::Group"

    props = {
        'InitialVersion': (GroupVersion, False),
        'Name': (str, True),
        'RoleArn': (str, False),
        'Tags': (dict, False),
    }


class GroupVersion(AWSObject):
    resource_type = "AWS::Greengrass::GroupVersion"

    props = {
        'ConnectorDefinitionVersionArn': (str, False),
        'CoreDefinitionVersionArn': (str, False),
        'DeviceDefinitionVersionArn': (str, False),
        'FunctionDefinitionVersionArn': (str, False),
        'GroupId': (str, True),
        'LoggerDefinitionVersionArn': (str, False),
        'ResourceDefinitionVersionArn': (str, False),
        'SubscriptionDefinitionVersionArn': (str, False),
    }


class Logger(AWSProperty):
    props = {
        'Component': (str, True),
        'Id': (str, True),
        'Level': (str, True),
        'Space': (integer, False),
        'Type': (str, True),
    }


class LoggerDefinitionVersion(AWSProperty):
    props = {
        'Loggers': ([Logger], True),
    }


class LoggerDefinition(AWSObject):
    resource_type = "AWS::Greengrass::LoggerDefinition"

    props = {
        'InitialVersion': (LoggerDefinitionVersion, False),
        'Name': (str, True),
        'Tags': (dict, False),
    }


class LoggerDefinitionVersion(AWSObject):
    resource_type = "AWS::Greengrass::LoggerDefinitionVersion"

    props = {
        'LoggerDefinitionId': (str, True),
        'Loggers': ([Logger], True),
    }


class GroupOwnerSetting(AWSProperty):
    props = {
        'AutoAddGroupOwner': (boolean, True),
        'GroupOwner': (str, False),
    }


class LocalDeviceResourceData(AWSProperty):
    props = {
        'GroupOwnerSetting': (GroupOwnerSetting, False),
        'SourcePath': (str, True),
    }


class LocalVolumeResourceData(AWSProperty):
    props = {
        'DestinationPath': (str, True),
        'GroupOwnerSetting': (GroupOwnerSetting, False),
        'SourcePath': (str, True),
    }


class ResourceDownloadOwnerSetting(AWSProperty):
    props = {
        'GroupOwner': (str, True),
        'GroupPermission': (str, True),
    }


class S3MachineLearningModelResourceData(AWSProperty):
    props = {
        'DestinationPath': (str, True),
        'OwnerSetting': (ResourceDownloadOwnerSetting, False),
        'S3Uri': (str, True),
    }


class SageMakerMachineLearningModelResourceData(AWSProperty):
    props = {
        'DestinationPath': (str, True),
        'OwnerSetting': (ResourceDownloadOwnerSetting, False),
        'SageMakerJobArn': (str, True),
    }


class SecretsManagerSecretResourceData(AWSProperty):
    props = {
        'ARN': (str, True),
        'AdditionalStagingLabelsToDownload': ([str], False),
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
        'Id': (str, True),
        'Name': (str, True),
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
        'Name': (str, True),
        'Tags': (dict, False),
    }


class ResourceDefinitionVersion(AWSObject):
    resource_type = "AWS::Greengrass::ResourceDefinitionVersion"

    props = {
        'ResourceDefinitionId': (str, True),
        'Resources': ([ResourceInstance], True),
    }


class Subscription(AWSProperty):
    props = {
        'Id': (str, True),
        'Source': (str, True),
        'Subject': (str, True),
        'Target': (str, True),
    }


class SubscriptionDefinitionVersionProperty(AWSProperty):
    props = {
        'Subscriptions': ([Subscription], True),
    }


class SubscriptionDefinition(AWSObject):
    resource_type = "AWS::Greengrass::SubscriptionDefinition"

    props = {
        'InitialVersion': (SubscriptionDefinitionVersionProperty, False),
        'Name': (str, True),
        'Tags': (dict, False),
    }


class SubscriptionDefinitionVersion(AWSObject):
    resource_type = "AWS::Greengrass::SubscriptionDefinitionVersion"

    props = {
        'SubscriptionDefinitionId': (str, True),
        'Subscriptions': ([Subscription], True),
    }
