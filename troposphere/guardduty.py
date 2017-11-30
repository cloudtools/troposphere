# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject
from .validators import boolean


class Detector(AWSObject):
    props = {
        'Enable': (boolean, True),
    }


class IPSet(AWSObject):
    props = {
        'Activate': (boolean, True),
        'DetectorId': (basestring, True),
        'Format': (basestring, True),
        'Location': (basestring, True),
        'Name': (basestring, False),
    }


class ThreatIntelSet(AWSObject):
    props = {
        'Activate': (boolean, True),
        'DetectorId': (basestring, True),
        'Format': (basestring, True),
        'Location': (basestring, True),
        'Name': (basestring, False),
    }
