# Copyright (c) 2016, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import integer


class Artifacts(AWSProperty):
    props = {
        'Location': (basestring, False),
        'Name': (basestring, False),
        'NameSpaceType': (basestring, False),
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
