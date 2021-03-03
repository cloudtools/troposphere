# Copyright (c) 2012-2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import AWSObject, AWSProperty
from .validators import (session_findingpublishingfrequency,
                         session_status, integer,
                         findingsfilter_action)


class Session(AWSObject):
    resource_type = "AWS::Macie::Session"

    props = {
        'FindingPublishingFrequency': (session_findingpublishingfrequency, False),  # NOQA
        'Status': (session_status, False),
    }


class CustomDataIdentifier(AWSObject):
    resource_type = "AWS::Macie::CustomDataIdentifier"

    props = {
        'Description': (basestring, False),
        'IgnoreWords': ([basestring], False),
        'Keywords': ([basestring], False),
        'MaximumMatchDistance': (integer, False),
        'Name': (basestring, True),
        'Regex': (basestring, True)
    }


class FindingCriteria(AWSProperty):
    props = {
        'Criterion': (dict, False),
    }


class FindingsFilter(AWSObject):
    resource_type = "AWS::Macie::FindingsFilter"

    props = {
        'Action': (findingsfilter_action, False),
        'Description': (basestring, False),
        'FindingCriteria': (FindingCriteria, False),
        'Name': (basestring, False),
        'Position': (integer, False)
    }
