# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.ecs import LAUNCH_TYPE_EC2  # noqa: F401
from .validators.ecs import LAUNCH_TYPE_FARGATE  # noqa: F401
from .validators.ecs import RUNTIME_PLATFORM_CPU_CONFIGURATIONS  # noqa: F401
from .validators.ecs import RUNTIME_PLATFORM_OS_FAMILY  # noqa: F401
from .validators.ecs import SCHEDULING_STRATEGY_DAEMON  # noqa: F401
from .validators.ecs import SCHEDULING_STRATEGY_REPLICA  # noqa: F401
from .validators.ecs import (
    ecs_efs_encryption_status,
    ecs_proxy_type,
    launch_type_validator,
    placement_constraint_validator,
    placement_strategy_validator,
    scope_validator,
    validate_ephemeral_storage_size,
    validate_network_port,
    validate_runtime_platform,
    validate_scaling_step_size,
    validate_target_capacity,
    validate_transit_encryption_port,
)


class ManagedScaling(AWSProperty):
    """
    `ManagedScaling <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html>`__
    """

    props: PropsDictType = {
        "InstanceWarmupPeriod": (integer, False),
        "MaximumScalingStepSize": (validate_scaling_step_size, False),
        "MinimumScalingStepSize": (validate_scaling_step_size, False),
        "Status": (str, False),
        "TargetCapacity": (validate_target_capacity, False),
    }


class AutoScalingGroupProvider(AWSProperty):
    """
    `AutoScalingGroupProvider <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-autoscalinggroupprovider.html>`__
    """

    props: PropsDictType = {
        "AutoScalingGroupArn": (str, True),
        "ManagedDraining": (str, False),
        "ManagedScaling": (ManagedScaling, False),
        "ManagedTerminationProtection": (str, False),
    }


class CapacityProvider(AWSObject):
    """
    `CapacityProvider <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-capacityprovider.html>`__
    """

    resource_type = "AWS::ECS::CapacityProvider"

    props: PropsDictType = {
        "AutoScalingGroupProvider": (AutoScalingGroupProvider, True),
        "Name": (str, False),
        "Tags": (Tags, False),
    }


class CapacityProviderStrategyItem(AWSProperty):
    """
    `CapacityProviderStrategyItem <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-capacityproviderstrategyitem.html>`__
    """

    props: PropsDictType = {
        "Base": (integer, False),
        "CapacityProvider": (str, False),
        "Weight": (integer, False),
    }


class ExecuteCommandLogConfiguration(AWSProperty):
    """
    `ExecuteCommandLogConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html>`__
    """

    props: PropsDictType = {
        "CloudWatchEncryptionEnabled": (boolean, False),
        "CloudWatchLogGroupName": (str, False),
        "S3BucketName": (str, False),
        "S3EncryptionEnabled": (boolean, False),
        "S3KeyPrefix": (str, False),
    }


class ExecuteCommandConfiguration(AWSProperty):
    """
    `ExecuteCommandConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandconfiguration.html>`__
    """

    props: PropsDictType = {
        "KmsKeyId": (str, False),
        "LogConfiguration": (ExecuteCommandLogConfiguration, False),
        "Logging": (str, False),
    }


class ManagedStorageConfiguration(AWSProperty):
    """
    `ManagedStorageConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-managedstorageconfiguration.html>`__
    """

    props: PropsDictType = {
        "FargateEphemeralStorageKmsKeyId": (str, False),
        "KmsKeyId": (str, False),
    }


class ClusterConfiguration(AWSProperty):
    """
    `ClusterConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clusterconfiguration.html>`__
    """

    props: PropsDictType = {
        "ExecuteCommandConfiguration": (ExecuteCommandConfiguration, False),
        "ManagedStorageConfiguration": (ManagedStorageConfiguration, False),
    }


