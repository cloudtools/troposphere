# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer


class ResourceSpec(AWSProperty):
    props = {
        'InstanceType': (str, False),
        'SageMakerImageArn': (str, False),
        'SageMakerImageVersionArn': (str, False),
    }


class App(AWSObject):
    resource_type = "AWS::SageMaker::App"

    props = {
        'AppName': (str, True),
        'AppType': (str, True),
        'DomainId': (str, True),
        'ResourceSpec': (ResourceSpec, False),
        'Tags': (Tags, False),
        'UserProfileName': (str, True),
    }


class FileSystemConfig(AWSProperty):
    props = {
        'DefaultGid': (integer, False),
        'DefaultUid': (integer, False),
        'MountPath': (str, False),
    }


class KernelSpec(AWSProperty):
    props = {
        'DisplayName': (str, False),
        'Name': (str, True),
    }


class KernelGatewayImageConfig(AWSProperty):
    props = {
        'FileSystemConfig': (FileSystemConfig, False),
        'KernelSpecs': ([KernelSpec], True),
    }


class AppImageConfig(AWSObject):
    resource_type = "AWS::SageMaker::AppImageConfig"

    props = {
        'AppImageConfigName': (str, True),
        'KernelGatewayImageConfig': (KernelGatewayImageConfig, False),
        'Tags': (Tags, False),
    }


class GitConfig(AWSProperty):
    props = {
        'Branch': (str, False),
        'RepositoryUrl': (str, True),
        'SecretArn': (str, False),
    }


class CodeRepository(AWSObject):
    resource_type = "AWS::SageMaker::CodeRepository"

    props = {
        'CodeRepositoryName': (str, False),
        'GitConfig': (GitConfig, True),
    }


class DataQualityAppSpecification(AWSProperty):
    props = {
        'ContainerArguments': ([str], False),
        'ContainerEntrypoint': ([str], False),
        'Environment': (dict, False),
        'ImageUri': (str, True),
        'PostAnalyticsProcessorSourceUri': (str, False),
        'RecordPreprocessorSourceUri': (str, False),
    }


class ConstraintsResource(AWSProperty):
    props = {
        'S3Uri': (str, False),
    }


class StatisticsResource(AWSProperty):
    props = {
        'S3Uri': (str, False),
    }


class DataQualityBaselineConfig(AWSProperty):
    props = {
        'BaseliningJobName': (str, False),
        'ConstraintsResource': (ConstraintsResource, False),
        'StatisticsResource': (StatisticsResource, False),
    }


class EndpointInput(AWSProperty):
    props = {
        'EndpointName': (str, True),
        'LocalPath': (str, True),
        'S3DataDistributionType': (str, False),
        'S3InputMode': (str, False),
    }


class DataQualityJobInput(AWSProperty):
    props = {
        'EndpointInput': (EndpointInput, True),
    }


class S3Output(AWSProperty):
    props = {
        'LocalPath': (str, True),
        'S3UploadMode': (str, False),
        'S3Uri': (str, True),
    }


class MonitoringOutput(AWSProperty):
    props = {
        'S3Output': (S3Output, True),
    }


class MonitoringOutputConfig(AWSProperty):
    props = {
        'KmsKeyId': (str, False),
        'MonitoringOutputs': ([MonitoringOutput], True),
    }


class ClusterConfig(AWSProperty):
    props = {
        'InstanceCount': (integer, True),
        'InstanceType': (str, True),
        'VolumeKmsKeyId': (str, False),
        'VolumeSizeInGB': (integer, True),
    }


class MonitoringResources(AWSProperty):
    props = {
        'ClusterConfig': (ClusterConfig, True),
    }


class VpcConfig(AWSProperty):
    props = {
        'Subnets': ([str], True),
        'SecurityGroupIds': ([str], True),
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
        'JobDefinitionName': (str, False),
        'JobResources': (MonitoringResources, True),
        'NetworkConfig': (NetworkConfig, False),
        'RoleArn': (str, True),
        'StoppingCondition': (StoppingCondition, False),
        'Tags': (Tags, False),
    }


