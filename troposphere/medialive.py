# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#

from . import AWSObject
from . import AWSProperty
from troposphere import Tags
from .validators import integer


class AudioLanguageSelection(AWSProperty):
    props = {
        'LanguageCode': (str, False),
        'LanguageSelectionPolicy': (str, False),
    }


class AudioPidSelection(AWSProperty):
    props = {
        'Pid': (integer, False),
    }


class AudioSelectorSettings(AWSProperty):
    props = {
        'AudioLanguageSelection': (AudioLanguageSelection, False),
        'AudioPidSelection': (AudioPidSelection, False),
    }


class AudioSelector(AWSProperty):
    props = {
        'Name': (str, False),
        'SelectorSettings': (AudioSelectorSettings, False),
    }


class AribSourceSettings(AWSProperty):
    props = {
    }


class DvbSubSourceSettings(AWSProperty):
    props = {
        'Pid': (integer, False),
    }


class EmbeddedSourceSettings(AWSProperty):
    props = {
        'Convert608To708': (str, False),
        'Scte20Detection': (str, False),
        'Source608ChannelNumber': (integer, False),
        'Source608TrackNumber': (integer, False),
    }


class Scte20SourceSettings(AWSProperty):
    props = {
        'Convert608To708': (str, False),
        'Source608ChannelNumber': (integer, False),
    }


class Scte27SourceSettings(AWSProperty):
    props = {
        'Pid': (integer, False),
    }


class TeletextSourceSettings(AWSProperty):
    props = {
        'PageNumber': (str, False),
    }


class CaptionSelectorSettings(AWSProperty):
    props = {
        'AribSourceSettings': (AribSourceSettings, False),
        'DvbSubSourceSettings': (DvbSubSourceSettings, False),
        'EmbeddedSourceSettings': (EmbeddedSourceSettings, False),
        'Scte20SourceSettings': (Scte20SourceSettings, False),
        'Scte27SourceSettings': (Scte27SourceSettings, False),
        'TeletextSourceSettings': (TeletextSourceSettings, False),
    }


class CaptionSelector(AWSProperty):
    props = {
        'LanguageCode': (str, False),
        'Name': (str, False),
        'SelectorSettings': (CaptionSelectorSettings, False),
    }


class HlsInputSettings(AWSProperty):
    props = {
        'Bandwidth': (integer, False),
        'BufferSegments': (integer, False),
        'Retries': (integer, False),
        'RetryInterval': (integer, False),
    }


class NetworkInputSettings(AWSProperty):
    props = {
        'HlsInputSettings': (HlsInputSettings, False),
        'ServerValidation': (str, False),
    }


class VideoSelectorPid(AWSProperty):
    props = {
        'Pid': (integer, False),
    }


class VideoSelectorProgramId(AWSProperty):
    props = {
        'ProgramId': (integer, False),
    }


class VideoSelectorSettings(AWSProperty):
    props = {
        'VideoSelectorPid': (VideoSelectorPid, False),
        'VideoSelectorProgramId': (VideoSelectorProgramId, False),
    }


class VideoSelector(AWSProperty):
    props = {
        'ColorSpace': (str, False),
        'ColorSpaceUsage': (str, False),
        'SelectorSettings': (VideoSelectorSettings, False),
    }


class InputSettings(AWSProperty):
    props = {
        'AudioSelectors': ([AudioSelector], False),
        'CaptionSelectors': ([CaptionSelector], False),
        'DeblockFilter': (str, False),
        'DenoiseFilter': (str, False),
        'FilterStrength': (integer, False),
        'InputFilter': (str, False),
        'NetworkInputSettings': (NetworkInputSettings, False),
        'SourceEndBehavior': (str, False),
        'VideoSelector': (VideoSelector, False),
    }


class InputAttachment(AWSProperty):
    props = {
        'InputAttachmentName': (str, False),
        'InputId': (str, False),
        'InputSettings': (InputSettings, False),
    }


class InputSpecification(AWSProperty):
    props = {
        'Codec': (str, False),
        'MaximumBitrate': (str, False),
        'Resolution': (str, False),
    }


class MediaPackageOutputDestinationSettings(AWSProperty):
    props = {
        'ChannelId': (str, False),
    }


class OutputDestinationSettings(AWSProperty):
    props = {
        'PasswordParam': (str, False),
        'StreamName': (str, False),
        'Url': (str, False),
        'Username': (str, False),
    }


class OutputDestination(AWSProperty):
    props = {
        'Id': (str, False),
        'MediaPackageSettings':
            ([MediaPackageOutputDestinationSettings], False),
        'Settings': ([OutputDestinationSettings], False),
    }


class Channel(AWSObject):
    resource_type = "AWS::MediaLive::Channel"

    props = {
        'ChannelClass': (str, False),
        'Destinations': ([OutputDestination], False),
        'EncoderSettings': (dict, False),
        'InputAttachments': ([InputAttachment], False),
        'InputSpecification': (InputSpecification, False),
        'LogLevel': (str, False),
        'Name': (str, False),
        'RoleArn': (str, False),
        'Tags': (Tags, False),
    }


class InputDestinationRequest(AWSProperty):
    props = {
        'StreamName': (str, False),
    }


class InputSourceRequest(AWSProperty):
    props = {
        'PasswordParam': (str, False),
        'Url': (str, False),
        'Username': (str, False),
    }


class InputVpcRequest(AWSProperty):
    props = {
        'SecurityGroupIds': ([str], False),
        'SubnetIds': ([str], False),
    }


class MediaConnectFlowRequest(AWSProperty):
    props = {
        'FlowArn': (str, False),
    }


class Input(AWSObject):
    resource_type = "AWS::MediaLive::Input"

    props = {
        'Destinations': ([InputDestinationRequest], False),
        'InputSecurityGroups': ([str], False),
        'MediaConnectFlows': ([MediaConnectFlowRequest], False),
        'Name': (str, False),
        'RoleArn': (str, False),
        'Sources': ([InputSourceRequest], False),
        'Tags': (Tags, False),
        'Type': (str, False),
        'Vpc': (InputVpcRequest, False),
    }


class InputWhitelistRuleCidr(AWSProperty):
    props = {
        'Cidr': (str, False),
    }


class InputSecurityGroup(AWSObject):
    resource_type = "AWS::MediaLive::InputSecurityGroup"

    props = {
        'Tags': (Tags, False),
        'WhitelistRules': ([InputWhitelistRuleCidr], False),
    }
