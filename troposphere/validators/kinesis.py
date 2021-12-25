# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import tags_or_list


def kinesis_stream_mode(mode):
    """
    Property: StreamModeDetails.StreamMode
    """
    valid_modes = ["ON_DEMAND", "PROVISIONED"]
    if mode not in valid_modes:
        raise ValueError('ContentType must be one of: "%s"' % (", ".join(valid_modes)))
    return mode


def validate_tags_or_list(x):
    """
    Property: Stream.Tags
    """
    return tags_or_list(x)
