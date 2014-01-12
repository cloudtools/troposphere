# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty


WebServer = "WebServer"
Worker = "Worker"
WebServerType = "Standard"
WorkerType = "SQS/HTTP"


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
        'ApplicationName': (basestring, False),
        'ApplicationVersions': (list, True),
        'ConfigurationTemplates': (list, False),
        'Description': (basestring, False),
    }


def validate_tier_name(name):
    valid_names = [WebServer, Worker]
    if name not in valid_names:
        raise ValueError('Tier name needs to be one of %r' % valid_names)
    return name


def validate_tier_type(tier_type):
    valid_types = [WebServerType, WorkerType]
    if tier_type not in valid_types:
        raise ValueError('Tier type needs to be one of %r' % valid_types)
    return tier_type


class Tier(AWSProperty):
    props = {
        'Name': (validate_tier_name, False),
        'Type': (validate_tier_type, False),
        'Version': (basestring, False),
    }


class Environment(AWSObject):
    type = "AWS::ElasticBeanstalk::Environment"

    props = {
        'ApplicationName': (basestring, True),
        'CNAMEPrefix': (basestring, False),
        'Description': (basestring, False),
        'EnvironmentName': (basestring, False),
        'OptionSettings': (list, False),
        'OptionsToRemove': (list, False),
        'SolutionStackName': (basestring, False),
        'TemplateName': (basestring, False),
        'Tier': (Tier, False),
        'VersionLabel': (basestring, False),
    }