class Device(AWSObject):
    resource_type = "AWS::SageMaker::Device"

    props = {
        'Device': (dict, False),
        'DeviceFleetName': (str, True),
        'Tags': (Tags, False),
    }


class EdgeOutputConfig(AWSProperty):
    props = {
        'KmsKeyId': (str, False),
        'S3OutputLocation': (str, True),
    }


class DeviceFleet(AWSObject):
    resource_type = "AWS::SageMaker::DeviceFleet"

    props = {
        'Description': (str, False),
        'DeviceFleetName': (str, True),
        'OutputConfig': (EdgeOutputConfig, True),
        'RoleArn': (str, True),
        'Tags': (Tags, False),
    }


class JupyterServerAppSettings(AWSProperty):
    props = {
        'DefaultResourceSpec': (ResourceSpec, False),
    }


class CustomImage(AWSProperty):
    props = {
        'AppImageConfigName': (str, True),
        'ImageName': (str, True),
        'ImageVersionNumber': (integer, False),
    }


class KernelGatewayAppSettings(AWSProperty):
    props = {
        'CustomImages': ([CustomImage], False),
        'DefaultResourceSpec': (ResourceSpec, False),
    }


class SharingSettings(AWSProperty):
    props = {
        'NotebookOutputOption': (str, False),
        'S3KmsKeyId': (str, False),
        'S3OutputPath': (str, False),
    }


class UserSettings(AWSProperty):
    props = {
        'ExecutionRole': (str, False),
        'JupyterServerAppSettings': (JupyterServerAppSettings, False),
        'KernelGatewayAppSettings': (KernelGatewayAppSettings, False),
        'SecurityGroups': ([str], False),
        'SharingSettings': (SharingSettings, False),
    }


class Domain(AWSObject):
    resource_type = "AWS::SageMaker::Domain"

    props = {
        'AppNetworkAccessType': (str, False),
        'AuthMode': (str, True),
        'DefaultUserSettings': (UserSettings, True),
        'DomainName': (str, True),
        'KmsKeyId': (str, False),
        'SubnetIds': ([str], True),
        'Tags': (Tags, False),
        'VpcId': (str, True),
    }


class Alarm(AWSProperty):
    props = {
        'AlarmName': (str, True),
    }


class AutoRollbackConfig(AWSProperty):
    props = {
        'Alarms': ([Alarm], True),
    }


class CapacitySize(AWSProperty):
    props = {
        'Type': (str, True),
        'Value': (integer, True),
    }


class TrafficRoutingConfig(AWSProperty):
    props = {
        'CanarySize': (CapacitySize, False),
        'Type': (str, True),
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
        'VariantPropertyType': (str, False),
    }


class Endpoint(AWSObject):
    resource_type = "AWS::SageMaker::Endpoint"

    props = {
        'DeploymentConfig': (DeploymentConfig, False),
        'EndpointConfigName': (str, True),
        'EndpointName': (str, False),
        'ExcludeRetainedVariantProperties': ([VariantProperty], False),
        'RetainAllVariantProperties': (boolean, False),
        'Tags': (Tags, False),
    }


class CaptureContentTypeHeader(AWSProperty):
    props = {
        'CsvContentTypes': ([str], False),
        'JsonContentTypes': ([str], False),
    }


class CaptureOption(AWSProperty):
    props = {
        'CaptureMode': (str, True),
    }


class DataCaptureConfig(AWSProperty):
    props = {
        'CaptureContentTypeHeader': (CaptureContentTypeHeader, False),
        'CaptureOptions': ([CaptureOption], True),
        'DestinationS3Uri': (str, True),
        'EnableCapture': (boolean, False),
        'InitialSamplingPercentage': (integer, True),
        'KmsKeyId': (str, False),
    }


class ProductionVariant(AWSProperty):
    props = {
        'ModelName': (str, True),
        'VariantName': (str, True),
        'InitialInstanceCount': (integer, True),
        'InstanceType': (str, True),
        'InitialVariantWeight': (float, True)
    }


