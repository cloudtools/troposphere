# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject
from . import AWSProperty
from troposphere import Tags


class Fleet(AWSObject):
    resource_type = "AWS::RoboMaker::Fleet"

    props = {
        'Name': (basestring, False),
        'Tags': (Tags, False),
    }


class Robot(AWSObject):
    resource_type = "AWS::RoboMaker::Robot"

    props = {
        'Architecture': (basestring, True),
        'Fleet': (basestring, False),
        'GreengrassGroupId': (basestring, True),
        'Name': (basestring, False),
        'Tags': (Tags, False),
    }


class RobotSoftwareSuite(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Version': (basestring, True),
    }


class SourceConfig(AWSProperty):
    props = {
        'Architecture': (basestring, True),
        'S3Bucket': (basestring, True),
        'S3Key': (basestring, True),
    }


class RobotApplication(AWSObject):
    resource_type = "AWS::RoboMaker::RobotApplication"

    props = {
        'CurrentRevisionId': (basestring, False),
        'Name': (basestring, False),
        'RobotSoftwareSuite': (RobotSoftwareSuite, True),
        'Sources': ([SourceConfig], True),
        'Tags': (Tags, False),
    }


class RobotApplicationVersion(AWSObject):
    resource_type = "AWS::RoboMaker::RobotApplicationVersion"

    props = {
        'Application': (basestring, True),
        'CurrentRevisionId': (basestring, False),
    }


class RenderingEngine(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Version': (basestring, True),
    }


class SimulationSoftwareSuite(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Version': (basestring, True),
    }


class SimulationApplication(AWSObject):
    resource_type = "AWS::RoboMaker::SimulationApplication"

    props = {
        'CurrentRevisionId': (basestring, False),
        'Name': (basestring, False),
        'RenderingEngine': (RenderingEngine, True),
        'RobotSoftwareSuite': (RobotSoftwareSuite, True),
        'SimulationSoftwareSuite': (SimulationSoftwareSuite, True),
        'Sources': ([SourceConfig], True),
        'Tags': (Tags, False),
    }


class SimulationApplicationVersion(AWSObject):
    resource_type = "AWS::RoboMaker::SimulationApplicationVersion"

    props = {
        'Application': (basestring, True),
        'CurrentRevisionId': (basestring, False),
    }