class ClusterSetting(AWSProperty):
    """
    `ClusterSetting <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersettings.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Value": (str, False),
    }


class ServiceConnectDefaults(AWSProperty):
    """
    `ServiceConnectDefaults <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-serviceconnectdefaults.html>`__
    """

    props: PropsDictType = {
        "Namespace": (str, False),
    }


class Cluster(AWSObject):
    """
    `Cluster <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html>`__
    """

    resource_type = "AWS::ECS::Cluster"

    props: PropsDictType = {
        "CapacityProviders": ([str], False),
        "ClusterName": (str, False),
        "ClusterSettings": ([ClusterSetting], False),
        "Configuration": (ClusterConfiguration, False),
        "DefaultCapacityProviderStrategy": ([CapacityProviderStrategyItem], False),
        "ServiceConnectDefaults": (ServiceConnectDefaults, False),
        "Tags": (Tags, False),
    }


class CapacityProviderStrategy(AWSProperty):
    """
    `CapacityProviderStrategy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-clustercapacityproviderassociations-capacityproviderstrategy.html>`__
    """

    props: PropsDictType = {
        "Base": (integer, False),
        "CapacityProvider": (str, True),
        "Weight": (integer, False),
    }


class ClusterCapacityProviderAssociations(AWSObject):
    """
    `ClusterCapacityProviderAssociations <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-clustercapacityproviderassociations.html>`__
    """

    resource_type = "AWS::ECS::ClusterCapacityProviderAssociations"

    props: PropsDictType = {
        "CapacityProviders": ([str], True),
        "Cluster": (str, True),
        "DefaultCapacityProviderStrategy": ([CapacityProviderStrategy], True),
    }


class PrimaryTaskSet(AWSObject):
    """
    `PrimaryTaskSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-primarytaskset.html>`__
    """

    resource_type = "AWS::ECS::PrimaryTaskSet"

    props: PropsDictType = {
        "Cluster": (str, True),
        "Service": (str, True),
        "TaskSetId": (str, True),
    }


class DeploymentAlarms(AWSProperty):
    """
    `DeploymentAlarms <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentalarms.html>`__
    """

    props: PropsDictType = {
        "AlarmNames": ([str], True),
        "Enable": (boolean, True),
        "Rollback": (boolean, True),
    }


class DeploymentCircuitBreaker(AWSProperty):
    """
    `DeploymentCircuitBreaker <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentcircuitbreaker.html>`__
    """

    props: PropsDictType = {
        "Enable": (boolean, True),
        "Rollback": (boolean, True),
    }


class DeploymentConfiguration(AWSProperty):
    """
    `DeploymentConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentconfiguration.html>`__
    """

    props: PropsDictType = {
        "Alarms": (DeploymentAlarms, False),
        "DeploymentCircuitBreaker": (DeploymentCircuitBreaker, False),
        "MaximumPercent": (integer, False),
        "MinimumHealthyPercent": (integer, False),
    }


class DeploymentController(AWSProperty):
    """
    `DeploymentController <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentcontroller.html>`__
    """

    props: PropsDictType = {
        "Type": (str, False),
    }


class LoadBalancer(AWSProperty):
    """
    `LoadBalancer <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-loadbalancer.html>`__
    """

    props: PropsDictType = {
        "ContainerName": (str, False),
        "ContainerPort": (validate_network_port, False),
        "LoadBalancerName": (str, False),
        "TargetGroupArn": (str, False),
    }


class AwsvpcConfiguration(AWSProperty):
    """
    `AwsvpcConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-awsvpcconfiguration.html>`__
    """

    props: PropsDictType = {
        "AssignPublicIp": (str, False),
        "SecurityGroups": ([str], False),
        "Subnets": ([str], False),
    }


class NetworkConfiguration(AWSProperty):
    """
    `NetworkConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-networkconfiguration.html>`__
    """

    props: PropsDictType = {
        "AwsvpcConfiguration": (AwsvpcConfiguration, False),
    }


class PlacementConstraint(AWSProperty):
    """
    `PlacementConstraint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-taskdefinitionplacementconstraint.html>`__
    """

    props: PropsDictType = {
        "Expression": (str, False),
        "Type": (placement_constraint_validator, True),
    }


class PlacementStrategy(AWSProperty):
    """
    `PlacementStrategy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-placementstrategy.html>`__
    """

    props: PropsDictType = {
        "Field": (str, False),
        "Type": (placement_strategy_validator, True),
    }


class Secret(AWSProperty):
    """
    `Secret <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-secret.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "ValueFrom": (str, True),
    }


class LogConfiguration(AWSProperty):
    """
    `LogConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-logconfiguration.html>`__
    """

    props: PropsDictType = {
        "LogDriver": (str, True),
        "Options": (dict, False),
        "SecretOptions": ([Secret], False),
    }


class ServiceConnectClientAlias(AWSProperty):
    """
    `ServiceConnectClientAlias <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectclientalias.html>`__
    """

    props: PropsDictType = {
        "DnsName": (str, False),
        "Port": (integer, True),
    }


class ServiceConnectTlsCertificateAuthority(AWSProperty):
    """
    `ServiceConnectTlsCertificateAuthority <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnecttlscertificateauthority.html>`__
    """

    props: PropsDictType = {
        "AwsPcaAuthorityArn": (str, False),
    }


class ServiceConnectTlsConfiguration(AWSProperty):
    """
    `ServiceConnectTlsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnecttlsconfiguration.html>`__
    """

    props: PropsDictType = {
        "IssuerCertificateAuthority": (ServiceConnectTlsCertificateAuthority, True),
        "KmsKey": (str, False),
        "RoleArn": (str, False),
    }


class TimeoutConfiguration(AWSProperty):
    """
    `TimeoutConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-timeoutconfiguration.html>`__
    """

    props: PropsDictType = {
        "IdleTimeoutSeconds": (integer, False),
        "PerRequestTimeoutSeconds": (integer, False),
    }


class ServiceConnectService(AWSProperty):
    """
    `ServiceConnectService <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectservice.html>`__
    """

    props: PropsDictType = {
        "ClientAliases": ([ServiceConnectClientAlias], False),
        "DiscoveryName": (str, False),
        "IngressPortOverride": (integer, False),
        "PortName": (str, True),
        "Timeout": (TimeoutConfiguration, False),
        "Tls": (ServiceConnectTlsConfiguration, False),
    }


class ServiceConnectConfiguration(AWSProperty):
    """
    `ServiceConnectConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectconfiguration.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, True),
        "LogConfiguration": (LogConfiguration, False),
        "Namespace": (str, False),
        "Services": ([ServiceConnectService], False),
    }


