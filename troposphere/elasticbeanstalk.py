# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer

WebServer = "WebServer"
Worker = "Worker"
WebServerType = "Standard"
WorkerType = "SQS/HTTP"


class MaxAgeRule(AWSProperty):
    props = {
      'DeleteSourceFromS3': (boolean, False),
      'Enabled': (boolean, False),
      'MaxAgeInDays': (integer, False),
    }


class MaxCountRule(AWSProperty):
    props = {
      'DeleteSourceFromS3': (boolean, False),
      'Enabled': (boolean, False),
      'MaxCount': (integer, False),
    }


class ApplicationVersionLifecycleConfig(AWSProperty):
    props = {
        'MaxAgeRule': (MaxAgeRule, False),
        'MaxCountRule': (MaxCountRule, False),
    }


class SourceBundle(AWSProperty):
    props = {
        'S3Bucket': (basestring, True),
        'S3Key': (basestring, True),
    }


class SourceConfiguration(AWSProperty):
    props = {
        'ApplicationName': (basestring, True),
        'TemplateName': (basestring, True),
    }


class ApplicationResourceLifecycleConfig(AWSProperty):
    props = {
        'ServiceRole': (basestring, False),
        'VersionLifecycleConfig': (ApplicationVersionLifecycleConfig, False),
    }


class OptionSettings(AWSProperty):
    props = {
        'Namespace': (basestring, True),
        'OptionName': (basestring, True),
        'ResourceName': (basestring, False),
        'Value': (basestring, True),
    }


class Application(AWSObject):
    resource_type = "AWS::ElasticBeanstalk::Application"

    props = {
        'ApplicationName': (basestring, False),
        'Description': (basestring, False),
        'ResourceLifecycleConfig': (ApplicationResourceLifecycleConfig, False),
    }


class ApplicationVersion(AWSObject):
    resource_type = "AWS::ElasticBeanstalk::ApplicationVersion"

    props = {
        'ApplicationName': (basestring, True),
        'Description': (basestring, False),
        'SourceBundle': (SourceBundle, False),
    }


class ConfigurationTemplate(AWSObject):
    resource_type = "AWS::ElasticBeanstalk::ConfigurationTemplate"

    props = {
        'ApplicationName': (basestring, True),
        'Description': (basestring, False),
        'EnvironmentId': (basestring, False),
        'OptionSettings': ([OptionSettings], False),
        'PlatformArn': (basestring, False),
        'SolutionStackName': (basestring, False),
        'SourceConfiguration': (SourceConfiguration, False),
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
    resource_type = "AWS::ElasticBeanstalk::Environment"

    props = {
        'ApplicationName': (basestring, True),
        'CNAMEPrefix': (basestring, False),
        'Description': (basestring, False),
        'EnvironmentName': (basestring, False),
        'OptionSettings': ([OptionSettings], False),
        'PlatformArn': (basestring, False),
        'SolutionStackName': (basestring, False),
        'Tags': (Tags, False),
        'TemplateName': (basestring, False),
        'Tier': (Tier, False),
        'VersionLabel': (basestring, False),
    }
