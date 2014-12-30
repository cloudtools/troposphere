# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject


class Domain(AWSObject):
    resource_type = "AWS::SDB::Domain"

    props = {}
