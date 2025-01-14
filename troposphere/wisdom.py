# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import double


class TagCondition(AWSProperty):
    """
    `TagCondition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-tagcondition.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Value": (str, False),
    }


class OrCondition(AWSProperty):
    """
    `OrCondition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-orcondition.html>`__
    """

    props: PropsDictType = {
        "AndConditions": ([TagCondition], False),
        "TagCondition": (TagCondition, False),
    }


class TagFilter(AWSProperty):
    """
    `TagFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-tagfilter.html>`__
    """

    props: PropsDictType = {
        "AndConditions": ([TagCondition], False),
        "OrConditions": ([OrCondition], False),
        "TagCondition": (TagCondition, False),
    }


class KnowledgeBaseAssociationConfigurationData(AWSProperty):
    """
    `KnowledgeBaseAssociationConfigurationData <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-knowledgebaseassociationconfigurationdata.html>`__
    """

    props: PropsDictType = {
        "ContentTagFilter": (TagFilter, False),
        "MaxResults": (double, False),
        "OverrideKnowledgeBaseSearchType": (str, False),
    }


class AssociationConfigurationData(AWSProperty):
    """
    `AssociationConfigurationData <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-associationconfigurationdata.html>`__
    """

    props: PropsDictType = {
        "KnowledgeBaseAssociationConfigurationData": (
            KnowledgeBaseAssociationConfigurationData,
            True,
        ),
    }


class AssociationConfiguration(AWSProperty):
    """
    `AssociationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-associationconfiguration.html>`__
    """

    props: PropsDictType = {
        "AssociationConfigurationData": (AssociationConfigurationData, False),
        "AssociationId": (str, False),
        "AssociationType": (str, False),
    }


class AnswerRecommendationAIAgentConfiguration(AWSProperty):
    """
    `AnswerRecommendationAIAgentConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration.html>`__
    """

    props: PropsDictType = {
        "AnswerGenerationAIGuardrailId": (str, False),
        "AnswerGenerationAIPromptId": (str, False),
        "AssociationConfigurations": ([AssociationConfiguration], False),
        "IntentLabelingGenerationAIPromptId": (str, False),
        "QueryReformulationAIPromptId": (str, False),
    }


class ManualSearchAIAgentConfiguration(AWSProperty):
    """
    `ManualSearchAIAgentConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-manualsearchaiagentconfiguration.html>`__
    """

    props: PropsDictType = {
        "AnswerGenerationAIGuardrailId": (str, False),
        "AnswerGenerationAIPromptId": (str, False),
        "AssociationConfigurations": ([AssociationConfiguration], False),
    }


class SelfServiceAIAgentConfiguration(AWSProperty):
    """
    `SelfServiceAIAgentConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-selfserviceaiagentconfiguration.html>`__
    """

    props: PropsDictType = {
        "AssociationConfigurations": ([AssociationConfiguration], False),
        "SelfServiceAIGuardrailId": (str, False),
        "SelfServiceAnswerGenerationAIPromptId": (str, False),
        "SelfServicePreProcessingAIPromptId": (str, False),
    }


class AIAgentConfiguration(AWSProperty):
    """
    `AIAgentConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-aiagentconfiguration.html>`__
    """

    props: PropsDictType = {
        "AnswerRecommendationAIAgentConfiguration": (
            AnswerRecommendationAIAgentConfiguration,
            False,
        ),
        "ManualSearchAIAgentConfiguration": (ManualSearchAIAgentConfiguration, False),
        "SelfServiceAIAgentConfiguration": (SelfServiceAIAgentConfiguration, False),
    }


class AIAgent(AWSObject):
    """
    `AIAgent <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagent.html>`__
    """

    resource_type = "AWS::Wisdom::AIAgent"

    props: PropsDictType = {
        "AssistantId": (str, True),
        "Configuration": (AIAgentConfiguration, True),
        "Description": (str, False),
        "Name": (str, False),
        "Tags": (dict, False),
        "Type": (str, True),
    }


class AIAgentVersion(AWSObject):
    """
    `AIAgentVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagentversion.html>`__
    """

    resource_type = "AWS::Wisdom::AIAgentVersion"

    props: PropsDictType = {
        "AIAgentId": (str, True),
        "AssistantId": (str, True),
        "ModifiedTimeSeconds": (double, False),
    }


class GuardrailContentFilterConfig(AWSProperty):
    """
    `GuardrailContentFilterConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailcontentfilterconfig.html>`__
    """

    props: PropsDictType = {
        "InputStrength": (str, True),
        "OutputStrength": (str, True),
        "Type": (str, True),
    }


class AIGuardrailContentPolicyConfig(AWSProperty):
    """
    `AIGuardrailContentPolicyConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-aiguardrailcontentpolicyconfig.html>`__
    """

    props: PropsDictType = {
        "FiltersConfig": ([GuardrailContentFilterConfig], True),
    }


class GuardrailContextualGroundingFilterConfig(AWSProperty):
    """
    `GuardrailContextualGroundingFilterConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailcontextualgroundingfilterconfig.html>`__
    """

    props: PropsDictType = {
        "Threshold": (double, True),
        "Type": (str, True),
    }


class AIGuardrailContextualGroundingPolicyConfig(AWSProperty):
    """
    `AIGuardrailContextualGroundingPolicyConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-aiguardrailcontextualgroundingpolicyconfig.html>`__
    """

    props: PropsDictType = {
        "FiltersConfig": ([GuardrailContextualGroundingFilterConfig], True),
    }


class GuardrailPiiEntityConfig(AWSProperty):
    """
    `GuardrailPiiEntityConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailpiientityconfig.html>`__
    """

    props: PropsDictType = {
        "Action": (str, True),
        "Type": (str, True),
    }


class GuardrailRegexConfig(AWSProperty):
    """
    `GuardrailRegexConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailregexconfig.html>`__
    """

    props: PropsDictType = {
        "Action": (str, True),
        "Description": (str, False),
        "Name": (str, True),
        "Pattern": (str, True),
    }


class AIGuardrailSensitiveInformationPolicyConfig(AWSProperty):
    """
    `AIGuardrailSensitiveInformationPolicyConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig.html>`__
    """

    props: PropsDictType = {
        "PiiEntitiesConfig": ([GuardrailPiiEntityConfig], False),
        "RegexesConfig": ([GuardrailRegexConfig], False),
    }


class GuardrailTopicConfig(AWSProperty):
    """
    `GuardrailTopicConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailtopicconfig.html>`__
    """

    props: PropsDictType = {
        "Definition": (str, True),
        "Examples": ([str], False),
        "Name": (str, True),
        "Type": (str, True),
    }


class AIGuardrailTopicPolicyConfig(AWSProperty):
    """
    `AIGuardrailTopicPolicyConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-aiguardrailtopicpolicyconfig.html>`__
    """

    props: PropsDictType = {
        "TopicsConfig": ([GuardrailTopicConfig], True),
    }


class GuardrailManagedWordsConfig(AWSProperty):
    """
    `GuardrailManagedWordsConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailmanagedwordsconfig.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
    }


class GuardrailWordConfig(AWSProperty):
    """
    `GuardrailWordConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailwordconfig.html>`__
    """

    props: PropsDictType = {
        "Text": (str, True),
    }


class AIGuardrailWordPolicyConfig(AWSProperty):
    """
    `AIGuardrailWordPolicyConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-aiguardrailwordpolicyconfig.html>`__
    """

    props: PropsDictType = {
        "ManagedWordListsConfig": ([GuardrailManagedWordsConfig], False),
        "WordsConfig": ([GuardrailWordConfig], False),
    }


class AIGuardrail(AWSObject):
    """
    `AIGuardrail <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrail.html>`__
    """

    resource_type = "AWS::Wisdom::AIGuardrail"

    props: PropsDictType = {
        "AssistantId": (str, True),
        "BlockedInputMessaging": (str, True),
        "BlockedOutputsMessaging": (str, True),
        "ContentPolicyConfig": (AIGuardrailContentPolicyConfig, False),
        "ContextualGroundingPolicyConfig": (
            AIGuardrailContextualGroundingPolicyConfig,
            False,
        ),
        "Description": (str, False),
        "Name": (str, False),
        "SensitiveInformationPolicyConfig": (
            AIGuardrailSensitiveInformationPolicyConfig,
            False,
        ),
        "Tags": (dict, False),
        "TopicPolicyConfig": (AIGuardrailTopicPolicyConfig, False),
        "WordPolicyConfig": (AIGuardrailWordPolicyConfig, False),
    }


class AIGuardrailVersion(AWSObject):
    """
    `AIGuardrailVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrailversion.html>`__
    """

    resource_type = "AWS::Wisdom::AIGuardrailVersion"

    props: PropsDictType = {
        "AIGuardrailId": (str, True),
        "AssistantId": (str, True),
        "ModifiedTimeSeconds": (double, False),
    }


class TextFullAIPromptEditTemplateConfiguration(AWSProperty):
    """
    `TextFullAIPromptEditTemplateConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiprompt-textfullaipromptedittemplateconfiguration.html>`__
    """

    props: PropsDictType = {
        "Text": (str, True),
    }


class AIPromptTemplateConfiguration(AWSProperty):
    """
    `AIPromptTemplateConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiprompt-aiprompttemplateconfiguration.html>`__
    """

    props: PropsDictType = {
        "TextFullAIPromptEditTemplateConfiguration": (
            TextFullAIPromptEditTemplateConfiguration,
            True,
        ),
    }


class AIPrompt(AWSObject):
    """
    `AIPrompt <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html>`__
    """

    resource_type = "AWS::Wisdom::AIPrompt"

    props: PropsDictType = {
        "ApiFormat": (str, True),
        "AssistantId": (str, False),
        "Description": (str, False),
        "ModelId": (str, True),
        "Name": (str, False),
        "Tags": (dict, False),
        "TemplateConfiguration": (AIPromptTemplateConfiguration, True),
        "TemplateType": (str, True),
        "Type": (str, True),
    }


class AIPromptVersion(AWSObject):
    """
    `AIPromptVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aipromptversion.html>`__
    """

    resource_type = "AWS::Wisdom::AIPromptVersion"

    props: PropsDictType = {
        "AIPromptId": (str, True),
        "AssistantId": (str, True),
        "ModifiedTimeSeconds": (double, False),
    }


class ServerSideEncryptionConfiguration(AWSProperty):
    """
    `ServerSideEncryptionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration.html>`__
    """

    props: PropsDictType = {
        "KmsKeyId": (str, False),
    }


class Assistant(AWSObject):
    """
    `Assistant <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html>`__
    """

    resource_type = "AWS::Wisdom::Assistant"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "ServerSideEncryptionConfiguration": (ServerSideEncryptionConfiguration, False),
        "Tags": (Tags, False),
        "Type": (str, True),
    }


class AssociationData(AWSProperty):
    """
    `AssociationData <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistantassociation-associationdata.html>`__
    """

    props: PropsDictType = {
        "KnowledgeBaseId": (str, True),
    }


class AssistantAssociation(AWSObject):
    """
    `AssistantAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html>`__
    """

    resource_type = "AWS::Wisdom::AssistantAssociation"

    props: PropsDictType = {
        "AssistantId": (str, True),
        "Association": (AssociationData, True),
        "AssociationType": (str, True),
        "Tags": (Tags, False),
    }


class RenderingConfiguration(AWSProperty):
    """
    `RenderingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-renderingconfiguration.html>`__
    """

    props: PropsDictType = {
        "TemplateUri": (str, False),
    }


class AppIntegrationsConfiguration(AWSProperty):
    """
    `AppIntegrationsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html>`__
    """

    props: PropsDictType = {
        "AppIntegrationArn": (str, True),
        "ObjectFields": ([str], False),
    }


class CrawlerLimits(AWSProperty):
    """
    `CrawlerLimits <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-crawlerlimits.html>`__
    """

    props: PropsDictType = {
        "RateLimit": (double, False),
    }


class SeedUrl(AWSProperty):
    """
    `SeedUrl <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-seedurl.html>`__
    """

    props: PropsDictType = {
        "Url": (str, False),
    }


class UrlConfiguration(AWSProperty):
    """
    `UrlConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-urlconfiguration.html>`__
    """

    props: PropsDictType = {
        "SeedUrls": ([SeedUrl], False),
    }


class WebCrawlerConfiguration(AWSProperty):
    """
    `WebCrawlerConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-webcrawlerconfiguration.html>`__
    """

    props: PropsDictType = {
        "CrawlerLimits": (CrawlerLimits, False),
        "ExclusionFilters": ([str], False),
        "InclusionFilters": ([str], False),
        "Scope": (str, False),
        "UrlConfiguration": (UrlConfiguration, True),
    }


class ManagedSourceConfiguration(AWSProperty):
    """
    `ManagedSourceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-managedsourceconfiguration.html>`__
    """

    props: PropsDictType = {
        "WebCrawlerConfiguration": (WebCrawlerConfiguration, True),
    }


class SourceConfiguration(AWSProperty):
    """
    `SourceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-sourceconfiguration.html>`__
    """

    props: PropsDictType = {
        "AppIntegrations": (AppIntegrationsConfiguration, False),
        "ManagedSourceConfiguration": (ManagedSourceConfiguration, False),
    }


class FixedSizeChunkingConfiguration(AWSProperty):
    """
    `FixedSizeChunkingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-fixedsizechunkingconfiguration.html>`__
    """

    props: PropsDictType = {
        "MaxTokens": (double, True),
        "OverlapPercentage": (double, True),
    }


class HierarchicalChunkingLevelConfiguration(AWSProperty):
    """
    `HierarchicalChunkingLevelConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-hierarchicalchunkinglevelconfiguration.html>`__
    """

    props: PropsDictType = {
        "MaxTokens": (double, True),
    }


class HierarchicalChunkingConfiguration(AWSProperty):
    """
    `HierarchicalChunkingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-hierarchicalchunkingconfiguration.html>`__
    """

    props: PropsDictType = {
        "LevelConfigurations": ([HierarchicalChunkingLevelConfiguration], True),
        "OverlapTokens": (double, True),
    }


class SemanticChunkingConfiguration(AWSProperty):
    """
    `SemanticChunkingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-semanticchunkingconfiguration.html>`__
    """

    props: PropsDictType = {
        "BreakpointPercentileThreshold": (double, True),
        "BufferSize": (double, True),
        "MaxTokens": (double, True),
    }


class ChunkingConfiguration(AWSProperty):
    """
    `ChunkingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-chunkingconfiguration.html>`__
    """

    props: PropsDictType = {
        "ChunkingStrategy": (str, True),
        "FixedSizeChunkingConfiguration": (FixedSizeChunkingConfiguration, False),
        "HierarchicalChunkingConfiguration": (HierarchicalChunkingConfiguration, False),
        "SemanticChunkingConfiguration": (SemanticChunkingConfiguration, False),
    }


class ParsingPrompt(AWSProperty):
    """
    `ParsingPrompt <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-parsingprompt.html>`__
    """

    props: PropsDictType = {
        "ParsingPromptText": (str, True),
    }


class BedrockFoundationModelConfiguration(AWSProperty):
    """
    `BedrockFoundationModelConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-bedrockfoundationmodelconfiguration.html>`__
    """

    props: PropsDictType = {
        "ModelArn": (str, True),
        "ParsingPrompt": (ParsingPrompt, False),
    }


class ParsingConfiguration(AWSProperty):
    """
    `ParsingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-parsingconfiguration.html>`__
    """

    props: PropsDictType = {
        "BedrockFoundationModelConfiguration": (
            BedrockFoundationModelConfiguration,
            False,
        ),
        "ParsingStrategy": (str, True),
    }


class VectorIngestionConfiguration(AWSProperty):
    """
    `VectorIngestionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-vectoringestionconfiguration.html>`__
    """

    props: PropsDictType = {
        "ChunkingConfiguration": (ChunkingConfiguration, False),
        "ParsingConfiguration": (ParsingConfiguration, False),
    }


class KnowledgeBase(AWSObject):
    """
    `KnowledgeBase <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html>`__
    """

    resource_type = "AWS::Wisdom::KnowledgeBase"

    props: PropsDictType = {
        "Description": (str, False),
        "KnowledgeBaseType": (str, True),
        "Name": (str, True),
        "RenderingConfiguration": (RenderingConfiguration, False),
        "ServerSideEncryptionConfiguration": (ServerSideEncryptionConfiguration, False),
        "SourceConfiguration": (SourceConfiguration, False),
        "Tags": (Tags, False),
        "VectorIngestionConfiguration": (VectorIngestionConfiguration, False),
    }


class MessageTemplateBodyContentProvider(AWSProperty):
    """
    `MessageTemplateBodyContentProvider <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-messagetemplatebodycontentprovider.html>`__
    """

    props: PropsDictType = {
        "Content": (str, False),
    }


class EmailMessageTemplateContentBody(AWSProperty):
    """
    `EmailMessageTemplateContentBody <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-emailmessagetemplatecontentbody.html>`__
    """

    props: PropsDictType = {
        "Html": (MessageTemplateBodyContentProvider, False),
        "PlainText": (MessageTemplateBodyContentProvider, False),
    }


class EmailMessageTemplateHeader(AWSProperty):
    """
    `EmailMessageTemplateHeader <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-emailmessagetemplateheader.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Value": (str, False),
    }


