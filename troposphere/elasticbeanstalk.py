# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty


class SourceBundle(AWSProperty):
    props = {
        'S3Bucket': (basestring, True),
        'S3Key': (basestring, True),
    }


class ApplicationVersion(AWSProperty):
    props = {
        'Description': (basestring, False),
        'SourceBundle': (SourceBundle, False),
        'VersionLabel': (basestring, True),
    }


class OptionSettings(AWSProperty):
    props = {
        'Namespace': (basestring, True),
        'OptionName': (basestring, True),
        'Value': (basestring, True),
    }


class ConfigurationTemplate(AWSProperty):
    props = {
        'TemplateName': (basestring, True),
        'Description': (basestring, False),
        'OptionSettings': (list, False),
        'SolutionStackName': (basestring, False),
    }


class Application(AWSObject):
    type = "AWS::ElasticBeanstalk::Application"

    props = {
        'ApplicationVersions': (list, True),
        'ConfigurationTemplates': (list, False),
        'Description': (basestring, False),
    }


class Environment(AWSObject):
    type = "AWS::ElasticBeanstalk::Environment"

    props = {
        'ApplicationName': (basestring, True),
        'CNAMEPrefix': (basestring, False),
        'Description': (basestring, False),
        'OptionSettings': (list, False),
        'OptionsToRemove': (list, False),
        'SolutionStackName': (basestring, False),
        'TemplateName': (basestring, False),
        'VersionLabel': (basestring, False),
    }
