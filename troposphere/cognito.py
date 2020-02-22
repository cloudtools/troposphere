# Copyright (c) 2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, positive_integer


VALID_RECOVERYOPTION_NAME = (
    'admin_only', 'verified_email', 'verified_phone_number')


def validate_recoveryoption_name(recoveryoption_name):
    """Validate Name for RecoveryOption"""

    if recoveryoption_name not in VALID_RECOVERYOPTION_NAME:
        raise ValueError("RecoveryOption Name must be one of: %s" %
                         ", ".join(VALID_RECOVERYOPTION_NAME))
    return recoveryoption_name


class CognitoIdentityProvider(AWSProperty):
    props = {
        'ClientId': (basestring, False),
        'ProviderName': (basestring, False),
        'ServerSideTokenCheck': (bool, False),
    }


class CognitoStreams(AWSProperty):
    props = {
        'RoleArn': (basestring, False),
        'StreamingStatus': (basestring, False),
        'StreamName': (basestring, False),
    }


class PushSync(AWSProperty):
    props = {
        'ApplicationArns': ([basestring], False),
        'RoleArn': (basestring, False),
    }


class IdentityPool(AWSObject):
    resource_type = "AWS::Cognito::IdentityPool"

    props = {
        'AllowUnauthenticatedIdentities': (bool, True),
        'CognitoEvents': (dict, False),
        'CognitoIdentityProviders': ([CognitoIdentityProvider], False),
        'CognitoStreams': (CognitoStreams, False),
        'DeveloperProviderName': (basestring, False),
        'IdentityPoolName': (basestring, False),
        'OpenIdConnectProviderARNs': ([basestring], False),
        'PushSync': (PushSync, False),
        'SamlProviderARNs': ([basestring], False),
        'SupportedLoginProviders': (dict, False),
    }


class MappingRule(AWSProperty):
    props = {
        'Claim': (basestring, True),
        'MatchType': (basestring, True),
        'RoleARN': (basestring, True),
        'Value': (basestring, True),
    }


class RulesConfiguration(AWSProperty):
    props = {
        'Rules': ([MappingRule], True),
    }


class RoleMapping(AWSProperty):
    props = {
        'AmbiguousRoleResolution': (basestring, False),
        'RulesConfiguration': (RulesConfiguration, False),
        'Type': (basestring, True),
    }


class IdentityPoolRoleAttachment(AWSObject):
    resource_type = "AWS::Cognito::IdentityPoolRoleAttachment"

    props = {
        'IdentityPoolId': (basestring, True),
        'RoleMappings': (dict, False),
        'Roles': (dict, False),
    }


class InviteMessageTemplate(AWSProperty):
    props = {
        'EmailMessage': (basestring, False),
        'EmailSubject': (basestring, False),
        'SMSMessage': (basestring, False),
    }


class AdminCreateUserConfig(AWSProperty):
    props = {
        'AllowAdminCreateUserOnly': (boolean, False),
        'InviteMessageTemplate': (InviteMessageTemplate, False),
        'UnusedAccountValidityDays': (positive_integer, False),
    }


class DeviceConfiguration(AWSProperty):
    props = {
        'ChallengeRequiredOnNewDevice': (boolean, False),
        'DeviceOnlyRememberedOnUserPrompt': (boolean, False),
    }


class EmailConfiguration(AWSProperty):
    props = {
        'ConfigurationSet': (basestring, False),
        'EmailSendingAccount': (basestring, False),
        'From': (basestring, False),
        'ReplyToEmailAddress': (basestring, False),
        'SourceArn': (basestring, False),
    }


class LambdaConfig(AWSProperty):
    props = {
        'CreateAuthChallenge': (basestring, False),
        'CustomMessage': (basestring, False),
        'DefineAuthChallenge': (basestring, False),
        'PostAuthentication': (basestring, False),
        'PostConfirmation': (basestring, False),
        'PreAuthentication': (basestring, False),
        'PreSignUp': (basestring, False),
        'PreTokenGeneration': (basestring, False),
        'UserMigration': (basestring, False),
        'VerifyAuthChallengeResponse': (basestring, False),
    }


class PasswordPolicy(AWSProperty):
    props = {
        'MinimumLength': (positive_integer, False),
        'RequireLowercase': (boolean, False),
        'RequireNumbers': (boolean, False),
        'RequireSymbols': (boolean, False),
        'RequireUppercase': (boolean, False),
        'TemporaryPasswordValidityDays': (positive_integer, False),
    }


class Policies(AWSProperty):
    props = {
        'PasswordPolicy': (PasswordPolicy, False),
    }


