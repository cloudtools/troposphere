# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject


class Workspace(AWSObject):
    resource_type = "AWS::WorkSpaces::Workspace"

    props = {
        'BundleId': (basestring, True),
        'DirectoryId': (basestring, True),
        'UserName': (basestring, True),
    }
