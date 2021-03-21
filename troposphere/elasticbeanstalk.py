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
        'S3Bucket': (str, True),
        'S3Key': (str, True),
    }


class SourceConfiguration(AWSProperty):
    props = {
        'ApplicationName': (str, True),
        'TemplateName': (str, True),
    }


class ApplicationResourceLifecycleConfig(AWSProperty):
    props = {
        'ServiceRole': (str, False),
        'VersionLifecycleConfig': (ApplicationVersionLifecycleConfig, False),
    }


class OptionSettings(AWSProperty):
    props = {
        'Namespace': (str, True),
        'OptionName': (str, True),
        'ResourceName': (str, False),
        'Value': (str, True),
    }


class Application(AWSObject):
    resource_type = "AWS::ElasticBeanstalk::Application"

    props = {
        'ApplicationName': (str, False),
        'Description': (str, False),
        'ResourceLifecycleConfig': (ApplicationResourceLifecycleConfig, False),
    }


class ApplicationVersion(AWSObject):
    resource_type = "AWS::ElasticBeanstalk::ApplicationVersion"

    props = {
        'ApplicationName': (str, True),
        'Description': (str, False),
        'SourceBundle': (SourceBundle, False),
    }


class ConfigurationTemplate(AWSObject):
    resource_type = "AWS::ElasticBeanstalk::ConfigurationTemplate"

    props = {
        'ApplicationName': (str, True),
        'Description': (str, False),
        'EnvironmentId': (str, False),
        'OptionSettings': ([OptionSettings], False),
        'PlatformArn': (str, False),
        'SolutionStackName': (str, False),
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
        'Version': (str, False),
    }


class Environment(AWSObject):
    resource_type = "AWS::ElasticBeanstalk::Environment"

    props = {
        'ApplicationName': (str, True),
        'CNAMEPrefix': (str, False),
        'Description': (str, False),
        'EnvironmentName': (str, False),
        'OptionSettings': ([OptionSettings], False),
        'PlatformArn': (str, False),
        'SolutionStackName': (str, False),
        'Tags': (Tags, False),
        'TemplateName': (str, False),
        'Tier': (Tier, False),
        'VersionLabel': (str, False),
    }
