# Copyright (c) 2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject
from .validators import boolean


class Graph(AWSObject):
    resource_type = "AWS::Detective::Graph"

    props = {
    }


class MemberInvitation(AWSObject):
    resource_type = "AWS::Detective::MemberInvitation"

    props = {
        'DisableEmailNotification': (boolean, False),
        'GraphArn': (basestring, True),
        'MemberEmailAddress': (basestring, True),
        'MemberId': (basestring, True),
        'Message': (basestring, False),
    }
