# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer


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
        'Tags': (Tags, False)
    }


class CaptureContentTypeHeader(AWSProperty):
    props = {
        'CsvContentTypes': ([basestring], False),
        'JsonContentTypes': ([basestring], False),
    }


class CaptureOption(AWSProperty):
    props = {
        'CaptureMode': (basestring, True),
    }


class DataCaptureConfig(AWSProperty):
    props = {
        'CaptureContentTypeHeader': (CaptureContentTypeHeader, False),
        'CaptureOptions': ([CaptureOption], True),
        'DestinationS3Uri': (basestring, True),
        'EnableCapture': (boolean, False),
        'InitialSamplingPercentage': (integer, True),
        'KmsKeyId': (basestring, False),
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
        'DataCaptureConfig': (DataCaptureConfig, False),
        'EndpointConfigName': (basestring, False),
        'KmsKeyId': (basestring, False),
        'ProductionVariants': ([ProductionVariant], True),
        'Tags': (Tags, False),
    }


class ContainerDefinition(AWSProperty):
    props = {
        'ContainerHostname': (basestring, False),
        'Environment': (dict, False),
        'Mode': (basestring, False),
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
        'Containers': ([ContainerDefinition], False),
        'ExecutionRoleArn': (basestring, True),
        'ModelName': (basestring, False),
        'PrimaryContainer': (ContainerDefinition, False),
        'Tags': (Tags, False),
        'VpcConfig': (VpcConfig, False),
    }


class MonitoringExecutionSummary(AWSProperty):
    props = {
        'CreationTime': (basestring, True),
        'EndpointName': (basestring, False),
        'FailureReason': (basestring, False),
        'LastModifiedTime': (basestring, True),
        'MonitoringExecutionStatus': (basestring, True),
        'MonitoringScheduleName': (basestring, True),
        'ProcessingJobArn': (basestring, False),
        'ScheduledTime': (basestring, True),
    }


class ConstraintsResource(AWSProperty):
    props = {
        'S3Uri': (basestring, False),
    }


class StatisticsResource(AWSProperty):
    props = {
        'S3Uri': (basestring, False),
    }


class BaselineConfig(AWSProperty):
    props = {
        'ConstraintsResource': (ConstraintsResource, False),
        'StatisticsResource': (StatisticsResource, False),
    }


class MonitoringAppSpecification(AWSProperty):
    props = {
        'ContainerArguments': ([basestring], False),
        'ContainerEntrypoint': ([basestring], False),
        'ImageUri': (basestring, True),
        'PostAnalyticsProcessorSourceUri': (basestring, False),
        'RecordPreprocessorSourceUri': (basestring, False),
    }


class EndpointInput(AWSProperty):
    props = {
        'EndpointName': (basestring, True),
        'LocalPath': (basestring, True),
        'S3DataDistributionType': (basestring, False),
        'S3InputMode': (basestring, False),
    }


class MonitoringInput(AWSProperty):
    props = {
        'EndpointInput': (EndpointInput, True),
    }


class MonitoringInputs(AWSProperty):
    props = {
        'MonitoringInputs': ([MonitoringInput], False),
    }


class S3Output(AWSProperty):
    props = {
        'LocalPath': (basestring, True),
        'S3UploadMode': (basestring, False),
        'S3Uri': (basestring, True),
    }


class MonitoringOutput(AWSProperty):
    props = {
        'S3Output': (S3Output, True),
    }


class MonitoringOutputConfig(AWSProperty):
    props = {
        'KmsKeyId': (basestring, False),
        'MonitoringOutputs': ([MonitoringOutput], True),
    }


class ClusterConfig(AWSProperty):
    props = {
        'InstanceCount': (integer, True),
        'InstanceType': (basestring, True),
        'VolumeKmsKeyId': (basestring, False),
        'VolumeSizeInGB': (integer, True),
    }


class MonitoringResources(AWSProperty):
    props = {
        'ClusterConfig': (ClusterConfig, True),
    }


class NetworkConfig(AWSProperty):
    props = {
        'EnableInterContainerTrafficEncryption': (boolean, False),
        'EnableNetworkIsolation': (boolean, False),
        'VpcConfig': (VpcConfig, False),
    }


class StoppingCondition(AWSProperty):
    props = {
        'MaxRuntimeInSeconds': (integer, True),
    }


class MonitoringJobDefinition(AWSProperty):
    props = {
        'BaselineConfig': (BaselineConfig, False),
        'Environment': (dict, False),
        'MonitoringAppSpecification': (MonitoringAppSpecification, True),
        'MonitoringInputs': (MonitoringInputs, True),
        'MonitoringOutputConfig': (MonitoringOutputConfig, True),
        'MonitoringResources': (MonitoringResources, True),
        'NetworkConfig': (NetworkConfig, False),
        'RoleArn': (basestring, True),
        'StoppingCondition': (StoppingCondition, False),
    }


class ScheduleConfig(AWSProperty):
    props = {
        'ScheduleExpression': (basestring, True),
    }


class MonitoringScheduleConfig(AWSProperty):
    props = {
        'MonitoringJobDefinition': (MonitoringJobDefinition, True),
        'ScheduleConfig': (ScheduleConfig, False),
    }


class MonitoringSchedule(AWSObject):
    resource_type = "AWS::SageMaker::MonitoringSchedule"

    props = {
        'CreationTime': (basestring, False),
        'EndpointName': (basestring, False),
        'FailureReason': (basestring, False),
        'LastModifiedTime': (basestring, False),
        'LastMonitoringExecutionSummary':
            (MonitoringExecutionSummary, False),
        'MonitoringScheduleArn': (basestring, False),
        'MonitoringScheduleConfig': (MonitoringScheduleConfig, True),
        'MonitoringScheduleName': (basestring, True),
        'MonitoringScheduleStatus': (basestring, False),
        'Tags': (Tags, False),
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
