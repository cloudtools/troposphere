# Copyright (c) 2016, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty, Tags
from .validators import boolean, integer, positive_integer


VALID_IMAGE_PULL_CREDENTIALS = ('CODEBUILD', 'SERVICE_ROLE')
VALID_CREDENTIAL_PROVIDERS = ('SECRETS_MANAGER')
VALID_WEBHOOKFILTER_TYPES = ('EVENT', 'ACTOR_ACCOUNT_ID', 'HEAD_REF',
                             'BASE_REF', 'FILE_PATH')
VALID_PROJECTFILESYSTEMLOCATION_TYPE = ('EFS')


def validate_image_pull_credentials(image_pull_credentials):
    """Validate ImagePullCredentialsType for Project"""

    if image_pull_credentials not in VALID_IMAGE_PULL_CREDENTIALS:
        raise ValueError("Project ImagePullCredentialsType must be one of: %s" %  # NOQA
                         ", ".join(VALID_IMAGE_PULL_CREDENTIALS))
    return image_pull_credentials


def validate_credentials_provider(credential_provider):
    """Validate CredentialProvider for Project's RegistryCredential"""

    if credential_provider not in VALID_CREDENTIAL_PROVIDERS:
        raise ValueError("RegistryCredential CredentialProvider must be one of: %s" %  # NOQA
                         ", ".join(VALID_CREDENTIAL_PROVIDERS))
    return credential_provider


def validate_webhookfilter_type(webhookfilter_type):
    """Validate WebHookFilter type property for a Project"""

    if webhookfilter_type not in VALID_WEBHOOKFILTER_TYPES:
        raise ValueError("Project Webhookfilter Type must be one of: %s" %
                         ", ".join(VALID_WEBHOOKFILTER_TYPES))
    return webhookfilter_type


def validate_projectfilesystemlocation_type(projectfilesystemlocation_type):
    """Validate ProjectFileSystemLocation type property"""

    if projectfilesystemlocation_type not in VALID_PROJECTFILESYSTEMLOCATION_TYPE:  # NOQA
        raise ValueError("ProjectFileSystemLocation Type must be one of: %s" %  # NOQA
                         ", ".join(VALID_PROJECTFILESYSTEMLOCATION_TYPE))
    return projectfilesystemlocation_type


class SourceAuth(AWSProperty):
    props = {
        'Resource': (basestring, False),
        'Type': (basestring, True),
    }

    def validate(self):
        valid_types = [
            'OAUTH'
        ]
        auth_types = self.properties.get('Type')
        if auth_types not in valid_types:
            raise ValueError('SourceAuth Type: must be one of %s' %
                             ','.join(valid_types))


class Artifacts(AWSProperty):
    props = {
        'ArtifactIdentifier': (basestring, False),
        'EncryptionDisabled': (boolean, False),
        'Location': (basestring, False),
        'Name': (basestring, False),
        'NamespaceType': (basestring, False),
        'OverrideArtifactName': (boolean, False),
        'Packaging': (basestring, False),
        'Path': (basestring, False),
        'Type': (basestring, True),
    }

    def validate(self):
        valid_types = [
            'CODEPIPELINE',
            'NO_ARTIFACTS',
            'S3',
        ]
        artifact_type = self.properties.get('Type')
        if artifact_type not in valid_types:
            raise ValueError('Artifacts Type: must be one of %s' %
                             ','.join(valid_types))

        if artifact_type == 'S3':
            for required_property in ['Name', 'Location']:
                if not self.properties.get(required_property):
                    raise ValueError(
                        'Artifacts Type S3: requires %s to be set' %
                        required_property
                    )


class EnvironmentVariable(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Type': (basestring, False),
        'Value': (basestring, True),
    }

    def validate(self):
        if 'Type' in self.properties:
            valid_types = [
                'PARAMETER_STORE',
                'PLAINTEXT',
                'SECRETS_MANAGER'
            ]
            env_type = self.properties.get('Type')
            if env_type not in valid_types:
                raise ValueError(
                    'EnvironmentVariable Type: must be one of %s' %
                    ','.join(valid_types))


class RegistryCredential(AWSProperty):
    props = {
        'Credential': (basestring, True),
        'CredentialProvider': (validate_credentials_provider, True),
    }


