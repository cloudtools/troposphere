# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject


class Document(AWSObject):
    resource_type = "AWS::SSM::Document"

    props = {
        # Need a better implementation of the SSM Document
        'Content': (dict, True),
    }
