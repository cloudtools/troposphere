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
    props = {
        'ApplicationVersions': (list, True),
        'ConfigurationTemplates': (list, False),
        'Description': (basestring, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::ElasticBeanstalk::Application"
        sup = super(Application, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class Environment(AWSObject):
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

    def __init__(self, name, **kwargs):
        self.type = "AWS::ElasticBeanstalk::Environment"
        sup = super(Environment, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)