class Environment(AWSProperty):
    props = {
        'Certificate': (basestring, False),
        'ComputeType': (basestring, True),
        'EnvironmentVariables': ((list, [EnvironmentVariable]), False),
        'Image': (basestring, True),
        'ImagePullCredentialsType': (validate_image_pull_credentials, False),
        'PrivilegedMode': (boolean, False),
        'RegistryCredential': (RegistryCredential, False),
        'Type': (basestring, True),
    }

    def validate(self):
        valid_types = [
            'ARM_CONTAINER',
            'LINUX_CONTAINER',
            'LINUX_GPU_CONTAINER',
            'WINDOWS_CONTAINER',
        ]
        env_type = self.properties.get('Type')
        if env_type not in valid_types:
            raise ValueError('Environment Type: must be one of %s' %
                             ','.join(valid_types))


class BatchRestrictions(AWSProperty):
    props = {
        'ComputeTypesAllowed': ([basestring], False),
        'MaximumBuildsAllowed': (integer, False),
    }


class ProjectBuildBatchConfig(AWSProperty):
    props = {
        'CombineArtifacts': (boolean, False),
        'Restrictions': (BatchRestrictions, False),
        'ServiceRole': (basestring, False),
        'TimeoutInMins': (integer, False),
    }


class ProjectCache(AWSProperty):
    props = {
        'Location': (basestring, False),
        'Modes': ([basestring], False),
        'Type': (basestring, True),
    }

    def validate(self):
        valid_types = [
            'NO_CACHE',
            'LOCAL',
            'S3',
        ]
        cache_type = self.properties.get('Type')
        if cache_type not in valid_types:
            raise ValueError('ProjectCache Type: must be one of %s' %
                             ','.join(valid_types))


class BuildStatusConfig(AWSProperty):
    props = {
        'Context': (basestring, False),
        'TargetUrl': (basestring, False),
    }


class GitSubmodulesConfig(AWSProperty):
    props = {
        'FetchSubmodules': (boolean, True),
    }


class Source(AWSProperty):
    props = {
        'Auth': (SourceAuth, False),
        'BuildSpec': (basestring, False),
        'BuildStatusConfig': (BuildStatusConfig, False),
        'GitCloneDepth': (positive_integer, False),
        'GitSubmodulesConfig': (GitSubmodulesConfig, False),
        'InsecureSsl': (boolean, False),
        'Location': (basestring, False),
        'ReportBuildStatus': (boolean, False),
        'SourceIdentifier': (basestring, False),
        'Type': (basestring, True),
    }

    def validate(self):
        valid_types = [
            'BITBUCKET',
            'CODECOMMIT',
            'CODEPIPELINE',
            'GITHUB',
            'GITHUB_ENTERPRISE',
            'NO_SOURCE',
            'S3',
        ]

        location_agnostic_types = [
            'CODEPIPELINE',
            'NO_SOURCE',
        ]

        source_type = self.properties.get('Type')

        # Don't do additional checks if source_type can't
        # be determined (for example, being a Ref).
        if isinstance(source_type, AWSHelperFn):
            return

        if source_type not in valid_types:
            raise ValueError('Source Type: must be one of %s' %
                             ','.join(valid_types))

        location = self.properties.get('Location')

        if source_type not in location_agnostic_types and not location:
            raise ValueError(
                'Source Location: must be defined when type is %s' %
                source_type
            )

        auth = self.properties.get('Auth')
        if auth is not None and source_type != 'GITHUB':
            raise ValueError("SourceAuth: must only be defined when using "
                             "'GITHUB' Source Type.")


class VpcConfig(AWSProperty):
    props = {
        'SecurityGroupIds': ([basestring], True),
        'Subnets': ([basestring], True),
        'VpcId': (basestring, True),
    }


class WebhookFilter(AWSProperty):
    props = {
        'ExcludeMatchedPattern': (boolean, False),
        'Pattern': (basestring, True),
        'Type': (validate_webhookfilter_type, True),
    }