class EndpointConfig(AWSObject):
    resource_type = "AWS::SageMaker::EndpointConfig"

    props = {
        'DataCaptureConfig': (DataCaptureConfig, False),
        'EndpointConfigName': (str, False),
        'KmsKeyId': (str, False),
        'ProductionVariants': ([ProductionVariant], True),
        'Tags': (Tags, False),
    }


class FeatureDefinition(AWSProperty):
    props = {
        'FeatureName': (str, True),
        'FeatureType': (str, True),
    }


class FeatureGroup(AWSObject):
    resource_type = "AWS::SageMaker::FeatureGroup"

    props = {
        'Description': (str, False),
        'EventTimeFeatureName': (str, True),
        'FeatureDefinitions': ([FeatureDefinition], True),
        'FeatureGroupName': (str, True),
        'OfflineStoreConfig': (dict, False),
        'OnlineStoreConfig': (dict, False),
        'RecordIdentifierFeatureName': (str, True),
        'RoleArn': (str, False),
        'Tags': (Tags, False),
    }


class Image(AWSObject):
    resource_type = "AWS::SageMaker::Image"

    props = {
        'ImageDescription': (str, False),
        'ImageDisplayName': (str, False),
        'ImageName': (str, True),
        'ImageRoleArn': (str, True),
        'Tags': (Tags, False),
    }


class ImageVersion(AWSObject):
    resource_type = "AWS::SageMaker::ImageVersion"

    props = {
        'BaseImage': (str, True),
        'ImageName': (str, True),
    }


class ImageConfig(AWSProperty):
    props = {
        'RepositoryAccessMode': (str, True),
    }


class MultiModelConfig(AWSProperty):
    props = {
        'ModelCacheSetting': (str, False),
    }


class ContainerDefinition(AWSProperty):
    props = {
        'ContainerHostname': (str, False),
        'Environment': (dict, False),
        'Image': (str, False),
        'ImageConfig': (ImageConfig, False),
        'Mode': (str, False),
        'ModelDataUrl': (str, False),
        'ModelPackageName': (str, False),
        'MultiModelConfig': (MultiModelConfig, False),
    }


class InferenceExecutionConfig(AWSProperty):
    props = {
        'Mode': (str, True),
    }


class Model(AWSObject):
    resource_type = "AWS::SageMaker::Model"

    props = {
        'Containers': ([ContainerDefinition], False),
        'EnableNetworkIsolation': (boolean, False),
        'ExecutionRoleArn': (str, True),
        'InferenceExecutionConfig': (InferenceExecutionConfig, False),
        'ModelName': (str, False),
        'PrimaryContainer': (ContainerDefinition, False),
        'Tags': (Tags, False),
        'VpcConfig': (VpcConfig, False),
    }


class ModelBiasAppSpecification(AWSProperty):
    props = {
        'ConfigUri': (str, True),
        'Environment': (dict, False),
        'ImageUri': (str, True),
    }


class ModelBiasBaselineConfig(AWSProperty):
    props = {
        'BaseliningJobName': (str, False),
        'ConstraintsResource': (ConstraintsResource, False),
    }


class MonitoringGroundTruthS3Input(AWSProperty):
    props = {
        'S3Uri': (str, True),
    }


class ModelBiasJobInput(AWSProperty):
    props = {
        'EndpointInput': (EndpointInput, True),
        'GroundTruthS3Input': (MonitoringGroundTruthS3Input, True),
    }


class ModelBiasJobDefinition(AWSObject):
    resource_type = "AWS::SageMaker::ModelBiasJobDefinition"

    props = {
        'JobDefinitionName': (str, False),
        'JobResources': (MonitoringResources, True),
        'ModelBiasAppSpecification': (ModelBiasAppSpecification, True),
        'ModelBiasBaselineConfig': (ModelBiasBaselineConfig, False),
        'ModelBiasJobInput': (ModelBiasJobInput, True),
        'ModelBiasJobOutputConfig': (MonitoringOutputConfig, True),
        'NetworkConfig': (NetworkConfig, False),
        'RoleArn': (str, True),
        'StoppingCondition': (StoppingCondition, False),
        'Tags': (Tags, False),
    }


