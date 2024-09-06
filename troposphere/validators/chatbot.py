# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


def validate_logginglevel(slackchannelconfiguration_logginglevel):
    """
    Validate LoggingLevel for SlackChannelConfiguration
    Property: SlackChannelConfiguration.LoggingLevel
    """

    VALID_SLACKCHANNELCONFIGURATION_LOGGINGLEVEL = ("ERROR", "INFO", "NONE")

    if (
        slackchannelconfiguration_logginglevel
        not in VALID_SLACKCHANNELCONFIGURATION_LOGGINGLEVEL
    ):
        raise ValueError(
            "SlackChannelConfiguration LoggingLevel must be one of: %s"
            % ", ".join(VALID_SLACKCHANNELCONFIGURATION_LOGGINGLEVEL)
        )
    return slackchannelconfiguration_logginglevel
