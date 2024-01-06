# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, integer
from .validators.cognito import validate_recoveryoption_name


class CognitoIdentityProvider(AWSProperty):
    """
    `CognitoIdentityProvider <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitoidentityprovider.html>`__
    """

    props: PropsDictType = {
        "ClientId": (str, False),
        "ProviderName": (str, False),
        "ServerSideTokenCheck": (boolean, False),
    }


class CognitoStreams(AWSProperty):
    """
    `CognitoStreams <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitostreams.html>`__
    """

    props: PropsDictType = {
        "RoleArn": (str, False),
        "StreamName": (str, False),
        "StreamingStatus": (str, False),
    }


class PushSync(AWSProperty):
    """
    `PushSync <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-pushsync.html>`__
    """

    props: PropsDictType = {
        "ApplicationArns": ([str], False),
        "RoleArn": (str, False),
    }


class IdentityPool(AWSObject):
    """
    `IdentityPool <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html>`__
    """

    resource_type = "AWS::Cognito::IdentityPool"

    props: PropsDictType = {
        "AllowClassicFlow": (boolean, False),
        "AllowUnauthenticatedIdentities": (boolean, True),
        "CognitoEvents": (dict, False),
        "CognitoIdentityProviders": ([CognitoIdentityProvider], False),
        "CognitoStreams": (CognitoStreams, False),
        "DeveloperProviderName": (str, False),
        "IdentityPoolName": (str, False),
        "OpenIdConnectProviderARNs": ([str], False),
        "PushSync": (PushSync, False),
        "SamlProviderARNs": ([str], False),
        "SupportedLoginProviders": (dict, False),
    }


class IdentityPoolPrincipalTag(AWSObject):
    """
    `IdentityPoolPrincipalTag <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolprincipaltag.html>`__
    """

    resource_type = "AWS::Cognito::IdentityPoolPrincipalTag"

    props: PropsDictType = {
        "IdentityPoolId": (str, True),
        "IdentityProviderName": (str, True),
        "PrincipalTags": (dict, False),
        "UseDefaults": (boolean, False),
    }


class IdentityPoolRoleAttachment(AWSObject):
    """
    `IdentityPoolRoleAttachment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolroleattachment.html>`__
    """

    resource_type = "AWS::Cognito::IdentityPoolRoleAttachment"

    props: PropsDictType = {
        "IdentityPoolId": (str, True),
        "RoleMappings": (dict, False),
        "Roles": (dict, False),
    }


class CloudWatchLogsConfiguration(AWSProperty):
    """
    `CloudWatchLogsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-logdeliveryconfiguration-cloudwatchlogsconfiguration.html>`__
    """

    props: PropsDictType = {
        "LogGroupArn": (str, False),
    }


class LogConfiguration(AWSProperty):
    """
    `LogConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-logdeliveryconfiguration-logconfiguration.html>`__
    """

    props: PropsDictType = {
        "CloudWatchLogsConfiguration": (CloudWatchLogsConfiguration, False),
        "EventSource": (str, False),
        "LogLevel": (str, False),
    }


class LogDeliveryConfiguration(AWSObject):
    """
    `LogDeliveryConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-logdeliveryconfiguration.html>`__
    """

    resource_type = "AWS::Cognito::LogDeliveryConfiguration"

    props: PropsDictType = {
        "LogConfigurations": ([LogConfiguration], False),
        "UserPoolId": (str, True),
    }


class RecoveryOption(AWSProperty):
    """
    `RecoveryOption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-recoveryoption.html>`__
    """

    props: PropsDictType = {
        "Name": (validate_recoveryoption_name, False),
        "Priority": (integer, False),
    }


class AccountRecoverySetting(AWSProperty):
    """
    `AccountRecoverySetting <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-accountrecoverysetting.html>`__
    """

    props: PropsDictType = {
        "RecoveryMechanisms": ([RecoveryOption], False),
    }


class InviteMessageTemplate(AWSProperty):
    """
    `InviteMessageTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-invitemessagetemplate.html>`__
    """

    props: PropsDictType = {
        "EmailMessage": (str, False),
        "EmailSubject": (str, False),
        "SMSMessage": (str, False),
    }


