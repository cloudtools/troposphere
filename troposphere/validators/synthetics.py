# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def canary_runtime_version(runtime_version):
    """
    Property: Canary.RuntimeVersion
    """

    valid_runtime_versions = ["syn-nodejs-2.0", "syn-nodejs-2.0-beta", "syn-1.0"]
    if runtime_version not in valid_runtime_versions:
        raise ValueError(
            'RuntimeVersion must be one of: "%s"' % (", ".join(valid_runtime_versions))
        )
    return runtime_version
