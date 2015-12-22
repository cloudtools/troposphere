# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, integer


class ActionTypeID(AWSProperty):
    props = {
        'Category': (basestring, True),
        'Owner': (basestring, True),
        'Provider': (basestring, True),
        'Version': (basestring, True)
    }


class ArtifactDetails(AWSProperty):
    props = {
        'MaximumCount': (integer, True),
        'MinimumCount': (integer, True)
    }


class Blockers(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Type': (basestring, True)
    }


class ConfigurationProperties(AWSProperty):
    props = {
        'Description': (basestring, False),
        'Key': (boolean, True),
        'Name': (basestring, True),
        'Queryable': (boolean, False),
        'Required': (boolean, True),
        'Secret': (boolean, True),
        'Type': (basestring, False)
    }


class EncryptionKey(AWSProperty):
    props = {
        'Id': (basestring, True),
        'Type': (basestring, True)
    }


class DisableInboundStageTransitions(AWSProperty):
    props = {
        'Reason': (basestring, True),
        'StageName': (basestring, True)
    }


class InputArtifacts(AWSProperty):
    props = {
        'Name': (basestring, True)
    }


class OutputArtifacts(AWSProperty):
    props = {
        'Name': (basestring, True)
    }


class Settings(AWSProperty):
    props = {
        'EntityUrlTemplate': (basestring, False),
        'ExecutionUrlTemplate': (basestring, False),
        'RevisionUrlTemplate': (basestring, False),
        'ThirdPartyConfigurationUrl': (basestring, False)
    }


class ArtifactStore(AWSProperty):
    props = {
        'EncryptionKey': (EncryptionKey, False),
        'Location': (basestring, True),
        'Type': (basestring, True)
    }


class Actions(AWSProperty):
    props = {
        'ActionTypeId': (ActionTypeID, True),
        'Configuration': (dict, False),
        'InputArtifacts': ([InputArtifacts], False),
        'Name': (basestring, True),
        'OutputArtifacts': ([OutputArtifacts], False),
        'RoleArn': (basestring, False),
        'RunOrder': (integer, False)
    }


class Stages(AWSProperty):
    props = {
        'Actions': ([Actions], True),
        'Blockers': ([Blockers], False),
        'Name': (basestring, True)
    }


class CustomActionType(AWSObject):
    resource_type = "AWS::CodePipeline::CustomActionType"

    props = {
        'Category': (basestring, True),
        'ConfigurationProperties': ([ConfigurationProperties], False),
        'InputArtifactDetails': (ArtifactDetails, True),
        'OutputArtifactDetails': (ArtifactDetails, True),
        'Provider': (basestring, True),
        'Settings': (Settings, False),
        'Version': (basestring, False)
    }


class Pipeline(AWSObject):
    resource_type = "AWS::CodePipeline::Pipeline"

    props = {
        'ArtifactStore': (ArtifactStore, True),
        'DisableInboundStageTransitions':
            ([DisableInboundStageTransitions], False),
        'Name': (basestring, False),
        'RestartExecutionOnUpdate': (boolean, False),
        'RoleArn': (basestring, True),
        'Stages': ([Stages], True)
    }
