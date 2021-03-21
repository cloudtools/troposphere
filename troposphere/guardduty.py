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
        'FindingPublishingFrequency': (str, False),
    }


class Condition(AWSProperty):
    props = {
        'Eq': ([str], False),
        'Gte': (integer, False),
        'Lt': (integer, False),
        'Lte': (integer, False),
        'Neq': ([str], False),
    }


class FindingCriteria(AWSProperty):
    props = {
        'Criterion': (dict, False),
        'ItemType': (Condition, False),
    }


class Filter(AWSObject):
    resource_type = "AWS::GuardDuty::Filter"

    props = {
        'Action': (str, True),
        'Description': (str, True),
        'DetectorId': (str, True),
        'FindingCriteria': (FindingCriteria, True),
        'Name': (str, False),
        'Rank': (integer, True),
    }


class IPSet(AWSObject):
    resource_type = 'AWS::GuardDuty::IPSet'

    props = {
        'Activate': (boolean, True),
        'DetectorId': (str, True),
        'Format': (str, True),
        'Location': (str, True),
        'Name': (str, False),
    }


class Master(AWSObject):
    resource_type = "AWS::GuardDuty::Master"

    props = {
        'DetectorId': (str, True),
        'InvitationId': (str, False),
        'MasterId': (str, True),
    }


class Member(AWSObject):
    resource_type = "AWS::GuardDuty::Member"

    props = {
        'DetectorId': (str, True),
        'Email': (str, True),
        'MemberId': (str, True),
        'Message': (str, False),
        'Status': (str, False),
        'DisableEmailNotification': (bool, False),
    }


class ThreatIntelSet(AWSObject):
    resource_type = 'AWS::GuardDuty::ThreatIntelSet'

    props = {
        'Activate': (boolean, True),
        'DetectorId': (str, True),
        'Format': (str, True),
        'Location': (str, True),
        'Name': (str, False),
    }
