# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject
from .validators import boolean


class Workspace(AWSObject):
    resource_type = "AWS::WorkSpaces::Workspace"

    props = {
        'BundleId': (basestring, True),
        'DirectoryId': (basestring, True),
        'UserName': (basestring, True),
        'RootVolumeEncryptionEnabled': (boolean, False),
        'UserVolumeEncryptionEnabled': (boolean, False),
        'VolumeEncryptionKey': (basestring, False),
    }
