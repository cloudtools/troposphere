# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, integer


class Detector(AWSObject):
    resource_type = 'AWS::GuardDuty::Detector'

    props = {
        'Enable': (boolean, True),
        'FindingPublishingFrequency': (basestring, False),
    }


class Condition(AWSProperty):
    props = {
        'Eq': ([basestring], False),
        'Gte': (integer, False),
        'Lt': (integer, False),
        'Lte': (integer, False),
        'Neq': ([basestring], False),
    }


class FindingCriteria(AWSProperty):
    props = {
        'Criterion': (dict, False),
        'ItemType': (Condition, False),
    }


class Filter(AWSObject):
    resource_type = "AWS::GuardDuty::Filter"

    props = {
        'Action': (basestring, True),
        'Description': (basestring, True),
        'DetectorId': (basestring, True),
        'FindingCriteria': (FindingCriteria, True),
        'Name': (basestring, False),
        'Rank': (integer, True),
    }


class IPSet(AWSObject):
    resource_type = 'AWS::GuardDuty::IPSet'

    props = {
        'Activate': (boolean, True),
        'DetectorId': (basestring, True),
        'Format': (basestring, True),
        'Location': (basestring, True),
        'Name': (basestring, False),
    }


class Master(AWSObject):
    resource_type = "AWS::GuardDuty::Master"

    props = {
        'DetectorId': (basestring, True),
        'InvitationId': (basestring, False),
        'MasterId': (basestring, True),
    }


class Member(AWSObject):
    resource_type = "AWS::GuardDuty::Member"

    props = {
        'DetectorId': (basestring, True),
        'Email': (basestring, True),
        'MemberId': (basestring, True),
        'Message': (basestring, False),
        'Status': (basestring, False),
        'DisableEmailNotification': (bool, False),
    }


class ThreatIntelSet(AWSObject):
    resource_type = 'AWS::GuardDuty::ThreatIntelSet'

    props = {
        'Activate': (boolean, True),
        'DetectorId': (basestring, True),
        'Format': (basestring, True),
        'Location': (basestring, True),
        'Name': (basestring, False),
    }
