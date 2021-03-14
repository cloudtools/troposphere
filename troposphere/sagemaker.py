# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer


class ResourceSpec(AWSProperty):
    props = {
        'InstanceType': (basestring, False),
        'SageMakerImageArn': (basestring, False),
        'SageMakerImageVersionArn': (basestring, False),
    }


class App(AWSObject):
    resource_type = "AWS::SageMaker::App"

    props = {
        'AppName': (basestring, True),
        'AppType': (basestring, True),
        'DomainId': (basestring, True),
        'ResourceSpec': (ResourceSpec, False),
        'Tags': (Tags, False),
        'UserProfileName': (basestring, True),
    }


class FileSystemConfig(AWSProperty):
    props = {
        'DefaultGid': (integer, False),
        'DefaultUid': (integer, False),
        'MountPath': (basestring, False),
    }


class KernelSpec(AWSProperty):
    props = {
        'DisplayName': (basestring, False),
        'Name': (basestring, True),
    }


class KernelGatewayImageConfig(AWSProperty):
    props = {
        'FileSystemConfig': (FileSystemConfig, False),
        'KernelSpecs': ([KernelSpec], True),
    }


class AppImageConfig(AWSObject):
    resource_type = "AWS::SageMaker::AppImageConfig"

    props = {
        'AppImageConfigName': (basestring, True),
        'KernelGatewayImageConfig': (KernelGatewayImageConfig, False),
        'Tags': (Tags, False),
    }


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
        'GitConfig': (GitConfig, True),
    }


class DataQualityAppSpecification(AWSProperty):
    props = {
        'ContainerArguments': ([basestring], False),
        'ContainerEntrypoint': ([basestring], False),
        'Environment': (dict, False),
        'ImageUri': (basestring, True),
        'PostAnalyticsProcessorSourceUri': (basestring, False),
        'RecordPreprocessorSourceUri': (basestring, False),
    }


class ConstraintsResource(AWSProperty):
    props = {
        'S3Uri': (basestring, False),
    }


class StatisticsResource(AWSProperty):
    props = {
        'S3Uri': (basestring, False),
    }


class DataQualityBaselineConfig(AWSProperty):
    props = {
        'BaseliningJobName': (basestring, False),
        'ConstraintsResource': (ConstraintsResource, False),
        'StatisticsResource': (StatisticsResource, False),
    }


class EndpointInput(AWSProperty):
    props = {
        'EndpointName': (basestring, True),
        'LocalPath': (basestring, True),
        'S3DataDistributionType': (basestring, False),
        'S3InputMode': (basestring, False),
    }


