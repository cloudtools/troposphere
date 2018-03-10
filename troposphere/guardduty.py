# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject
from .validators import boolean


class Detector(AWSObject):
    resource_type = 'AWS::GuardDuty::Detector'

    props = {
        'Enable': (boolean, True),
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
        'InvitationId': (basestring, True),
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
