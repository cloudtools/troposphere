# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double


class PredictiveDialerConfig(AWSProperty):
    """
    `PredictiveDialerConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-predictivedialerconfig.html>`__
    """

    props: PropsDictType = {
        "BandwidthAllocation": (double, True),
    }


class ProgressiveDialerConfig(AWSProperty):
    """
    `ProgressiveDialerConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-progressivedialerconfig.html>`__
    """

    props: PropsDictType = {
        "BandwidthAllocation": (double, True),
    }


class DialerConfig(AWSProperty):
    """
    `DialerConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-dialerconfig.html>`__
    """

    props: PropsDictType = {
        "PredictiveDialerConfig": (PredictiveDialerConfig, False),
        "ProgressiveDialerConfig": (ProgressiveDialerConfig, False),
    }


class AnswerMachineDetectionConfig(AWSProperty):
    """
    `AnswerMachineDetectionConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-answermachinedetectionconfig.html>`__
    """

    props: PropsDictType = {
        "EnableAnswerMachineDetection": (boolean, True),
    }


class OutboundCallConfig(AWSProperty):
    """
    `OutboundCallConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-outboundcallconfig.html>`__
    """

    props: PropsDictType = {
        "AnswerMachineDetectionConfig": (AnswerMachineDetectionConfig, False),
        "ConnectContactFlowArn": (str, True),
        "ConnectQueueArn": (str, True),
        "ConnectSourcePhoneNumber": (str, False),
    }


class Campaign(AWSObject):
    """
    `Campaign <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaigns-campaign.html>`__
    """

    resource_type = "AWS::ConnectCampaigns::Campaign"

    props: PropsDictType = {
        "ConnectInstanceArn": (str, True),
        "DialerConfig": (DialerConfig, True),
        "Name": (str, True),
        "OutboundCallConfig": (OutboundCallConfig, True),
        "Tags": (Tags, False),
    }
