# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.rds import (
    validate_backtrack_window,
    validate_backup_retention_period,
    validate_backup_window,
    validate_capacity,
    validate_dbinstance,
    validate_engine,
    validate_engine_mode,
    validate_iops,
    validate_license_model,
    validate_network_port,
    validate_str_or_int,
    validate_tags_or_list,
    validate_v2_capacity,
    validate_v2_max_capacity,
)


class CustomDBEngineVersion(AWSObject):
    """
    `CustomDBEngineVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-customdbengineversion.html>`__
    """

    resource_type = "AWS::RDS::CustomDBEngineVersion"

    props: PropsDictType = {
        "DatabaseInstallationFilesS3BucketName": (str, False),
        "DatabaseInstallationFilesS3Prefix": (str, False),
        "Description": (str, False),
        "Engine": (str, True),
        "EngineVersion": (str, True),
        "ImageId": (str, False),
        "KMSKeyId": (str, False),
        "Manifest": (str, False),
        "SourceCustomDbEngineVersionIdentifier": (str, False),
        "Status": (str, False),
        "Tags": (Tags, False),
        "UseAwsProvidedLatestImage": (boolean, False),
    }


class DBClusterRole(AWSProperty):
    """
    `DBClusterRole <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-dbclusterrole.html>`__
    """

    props: PropsDictType = {
        "FeatureName": (str, False),
        "RoleArn": (str, True),
    }


class MasterUserSecret(AWSProperty):
    """
    `MasterUserSecret <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-masterusersecret.html>`__
    """

    props: PropsDictType = {
        "KmsKeyId": (str, False),
        "SecretArn": (str, False),
    }


class ScalingConfiguration(AWSProperty):
    """
    `ScalingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-scalingconfiguration.html>`__
    """

    props: PropsDictType = {
        "AutoPause": (boolean, False),
        "MaxCapacity": (validate_capacity, False),
        "MinCapacity": (validate_capacity, False),
        "SecondsBeforeTimeout": (integer, False),
        "SecondsUntilAutoPause": (integer, False),
        "TimeoutAction": (str, False),
    }


class ServerlessV2ScalingConfiguration(AWSProperty):
    """
    `ServerlessV2ScalingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-serverlessv2scalingconfiguration.html>`__
    """

    props: PropsDictType = {
        "MaxCapacity": (validate_v2_max_capacity, False),
        "MinCapacity": (validate_v2_capacity, False),
        "SecondsUntilAutoPause": (integer, False),
    }


