# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject


class Domain(AWSObject):
    props = {}

    def __init__(self, name, **kwargs):
        self.type = "AWS::SDB::Domain"
        sup = super(Domain, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)