class ModelExplainabilityAppSpecification(AWSProperty):
    props = {
        'ConfigUri': (str, True),
        'Environment': (dict, False),
        'ImageUri': (str, True),
    }


class ModelExplainabilityBaselineConfig(AWSProperty):
    props = {
        'BaseliningJobName': (str, False),
        'ConstraintsResource': (ConstraintsResource, False),
    }


class ModelExplainabilityJobInput(AWSProperty):
    props = {
        'EndpointInput': (EndpointInput, True),
    }


class ModelExplainabilityJobDefinition(AWSObject):
    resource_type = "AWS::SageMaker::ModelExplainabilityJobDefinition"

    props = {
        'JobDefinitionName': (str, False),
        'JobResources': (MonitoringResources, True),
        'ModelExplainabilityAppSpecification':
            (ModelExplainabilityAppSpecification, True),
        'ModelExplainabilityBaselineConfig':
            (ModelExplainabilityBaselineConfig, False),
        'ModelExplainabilityJobInput': (ModelExplainabilityJobInput, True),
        'ModelExplainabilityJobOutputConfig':
            (MonitoringOutputConfig, True),
        'NetworkConfig': (NetworkConfig, False),
        'RoleArn': (str, True),
        'StoppingCondition': (StoppingCondition, False),
        'Tags': (Tags, False),
    }


class ModelPackageGroup(AWSObject):
    resource_type = "AWS::SageMaker::ModelPackageGroup"

    props = {
        'ModelPackageGroupDescription': (str, False),
        'ModelPackageGroupName': (str, True),
        'ModelPackageGroupPolicy': (dict, False),
        'Tags': (Tags, False),
    }


class ModelQualityAppSpecification(AWSProperty):
    props = {
        'ContainerArguments': ([str], False),
        'ContainerEntrypoint': ([str], False),
        'Environment': (dict, False),
        'ImageUri': (str, True),
        'PostAnalyticsProcessorSourceUri': (str, False),
        'ProblemType': (str, True),
        'RecordPreprocessorSourceUri': (str, False),
    }


class ModelQualityBaselineConfig(AWSProperty):
    props = {
        'BaseliningJobName': (str, False),
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
        'JobDefinitionName': (str, False),
        'JobResources': (MonitoringResources, True),
        'ModelQualityAppSpecification':
            (ModelQualityAppSpecification, True),
        'ModelQualityBaselineConfig': (ModelQualityBaselineConfig, False),
        'ModelQualityJobInput': (ModelQualityJobInput, True),
        'ModelQualityJobOutputConfig': (MonitoringOutputConfig, True),
        'NetworkConfig': (NetworkConfig, False),
        'RoleArn': (str, True),
        'StoppingCondition': (StoppingCondition, False),
        'Tags': (Tags, False),
    }


class MonitoringExecutionSummary(AWSProperty):
    props = {
        'CreationTime': (str, True),
        'EndpointName': (str, False),
        'FailureReason': (str, False),
        'LastModifiedTime': (str, True),
        'MonitoringExecutionStatus': (str, True),
        'MonitoringScheduleName': (str, True),
        'ProcessingJobArn': (str, False),
        'ScheduledTime': (str, True),
    }


class BaselineConfig(AWSProperty):
    props = {
        'ConstraintsResource': (ConstraintsResource, False),
        'StatisticsResource': (StatisticsResource, False),
    }


class MonitoringAppSpecification(AWSProperty):
    props = {
        'ContainerArguments': ([str], False),
        'ContainerEntrypoint': ([str], False),
        'ImageUri': (str, True),
        'PostAnalyticsProcessorSourceUri': (str, False),
        'RecordPreprocessorSourceUri': (str, False),
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
        'RoleArn': (str, True),
        'StoppingCondition': (StoppingCondition, False),
    }