class EmailMessageTemplateContent(AWSProperty):
    """
    `EmailMessageTemplateContent <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-emailmessagetemplatecontent.html>`__
    """

    props: PropsDictType = {
        "Body": (EmailMessageTemplateContentBody, True),
        "Headers": ([EmailMessageTemplateHeader], True),
        "Subject": (str, True),
    }


class SmsMessageTemplateContentBody(AWSProperty):
    """
    `SmsMessageTemplateContentBody <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-smsmessagetemplatecontentbody.html>`__
    """

    props: PropsDictType = {
        "PlainText": (MessageTemplateBodyContentProvider, False),
    }


class SmsMessageTemplateContent(AWSProperty):
    """
    `SmsMessageTemplateContent <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-smsmessagetemplatecontent.html>`__
    """

    props: PropsDictType = {
        "Body": (SmsMessageTemplateContentBody, True),
    }


class Content(AWSProperty):
    """
    `Content <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-content.html>`__
    """

    props: PropsDictType = {
        "EmailMessageTemplateContent": (EmailMessageTemplateContent, False),
        "SmsMessageTemplateContent": (SmsMessageTemplateContent, False),
    }


class GroupingConfiguration(AWSProperty):
    """
    `GroupingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-groupingconfiguration.html>`__
    """

    props: PropsDictType = {
        "Criteria": (str, True),
        "Values": ([str], True),
    }


