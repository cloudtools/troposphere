# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def canary_runtime_version(runtime_version):
    """
    Property: Canary.RuntimeVersion
    """

    valid_runtime_versions = [
        "syn-nodejs-playwright-1.0",
        "syn-nodejs-puppeteer-4.0",
        "syn-nodejs-puppeteer-5.0",
        "syn-nodejs-puppeteer-5.1",
        "syn-nodejs-puppeteer-5.2",
        "syn-nodejs-puppeteer-6.0",
        "syn-nodejs-puppeteer-6.1",
        "syn-nodejs-puppeteer-6.2",
        "syn-nodejs-puppeteer-7.0",
        "syn-nodejs-puppeteer-8.0",
        "syn-nodejs-puppeteer-9.0",
        "syn-nodejs-puppeteer-9.1",
        "syn-python-selenium-1.0",
        "syn-python-selenium-1.1",
        "syn-python-selenium-1.2",
        "syn-python-selenium-1.3",
        "syn-python-selenium-2.0",
        "syn-python-selenium-2.1",
        "syn-python-selenium-3.0",
        "syn-python-selenium-4.0",
        "syn-python-selenium-4.1",
    ]
    if runtime_version not in valid_runtime_versions:
        raise ValueError(
            'RuntimeVersion must be one of: "%s"' % (", ".join(valid_runtime_versions))
        )
    return runtime_version
