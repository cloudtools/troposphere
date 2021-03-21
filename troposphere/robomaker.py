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
        'Name': (str, False),
        'Tags': (Tags, False),
    }


class Robot(AWSObject):
    resource_type = "AWS::RoboMaker::Robot"

    props = {
        'Architecture': (str, True),
        'Fleet': (str, False),
        'GreengrassGroupId': (str, True),
        'Name': (str, False),
        'Tags': (Tags, False),
    }


class RobotSoftwareSuite(AWSProperty):
    props = {
        'Name': (str, True),
        'Version': (str, True),
    }


class SourceConfig(AWSProperty):
    props = {
        'Architecture': (str, True),
        'S3Bucket': (str, True),
        'S3Key': (str, True),
    }


class RobotApplication(AWSObject):
    resource_type = "AWS::RoboMaker::RobotApplication"

    props = {
        'CurrentRevisionId': (str, False),
        'Name': (str, False),
        'RobotSoftwareSuite': (RobotSoftwareSuite, True),
        'Sources': ([SourceConfig], True),
        'Tags': (Tags, False),
    }


class RobotApplicationVersion(AWSObject):
    resource_type = "AWS::RoboMaker::RobotApplicationVersion"

    props = {
        'Application': (str, True),
        'CurrentRevisionId': (str, False),
    }


class RenderingEngine(AWSProperty):
    props = {
        'Name': (str, True),
        'Version': (str, True),
    }


class SimulationSoftwareSuite(AWSProperty):
    props = {
        'Name': (str, True),
        'Version': (str, True),
    }


class SimulationApplication(AWSObject):
    resource_type = "AWS::RoboMaker::SimulationApplication"

    props = {
        'CurrentRevisionId': (str, False),
        'Name': (str, False),
        'RenderingEngine': (RenderingEngine, True),
        'RobotSoftwareSuite': (RobotSoftwareSuite, True),
        'SimulationSoftwareSuite': (SimulationSoftwareSuite, True),
        'Sources': ([SourceConfig], True),
        'Tags': (Tags, False),
    }


class SimulationApplicationVersion(AWSObject):
    resource_type = "AWS::RoboMaker::SimulationApplicationVersion"

    props = {
        'Application': (str, True),
        'CurrentRevisionId': (str, False),
    }