class ServiceRegistry(AWSProperty):
    """
    `ServiceRegistry <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-serviceregistry.html>`__
    """

    props: PropsDictType = {
        "ContainerName": (str, False),
        "ContainerPort": (integer, False),
        "Port": (integer, False),
        "RegistryArn": (str, False),
    }


class EBSTagSpecification(AWSProperty):
    """
    `EBSTagSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-ebstagspecification.html>`__
    """

    props: PropsDictType = {
        "PropagateTags": (str, False),
        "ResourceType": (str, True),
        "Tags": (Tags, False),
    }


class ServiceManagedEBSVolumeConfiguration(AWSProperty):
    """
    `ServiceManagedEBSVolumeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-servicemanagedebsvolumeconfiguration.html>`__
    """

    props: PropsDictType = {
        "Encrypted": (boolean, False),
        "FilesystemType": (str, False),
        "Iops": (integer, False),
        "KmsKeyId": (str, False),
        "RoleArn": (str, True),
        "SizeInGiB": (integer, False),
        "SnapshotId": (str, False),
        "TagSpecifications": ([EBSTagSpecification], False),
        "Throughput": (integer, False),
        "VolumeType": (str, False),
    }


class ServiceVolumeConfiguration(AWSProperty):
    """
    `ServiceVolumeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-servicevolumeconfiguration.html>`__
    """

    props: PropsDictType = {
        "ManagedEBSVolume": (ServiceManagedEBSVolumeConfiguration, False),
        "Name": (str, True),
    }


