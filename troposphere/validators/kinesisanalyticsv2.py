# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_runtime_environment(runtime_environment):
    """
    Validate RuntimeEnvironment for Application
    Property: Application.RuntimeEnvironment
    """

    VALID_RUNTIME_ENVIRONMENTS = (
        "FLINK-1_6",
        "FLINK-1_8",
        "FLINK-1_11",
        "FLINK-1_13",
        "SQL-1_0",
        "ZEPPELIN-FLINK-1_0",
        "ZEPPELIN-FLINK-2_0",
    )

    if runtime_environment not in VALID_RUNTIME_ENVIRONMENTS:
        raise ValueError(
            "Application RuntimeEnvironment must be one of: %s"
            % ", ".join(VALID_RUNTIME_ENVIRONMENTS)
        )
    return runtime_environment