class DBCluster(AWSObject):
    """
    `DBCluster <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html>`__
    """

    resource_type = "AWS::RDS::DBCluster"

    props: PropsDictType = {
        "AllocatedStorage": (integer, False),
        "AssociatedRoles": ([DBClusterRole], False),
        "AutoMinorVersionUpgrade": (boolean, False),
        "AvailabilityZones": ([str], False),
        "BacktrackWindow": (validate_backtrack_window, False),
        "BackupRetentionPeriod": (validate_backup_retention_period, False),
        "ClusterScalabilityType": (str, False),
        "CopyTagsToSnapshot": (boolean, False),
        "DBClusterIdentifier": (str, False),
        "DBClusterInstanceClass": (str, False),
        "DBClusterParameterGroupName": (str, False),
        "DBInstanceParameterGroupName": (str, False),
        "DBSubnetGroupName": (str, False),
        "DBSystemId": (str, False),
        "DatabaseInsightsMode": (str, False),
        "DatabaseName": (str, False),
        "DeleteAutomatedBackups": (boolean, False),
        "DeletionProtection": (boolean, False),
        "Domain": (str, False),
        "DomainIAMRoleName": (str, False),
        "EnableCloudwatchLogsExports": ([str], False),
        "EnableGlobalWriteForwarding": (boolean, False),
        "EnableHttpEndpoint": (boolean, False),
        "EnableIAMDatabaseAuthentication": (boolean, False),
        "EnableLocalWriteForwarding": (boolean, False),
        "Engine": (validate_engine, False),
        "EngineLifecycleSupport": (str, False),
        "EngineMode": (validate_engine_mode, False),
        "EngineVersion": (str, False),
        "GlobalClusterIdentifier": (str, False),
        "Iops": (integer, False),
        "KmsKeyId": (str, False),
        "ManageMasterUserPassword": (boolean, False),
        "MasterUserPassword": (str, False),
        "MasterUserSecret": (MasterUserSecret, False),
        "MasterUsername": (str, False),
        "MonitoringInterval": (integer, False),
        "MonitoringRoleArn": (str, False),
        "NetworkType": (str, False),
        "PerformanceInsightsEnabled": (boolean, False),
        "PerformanceInsightsKmsKeyId": (str, False),
        "PerformanceInsightsRetentionPeriod": (integer, False),
        "Port": (validate_network_port, False),
        "PreferredBackupWindow": (validate_backup_window, False),
        "PreferredMaintenanceWindow": (str, False),
        "PubliclyAccessible": (boolean, False),
        "ReplicationSourceIdentifier": (str, False),
        "RestoreToTime": (str, False),
        "RestoreType": (str, False),
        "ScalingConfiguration": (ScalingConfiguration, False),
        "ServerlessV2ScalingConfiguration": (ServerlessV2ScalingConfiguration, False),
        "SnapshotIdentifier": (str, False),
        "SourceDBClusterIdentifier": (str, False),
        "SourceRegion": (str, False),
        "StorageEncrypted": (boolean, False),
        "StorageType": (str, False),
        "Tags": (validate_tags_or_list, False),
        "UseLatestRestorableTime": (boolean, False),
        "VpcSecurityGroupIds": ([str], False),
    }


class DBClusterParameterGroup(AWSObject):
    """
    `DBClusterParameterGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html>`__
    """

    resource_type = "AWS::RDS::DBClusterParameterGroup"

    props: PropsDictType = {
        "DBClusterParameterGroupName": (str, False),
        "Description": (str, True),
        "Family": (str, True),
        "Parameters": (dict, True),
        "Tags": (validate_tags_or_list, False),
    }


class CertificateDetails(AWSProperty):
    """
    `CertificateDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-certificatedetails.html>`__
    """

    props: PropsDictType = {
        "CAIdentifier": (str, False),
        "ValidTill": (str, False),
    }


class DBInstanceRole(AWSProperty):
    """
    `DBInstanceRole <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-dbinstancerole.html>`__
    """

    props: PropsDictType = {
        "FeatureName": (str, True),
        "RoleArn": (str, True),
    }


class DBInstanceStatusInfo(AWSProperty):
    """
    `DBInstanceStatusInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-dbinstancestatusinfo.html>`__
    """

    props: PropsDictType = {
        "Message": (str, False),
        "Normal": (boolean, False),
        "Status": (str, False),
        "StatusType": (str, False),
    }


class Endpoint(AWSProperty):
    """
    `Endpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-endpoint.html>`__
    """

    props: PropsDictType = {
        "Address": (str, False),
        "HostedZoneId": (str, False),
        "Port": (str, False),
    }


