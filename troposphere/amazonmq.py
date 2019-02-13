# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer


class ConfigurationId(AWSProperty):
    props = {
        'Id': (basestring, True),
        'Revision': (integer, True),
    }


class MaintenanceWindow(AWSProperty):
    props = {
        'DayOfWeek': (basestring, True),
        'TimeOfDay': (basestring, True),
        'TimeZone': (basestring, True),
    }


class User(AWSProperty):
    props = {
        'ConsoleAccess': (boolean, False),
        'Groups': ([basestring], False),
        'Password': (basestring, True),
        'Username': (basestring, True),
    }


class LogsConfiguration(AWSProperty):
    props = {
        'Audit': (boolean, False),
        'General': (boolean, False),
    }


class Broker(AWSObject):
    resource_type = "AWS::AmazonMQ::Broker"

    props = {
        'AutoMinorVersionUpgrade': (boolean, True),
        'BrokerName': (basestring, True),
        'Users': ([User], True),
        'Configuration': (ConfigurationId, False),
        'DeploymentMode': (basestring, True),
        'EngineType': (basestring, True),
        'EngineVersion': (basestring, True),
        'HostInstanceType': (basestring, True),
        'Logs': (LogsConfiguration, False),
        'MaintenanceWindowStartTime': (MaintenanceWindow, False),
        'PubliclyAccessible': (boolean, True),
        'SecurityGroups': ([basestring], False),
        'SubnetIds': ([basestring], False),
        'Tags': ((Tags, list), False),
    }


class Configuration(AWSObject):
    resource_type = "AWS::AmazonMQ::Configuration"

    props = {
        'Data': (basestring, True),
        'Description': (basestring, False),
        'EngineType': (basestring, True),
        'EngineVersion': (basestring, True),
        'Name': (basestring, True),
    }


class ConfigurationAssociation(AWSObject):
    resource_type = "AWS::AmazonMQ::ConfigurationAssociation"

    props = {
        'Broker': (basestring, True),
        'Configuration': (ConfigurationId, True),
    }