class Service(AWSObject):
    """
    `Service <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html>`__
    """

    resource_type = "AWS::ECS::Service"

    props: PropsDictType = {
        "CapacityProviderStrategy": ([CapacityProviderStrategyItem], False),
        "Cluster": (str, False),
        "DeploymentConfiguration": (DeploymentConfiguration, False),
        "DeploymentController": (DeploymentController, False),
        "DesiredCount": (integer, False),
        "EnableECSManagedTags": (boolean, False),
        "EnableExecuteCommand": (boolean, False),
        "HealthCheckGracePeriodSeconds": (integer, False),
        "LaunchType": (launch_type_validator, False),
        "LoadBalancers": ([LoadBalancer], False),
        "NetworkConfiguration": (NetworkConfiguration, False),
        "PlacementConstraints": ([PlacementConstraint], False),
        "PlacementStrategies": ([PlacementStrategy], False),
        "PlatformVersion": (str, False),
        "PropagateTags": (str, False),
        "Role": (str, False),
        "SchedulingStrategy": (str, False),
        "ServiceConnectConfiguration": (ServiceConnectConfiguration, False),
        "ServiceName": (str, False),
        "ServiceRegistries": ([ServiceRegistry], False),
        "Tags": (Tags, False),
        "TaskDefinition": (str, False),
        "VolumeConfigurations": ([ServiceVolumeConfiguration], False),
    }


class ContainerDependency(AWSProperty):
    """
    `ContainerDependency <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdependency.html>`__
    """

    props: PropsDictType = {
        "Condition": (str, False),
        "ContainerName": (str, False),
    }


