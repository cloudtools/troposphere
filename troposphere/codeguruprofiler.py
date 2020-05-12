# Copyright (c) 2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject


class ProfilingGroup(AWSObject):
    resource_type = "AWS::CodeGuruProfiler::ProfilingGroup"

    props = {
        'ProfilingGroupName': (basestring, True),
    }
