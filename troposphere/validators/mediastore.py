# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def containerlevelmetrics_status(status):
    """
    Property: MetricPolicy.ContainerLevelMetrics
    """
    valid_status = ["DISABLED", "ENABLED"]
    if status not in valid_status:
        raise ValueError(
            'ContainerLevelMetrics must be one of: "%s"' % (", ".join(valid_status))
        )
    return status