class AgentAttributes(AWSProperty):
    """
    `AgentAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-agentattributes.html>`__
    """

    props: PropsDictType = {
        "FirstName": (str, False),
        "LastName": (str, False),
    }


class CustomerProfileAttributes(AWSProperty):
    """
    `CustomerProfileAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html>`__
    """

    props: PropsDictType = {
        "AccountNumber": (str, False),
        "AdditionalInformation": (str, False),
        "Address1": (str, False),
        "Address2": (str, False),
        "Address3": (str, False),
        "Address4": (str, False),
        "BillingAddress1": (str, False),
        "BillingAddress2": (str, False),
        "BillingAddress3": (str, False),
        "BillingAddress4": (str, False),
        "BillingCity": (str, False),
        "BillingCountry": (str, False),
        "BillingCounty": (str, False),
        "BillingPostalCode": (str, False),
        "BillingProvince": (str, False),
        "BillingState": (str, False),
        "BirthDate": (str, False),
        "BusinessEmailAddress": (str, False),
        "BusinessName": (str, False),
        "BusinessPhoneNumber": (str, False),
        "City": (str, False),
        "Country": (str, False),
        "County": (str, False),
        "Custom": (dict, False),
        "EmailAddress": (str, False),
        "FirstName": (str, False),
        "Gender": (str, False),
        "HomePhoneNumber": (str, False),
        "LastName": (str, False),
        "MailingAddress1": (str, False),
        "MailingAddress2": (str, False),
        "MailingAddress3": (str, False),
        "MailingAddress4": (str, False),
        "MailingCity": (str, False),
        "MailingCountry": (str, False),
        "MailingCounty": (str, False),
        "MailingPostalCode": (str, False),
        "MailingProvince": (str, False),
        "MailingState": (str, False),
        "MiddleName": (str, False),
        "MobilePhoneNumber": (str, False),
        "PartyType": (str, False),
        "PhoneNumber": (str, False),
        "PostalCode": (str, False),
        "ProfileARN": (str, False),
        "ProfileId": (str, False),
        "Province": (str, False),
        "ShippingAddress1": (str, False),
        "ShippingAddress2": (str, False),
        "ShippingAddress3": (str, False),
        "ShippingAddress4": (str, False),
        "ShippingCity": (str, False),
        "ShippingCountry": (str, False),
        "ShippingCounty": (str, False),
        "ShippingPostalCode": (str, False),
        "ShippingProvince": (str, False),
        "ShippingState": (str, False),
        "State": (str, False),
    }