class AdminCreateUserConfig(AWSProperty):
    """
    `AdminCreateUserConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-admincreateuserconfig.html>`__
    """

    props: PropsDictType = {
        "AllowAdminCreateUserOnly": (boolean, False),
        "InviteMessageTemplate": (InviteMessageTemplate, False),
        "UnusedAccountValidityDays": (integer, False),
    }


class DeviceConfiguration(AWSProperty):
    """
    `DeviceConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-deviceconfiguration.html>`__
    """

    props: PropsDictType = {
        "ChallengeRequiredOnNewDevice": (boolean, False),
        "DeviceOnlyRememberedOnUserPrompt": (boolean, False),
    }


class EmailConfiguration(AWSProperty):
    """
    `EmailConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-emailconfiguration.html>`__
    """

    props: PropsDictType = {
        "ConfigurationSet": (str, False),
        "EmailSendingAccount": (str, False),
        "From": (str, False),
        "ReplyToEmailAddress": (str, False),
        "SourceArn": (str, False),
    }


class CustomEmailSender(AWSProperty):
    """
    `CustomEmailSender <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-customemailsender.html>`__
    """

    props: PropsDictType = {
        "LambdaArn": (str, False),
        "LambdaVersion": (str, False),
    }


class CustomSMSSender(AWSProperty):
    """
    `CustomSMSSender <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-customsmssender.html>`__
    """

    props: PropsDictType = {
        "LambdaArn": (str, False),
        "LambdaVersion": (str, False),
    }


class PreTokenGenerationConfig(AWSProperty):
    """
    `PreTokenGenerationConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-pretokengenerationconfig.html>`__
    """

    props: PropsDictType = {
        "LambdaArn": (str, False),
        "LambdaVersion": (str, False),
    }


class LambdaConfig(AWSProperty):
    """
    `LambdaConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html>`__
    """

    props: PropsDictType = {
        "CreateAuthChallenge": (str, False),
        "CustomEmailSender": (CustomEmailSender, False),
        "CustomMessage": (str, False),
        "CustomSMSSender": (CustomSMSSender, False),
        "DefineAuthChallenge": (str, False),
        "KMSKeyID": (str, False),
        "PostAuthentication": (str, False),
        "PostConfirmation": (str, False),
        "PreAuthentication": (str, False),
        "PreSignUp": (str, False),
        "PreTokenGeneration": (str, False),
        "PreTokenGenerationConfig": (PreTokenGenerationConfig, False),
        "UserMigration": (str, False),
        "VerifyAuthChallengeResponse": (str, False),
    }


class PasswordPolicy(AWSProperty):
    """
    `PasswordPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-passwordpolicy.html>`__
    """

    props: PropsDictType = {
        "MinimumLength": (integer, False),
        "RequireLowercase": (boolean, False),
        "RequireNumbers": (boolean, False),
        "RequireSymbols": (boolean, False),
        "RequireUppercase": (boolean, False),
        "TemporaryPasswordValidityDays": (integer, False),
    }


class Policies(AWSProperty):
    """
    `Policies <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-policies.html>`__
    """

    props: PropsDictType = {
        "PasswordPolicy": (PasswordPolicy, False),
    }


class NumberAttributeConstraints(AWSProperty):
    """
    `NumberAttributeConstraints <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-numberattributeconstraints.html>`__
    """

    props: PropsDictType = {
        "MaxValue": (str, False),
        "MinValue": (str, False),
    }


class StringAttributeConstraints(AWSProperty):
    """
    `StringAttributeConstraints <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-stringattributeconstraints.html>`__
    """

    props: PropsDictType = {
        "MaxLength": (str, False),
        "MinLength": (str, False),
    }


class SchemaAttribute(AWSProperty):
    """
    `SchemaAttribute <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html>`__
    """

    props: PropsDictType = {
        "AttributeDataType": (str, False),
        "DeveloperOnlyAttribute": (boolean, False),
        "Mutable": (boolean, False),
        "Name": (str, False),
        "NumberAttributeConstraints": (NumberAttributeConstraints, False),
        "Required": (boolean, False),
        "StringAttributeConstraints": (StringAttributeConstraints, False),
    }


