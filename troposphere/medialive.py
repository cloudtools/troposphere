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
        'LanguageCode': (basestring, False),
        'LanguageSelectionPolicy': (basestring, False),
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
        'Name': (basestring, False),
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
        'Convert608To708': (basestring, False),
        'Scte20Detection': (basestring, False),
        'Source608ChannelNumber': (integer, False),
        'Source608TrackNumber': (integer, False),
    }


class Scte20SourceSettings(AWSProperty):
    props = {
        'Convert608To708': (basestring, False),
        'Source608ChannelNumber': (integer, False),
    }


class Scte27SourceSettings(AWSProperty):
    props = {
        'Pid': (integer, False),
    }


class TeletextSourceSettings(AWSProperty):
    props = {
        'PageNumber': (basestring, False),
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
        'LanguageCode': (basestring, False),
        'Name': (basestring, False),
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
        'ServerValidation': (basestring, False),
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
        'ColorSpace': (basestring, False),
        'ColorSpaceUsage': (basestring, False),
        'SelectorSettings': (VideoSelectorSettings, False),
    }


class InputSettings(AWSProperty):
    props = {
        'AudioSelectors': ([AudioSelector], False),
        'CaptionSelectors': ([CaptionSelector], False),
        'DeblockFilter': (basestring, False),
        'DenoiseFilter': (basestring, False),
        'FilterStrength': (integer, False),
        'InputFilter': (basestring, False),
        'NetworkInputSettings': (NetworkInputSettings, False),
        'SourceEndBehavior': (basestring, False),
        'VideoSelector': (VideoSelector, False),
    }


class InputAttachment(AWSProperty):
    props = {
        'InputAttachmentName': (basestring, False),
        'InputId': (basestring, False),
        'InputSettings': (InputSettings, False),
    }


class InputSpecification(AWSProperty):
    props = {
        'Codec': (basestring, False),
        'MaximumBitrate': (basestring, False),
        'Resolution': (basestring, False),
    }


class MediaPackageOutputDestinationSettings(AWSProperty):
    props = {
        'ChannelId': (basestring, False),
    }


class OutputDestinationSettings(AWSProperty):
    props = {
        'PasswordParam': (basestring, False),
        'StreamName': (basestring, False),
        'Url': (basestring, False),
        'Username': (basestring, False),
    }


class OutputDestination(AWSProperty):
    props = {
        'Id': (basestring, False),
        'MediaPackageSettings':
            ([MediaPackageOutputDestinationSettings], False),
        'Settings': ([OutputDestinationSettings], False),
    }


class Channel(AWSObject):
    resource_type = "AWS::MediaLive::Channel"

    props = {
        'ChannelClass': (basestring, False),
        'Destinations': ([OutputDestination], False),
        'EncoderSettings': (dict, False),
        'InputAttachments': ([InputAttachment], False),
        'InputSpecification': (InputSpecification, False),
        'LogLevel': (basestring, False),
        'Name': (basestring, False),
        'RoleArn': (basestring, False),
        'Tags': (Tags, False),
    }


class InputDestinationRequest(AWSProperty):
    props = {
        'StreamName': (basestring, False),
    }


class InputSourceRequest(AWSProperty):
    props = {
        'PasswordParam': (basestring, False),
        'Url': (basestring, False),
        'Username': (basestring, False),
    }


class InputVpcRequest(AWSProperty):
    props = {
        'SecurityGroupIds': ([basestring], False),
        'SubnetIds': ([basestring], False),
    }


class MediaConnectFlowRequest(AWSProperty):
    props = {
        'FlowArn': (basestring, False),
    }


class Input(AWSObject):
    resource_type = "AWS::MediaLive::Input"

    props = {
        'Destinations': ([InputDestinationRequest], False),
        'InputSecurityGroups': ([basestring], False),
        'MediaConnectFlows': ([MediaConnectFlowRequest], False),
        'Name': (basestring, False),
        'RoleArn': (basestring, False),
        'Sources': ([InputSourceRequest], False),
        'Tags': (Tags, False),
        'Type': (basestring, False),
        'Vpc': (InputVpcRequest, False),
    }


class InputWhitelistRuleCidr(AWSProperty):
    props = {
        'Cidr': (basestring, False),
    }


class InputSecurityGroup(AWSObject):
    resource_type = "AWS::MediaLive::InputSecurityGroup"

    props = {
        'Tags': (Tags, False),
        'WhitelistRules': ([InputWhitelistRuleCidr], False),
    }