class NumberAttributeConstraints(AWSProperty):
    props = {
        'MaxValue': (basestring, False),
        'MinValue': (basestring, False),
    }


class StringAttributeConstraints(AWSProperty):
    props = {
        'MaxLength': (basestring, False),
        'MinLength': (basestring, False),
    }


class SchemaAttribute(AWSProperty):
    props = {
        'AttributeDataType': (basestring, False),
        'DeveloperOnlyAttribute': (boolean, False),
        'Mutable': (boolean, False),
        'Name': (basestring, False),
        'NumberAttributeConstraints': (NumberAttributeConstraints, False),
        'StringAttributeConstraints': (StringAttributeConstraints, False),
        'Required': (boolean, False),
    }


class SmsConfiguration(AWSProperty):
    props = {
        'ExternalId': (basestring, False),
        'SnsCallerArn': (basestring, True),
    }


class UserPoolAddOns(AWSProperty):
    props = {
        'AdvancedSecurityMode': (basestring, False),
    }


class VerificationMessageTemplate(AWSProperty):
    props = {
        'DefaultEmailOption': (basestring, False),
        'EmailMessage': (basestring, False),
        'EmailMessageByLink': (basestring, False),
        'EmailSubject': (basestring, False),
        'EmailSubjectByLink': (basestring, False),
        'SmsMessage': (basestring, False),
    }


class RecoveryOption(AWSProperty):
    props = {
        'Name': (validate_recoveryoption_name, False),
        'Priority': (positive_integer, False)
    }


class AccountRecoverySetting(AWSProperty):
    props = {
        'RecoveryMechanisms': ([RecoveryOption], False)
    }


class UsernameConfiguration(AWSProperty):
    props = {
        'CaseSensitive': (boolean, False),
    }


class UserPool(AWSObject):
    resource_type = "AWS::Cognito::UserPool"

    props = {
        'AccountRecoverySetting': (AccountRecoverySetting, False),
        'AdminCreateUserConfig': (AdminCreateUserConfig, False),
        'AliasAttributes': ([basestring], False),
        'AutoVerifiedAttributes': ([basestring], False),
        'DeviceConfiguration': (DeviceConfiguration, False),
        'EmailConfiguration': (EmailConfiguration, False),
        'EmailVerificationMessage': (basestring, False),
        'EmailVerificationSubject': (basestring, False),
        'EnabledMfas': ([basestring], False),
        'LambdaConfig': (LambdaConfig, False),
        'MfaConfiguration': (basestring, False),
        'Policies': (Policies, False),
        'Schema': ([SchemaAttribute], False),
        'SmsAuthenticationMessage': (basestring, False),
        'SmsConfiguration': (SmsConfiguration, False),
        'SmsVerificationMessage': (basestring, False),
        'UserPoolAddOns': (UserPoolAddOns, False),
        'UserPoolName': (basestring, False),
        'UserPoolTags': (dict, False),
        'UsernameAttributes': ([basestring], False),
        'UsernameConfiguration': (UsernameConfiguration, False),
        'VerificationMessageTemplate': (VerificationMessageTemplate, False),
    }


class AnalyticsConfiguration(AWSProperty):
    props = {
        'ApplicationId': (basestring, False),
        'ExternalId': (basestring, False),
        'RoleArn': (basestring, False),
        'UserDataShared': (boolean, False),
    }


class UserPoolClient(AWSObject):
    resource_type = "AWS::Cognito::UserPoolClient"

    props = {
        'AllowedOAuthFlows': ([basestring], False),
        'AllowedOAuthFlowsUserPoolClient': (boolean, False),
        'AllowedOAuthScopes': ([basestring], False),
        'AnalyticsConfiguration': (AnalyticsConfiguration, False),
        'CallbackURLs': ([basestring], False),
        'ClientName': (basestring, False),
        'DefaultRedirectURI': (basestring, False),
        'ExplicitAuthFlows': ([basestring], False),
        'GenerateSecret': (boolean, False),
        'LogoutURLs': ([basestring], False),
        'PreventUserExistenceErrors': (basestring, False),
        'ReadAttributes': ([basestring], False),
        'RefreshTokenValidity': (positive_integer, False),
        'SupportedIdentityProviders': ([basestring], False),
        'UserPoolId': (basestring, True),
        'WriteAttributes': ([basestring], False),
    }


class CustomDomainConfigType(AWSProperty):
    props = {
        'CertificateArn': (basestring, False),
    }


class UserPoolDomain(AWSObject):
    resource_type = "AWS::Cognito::UserPoolDomain"

    props = {
        'CustomDomainConfig': (CustomDomainConfigType, False),
        'Domain': (basestring, True),
        'UserPoolId': (basestring, True),
    }


