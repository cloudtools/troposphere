# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer
from .validators.codebuild import (
    validate_artifacts,
    validate_credentials_provider,
    validate_environment,
    validate_environment_variable,
    validate_environmentvariable_or_list,
    validate_image_pull_credentials,
    validate_project_cache,
    validate_project_triggers,
    validate_projectfilesystemlocation_type,
    validate_source,
    validate_source_auth,
    validate_status,
    validate_webhookfilter_type,
)


class VpcConfig(AWSProperty):
    """
    `VpcConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-vpcconfig.html>`__
    """

    props: PropsDictType = {
        "SecurityGroupIds": ([str], False),
        "Subnets": ([str], False),
        "VpcId": (str, False),
    }


class Fleet(AWSObject):
    """
    `Fleet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-fleet.html>`__
    """

    resource_type = "AWS::CodeBuild::Fleet"

    props: PropsDictType = {
        "BaseCapacity": (integer, False),
        "ComputeType": (str, False),
        "EnvironmentType": (str, False),
        "FleetServiceRole": (str, False),
        "FleetVpcConfig": (VpcConfig, False),
        "Name": (str, False),
        "OverflowBehavior": (str, False),
        "Tags": (Tags, False),
    }


class Artifacts(AWSProperty):
    """
    `Artifacts <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html>`__
    """

    props: PropsDictType = {
        "ArtifactIdentifier": (str, False),
        "EncryptionDisabled": (boolean, False),
        "Location": (str, False),
        "Name": (str, False),
        "NamespaceType": (str, False),
        "OverrideArtifactName": (boolean, False),
        "Packaging": (str, False),
        "Path": (str, False),
        "Type": (str, True),
    }

    def validate(self):
        validate_artifacts(self)


