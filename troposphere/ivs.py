# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class Channel(AWSObject):
    """
    `Channel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html>`__
    """

    resource_type = "AWS::IVS::Channel"

    props: PropsDictType = {
        "Authorized": (boolean, False),
        "InsecureIngest": (boolean, False),
        "LatencyMode": (str, False),
        "Name": (str, False),
        "RecordingConfigurationArn": (str, False),
        "Tags": (Tags, False),
        "Type": (str, False),
    }


class PlaybackKeyPair(AWSObject):
    """
    `PlaybackKeyPair <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackkeypair.html>`__
    """

    resource_type = "AWS::IVS::PlaybackKeyPair"

    props: PropsDictType = {
        "Name": (str, False),
        "PublicKeyMaterial": (str, False),
        "Tags": (Tags, False),
    }


class S3DestinationConfiguration(AWSProperty):
    """
    `S3DestinationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-s3destinationconfiguration.html>`__
    """

    props: PropsDictType = {
        "BucketName": (str, True),
    }


class DestinationConfiguration(AWSProperty):
    """
    `DestinationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-destinationconfiguration.html>`__
    """

    props: PropsDictType = {
        "S3": (S3DestinationConfiguration, True),
    }


class ThumbnailConfiguration(AWSProperty):
    """
    `ThumbnailConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html>`__
    """

    props: PropsDictType = {
        "RecordingMode": (str, True),
        "TargetIntervalSeconds": (integer, False),
    }


class RecordingConfiguration(AWSObject):
    """
    `RecordingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html>`__
    """

    resource_type = "AWS::IVS::RecordingConfiguration"

    props: PropsDictType = {
        "DestinationConfiguration": (DestinationConfiguration, True),
        "Name": (str, False),
        "RecordingReconnectWindowSeconds": (integer, False),
        "Tags": (Tags, False),
        "ThumbnailConfiguration": (ThumbnailConfiguration, False),
    }


class StreamKey(AWSObject):
    """
    `StreamKey <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-streamkey.html>`__
    """

    resource_type = "AWS::IVS::StreamKey"

    props: PropsDictType = {
        "ChannelArn": (str, True),
        "Tags": (Tags, False),
    }
