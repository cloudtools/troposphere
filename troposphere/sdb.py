# Copyright (c) 2011-2012, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import json
from . import AWSHelperFn, AWSObject


class Domain(AWSObject):
    props = {
        'Description': (basestring, False),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::SDB::Domain"
        sup = super(Domain, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)