class ProjectTriggers(AWSProperty):
    props = {
        'Webhook': (boolean, False),
        'FilterGroups': (list, False)
    }

    def validate(self):
        """ FilterGroups, if set, needs to be a list of a list of
        WebhookFilters
        """
        filter_groups = self.properties.get('FilterGroups')
        if filter_groups is not None:
            if not isinstance(filter_groups, list):
                self._raise_type('FilterGroups', filter_groups, list)

            for counti, elem in enumerate(filter_groups):
                if not isinstance(elem, list):
                    self._raise_type(
                        'FilterGroups[{}]'.format(counti),
                        filter_groups[counti], list
                    )
                for countj, hook in enumerate(filter_groups[counti]):
                    if not isinstance(hook, WebhookFilter):
                        self._raise_type(
                            'FilterGroups[{}][{}]'.format(counti, countj),
                            hook, WebhookFilter
                        )


def validate_status(status):
    """ Validate status
    :param status: The Status of CloudWatchLogs or S3Logs
    :return: The provided value if valid
    """
    valid_statuses = [
        'ENABLED',
        'DISABLED'
    ]

    if status not in valid_statuses:
        raise ValueError('Status: must be one of %s' %
                         ','.join(valid_statuses))
    return status


class CloudWatchLogs(AWSProperty):
    props = {
        "Status": (validate_status, True),
        "GroupName": (basestring, False),
        "StreamName": (basestring, False)
    }


class S3Logs(AWSProperty):
    props = {
        "EncryptionDisabled": (boolean, False),
        "Status": (validate_status, True),
        "Location": (basestring, False)
    }


class LogsConfig(AWSProperty):
    props = {
        'CloudWatchLogs': (CloudWatchLogs, False),
        'S3Logs': (S3Logs, False)
    }


class ProjectSourceVersion(AWSProperty):
    props = {
        'SourceIdentifier': (basestring, True),
        'SourceVersion': (basestring, False),
    }


class ProjectFileSystemLocation(AWSProperty):
    props = {
        'Identifier': (basestring, True),
        'Location': (basestring, True),
        'MountOptions': (basestring, False),
        'MountPoint': (basestring, True),
        'Type': (validate_projectfilesystemlocation_type, True),
    }


class Project(AWSObject):
    resource_type = "AWS::CodeBuild::Project"

    props = {
        'Artifacts': (Artifacts, True),
        'BadgeEnabled': (boolean, False),
        'BuildBatchConfig': (ProjectBuildBatchConfig, False),
        'Cache': (ProjectCache, False),
        'Description': (basestring, False),
        'EncryptionKey': (basestring, False),
        'Environment': (Environment, True),
        'FileSystemLocations': ([ProjectFileSystemLocation], False),
        'LogsConfig': (LogsConfig, False),
        'Name': (basestring, False),
        'QueuedTimeoutInMinutes': (integer, False),
        'SecondaryArtifacts': ([Artifacts], False),
        'SecondarySourceVersions': ([ProjectSourceVersion], False),
        'SecondarySources': ([Source], False),
        'ServiceRole': (basestring, True),
        'Source': (Source, True),
        'SourceVersion': (basestring, False),
        'Tags': (Tags, False),
        'TimeoutInMinutes': (integer, False),
        'Triggers': (ProjectTriggers, False),
        'VpcConfig': (VpcConfig, False),
    }


class S3ReportExportConfig(AWSProperty):
    props = {
        'Bucket': (basestring, True),
        'EncryptionDisabled': (boolean, False),
        'EncryptionKey': (basestring, False),
        'Packaging': (basestring, False),
        'Path': (basestring, False),
    }


class ReportExportConfig(AWSProperty):
    props = {
        'ExportConfigType': (basestring, True),
        'S3Destination': (S3ReportExportConfig, False),
    }


class ReportGroup(AWSObject):
    resource_type = "AWS::CodeBuild::ReportGroup"

    props = {
        'DeleteReports': (boolean, False),
        'ExportConfig': (ReportExportConfig, True),
        'Name': (basestring, False),
        'Tags': (Tags, False),
        'Type': (basestring, True),
    }


class SourceCredential(AWSObject):
    resource_type = "AWS::CodeBuild::SourceCredential"

    props = {
        'AuthType': (basestring, True),
        'ServerType': (basestring, True),
        'Token': (basestring, True),
        'Username': (basestring, False),
    }