class SmsConfiguration(AWSProperty):
    """
    `SmsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-smsconfiguration.html>`__
    """

    props: PropsDictType = {
        "ExternalId": (str, False),
        "SnsCallerArn": (str, False),
        "SnsRegion": (str, False),
    }


class UserAttributeUpdateSettings(AWSProperty):
    """
    `UserAttributeUpdateSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-userattributeupdatesettings.html>`__
    """

    props: PropsDictType = {
        "AttributesRequireVerificationBeforeUpdate": ([str], True),
    }


class UserPoolAddOns(AWSProperty):
    """
    `UserPoolAddOns <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-userpooladdons.html>`__
    """

    props: PropsDictType = {
        "AdvancedSecurityMode": (str, False),
    }


class UsernameConfiguration(AWSProperty):
    """
    `UsernameConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-usernameconfiguration.html>`__
    """

    props: PropsDictType = {
        "CaseSensitive": (boolean, False),
    }


class VerificationMessageTemplate(AWSProperty):
    """
    `VerificationMessageTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-verificationmessagetemplate.html>`__
    """

    props: PropsDictType = {
        "DefaultEmailOption": (str, False),
        "EmailMessage": (str, False),
        "EmailMessageByLink": (str, False),
        "EmailSubject": (str, False),
        "EmailSubjectByLink": (str, False),
        "SmsMessage": (str, False),
    }


class UserPool(AWSObject):
    """
    `UserPool <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html>`__
    """

    resource_type = "AWS::Cognito::UserPool"

    props: PropsDictType = {
        "AccountRecoverySetting": (AccountRecoverySetting, False),
        "AdminCreateUserConfig": (AdminCreateUserConfig, False),
        "AliasAttributes": ([str], False),
        "AutoVerifiedAttributes": ([str], False),
        "DeletionProtection": (str, False),
        "DeviceConfiguration": (DeviceConfiguration, False),
        "EmailConfiguration": (EmailConfiguration, False),
        "EmailVerificationMessage": (str, False),
        "EmailVerificationSubject": (str, False),
        "EnabledMfas": ([str], False),
        "LambdaConfig": (LambdaConfig, False),
        "MfaConfiguration": (str, False),
        "Policies": (Policies, False),
        "Schema": ([SchemaAttribute], False),
        "SmsAuthenticationMessage": (str, False),
        "SmsConfiguration": (SmsConfiguration, False),
        "SmsVerificationMessage": (str, False),
        "UserAttributeUpdateSettings": (UserAttributeUpdateSettings, False),
        "UserPoolAddOns": (UserPoolAddOns, False),
        "UserPoolName": (str, False),
        "UserPoolTags": (dict, False),
        "UsernameAttributes": ([str], False),
        "UsernameConfiguration": (UsernameConfiguration, False),
        "VerificationMessageTemplate": (VerificationMessageTemplate, False),
    }


class AnalyticsConfiguration(AWSProperty):
    """
    `AnalyticsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-analyticsconfiguration.html>`__
    """

    props: PropsDictType = {
        "ApplicationArn": (str, False),
        "ApplicationId": (str, False),
        "ExternalId": (str, False),
        "RoleArn": (str, False),
        "UserDataShared": (boolean, False),
    }


class TokenValidityUnits(AWSProperty):
    """
    `TokenValidityUnits <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-tokenvalidityunits.html>`__
    """

    props: PropsDictType = {
        "AccessToken": (str, False),
        "IdToken": (str, False),
        "RefreshToken": (str, False),
    }