class Environment(AWSProperty):
    """
    `Environment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-keyvaluepair.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Value": (str, False),
    }


class EnvironmentFile(AWSProperty):
    """
    `EnvironmentFile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-environmentfile.html>`__
    """

    props: PropsDictType = {
        "Type": (str, False),
        "Value": (str, False),
    }


class FirelensConfiguration(AWSProperty):
    """
    `FirelensConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-firelensconfiguration.html>`__
    """

    props: PropsDictType = {
        "Options": (dict, False),
        "Type": (str, False),
    }


class HealthCheck(AWSProperty):
    """
    `HealthCheck <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-healthcheck.html>`__
    """

    props: PropsDictType = {
        "Command": ([str], False),
        "Interval": (integer, False),
        "Retries": (integer, False),
        "StartPeriod": (integer, False),
        "Timeout": (integer, False),
    }


class HostEntry(AWSProperty):
    """
    `HostEntry <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-hostentry.html>`__
    """

    props: PropsDictType = {
        "Hostname": (str, False),
        "IpAddress": (str, False),
    }


class Device(AWSProperty):
    """
    `Device <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-device.html>`__
    """

    props: PropsDictType = {
        "ContainerPath": (str, False),
        "HostPath": (str, False),
        "Permissions": ([str], False),
    }


class KernelCapabilities(AWSProperty):
    """
    `KernelCapabilities <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-kernelcapabilities.html>`__
    """

    props: PropsDictType = {
        "Add": ([str], False),
        "Drop": ([str], False),
    }


class Tmpfs(AWSProperty):
    """
    `Tmpfs <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-tmpfs.html>`__
    """

    props: PropsDictType = {
        "ContainerPath": (str, False),
        "MountOptions": ([str], False),
        "Size": (integer, True),
    }


class LinuxParameters(AWSProperty):
    """
    `LinuxParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html>`__
    """

    props: PropsDictType = {
        "Capabilities": (KernelCapabilities, False),
        "Devices": ([Device], False),
        "InitProcessEnabled": (boolean, False),
        "MaxSwap": (integer, False),
        "SharedMemorySize": (integer, False),
        "Swappiness": (integer, False),
        "Tmpfs": ([Tmpfs], False),
    }


class MountPoint(AWSProperty):
    """
    `MountPoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-mountpoint.html>`__
    """

    props: PropsDictType = {
        "ContainerPath": (str, False),
        "ReadOnly": (boolean, False),
        "SourceVolume": (str, False),
    }


class PortMapping(AWSProperty):
    """
    `PortMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-portmapping.html>`__
    """

    props: PropsDictType = {
        "AppProtocol": (str, False),
        "ContainerPort": (validate_network_port, False),
        "ContainerPortRange": (str, False),
        "HostPort": (validate_network_port, False),
        "Name": (str, False),
        "Protocol": (str, False),
    }


class RepositoryCredentials(AWSProperty):
    """
    `RepositoryCredentials <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-repositorycredentials.html>`__
    """

    props: PropsDictType = {
        "CredentialsParameter": (str, False),
    }


class ResourceRequirement(AWSProperty):
    """
    `ResourceRequirement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-resourcerequirement.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
        "Value": (str, True),
    }


class SystemControl(AWSProperty):
    """
    `SystemControl <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-systemcontrol.html>`__
    """

    props: PropsDictType = {
        "Namespace": (str, False),
        "Value": (str, False),
    }


class Ulimit(AWSProperty):
    """
    `Ulimit <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-ulimit.html>`__
    """

    props: PropsDictType = {
        "HardLimit": (integer, True),
        "Name": (str, True),
        "SoftLimit": (integer, True),
    }


class VolumesFrom(AWSProperty):
    """
    `VolumesFrom <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volumefrom.html>`__
    """

    props: PropsDictType = {
        "ReadOnly": (boolean, False),
        "SourceContainer": (str, False),
    }


class ContainerDefinition(AWSProperty):
    """
    `ContainerDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinition.html>`__
    """

    props: PropsDictType = {
        "Command": ([str], False),
        "Cpu": (integer, False),
        "CredentialSpecs": ([str], False),
        "DependsOn": ([ContainerDependency], False),
        "DisableNetworking": (boolean, False),
        "DnsSearchDomains": ([str], False),
        "DnsServers": ([str], False),
        "DockerLabels": (dict, False),
        "DockerSecurityOptions": ([str], False),
        "EntryPoint": ([str], False),
        "Environment": ([Environment], False),
        "EnvironmentFiles": ([EnvironmentFile], False),
        "Essential": (boolean, False),
        "ExtraHosts": ([HostEntry], False),
        "FirelensConfiguration": (FirelensConfiguration, False),
        "HealthCheck": (HealthCheck, False),
        "Hostname": (str, False),
        "Image": (str, True),
        "Interactive": (boolean, False),
        "Links": ([str], False),
        "LinuxParameters": (LinuxParameters, False),
        "LogConfiguration": (LogConfiguration, False),
        "Memory": (integer, False),
        "MemoryReservation": (integer, False),
        "MountPoints": ([MountPoint], False),
        "Name": (str, True),
        "PortMappings": ([PortMapping], False),
        "Privileged": (boolean, False),
        "PseudoTerminal": (boolean, False),
        "ReadonlyRootFilesystem": (boolean, False),
        "RepositoryCredentials": (RepositoryCredentials, False),
        "ResourceRequirements": ([ResourceRequirement], False),
        "Secrets": ([Secret], False),
        "StartTimeout": (integer, False),
        "StopTimeout": (integer, False),
        "SystemControls": ([SystemControl], False),
        "Ulimits": ([Ulimit], False),
        "User": (str, False),
        "VolumesFrom": ([VolumesFrom], False),
        "WorkingDirectory": (str, False),
    }


class EphemeralStorage(AWSProperty):
    """
    `EphemeralStorage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-ephemeralstorage.html>`__
    """

    props: PropsDictType = {
        "SizeInGiB": (validate_ephemeral_storage_size, False),
    }


class InferenceAccelerator(AWSProperty):
    """
    `InferenceAccelerator <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-inferenceaccelerator.html>`__
    """

    props: PropsDictType = {
        "DeviceName": (str, False),
        "DeviceType": (str, False),
    }


class ProxyConfiguration(AWSProperty):
    """
    `ProxyConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-proxyconfiguration.html>`__
    """

    props: PropsDictType = {
        "ContainerName": (str, True),
        "ProxyConfigurationProperties": (list, False),
        "Type": (ecs_proxy_type, False),
    }


class RuntimePlatform(AWSProperty):
    """
    `RuntimePlatform <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-runtimeplatform.html>`__
    """

    props: PropsDictType = {
        "CpuArchitecture": (str, False),
        "OperatingSystemFamily": (str, False),
    }

    def validate(self):
        validate_runtime_platform(self)


class DockerVolumeConfiguration(AWSProperty):
    """
    `DockerVolumeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html>`__
    """

    props: PropsDictType = {
        "Autoprovision": (boolean, False),
        "Driver": (str, False),
        "DriverOpts": (dict, False),
        "Labels": (dict, False),
        "Scope": (scope_validator, False),
    }


class AuthorizationConfig(AWSProperty):
    """
    `AuthorizationConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-authorizationconfig.html>`__
    """

    props: PropsDictType = {
        "AccessPointId": (str, False),
        "IAM": (str, False),
    }


class EFSVolumeConfiguration(AWSProperty):
    """
    `EFSVolumeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html>`__
    """

    props: PropsDictType = {
        "AuthorizationConfig": (AuthorizationConfig, False),
        "FilesystemId": (str, True),
        "RootDirectory": (str, False),
        "TransitEncryption": (ecs_efs_encryption_status, False),
        "TransitEncryptionPort": (validate_transit_encryption_port, False),
    }


class FSxAuthorizationConfig(AWSProperty):
    """
    `FSxAuthorizationConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-fsxauthorizationconfig.html>`__
    """

    props: PropsDictType = {
        "CredentialsParameter": (str, True),
        "Domain": (str, True),
    }


class FSxWindowsFileServerVolumeConfiguration(AWSProperty):
    """
    `FSxWindowsFileServerVolumeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-fsxwindowsfileservervolumeconfiguration.html>`__
    """

    props: PropsDictType = {
        "AuthorizationConfig": (FSxAuthorizationConfig, False),
        "FileSystemId": (str, True),
        "RootDirectory": (str, True),
    }


class Host(AWSProperty):
    """
    `Host <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-hostvolumeproperties.html>`__
    """

    props: PropsDictType = {
        "SourcePath": (str, False),
    }


class Volume(AWSProperty):
    """
    `Volume <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volume.html>`__
    """

    props: PropsDictType = {
        "ConfiguredAtLaunch": (boolean, False),
        "DockerVolumeConfiguration": (DockerVolumeConfiguration, False),
        "EFSVolumeConfiguration": (EFSVolumeConfiguration, False),
        "FSxWindowsFileServerVolumeConfiguration": (
            FSxWindowsFileServerVolumeConfiguration,
            False,
        ),
        "Host": (Host, False),
        "Name": (str, False),
    }


class TaskDefinition(AWSObject):
    """
    `TaskDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html>`__
    """

    resource_type = "AWS::ECS::TaskDefinition"

    props: PropsDictType = {
        "ContainerDefinitions": ([ContainerDefinition], False),
        "Cpu": (str, False),
        "EphemeralStorage": (EphemeralStorage, False),
        "ExecutionRoleArn": (str, False),
        "Family": (str, False),
        "InferenceAccelerators": ([InferenceAccelerator], False),
        "IpcMode": (str, False),
        "Memory": (str, False),
        "NetworkMode": (str, False),
        "PidMode": (str, False),
        "PlacementConstraints": ([PlacementConstraint], False),
        "ProxyConfiguration": (ProxyConfiguration, False),
        "RequiresCompatibilities": ([str], False),
        "RuntimePlatform": (RuntimePlatform, False),
        "Tags": (Tags, False),
        "TaskRoleArn": (str, False),
        "Volumes": ([Volume], False),
    }


class Scale(AWSProperty):
    """
    `Scale <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-scale.html>`__
    """

    props: PropsDictType = {
        "Unit": (str, False),
        "Value": (double, False),
    }


class TaskSet(AWSObject):
    """
    `TaskSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html>`__
    """

    resource_type = "AWS::ECS::TaskSet"

    props: PropsDictType = {
        "Cluster": (str, True),
        "ExternalId": (str, False),
        "LaunchType": (str, False),
        "LoadBalancers": ([LoadBalancer], False),
        "NetworkConfiguration": (NetworkConfiguration, False),
        "PlatformVersion": (str, False),
        "Scale": (Scale, False),
        "Service": (str, True),
        "ServiceRegistries": ([ServiceRegistry], False),
        "Tags": (Tags, False),
        "TaskDefinition": (str, True),
    }
