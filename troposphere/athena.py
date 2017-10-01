# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject


class NamedQuery(AWSObject):
    resource_type = "AWS::Athena::NamedQuery"

    props = {
        'Database': (basestring, True),
        'Description': (basestring, False),
        'Name': (basestring, False),
        'QueryString': (basestring, True),
    }
