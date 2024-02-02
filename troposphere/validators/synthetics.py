# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def canary_runtime_version(runtime_version):
    """
    Property: Canary.RuntimeVersion
    """

    valid_runtime_versions = [
        "syn-nodejs-puppeteer-4.0",
        "syn-nodejs-puppeteer-5.0",
        "syn-nodejs-puppeteer-5.1",
        "syn-nodejs-puppeteer-6.0",
        "syn-nodejs-puppeteer-6.1",
    ]
    if runtime_version not in valid_runtime_versions:
        raise ValueError(
            'RuntimeVersion must be one of: "%s"' % (", ".join(valid_runtime_versions))
        )
    return runtime_version