class UserPoolClient(AWSObject):
    """
    `UserPoolClient <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html>`__
    """

    resource_type = "AWS::Cognito::UserPoolClient"

    props: PropsDictType = {
        "AccessTokenValidity": (integer, False),
        "AllowedOAuthFlows": ([str], False),
        "AllowedOAuthFlowsUserPoolClient": (boolean, False),
        "AllowedOAuthScopes": ([str], False),
        "AnalyticsConfiguration": (AnalyticsConfiguration, False),
        "AuthSessionValidity": (integer, False),
        "CallbackURLs": ([str], False),
        "ClientName": (str, False),
        "DefaultRedirectURI": (str, False),
        "EnablePropagateAdditionalUserContextData": (boolean, False),
        "EnableTokenRevocation": (boolean, False),
        "ExplicitAuthFlows": ([str], False),
        "GenerateSecret": (boolean, False),
        "IdTokenValidity": (integer, False),
        "LogoutURLs": ([str], False),
        "PreventUserExistenceErrors": (str, False),
        "ReadAttributes": ([str], False),
        "RefreshTokenValidity": (integer, False),
        "SupportedIdentityProviders": ([str], False),
        "TokenValidityUnits": (TokenValidityUnits, False),
        "UserPoolId": (str, True),
        "WriteAttributes": ([str], False),
    }


class CustomDomainConfigType(AWSProperty):
    """
    `CustomDomainConfigType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpooldomain-customdomainconfigtype.html>`__
    """

    props: PropsDictType = {
        "CertificateArn": (str, False),
    }


class UserPoolDomain(AWSObject):
    """
    `UserPoolDomain <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooldomain.html>`__
    """

    resource_type = "AWS::Cognito::UserPoolDomain"

    props: PropsDictType = {
        "CustomDomainConfig": (CustomDomainConfigType, False),
        "Domain": (str, True),
        "UserPoolId": (str, True),
    }


class UserPoolGroup(AWSObject):
    """
    `UserPoolGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html>`__
    """

    resource_type = "AWS::Cognito::UserPoolGroup"

    props: PropsDictType = {
        "Description": (str, False),
        "GroupName": (str, False),
        "Precedence": (integer, False),
        "RoleArn": (str, False),
        "UserPoolId": (str, True),
    }


class UserPoolIdentityProvider(AWSObject):
    """
    `UserPoolIdentityProvider <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolidentityprovider.html>`__
    """

    resource_type = "AWS::Cognito::UserPoolIdentityProvider"

    props: PropsDictType = {
        "AttributeMapping": (dict, False),
        "IdpIdentifiers": ([str], False),
        "ProviderDetails": (dict, False),
        "ProviderName": (str, True),
        "ProviderType": (str, True),
        "UserPoolId": (str, True),
    }


class ResourceServerScopeType(AWSProperty):
    """
    `ResourceServerScopeType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolresourceserver-resourceserverscopetype.html>`__
    """

    props: PropsDictType = {
        "ScopeDescription": (str, True),
        "ScopeName": (str, True),
    }


class UserPoolResourceServer(AWSObject):
    """
    `UserPoolResourceServer <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolresourceserver.html>`__
    """

    resource_type = "AWS::Cognito::UserPoolResourceServer"

    props: PropsDictType = {
        "Identifier": (str, True),
        "Name": (str, True),
        "Scopes": ([ResourceServerScopeType], False),
        "UserPoolId": (str, True),
    }


class AccountTakeoverActionType(AWSProperty):
    """
    `AccountTakeoverActionType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype.html>`__
    """

    props: PropsDictType = {
        "EventAction": (str, True),
        "Notify": (boolean, True),
    }


class AccountTakeoverActionsType(AWSProperty):
    """
    `AccountTakeoverActionsType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype.html>`__
    """

    props: PropsDictType = {
        "HighAction": (AccountTakeoverActionType, False),
        "LowAction": (AccountTakeoverActionType, False),
        "MediumAction": (AccountTakeoverActionType, False),
    }


class NotifyEmailType(AWSProperty):
    """
    `NotifyEmailType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-notifyemailtype.html>`__
    """

    props: PropsDictType = {
        "HtmlBody": (str, False),
        "Subject": (str, True),
        "TextBody": (str, False),
    }


class NotifyConfigurationType(AWSProperty):
    """
    `NotifyConfigurationType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype.html>`__
    """

    props: PropsDictType = {
        "BlockEmail": (NotifyEmailType, False),
        "From": (str, False),
        "MfaEmail": (NotifyEmailType, False),
        "NoActionEmail": (NotifyEmailType, False),
        "ReplyTo": (str, False),
        "SourceArn": (str, True),
    }


