# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import integer, boolean


class Targets(AWSProperty):
    props = {
        'Key': (basestring, True),
        'Values': ([basestring], True),
    }


class Association(AWSObject):
    resource_type = "AWS::SSM::Association"

    props = {
        'DocumentVersion': (basestring, False),
        'InstanceId': (basestring, False),
        'Name': (basestring, True),
        'Parameters': (dict, False),
        'ScheduleExpression': (basestring, False),
        'Targets': ([Targets], False),
    }


class Document(AWSObject):
    resource_type = "AWS::SSM::Document"

    props = {
        # Need a better implementation of the SSM Document
        'Content': (dict, True),
        'DocumentType': (basestring, False),
    }


class MaintenanceWindow(AWSObject):
    resource_type = "AWS:SSM::MaintenanceWindow"

    props = {
        'AllowUnassociatedTargets': (boolean, True),
        'Cutoff': (integer, True),
        'Description': (basestring, False),
        'Duration': (integer, True),
        'Name': (basestring, True),
        'Schedule': (basestring, True),
    }


class Parameter(AWSObject):
    resource_type = "AWS::SSM::Parameter"

    props = {
        'Description': (basestring, False),
        'Name': (basestring, False),
        'Type': (basestring, True),
        'Value': (basestring, True),
    }
