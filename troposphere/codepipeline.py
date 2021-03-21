# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer


class ActionTypeId(AWSProperty):
    props = {
        'Category': (str, True),
        'Owner': (str, True),
        'Provider': (str, True),
        'Version': (str, True)
    }


class ArtifactDetails(AWSProperty):
    props = {
        'MaximumCount': (integer, True),
        'MinimumCount': (integer, True)
    }


class Blockers(AWSProperty):
    props = {
        'Name': (str, True),
        'Type': (str, True)
    }


class ConfigurationProperties(AWSProperty):
    props = {
        'Description': (str, False),
        'Key': (boolean, True),
        'Name': (str, True),
        'Queryable': (boolean, False),
        'Required': (boolean, True),
        'Secret': (boolean, True),
        'Type': (str, False)
    }


class EncryptionKey(AWSProperty):
    props = {
        'Id': (str, True),
        'Type': (str, True)
    }


class DisableInboundStageTransitions(AWSProperty):
    props = {
        'Reason': (str, True),
        'StageName': (str, True)
    }


class InputArtifacts(AWSProperty):
    props = {
        'Name': (str, True)
    }


class OutputArtifacts(AWSProperty):
    props = {
        'Name': (str, True)
    }


class Settings(AWSProperty):
    props = {
        'EntityUrlTemplate': (str, False),
        'ExecutionUrlTemplate': (str, False),
        'RevisionUrlTemplate': (str, False),
        'ThirdPartyConfigurationUrl': (str, False)
    }


class ArtifactStore(AWSProperty):
    props = {
        'EncryptionKey': (EncryptionKey, False),
        'Location': (str, True),
        'Type': (str, True)
    }


class ArtifactStoreMap(AWSProperty):
    props = {
        'ArtifactStore': (ArtifactStore, True),
        'Region': (str, True)
    }


class Actions(AWSProperty):
    props = {
        'ActionTypeId': (ActionTypeId, True),
        'Configuration': (dict, False),
        'InputArtifacts': ([InputArtifacts], False),
        'Name': (str, True),
        'Namespace': (str, False),
        'OutputArtifacts': ([OutputArtifacts], False),
        'Region': (str, False),
        'RoleArn': (str, False),
        'RunOrder': (integer, False)
    }


class Stages(AWSProperty):
    props = {
        'Actions': ([Actions], True),
        'Blockers': ([Blockers], False),
        'Name': (str, True)
    }


class CustomActionType(AWSObject):
    resource_type = "AWS::CodePipeline::CustomActionType"

    props = {
        'Category': (str, True),
        'ConfigurationProperties': ([ConfigurationProperties], False),
        'InputArtifactDetails': (ArtifactDetails, True),
        'OutputArtifactDetails': (ArtifactDetails, True),
        'Provider': (str, True),
        'Settings': (Settings, False),
        'Tags': (Tags, False),
        'Version': (str, False),
    }


class Pipeline(AWSObject):
    resource_type = "AWS::CodePipeline::Pipeline"

    props = {
        'ArtifactStore': (ArtifactStore, False),
        'ArtifactStores': ([ArtifactStoreMap], False),
        'DisableInboundStageTransitions':
            ([DisableInboundStageTransitions], False),
        'Name': (str, False),
        'RestartExecutionOnUpdate': (boolean, False),
        'RoleArn': (str, True),
        'Stages': ([Stages], True),
        'Tags': (Tags, False),
    }


class WebhookAuthConfiguration(AWSProperty):
    props = {
        'AllowedIPRange': (str, False),
        'SecretToken': (str, False),
    }


class WebhookFilterRule(AWSProperty):
    props = {
        'JsonPath': (str, True),
        'MatchEquals': (str, False),
    }


class Webhook(AWSObject):
    resource_type = "AWS::CodePipeline::Webhook"

    props = {
        'Authentication': (str, True),
        'AuthenticationConfiguration': (WebhookAuthConfiguration, True),
        'Filters': ([WebhookFilterRule], True),
        'Name': (str, False),
        'RegisterWithThirdParty': (boolean, False),
        'TargetAction': (str, True),
        'TargetPipeline': (str, True),
        'TargetPipelineVersion': (integer, True),
    }