class AccountTakeoverRiskConfigurationType(AWSProperty):
    """
    `AccountTakeoverRiskConfigurationType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype.html>`__
    """

    props: PropsDictType = {
        "Actions": (AccountTakeoverActionsType, True),
        "NotifyConfiguration": (NotifyConfigurationType, False),
    }


class CompromisedCredentialsActionsType(AWSProperty):
    """
    `CompromisedCredentialsActionsType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsactionstype.html>`__
    """

    props: PropsDictType = {
        "EventAction": (str, True),
    }


class CompromisedCredentialsRiskConfigurationType(AWSProperty):
    """
    `CompromisedCredentialsRiskConfigurationType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype.html>`__
    """

    props: PropsDictType = {
        "Actions": (CompromisedCredentialsActionsType, True),
        "EventFilter": ([str], False),
    }


class RiskExceptionConfigurationType(AWSProperty):
    """
    `RiskExceptionConfigurationType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype.html>`__
    """

    props: PropsDictType = {
        "BlockedIPRangeList": ([str], False),
        "SkippedIPRangeList": ([str], False),
    }


class UserPoolRiskConfigurationAttachment(AWSObject):
    """
    `UserPoolRiskConfigurationAttachment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolriskconfigurationattachment.html>`__
    """

    resource_type = "AWS::Cognito::UserPoolRiskConfigurationAttachment"

    props: PropsDictType = {
        "AccountTakeoverRiskConfiguration": (
            AccountTakeoverRiskConfigurationType,
            False,
        ),
        "ClientId": (str, True),
        "CompromisedCredentialsRiskConfiguration": (
            CompromisedCredentialsRiskConfigurationType,
            False,
        ),
        "RiskExceptionConfiguration": (RiskExceptionConfigurationType, False),
        "UserPoolId": (str, True),
    }


class UserPoolUICustomizationAttachment(AWSObject):
    """
    `UserPoolUICustomizationAttachment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluicustomizationattachment.html>`__
    """

    resource_type = "AWS::Cognito::UserPoolUICustomizationAttachment"

    props: PropsDictType = {
        "CSS": (str, False),
        "ClientId": (str, True),
        "UserPoolId": (str, True),
    }


class AttributeType(AWSProperty):
    """
    `AttributeType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpooluser-attributetype.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Value": (str, False),
    }


class UserPoolUser(AWSObject):
    """
    `UserPoolUser <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html>`__
    """

    resource_type = "AWS::Cognito::UserPoolUser"

    props: PropsDictType = {
        "ClientMetadata": (dict, False),
        "DesiredDeliveryMediums": ([str], False),
        "ForceAliasCreation": (boolean, False),
        "MessageAction": (str, False),
        "UserAttributes": ([AttributeType], False),
        "UserPoolId": (str, True),
        "Username": (str, False),
        "ValidationData": ([AttributeType], False),
    }


class UserPoolUserToGroupAttachment(AWSObject):
    """
    `UserPoolUserToGroupAttachment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolusertogroupattachment.html>`__
    """

    resource_type = "AWS::Cognito::UserPoolUserToGroupAttachment"

    props: PropsDictType = {
        "GroupName": (str, True),
        "UserPoolId": (str, True),
        "Username": (str, True),
    }


class MappingRule(AWSProperty):
    """
    `MappingRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-mappingrule.html>`__
    """

    props: PropsDictType = {
        "Claim": (str, True),
        "MatchType": (str, True),
        "RoleARN": (str, True),
        "Value": (str, True),
    }


class RulesConfiguration(AWSProperty):
    """
    `RulesConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rulesconfigurationtype.html>`__
    """

    props: PropsDictType = {
        "Rules": ([MappingRule], True),
    }


class RoleMapping(AWSProperty):
    """
    `RoleMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rolemapping.html>`__
    """

    props: PropsDictType = {
        "AmbiguousRoleResolution": (str, False),
        "IdentityProvider": (str, False),
        "RulesConfiguration": (RulesConfiguration, False),
        "Type": (str, True),
    }