class SystemEndpointAttributes(AWSProperty):
    """
    `SystemEndpointAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-systemendpointattributes.html>`__
    """

    props: PropsDictType = {
        "Address": (str, False),
    }


class SystemAttributes(AWSProperty):
    """
    `SystemAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-systemattributes.html>`__
    """

    props: PropsDictType = {
        "CustomerEndpoint": (SystemEndpointAttributes, False),
        "Name": (str, False),
        "SystemEndpoint": (SystemEndpointAttributes, False),
    }


class MessageTemplateAttributes(AWSProperty):
    """
    `MessageTemplateAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-messagetemplateattributes.html>`__
    """

    props: PropsDictType = {
        "AgentAttributes": (AgentAttributes, False),
        "CustomAttributes": (dict, False),
        "CustomerProfileAttributes": (CustomerProfileAttributes, False),
        "SystemAttributes": (SystemAttributes, False),
    }


class MessageTemplate(AWSObject):
    """
    `MessageTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplate.html>`__
    """

    resource_type = "AWS::Wisdom::MessageTemplate"

    props: PropsDictType = {
        "ChannelSubtype": (str, True),
        "Content": (Content, True),
        "DefaultAttributes": (MessageTemplateAttributes, False),
        "Description": (str, False),
        "GroupingConfiguration": (GroupingConfiguration, False),
        "KnowledgeBaseArn": (str, True),
        "Language": (str, False),
        "Name": (str, True),
        "Tags": (Tags, False),
    }


class MessageTemplateVersion(AWSObject):
    """
    `MessageTemplateVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplateversion.html>`__
    """

    resource_type = "AWS::Wisdom::MessageTemplateVersion"

    props: PropsDictType = {
        "MessageTemplateArn": (str, True),
        "MessageTemplateContentSha256": (str, False),
    }
