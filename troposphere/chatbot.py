# Copyright (c) 2012-2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import AWSObject


VALID_SLACKCHANNELCONFIGURATION_LOGGINGLEVEL = ('ERROR', 'INFO', 'NODE')


def validate_logginglevel(slackchannelconfiguration_logginglevel):
    """Validate LoggingLevel for SlackChannelConfiguration"""

    if slackchannelconfiguration_logginglevel not in VALID_SLACKCHANNELCONFIGURATION_LOGGINGLEVEL:  # NOQA
        raise ValueError("SlackChannelConfiguration LoggingLevel must be one of: %s" %  # NOQA
                         ", ".join(VALID_SLACKCHANNELCONFIGURATION_LOGGINGLEVEL))  # NOQA
    return slackchannelconfiguration_logginglevel


class SlackChannelConfiguration(AWSObject):
    resource_type = "AWS::Chatbot::SlackChannelConfiguration"

    props = {
        'Arn': (basestring, False),
        'ConfigurationName': (basestring, True),
        'IamRoleArn': (basestring, True),
        'LoggingLevel': (validate_logginglevel, False),
        'SlackChannelId': (basestring, True),
        'SlackWorkspaceId': (basestring, True),
        'SnsTopicArns': ([basestring], False),
    }
