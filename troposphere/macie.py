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
        'Description': (str, False),
        'IgnoreWords': ([str], False),
        'Keywords': ([str], False),
        'MaximumMatchDistance': (integer, False),
        'Name': (str, True),
        'Regex': (str, True)
    }


class FindingCriteria(AWSProperty):
    props = {
        'Criterion': (dict, False),
    }


class FindingsFilter(AWSObject):
    resource_type = "AWS::Macie::FindingsFilter"

    props = {
        'Action': (findingsfilter_action, False),
        'Description': (str, False),
        'FindingCriteria': (FindingCriteria, False),
        'Name': (str, False),
        'Position': (integer, False)
    }