class UserPoolGroup(AWSObject):
    resource_type = "AWS::Cognito::UserPoolGroup"

    props = {
        'Description': (basestring, False),
        'GroupName': (basestring, True),
        'Precedence': (positive_integer, False),
        'RoleArn': (basestring, False),
        'UserPoolId': (basestring, True),
    }


class UserPoolIdentityProvider(AWSObject):
    resource_type = "AWS::Cognito::UserPoolIdentityProvider"

    props = {
        'AttributeMapping': (dict, False),
        'IdpIdentifiers': ([basestring], False),
        'ProviderDetails': (dict, False),
        'ProviderName': (basestring, True),
        'ProviderType': (basestring, True),
        'UserPoolId': (basestring, True),
    }


class ResourceServerScopeType(AWSProperty):
    props = {
        "ScopeDescription": (basestring, True),
        "ScopeName": (basestring, True)
    }


class UserPoolResourceServer(AWSObject):
    resource_type = "AWS::Cognito::UserPoolResourceServer"

    props = {
        "Identifier": (basestring, True),
        "Name": (basestring, True),
        "Scopes": ([ResourceServerScopeType], False),
        "UserPoolId": (basestring, True)
    }


class AccountTakeoverActionType(AWSProperty):
    props = {
        'EventAction': (basestring, True),
        'Notify': (boolean, True),
    }


class AccountTakeoverActionsType(AWSProperty):
    props = {
        'HighAction': (AccountTakeoverActionType, False),
        'LowAction': (AccountTakeoverActionType, False),
        'MediumAction': (AccountTakeoverActionType, False),
    }


class NotifyEmailType(AWSProperty):
    props = {
        'HtmlBody': (basestring, False),
        'Subject': (basestring, True),
        'TextBody': (basestring, False),
    }


class NotifyConfigurationType(AWSProperty):
    props = {
        'BlockEmail': (NotifyEmailType, False),
        'From': (basestring, False),
        'MfaEmail': (NotifyEmailType, False),
        'NoActionEmail': (NotifyEmailType, False),
        'ReplyTo': (basestring, False),
        'SourceArn': (basestring, True),
    }


class AccountTakeoverRiskConfigurationType(AWSProperty):
    props = {
        'Actions': (AccountTakeoverActionsType, True),
        'NotifyConfiguration': (NotifyConfigurationType, False),
    }


class CompromisedCredentialsActionsType(AWSProperty):
    props = {
        'EventAction': (basestring, True),
    }


class CompromisedCredentialsRiskConfigurationType(AWSProperty):
    props = {
        'Actions': (CompromisedCredentialsActionsType, True),
        'EventFilter': ([basestring], False),
    }


class RiskExceptionConfigurationType(AWSProperty):
    props = {
        'BlockedIPRangeList': ([basestring], False),
        'SkippedIPRangeList': ([basestring], False),
    }


class UserPoolRiskConfigurationAttachment(AWSObject):
    resource_type = "AWS::Cognito::UserPoolRiskConfigurationAttachment"

    props = {
        'AccountTakeoverRiskConfiguration':
            (AccountTakeoverRiskConfigurationType, False),
        'ClientId': (basestring, True),
        'CompromisedCredentialsRiskConfiguration':
            (CompromisedCredentialsRiskConfigurationType, False),
        'RiskExceptionConfiguration':
            (RiskExceptionConfigurationType, False),
        'UserPoolId': (basestring, True),
    }


class UserPoolUICustomizationAttachment(AWSObject):
    resource_type = "AWS::Cognito::UserPoolUICustomizationAttachment"

    props = {
        'CSS': (basestring, False),
        'ClientId': (basestring, True),
        'UserPoolId': (basestring, True),
    }


class AttributeType(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Value': (basestring, False),
    }


class UserPoolUser(AWSObject):
    resource_type = "AWS::Cognito::UserPoolUser"

    props = {
        'ClientMetadata': (dict, False),
        'DesiredDeliveryMediums': ([basestring], False),
        'ForceAliasCreation': (boolean, False),
        'UserAttributes': ([AttributeType], False),
        'MessageAction': (basestring, False),
        'Username': (basestring, False),
        'UserPoolId': (basestring, True),
        'ValidationData': ([AttributeType], False),
    }


class UserPoolUserToGroupAttachment(AWSObject):
    resource_type = "AWS::Cognito::UserPoolUserToGroupAttachment"

    props = {
        'GroupName': (basestring, True),
        'Username': (basestring, True),
        'UserPoolId': (basestring, True),
    }
