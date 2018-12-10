# Copyright (c) 2016, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty, Tags
from .validators import boolean, integer, positive_integer


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
            ]
            env_type = self.properties.get('Type')
            if env_type not in valid_types:
                raise ValueError(
                    'EnvironmentVariable Type: must be one of %s' %
                    ','.join(valid_types))


class Environment(AWSProperty):
    props = {
        'Certificate': (basestring, False),
        'ComputeType': (basestring, True),
        'EnvironmentVariables': ((list, [EnvironmentVariable]), False),
        'Image': (basestring, True),
        'PrivilegedMode': (boolean, False),
        'Type': (basestring, True),
    }

    def validate(self):
        valid_types = [
            'LINUX_CONTAINER',
            'WINDOWS_CONTAINER',
        ]
        env_type = self.properties.get('Type')
        if env_type not in valid_types:
            raise ValueError('Environment Type: must be one of %s' %
                             ','.join(valid_types))


class ProjectCache(AWSProperty):
    props = {
        'Location': (basestring, False),
        'Type': (basestring, True),
    }

    def validate(self):
        valid_types = [
            'NO_CACHE',
            'S3',
        ]
        cache_type = self.properties.get('Type')
        if cache_type not in valid_types:
            raise ValueError('ProjectCache Type: must be one of %s' %
                             ','.join(valid_types))


class Source(AWSProperty):
    props = {
        'Auth': (SourceAuth, False),
        'BuildSpec': (basestring, False),
        'GitCloneDepth': (positive_integer, False),
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
        if auth is not None and source_type is not 'GITHUB':
            raise ValueError("SourceAuth: must only be defined when using "
                             "'GITHUB' Source Type.")


class VpcConfig(AWSProperty):
    props = {
        'SecurityGroupIds': ([basestring], True),
        'Subnets': ([basestring], True),
        'VpcId': (basestring, True),
    }


class ProjectTriggers(AWSProperty):
    props = {
        'Webhook': (boolean, False),
    }


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
        "Status": (validate_status, True),
        "Location": (basestring, False)
    }


class LogsConfig(AWSProperty):
    props = {
        'CloudWatchLogs': (CloudWatchLogs, False),
        'S3Logs': (S3Logs, False)
    }


class Project(AWSObject):
    resource_type = "AWS::CodeBuild::Project"

    props = {
        'Artifacts': (Artifacts, True),
        'BadgeEnabled': (boolean, False),
        'Cache': (ProjectCache, False),
        'Description': (basestring, False),
        'EncryptionKey': (basestring, False),
        'Environment': (Environment, True),
        "LogsConfig": (LogsConfig, False),
        'Name': (basestring, True),
        'SecondaryArtifacts': ([Artifacts], False),
        'SecondarySources': ([Source], False),
        'ServiceRole': (basestring, True),
        'Source': (Source, True),
        'Tags': (Tags, False),
        'TimeoutInMinutes': (integer, False),
        'Triggers': (ProjectTriggers, False),
        'VpcConfig': (VpcConfig, False),
    }
