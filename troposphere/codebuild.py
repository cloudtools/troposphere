# Copyright (c) 2016, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import integer, boolean


class Auth(AWSProperty):
    props = {
        'Type': (basestring, True),
    }

    def validate(self):
        valid_types = [
            'OAUTH'
        ]
        auth_types = self.properties.get('Type')
        if auth_types not in valid_types:
            raise ValueError('Auth Type: must be one of %s' %
                             ','.join(valid_types))


class Artifacts(AWSProperty):
    props = {
        'Location': (basestring, False),
        'Name': (basestring, False),
        'NamespaceType': (basestring, False),
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
        'Value': (basestring, True),
    }


class Environment(AWSProperty):
    props = {
        'ComputeType': (basestring, True),
        'EnvironmentVariables': ((list, [EnvironmentVariable]), False),
        'Image': (basestring, True),
        'PrivilegedMode': (boolean, False),
        'Type': (basestring, True),
    }

    def validate(self):
        valid_types = [
            'LINUX_CONTAINER',
        ]
        env_type = self.properties.get('Type')
        if env_type not in valid_types:
            raise ValueError('Environment Type: must be one of %s' %
                             ','.join(valid_types))


class Source(AWSProperty):
    props = {
        'BuildSpec': (basestring, False),
        'Location': (basestring, False),
        'Type': (basestring, True),
        'Auth': (Auth, False),
    }

    def validate(self):
        valid_types = [
            'CODECOMMIT',
            'CODEPIPELINE',
            'GITHUB',
            'S3',
        ]

        source_type = self.properties.get('Type')
        if source_type not in valid_types:
            raise ValueError('Source Type: must be one of %s' %
                             ','.join(valid_types))

        location = self.properties.get('Location')
        if source_type is not 'CODEPIPELINE' and not location:
            raise ValueError(
                'Source Location: must be defined when type is %s' %
                source_type
                )

        auth = self.properties.get('Auth')
        if auth is not None and source_type is not 'GITHUB':
            raise ValueError("Source Auth: must only be defined when using "
                             "'GITHUB' Source Type.")


class Project(AWSObject):
    resource_type = "AWS::CodeBuild::Project"

    props = {
        'Artifacts': (Artifacts, True),
        'Description': (basestring, False),
        'EncryptionKey': (basestring, False),
        'Environment': (Environment, True),
        'Name': (basestring, True),
        'ServiceRole': (basestring, True),
        'Source': (Source, True),
        'Tags': (Tags, False),
        'TimeoutInMinutes': (integer, False),
    }