class ProcessorFeature(AWSProperty):
    """
    `ProcessorFeature <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-processorfeature.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Value": (str, False),
    }


class DBInstance(AWSObject):
    """
    `DBInstance <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html>`__
    """

    resource_type = "AWS::RDS::DBInstance"

    props: PropsDictType = {
        "AllocatedStorage": (validate_str_or_int, False),
        "AllowMajorVersionUpgrade": (boolean, False),
        "ApplyImmediately": (boolean, False),
        "AssociatedRoles": ([DBInstanceRole], False),
        "AutoMinorVersionUpgrade": (boolean, False),
        "AutomaticBackupReplicationKmsKeyId": (str, False),
        "AutomaticBackupReplicationRegion": (str, False),
        "AutomaticBackupReplicationRetentionPeriod": (integer, False),
        "AvailabilityZone": (str, False),
        "BackupRetentionPeriod": (validate_backup_retention_period, False),
        "BackupTarget": (str, False),
        "CACertificateIdentifier": (str, False),
        "CertificateDetails": (CertificateDetails, False),
        "CertificateRotationRestart": (boolean, False),
        "CharacterSetName": (str, False),
        "CopyTagsToSnapshot": (boolean, False),
        "CustomIAMInstanceProfile": (str, False),
        "DBClusterIdentifier": (str, False),
        "DBClusterSnapshotIdentifier": (str, False),
        "DBInstanceClass": (str, False),
        "DBInstanceIdentifier": (str, False),
        "DBName": (str, False),
        "DBParameterGroupName": (str, False),
        "DBSecurityGroups": (list, False),
        "DBSnapshotIdentifier": (str, False),
        "DBSubnetGroupName": (str, False),
        "DBSystemId": (str, False),
        "DatabaseInsightsMode": (str, False),
        "DedicatedLogVolume": (boolean, False),
        "DeleteAutomatedBackups": (boolean, False),
        "DeletionProtection": (boolean, False),
        "Domain": (str, False),
        "DomainAuthSecretArn": (str, False),
        "DomainDnsIps": ([str], False),
        "DomainFqdn": (str, False),
        "DomainIAMRoleName": (str, False),
        "DomainOu": (str, False),
        "EnableCloudwatchLogsExports": ([str], False),
        "EnableIAMDatabaseAuthentication": (boolean, False),
        "EnablePerformanceInsights": (boolean, False),
        "Endpoint": (Endpoint, False),
        "Engine": (validate_engine, False),
        "EngineLifecycleSupport": (str, False),
        "EngineVersion": (str, False),
        "Iops": (validate_iops, False),
        "KmsKeyId": (str, False),
        "LicenseModel": (validate_license_model, False),
        "ManageMasterUserPassword": (boolean, False),
        "MasterUserPassword": (str, False),
        "MasterUserSecret": (MasterUserSecret, False),
        "MasterUsername": (str, False),
        "MaxAllocatedStorage": (integer, False),
        "MonitoringInterval": (integer, False),
        "MonitoringRoleArn": (str, False),
        "MultiAZ": (boolean, False),
        "NcharCharacterSetName": (str, False),
        "NetworkType": (str, False),
        "OptionGroupName": (str, False),
        "PerformanceInsightsKMSKeyId": (str, False),
        "PerformanceInsightsRetentionPeriod": (integer, False),
        "Port": (validate_network_port, False),
        "PreferredBackupWindow": (validate_backup_window, False),
        "PreferredMaintenanceWindow": (str, False),
        "ProcessorFeatures": ([ProcessorFeature], False),
        "PromotionTier": (integer, False),
        "PubliclyAccessible": (boolean, False),
        "ReplicaMode": (str, False),
        "RestoreTime": (str, False),
        "SourceDBClusterIdentifier": (str, False),
        "SourceDBInstanceAutomatedBackupsArn": (str, False),
        "SourceDBInstanceIdentifier": (str, False),
        "SourceDbiResourceId": (str, False),
        "SourceRegion": (str, False),
        "StatusInfos": ([DBInstanceStatusInfo], False),
        "StorageEncrypted": (boolean, False),
        "StorageThroughput": (integer, False),
        "StorageType": (str, False),
        "Tags": (validate_tags_or_list, False),
        "Timezone": (str, False),
        "UseDefaultProcessorFeatures": (boolean, False),
        "UseLatestRestorableTime": (boolean, False),
        "VPCSecurityGroups": ([str], False),
    }

    def validate(self):
        validate_dbinstance(self)


class DBParameterGroup(AWSObject):
    """
    `DBParameterGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbparametergroup.html>`__
    """

    resource_type = "AWS::RDS::DBParameterGroup"

    props: PropsDictType = {
        "DBParameterGroupName": (str, False),
        "Description": (str, True),
        "Family": (str, True),
        "Parameters": (dict, False),
        "Tags": (validate_tags_or_list, False),
    }


class AuthFormat(AWSProperty):
    """
    `AuthFormat <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxy-authformat.html>`__
    """

    props: PropsDictType = {
        "AuthScheme": (str, False),
        "ClientPasswordAuthType": (str, False),
        "Description": (str, False),
        "IAMAuth": (str, False),
        "SecretArn": (str, False),
    }


class DBProxy(AWSObject):
    """
    `DBProxy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxy.html>`__
    """

    resource_type = "AWS::RDS::DBProxy"

    props: PropsDictType = {
        "Auth": ([AuthFormat], True),
        "DBProxyName": (str, True),
        "DebugLogging": (boolean, False),
        "EngineFamily": (str, True),
        "IdleClientTimeout": (integer, False),
        "RequireTLS": (boolean, False),
        "RoleArn": (str, True),
        "Tags": (Tags, False),
        "VpcSecurityGroupIds": ([str], False),
        "VpcSubnetIds": ([str], True),
    }


class DBProxyEndpoint(AWSObject):
    """
    `DBProxyEndpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxyendpoint.html>`__
    """

    resource_type = "AWS::RDS::DBProxyEndpoint"

    props: PropsDictType = {
        "DBProxyEndpointName": (str, True),
        "DBProxyName": (str, True),
        "Tags": (Tags, False),
        "TargetRole": (str, False),
        "VpcSecurityGroupIds": ([str], False),
        "VpcSubnetIds": ([str], True),
    }


class ConnectionPoolConfigurationInfoFormat(AWSProperty):
    """
    `ConnectionPoolConfigurationInfoFormat <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxytargetgroup-connectionpoolconfigurationinfoformat.html>`__
    """

    props: PropsDictType = {
        "ConnectionBorrowTimeout": (integer, False),
        "InitQuery": (str, False),
        "MaxConnectionsPercent": (integer, False),
        "MaxIdleConnectionsPercent": (integer, False),
        "SessionPinningFilters": ([str], False),
    }


class DBProxyTargetGroup(AWSObject):
    """
    `DBProxyTargetGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxytargetgroup.html>`__
    """

    resource_type = "AWS::RDS::DBProxyTargetGroup"

    props: PropsDictType = {
        "ConnectionPoolConfigurationInfo": (
            ConnectionPoolConfigurationInfoFormat,
            False,
        ),
        "DBClusterIdentifiers": ([str], False),
        "DBInstanceIdentifiers": ([str], False),
        "DBProxyName": (str, True),
        "TargetGroupName": (str, True),
    }


class Ingress(AWSProperty):
    """
    `Ingress <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group-rule.html>`__
    """

    props: PropsDictType = {
        "CIDRIP": (str, False),
        "EC2SecurityGroupId": (str, False),
        "EC2SecurityGroupName": (str, False),
        "EC2SecurityGroupOwnerId": (str, False),
    }


class DBSecurityGroup(AWSObject):
    """
    `DBSecurityGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group.html>`__
    """

    resource_type = "AWS::RDS::DBSecurityGroup"

    props: PropsDictType = {
        "DBSecurityGroupIngress": ([Ingress], True),
        "EC2VpcId": (str, False),
        "GroupDescription": (str, True),
        "Tags": (validate_tags_or_list, False),
    }


class DBSecurityGroupIngress(AWSObject):
    """
    `DBSecurityGroupIngress <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html>`__
    """

    resource_type = "AWS::RDS::DBSecurityGroupIngress"

    props: PropsDictType = {
        "CIDRIP": (str, False),
        "DBSecurityGroupName": (str, True),
        "EC2SecurityGroupId": (str, False),
        "EC2SecurityGroupName": (str, False),
        "EC2SecurityGroupOwnerId": (str, False),
    }


class DBShardGroup(AWSObject):
    """
    `DBShardGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbshardgroup.html>`__
    """

    resource_type = "AWS::RDS::DBShardGroup"

    props: PropsDictType = {
        "ComputeRedundancy": (integer, False),
        "DBClusterIdentifier": (str, True),
        "DBShardGroupIdentifier": (str, False),
        "MaxACU": (double, True),
        "MinACU": (double, False),
        "PubliclyAccessible": (boolean, False),
        "Tags": (Tags, False),
    }


class DBSubnetGroup(AWSObject):
    """
    `DBSubnetGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbsubnetgroup.html>`__
    """

    resource_type = "AWS::RDS::DBSubnetGroup"

    props: PropsDictType = {
        "DBSubnetGroupDescription": (str, True),
        "DBSubnetGroupName": (str, False),
        "SubnetIds": (list, True),
        "Tags": (validate_tags_or_list, False),
    }


class EventSubscription(AWSObject):
    """
    `EventSubscription <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html>`__
    """

    resource_type = "AWS::RDS::EventSubscription"

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "EventCategories": ([str], False),
        "SnsTopicArn": (str, True),
        "SourceIds": ([str], False),
        "SourceType": (str, False),
        "SubscriptionName": (str, False),
        "Tags": (Tags, False),
    }


class GlobalEndpoint(AWSProperty):
    """
    `GlobalEndpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-globalcluster-globalendpoint.html>`__
    """

    props: PropsDictType = {
        "Address": (str, False),
    }


class GlobalCluster(AWSObject):
    """
    `GlobalCluster <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html>`__
    """

    resource_type = "AWS::RDS::GlobalCluster"

    props: PropsDictType = {
        "DeletionProtection": (boolean, False),
        "Engine": (str, False),
        "EngineLifecycleSupport": (str, False),
        "EngineVersion": (str, False),
        "GlobalClusterIdentifier": (str, False),
        "GlobalEndpoint": (GlobalEndpoint, False),
        "SourceDBClusterIdentifier": (str, False),
        "StorageEncrypted": (boolean, False),
        "Tags": (Tags, False),
    }


class Integration(AWSObject):
    """
    `Integration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-integration.html>`__
    """

    resource_type = "AWS::RDS::Integration"

    props: PropsDictType = {
        "AdditionalEncryptionContext": (dict, False),
        "DataFilter": (str, False),
        "Description": (str, False),
        "IntegrationName": (str, False),
        "KMSKeyId": (str, False),
        "SourceArn": (str, True),
        "Tags": (Tags, False),
        "TargetArn": (str, True),
    }


class OptionSetting(AWSProperty):
    """
    `OptionSetting <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionsetting.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Value": (str, False),
    }


class OptionConfiguration(AWSProperty):
    """
    `OptionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfiguration.html>`__
    """

    props: PropsDictType = {
        "DBSecurityGroupMemberships": ([str], False),
        "OptionName": (str, True),
        "OptionSettings": ([OptionSetting], False),
        "OptionVersion": (str, False),
        "Port": (validate_network_port, False),
        "VpcSecurityGroupMemberships": ([str], False),
    }


class OptionGroup(AWSObject):
    """
    `OptionGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html>`__
    """

    resource_type = "AWS::RDS::OptionGroup"

    props: PropsDictType = {
        "EngineName": (str, True),
        "MajorEngineVersion": (str, True),
        "OptionConfigurations": ([OptionConfiguration], False),
        "OptionGroupDescription": (str, True),
        "OptionGroupName": (str, False),
        "Tags": (validate_tags_or_list, False),
    }


class ReadEndpoint(AWSProperty):
    """
    `ReadEndpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-readendpoint.html>`__
    """

    props: PropsDictType = {
        "Address": (str, False),
    }