class EnvironmentVariable(AWSProperty):
    """
    `EnvironmentVariable <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environmentvariable.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Type": (str, False),
        "Value": (str, True),
    }

    def validate(self):
        validate_environment_variable(self)


class ProjectFleet(AWSProperty):
    """
    `ProjectFleet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfleet.html>`__
    """

    props: PropsDictType = {
        "FleetArn": (str, False),
    }


class RegistryCredential(AWSProperty):
    """
    `RegistryCredential <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-registrycredential.html>`__
    """

    props: PropsDictType = {
        "Credential": (str, True),
        "CredentialProvider": (validate_credentials_provider, True),
    }


class Environment(AWSProperty):
    """
    `Environment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html>`__
    """

    props: PropsDictType = {
        "Certificate": (str, False),
        "ComputeType": (str, True),
        "EnvironmentVariables": (validate_environmentvariable_or_list, False),
        "Fleet": (ProjectFleet, False),
        "Image": (str, True),
        "ImagePullCredentialsType": (validate_image_pull_credentials, False),
        "PrivilegedMode": (boolean, False),
        "RegistryCredential": (RegistryCredential, False),
        "Type": (str, True),
    }

    def validate(self):
        validate_environment(self)


class CloudWatchLogs(AWSProperty):
    """
    `CloudWatchLogs <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-cloudwatchlogsconfig.html>`__
    """

    props: PropsDictType = {
        "GroupName": (str, False),
        "Status": (validate_status, True),
        "StreamName": (str, False),
    }


class S3Logs(AWSProperty):
    """
    `S3Logs <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-s3logsconfig.html>`__
    """

    props: PropsDictType = {
        "EncryptionDisabled": (boolean, False),
        "Location": (str, False),
        "Status": (validate_status, True),
    }


class LogsConfig(AWSProperty):
    """
    `LogsConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-logsconfig.html>`__
    """

    props: PropsDictType = {
        "CloudWatchLogs": (CloudWatchLogs, False),
        "S3Logs": (S3Logs, False),
    }


class BatchRestrictions(AWSProperty):
    """
    `BatchRestrictions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-batchrestrictions.html>`__
    """

    props: PropsDictType = {
        "ComputeTypesAllowed": ([str], False),
        "MaximumBuildsAllowed": (integer, False),
    }


class ProjectBuildBatchConfig(AWSProperty):
    """
    `ProjectBuildBatchConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html>`__
    """

    props: PropsDictType = {
        "BatchReportMode": (str, False),
        "CombineArtifacts": (boolean, False),
        "Restrictions": (BatchRestrictions, False),
        "ServiceRole": (str, False),
        "TimeoutInMins": (integer, False),
    }


class ProjectCache(AWSProperty):
    """
    `ProjectCache <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectcache.html>`__
    """

    props: PropsDictType = {
        "Location": (str, False),
        "Modes": ([str], False),
        "Type": (str, True),
    }

    def validate(self):
        validate_project_cache(self)


class ProjectFileSystemLocation(AWSProperty):
    """
    `ProjectFileSystemLocation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html>`__
    """

    props: PropsDictType = {
        "Identifier": (str, True),
        "Location": (str, True),
        "MountOptions": (str, False),
        "MountPoint": (str, True),
        "Type": (validate_projectfilesystemlocation_type, True),
    }


class ProjectSourceVersion(AWSProperty):
    """
    `ProjectSourceVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectsourceversion.html>`__
    """

    props: PropsDictType = {
        "SourceIdentifier": (str, True),
        "SourceVersion": (str, False),
    }


class ProjectTriggers(AWSProperty):
    """
    `ProjectTriggers <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projecttriggers.html>`__
    """

    props: PropsDictType = {
        "BuildType": (str, False),
        "FilterGroups": (list, False),
        "Webhook": (boolean, False),
    }

    def validate(self):
        validate_project_triggers(self)


class BuildStatusConfig(AWSProperty):
    """
    `BuildStatusConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-buildstatusconfig.html>`__
    """

    props: PropsDictType = {
        "Context": (str, False),
        "TargetUrl": (str, False),
    }


class GitSubmodulesConfig(AWSProperty):
    """
    `GitSubmodulesConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-gitsubmodulesconfig.html>`__
    """

    props: PropsDictType = {
        "FetchSubmodules": (boolean, True),
    }


class SourceAuth(AWSProperty):
    """
    `SourceAuth <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-sourceauth.html>`__
    """

    props: PropsDictType = {
        "Resource": (str, False),
        "Type": (str, True),
    }

    def validate(self):
        validate_source_auth(self)


class Source(AWSProperty):
    """
    `Source <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html>`__
    """

    props: PropsDictType = {
        "Auth": (SourceAuth, False),
        "BuildSpec": (str, False),
        "BuildStatusConfig": (BuildStatusConfig, False),
        "GitCloneDepth": (integer, False),
        "GitSubmodulesConfig": (GitSubmodulesConfig, False),
        "InsecureSsl": (boolean, False),
        "Location": (str, False),
        "ReportBuildStatus": (boolean, False),
        "SourceIdentifier": (str, False),
        "Type": (str, True),
    }

    def validate(self):
        validate_source(self)


class Project(AWSObject):
    """
    `Project <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html>`__
    """

    resource_type = "AWS::CodeBuild::Project"

    props: PropsDictType = {
        "Artifacts": (Artifacts, True),
        "BadgeEnabled": (boolean, False),
        "BuildBatchConfig": (ProjectBuildBatchConfig, False),
        "Cache": (ProjectCache, False),
        "ConcurrentBuildLimit": (integer, False),
        "Description": (str, False),
        "EncryptionKey": (str, False),
        "Environment": (Environment, True),
        "FileSystemLocations": ([ProjectFileSystemLocation], False),
        "LogsConfig": (LogsConfig, False),
        "Name": (str, False),
        "QueuedTimeoutInMinutes": (integer, False),
        "ResourceAccessRole": (str, False),
        "SecondaryArtifacts": ([Artifacts], False),
        "SecondarySourceVersions": ([ProjectSourceVersion], False),
        "SecondarySources": ([Source], False),
        "ServiceRole": (str, True),
        "Source": (Source, True),
        "SourceVersion": (str, False),
        "Tags": (Tags, False),
        "TimeoutInMinutes": (integer, False),
        "Triggers": (ProjectTriggers, False),
        "Visibility": (str, False),
        "VpcConfig": (VpcConfig, False),
    }


class S3ReportExportConfig(AWSProperty):
    """
    `S3ReportExportConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, True),
        "BucketOwner": (str, False),
        "EncryptionDisabled": (boolean, False),
        "EncryptionKey": (str, False),
        "Packaging": (str, False),
        "Path": (str, False),
    }


class ReportExportConfig(AWSProperty):
    """
    `ReportExportConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-reportexportconfig.html>`__
    """

    props: PropsDictType = {
        "ExportConfigType": (str, True),
        "S3Destination": (S3ReportExportConfig, False),
    }


class ReportGroup(AWSObject):
    """
    `ReportGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html>`__
    """

    resource_type = "AWS::CodeBuild::ReportGroup"

    props: PropsDictType = {
        "DeleteReports": (boolean, False),
        "ExportConfig": (ReportExportConfig, True),
        "Name": (str, False),
        "Tags": (Tags, False),
        "Type": (str, True),
    }


class SourceCredential(AWSObject):
    """
    `SourceCredential <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html>`__
    """

    resource_type = "AWS::CodeBuild::SourceCredential"

    props: PropsDictType = {
        "AuthType": (str, True),
        "ServerType": (str, True),
        "Token": (str, True),
        "Username": (str, False),
    }


class ScopeConfiguration(AWSProperty):
    """
    `ScopeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-scopeconfiguration.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
    }


class WebhookFilter(AWSProperty):
    """
    `WebhookFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-webhookfilter.html>`__
    """

    props: PropsDictType = {
        "ExcludeMatchedPattern": (boolean, False),
        "Pattern": (str, True),
        "Type": (validate_webhookfilter_type, True),
    }
