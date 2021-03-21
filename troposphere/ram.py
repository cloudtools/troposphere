# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject
from troposphere import Tags
from .validators import boolean


class ResourceShare(AWSObject):
    resource_type = "AWS::RAM::ResourceShare"

    props = {
        'AllowExternalPrincipals': (boolean, False),
        'Name': (str, True),
        'Principals': ([str], False),
        'ResourceArns': ([str], False),
        'Tags': (Tags, False),
    }