class DataQualityJobInput(AWSProperty):
    props = {
        'EndpointInput': (EndpointInput, True),
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


class VpcConfig(AWSProperty):
    props = {
        'Subnets': ([basestring], True),
        'SecurityGroupIds': ([basestring], True),
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


class DataQualityJobDefinition(AWSObject):
    resource_type = "AWS::SageMaker::DataQualityJobDefinition"

    props = {
        'DataQualityAppSpecification': (DataQualityAppSpecification, True),
        'DataQualityBaselineConfig': (DataQualityBaselineConfig, False),
        'DataQualityJobInput': (DataQualityJobInput, True),
        'DataQualityJobOutputConfig': (MonitoringOutputConfig, True),
        'JobDefinitionName': (basestring, False),
        'JobResources': (MonitoringResources, True),
        'NetworkConfig': (NetworkConfig, False),
        'RoleArn': (basestring, True),
        'StoppingCondition': (StoppingCondition, False),
        'Tags': (Tags, False),
    }


class Device(AWSObject):
    resource_type = "AWS::SageMaker::Device"

    props = {
        'Device': (dict, False),
        'DeviceFleetName': (basestring, True),
        'Tags': (Tags, False),
    }


class EdgeOutputConfig(AWSProperty):
    props = {
        'KmsKeyId': (basestring, False),
        'S3OutputLocation': (basestring, True),
    }


class DeviceFleet(AWSObject):
    resource_type = "AWS::SageMaker::DeviceFleet"

    props = {
        'Description': (basestring, False),
        'DeviceFleetName': (basestring, True),
        'OutputConfig': (EdgeOutputConfig, True),
        'RoleArn': (basestring, True),
        'Tags': (Tags, False),
    }


class JupyterServerAppSettings(AWSProperty):
    props = {
        'DefaultResourceSpec': (ResourceSpec, False),
    }


class CustomImage(AWSProperty):
    props = {
        'AppImageConfigName': (basestring, True),
        'ImageName': (basestring, True),
        'ImageVersionNumber': (integer, False),
    }


class KernelGatewayAppSettings(AWSProperty):
    props = {
        'CustomImages': ([CustomImage], False),
        'DefaultResourceSpec': (ResourceSpec, False),
    }


class SharingSettings(AWSProperty):
    props = {
        'NotebookOutputOption': (basestring, False),
        'S3KmsKeyId': (basestring, False),
        'S3OutputPath': (basestring, False),
    }


class UserSettings(AWSProperty):
    props = {
        'ExecutionRole': (basestring, False),
        'JupyterServerAppSettings': (JupyterServerAppSettings, False),
        'KernelGatewayAppSettings': (KernelGatewayAppSettings, False),
        'SecurityGroups': ([basestring], False),
        'SharingSettings': (SharingSettings, False),
    }


class Domain(AWSObject):
    resource_type = "AWS::SageMaker::Domain"

    props = {
        'AppNetworkAccessType': (basestring, False),
        'AuthMode': (basestring, True),
        'DefaultUserSettings': (UserSettings, True),
        'DomainName': (basestring, True),
        'KmsKeyId': (basestring, False),
        'SubnetIds': ([basestring], True),
        'Tags': (Tags, False),
        'VpcId': (basestring, True),
    }


class Alarm(AWSProperty):
    props = {
        'AlarmName': (basestring, True),
    }


class AutoRollbackConfig(AWSProperty):
    props = {
        'Alarms': ([Alarm], True),
    }


class CapacitySize(AWSProperty):
    props = {
        'Type': (basestring, True),
        'Value': (integer, True),
    }


class TrafficRoutingConfig(AWSProperty):
    props = {
        'CanarySize': (CapacitySize, False),
        'Type': (basestring, True),
        'WaitIntervalInSeconds': (integer, False),
    }


class BlueGreenUpdatePolicy(AWSProperty):
    props = {
        'MaximumExecutionTimeoutInSeconds': (integer, False),
        'TerminationWaitInSeconds': (integer, False),
        'TrafficRoutingConfiguration': (TrafficRoutingConfig, True),
    }


class DeploymentConfig(AWSProperty):
    props = {
        'AutoRollbackConfiguration': (AutoRollbackConfig, False),
        'BlueGreenUpdatePolicy': (BlueGreenUpdatePolicy, True),
    }


class VariantProperty(AWSProperty):
    props = {
        'VariantPropertyType': (basestring, False),
    }


class Endpoint(AWSObject):
    resource_type = "AWS::SageMaker::Endpoint"

    props = {
        'DeploymentConfig': (DeploymentConfig, False),
        'EndpointConfigName': (basestring, True),
        'EndpointName': (basestring, False),
        'ExcludeRetainedVariantProperties': ([VariantProperty], False),
        'RetainAllVariantProperties': (boolean, False),
        'Tags': (Tags, False),
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


class FeatureDefinition(AWSProperty):
    props = {
        'FeatureName': (basestring, True),
        'FeatureType': (basestring, True),
    }


class FeatureGroup(AWSObject):
    resource_type = "AWS::SageMaker::FeatureGroup"

    props = {
        'Description': (basestring, False),
        'EventTimeFeatureName': (basestring, True),
        'FeatureDefinitions': ([FeatureDefinition], True),
        'FeatureGroupName': (basestring, True),
        'OfflineStoreConfig': (dict, False),
        'OnlineStoreConfig': (dict, False),
        'RecordIdentifierFeatureName': (basestring, True),
        'RoleArn': (basestring, False),
        'Tags': (Tags, False),
    }


class Image(AWSObject):
    resource_type = "AWS::SageMaker::Image"

    props = {
        'ImageDescription': (basestring, False),
        'ImageDisplayName': (basestring, False),
        'ImageName': (basestring, True),
        'ImageRoleArn': (basestring, True),
        'Tags': (Tags, False),
    }


class ImageVersion(AWSObject):
    resource_type = "AWS::SageMaker::ImageVersion"

    props = {
        'BaseImage': (basestring, True),
        'ImageName': (basestring, True),
    }


class ImageConfig(AWSProperty):
    props = {
        'RepositoryAccessMode': (basestring, True),
    }


class MultiModelConfig(AWSProperty):
    props = {
        'ModelCacheSetting': (basestring, False),
    }


class ContainerDefinition(AWSProperty):
    props = {
        'ContainerHostname': (basestring, False),
        'Environment': (dict, False),
        'Image': (basestring, False),
        'ImageConfig': (ImageConfig, False),
        'Mode': (basestring, False),
        'ModelDataUrl': (basestring, False),
        'ModelPackageName': (basestring, False),
        'MultiModelConfig': (MultiModelConfig, False),
    }


class InferenceExecutionConfig(AWSProperty):
    props = {
        'Mode': (basestring, True),
    }


class Model(AWSObject):
    resource_type = "AWS::SageMaker::Model"

    props = {
        'Containers': ([ContainerDefinition], False),
        'EnableNetworkIsolation': (boolean, False),
        'ExecutionRoleArn': (basestring, True),
        'InferenceExecutionConfig': (InferenceExecutionConfig, False),
        'ModelName': (basestring, False),
        'PrimaryContainer': (ContainerDefinition, False),
        'Tags': (Tags, False),
        'VpcConfig': (VpcConfig, False),
    }


class ModelBiasAppSpecification(AWSProperty):
    props = {
        'ConfigUri': (basestring, True),
        'Environment': (dict, False),
        'ImageUri': (basestring, True),
    }


class ModelBiasBaselineConfig(AWSProperty):
    props = {
        'BaseliningJobName': (basestring, False),
        'ConstraintsResource': (ConstraintsResource, False),
    }


class MonitoringGroundTruthS3Input(AWSProperty):
    props = {
        'S3Uri': (basestring, True),
    }


class ModelBiasJobInput(AWSProperty):
    props = {
        'EndpointInput': (EndpointInput, True),
        'GroundTruthS3Input': (MonitoringGroundTruthS3Input, True),
    }


class ModelBiasJobDefinition(AWSObject):
    resource_type = "AWS::SageMaker::ModelBiasJobDefinition"

    props = {
        'JobDefinitionName': (basestring, False),
        'JobResources': (MonitoringResources, True),
        'ModelBiasAppSpecification': (ModelBiasAppSpecification, True),
        'ModelBiasBaselineConfig': (ModelBiasBaselineConfig, False),
        'ModelBiasJobInput': (ModelBiasJobInput, True),
        'ModelBiasJobOutputConfig': (MonitoringOutputConfig, True),
        'NetworkConfig': (NetworkConfig, False),
        'RoleArn': (basestring, True),
        'StoppingCondition': (StoppingCondition, False),
        'Tags': (Tags, False),
    }


class ModelExplainabilityAppSpecification(AWSProperty):
    props = {
        'ConfigUri': (basestring, True),
        'Environment': (dict, False),
        'ImageUri': (basestring, True),
    }


class ModelExplainabilityBaselineConfig(AWSProperty):
    props = {
        'BaseliningJobName': (basestring, False),
        'ConstraintsResource': (ConstraintsResource, False),
    }


class ModelExplainabilityJobInput(AWSProperty):
    props = {
        'EndpointInput': (EndpointInput, True),
    }


class ModelExplainabilityJobDefinition(AWSObject):
    resource_type = "AWS::SageMaker::ModelExplainabilityJobDefinition"

    props = {
        'JobDefinitionName': (basestring, False),
        'JobResources': (MonitoringResources, True),
        'ModelExplainabilityAppSpecification':
            (ModelExplainabilityAppSpecification, True),
        'ModelExplainabilityBaselineConfig':
            (ModelExplainabilityBaselineConfig, False),
        'ModelExplainabilityJobInput': (ModelExplainabilityJobInput, True),
        'ModelExplainabilityJobOutputConfig':
            (MonitoringOutputConfig, True),
        'NetworkConfig': (NetworkConfig, False),
        'RoleArn': (basestring, True),
        'StoppingCondition': (StoppingCondition, False),
        'Tags': (Tags, False),
    }


class ModelPackageGroup(AWSObject):
    resource_type = "AWS::SageMaker::ModelPackageGroup"

    props = {
        'ModelPackageGroupDescription': (basestring, False),
        'ModelPackageGroupName': (basestring, True),
        'ModelPackageGroupPolicy': (dict, False),
        'Tags': (Tags, False),
    }


class ModelQualityAppSpecification(AWSProperty):
    props = {
        'ContainerArguments': ([basestring], False),
        'ContainerEntrypoint': ([basestring], False),
        'Environment': (dict, False),
        'ImageUri': (basestring, True),
        'PostAnalyticsProcessorSourceUri': (basestring, False),
        'ProblemType': (basestring, True),
        'RecordPreprocessorSourceUri': (basestring, False),
    }


class ModelQualityBaselineConfig(AWSProperty):
    props = {
        'BaseliningJobName': (basestring, False),
        'ConstraintsResource': (ConstraintsResource, False),
    }


class ModelQualityJobInput(AWSProperty):
    props = {
        'EndpointInput': (EndpointInput, True),
        'GroundTruthS3Input': (MonitoringGroundTruthS3Input, True),
    }


class ModelQualityJobDefinition(AWSObject):
    resource_type = "AWS::SageMaker::ModelQualityJobDefinition"

    props = {
        'JobDefinitionName': (basestring, False),
        'JobResources': (MonitoringResources, True),
        'ModelQualityAppSpecification':
            (ModelQualityAppSpecification, True),
        'ModelQualityBaselineConfig': (ModelQualityBaselineConfig, False),
        'ModelQualityJobInput': (ModelQualityJobInput, True),
        'ModelQualityJobOutputConfig': (MonitoringOutputConfig, True),
        'NetworkConfig': (NetworkConfig, False),
        'RoleArn': (basestring, True),
        'StoppingCondition': (StoppingCondition, False),
        'Tags': (Tags, False),
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


class MonitoringInput(AWSProperty):
    props = {
        'EndpointInput': (EndpointInput, True),
    }


class MonitoringInputs(AWSProperty):
    props = {
        'MonitoringInputs': ([MonitoringInput], False),
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


class NotebookInstanceLifecycleHook(AWSProperty):
    props = {
        'Content': (basestring, False),
    }


class NotebookInstanceLifecycleConfig(AWSObject):
    resource_type = "AWS::SageMaker::NotebookInstanceLifecycleConfig"

    props = {
        'NotebookInstanceLifecycleConfigName': (basestring, False),
        'OnCreate': ([NotebookInstanceLifecycleHook], False),
        'OnStart': ([NotebookInstanceLifecycleHook], False),
    }


class Pipeline(AWSObject):
    resource_type = "AWS::SageMaker::Pipeline"

    props = {
        'PipelineDefinition': (dict, True),
        'PipelineDescription': (basestring, False),
        'PipelineDisplayName': (basestring, False),
        'PipelineName': (basestring, True),
        'RoleArn': (basestring, True),
        'Tags': (Tags, False),
    }


class Project(AWSObject):
    resource_type = "AWS::SageMaker::Project"

    props = {
        'ProjectDescription': (basestring, False),
        'ProjectName': (basestring, True),
        'ServiceCatalogProvisioningDetails': (dict, True),
        'Tags': (Tags, False),
    }


class UserProfile(AWSObject):
    resource_type = "AWS::SageMaker::UserProfile"

    props = {
        'DomainId': (basestring, True),
        'SingleSignOnUserIdentifier': (basestring, False),
        'SingleSignOnUserValue': (basestring, False),
        'Tags': (Tags, False),
        'UserProfileName': (basestring, True),
        'UserSettings': (UserSettings, False),
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