class ScheduleConfig(AWSProperty):
    props = {
        'ScheduleExpression': (str, True),
    }


class MonitoringScheduleConfig(AWSProperty):
    props = {
        'MonitoringJobDefinition': (MonitoringJobDefinition, True),
        'ScheduleConfig': (ScheduleConfig, False),
    }


class MonitoringSchedule(AWSObject):
    resource_type = "AWS::SageMaker::MonitoringSchedule"

    props = {
        'CreationTime': (str, False),
        'EndpointName': (str, False),
        'FailureReason': (str, False),
        'LastModifiedTime': (str, False),
        'LastMonitoringExecutionSummary':
            (MonitoringExecutionSummary, False),
        'MonitoringScheduleArn': (str, False),
        'MonitoringScheduleConfig': (MonitoringScheduleConfig, True),
        'MonitoringScheduleName': (str, True),
        'MonitoringScheduleStatus': (str, False),
        'Tags': (Tags, False),
    }


class NotebookInstance(AWSObject):
    resource_type = "AWS::SageMaker::NotebookInstance"

    props = {
        'AcceleratorTypes': ([str], False),
        'AdditionalCodeRepositories': ([str], False),
        'DefaultCodeRepository': (str, False),
        'DirectInternetAccess': (str, False),
        'InstanceType': (str, True),
        'KmsKeyId': (str, False),
        'LifecycleConfigName': (str, False),
        'NotebookInstanceName': (str, False),
        'RoleArn': (str, True),
        'RootAccess': (str, False),
        'SecurityGroupIds': ([str], False),
        'SubnetId': (str, False),
        'Tags': (Tags, False),
        'VolumeSizeInGB': (integer, False),
    }


class NotebookInstanceLifecycleHook(AWSProperty):
    props = {
        'Content': (str, False),
    }


class NotebookInstanceLifecycleConfig(AWSObject):
    resource_type = "AWS::SageMaker::NotebookInstanceLifecycleConfig"

    props = {
        'NotebookInstanceLifecycleConfigName': (str, False),
        'OnCreate': ([NotebookInstanceLifecycleHook], False),
        'OnStart': ([NotebookInstanceLifecycleHook], False),
    }


class Pipeline(AWSObject):
    resource_type = "AWS::SageMaker::Pipeline"

    props = {
        'PipelineDefinition': (dict, True),
        'PipelineDescription': (str, False),
        'PipelineDisplayName': (str, False),
        'PipelineName': (str, True),
        'RoleArn': (str, True),
        'Tags': (Tags, False),
    }


class Project(AWSObject):
    resource_type = "AWS::SageMaker::Project"

    props = {
        'ProjectDescription': (str, False),
        'ProjectName': (str, True),
        'ServiceCatalogProvisioningDetails': (dict, True),
        'Tags': (Tags, False),
    }


class UserProfile(AWSObject):
    resource_type = "AWS::SageMaker::UserProfile"

    props = {
        'DomainId': (str, True),
        'SingleSignOnUserIdentifier': (str, False),
        'SingleSignOnUserValue': (str, False),
        'Tags': (Tags, False),
        'UserProfileName': (str, True),
        'UserSettings': (UserSettings, False),
    }


class CognitoMemberDefinition(AWSProperty):
    props = {
        'CognitoClientId': (str, True),
        'CognitoUserGroup': (str, True),
        'CognitoUserPool': (str, True),
    }


class MemberDefinition(AWSProperty):
    props = {
        'CognitoMemberDefinition': (CognitoMemberDefinition, True),
    }


class NotificationConfiguration(AWSProperty):
    props = {
        'NotificationTopicArn': (str, True),
    }


class Workteam(AWSObject):
    resource_type = "AWS::SageMaker::Workteam"

    props = {
        'Description': (str, False),
        'MemberDefinitions': ([MemberDefinition], False),
        'NotificationConfiguration': (NotificationConfiguration, False),
        'Tags': (Tags, False),
        'WorkteamName': (str, False),
    }
