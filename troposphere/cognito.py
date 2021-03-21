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
        'ClientId': (str, False),
        'ProviderName': (str, False),
        'ServerSideTokenCheck': (bool, False),
    }


class CognitoStreams(AWSProperty):
    props = {
        'RoleArn': (str, False),
        'StreamingStatus': (str, False),
        'StreamName': (str, False),
    }


class PushSync(AWSProperty):
    props = {
        'ApplicationArns': ([str], False),
        'RoleArn': (str, False),
    }


class IdentityPool(AWSObject):
    resource_type = "AWS::Cognito::IdentityPool"

    props = {
        'AllowUnauthenticatedIdentities': (bool, True),
        'CognitoEvents': (dict, False),
        'CognitoIdentityProviders': ([CognitoIdentityProvider], False),
        'CognitoStreams': (CognitoStreams, False),
        'DeveloperProviderName': (str, False),
        'IdentityPoolName': (str, False),
        'OpenIdConnectProviderARNs': ([str], False),
        'PushSync': (PushSync, False),
        'SamlProviderARNs': ([str], False),
        'SupportedLoginProviders': (dict, False),
    }


class MappingRule(AWSProperty):
    props = {
        'Claim': (str, True),
        'MatchType': (str, True),
        'RoleARN': (str, True),
        'Value': (str, True),
    }


class RulesConfiguration(AWSProperty):
    props = {
        'Rules': ([MappingRule], True),
    }


class RoleMapping(AWSProperty):
    props = {
        'AmbiguousRoleResolution': (str, False),
        'RulesConfiguration': (RulesConfiguration, False),
        'Type': (str, True),
    }


class IdentityPoolRoleAttachment(AWSObject):
    resource_type = "AWS::Cognito::IdentityPoolRoleAttachment"

    props = {
        'IdentityPoolId': (str, True),
        'RoleMappings': (dict, False),
        'Roles': (dict, False),
    }


class InviteMessageTemplate(AWSProperty):
    props = {
        'EmailMessage': (str, False),
        'EmailSubject': (str, False),
        'SMSMessage': (str, False),
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
        'ConfigurationSet': (str, False),
        'EmailSendingAccount': (str, False),
        'From': (str, False),
        'ReplyToEmailAddress': (str, False),
        'SourceArn': (str, False),
    }


class LambdaConfig(AWSProperty):
    props = {
        'CreateAuthChallenge': (str, False),
        'CustomMessage': (str, False),
        'DefineAuthChallenge': (str, False),
        'PostAuthentication': (str, False),
        'PostConfirmation': (str, False),
        'PreAuthentication': (str, False),
        'PreSignUp': (str, False),
        'PreTokenGeneration': (str, False),
        'UserMigration': (str, False),
        'VerifyAuthChallengeResponse': (str, False),
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
        'MaxValue': (str, False),
        'MinValue': (str, False),
    }


class StringAttributeConstraints(AWSProperty):
    props = {
        'MaxLength': (str, False),
        'MinLength': (str, False),
    }


class SchemaAttribute(AWSProperty):
    props = {
        'AttributeDataType': (str, False),
        'DeveloperOnlyAttribute': (boolean, False),
        'Mutable': (boolean, False),
        'Name': (str, False),
        'NumberAttributeConstraints': (NumberAttributeConstraints, False),
        'StringAttributeConstraints': (StringAttributeConstraints, False),
        'Required': (boolean, False),
    }


class SmsConfiguration(AWSProperty):
    props = {
        'ExternalId': (str, False),
        'SnsCallerArn': (str, True),
    }


class UserPoolAddOns(AWSProperty):
    props = {
        'AdvancedSecurityMode': (str, False),
    }


class VerificationMessageTemplate(AWSProperty):
    props = {
        'DefaultEmailOption': (str, False),
        'EmailMessage': (str, False),
        'EmailMessageByLink': (str, False),
        'EmailSubject': (str, False),
        'EmailSubjectByLink': (str, False),
        'SmsMessage': (str, False),
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
        'AliasAttributes': ([str], False),
        'AutoVerifiedAttributes': ([str], False),
        'DeviceConfiguration': (DeviceConfiguration, False),
        'EmailConfiguration': (EmailConfiguration, False),
        'EmailVerificationMessage': (str, False),
        'EmailVerificationSubject': (str, False),
        'EnabledMfas': ([str], False),
        'LambdaConfig': (LambdaConfig, False),
        'MfaConfiguration': (str, False),
        'Policies': (Policies, False),
        'Schema': ([SchemaAttribute], False),
        'SmsAuthenticationMessage': (str, False),
        'SmsConfiguration': (SmsConfiguration, False),
        'SmsVerificationMessage': (str, False),
        'UserPoolAddOns': (UserPoolAddOns, False),
        'UserPoolName': (str, False),
        'UserPoolTags': (dict, False),
        'UsernameAttributes': ([str], False),
        'UsernameConfiguration': (UsernameConfiguration, False),
        'VerificationMessageTemplate': (VerificationMessageTemplate, False),
    }


class AnalyticsConfiguration(AWSProperty):
    props = {
        'ApplicationId': (str, False),
        'ExternalId': (str, False),
        'RoleArn': (str, False),
        'UserDataShared': (boolean, False),
    }


class TokenValidityUnits(AWSProperty):
    props = {
        'AccessToken': (str, False),
        'IdToken': (str, False),
        'RefreshToken': (str, False),
    }


class UserPoolClient(AWSObject):
    resource_type = "AWS::Cognito::UserPoolClient"

    props = {
        'AccessTokenValidity': (positive_integer, False),
        'AllowedOAuthFlows': ([str], False),
        'AllowedOAuthFlowsUserPoolClient': (boolean, False),
        'AllowedOAuthScopes': ([str], False),
        'AnalyticsConfiguration': (AnalyticsConfiguration, False),
        'CallbackURLs': ([str], False),
        'ClientName': (str, False),
        'DefaultRedirectURI': (str, False),
        'ExplicitAuthFlows': ([str], False),
        'GenerateSecret': (boolean, False),
        'IdTokenValidity': (positive_integer, False),
        'LogoutURLs': ([str], False),
        'PreventUserExistenceErrors': (str, False),
        'ReadAttributes': ([str], False),
        'RefreshTokenValidity': (positive_integer, False),
        'SupportedIdentityProviders': ([str], False),
        'TokenValidityUnits': (TokenValidityUnits, False),
        'UserPoolId': (str, True),
        'WriteAttributes': ([str], False),
    }


class CustomDomainConfigType(AWSProperty):
    props = {
        'CertificateArn': (str, False),
    }


class UserPoolDomain(AWSObject):
    resource_type = "AWS::Cognito::UserPoolDomain"

    props = {
        'CustomDomainConfig': (CustomDomainConfigType, False),
        'Domain': (str, True),
        'UserPoolId': (str, True),
    }


class UserPoolGroup(AWSObject):
    resource_type = "AWS::Cognito::UserPoolGroup"

    props = {
        'Description': (str, False),
        'GroupName': (str, True),
        'Precedence': (positive_integer, False),
        'RoleArn': (str, False),
        'UserPoolId': (str, True),
    }


class UserPoolIdentityProvider(AWSObject):
    resource_type = "AWS::Cognito::UserPoolIdentityProvider"

    props = {
        'AttributeMapping': (dict, False),
        'IdpIdentifiers': ([str], False),
        'ProviderDetails': (dict, False),
        'ProviderName': (str, True),
        'ProviderType': (str, True),
        'UserPoolId': (str, True),
    }


class ResourceServerScopeType(AWSProperty):
    props = {
        "ScopeDescription": (str, True),
        "ScopeName": (str, True)
    }


class UserPoolResourceServer(AWSObject):
    resource_type = "AWS::Cognito::UserPoolResourceServer"

    props = {
        "Identifier": (str, True),
        "Name": (str, True),
        "Scopes": ([ResourceServerScopeType], False),
        "UserPoolId": (str, True)
    }


class AccountTakeoverActionType(AWSProperty):
    props = {
        'EventAction': (str, True),
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
        'HtmlBody': (str, False),
        'Subject': (str, True),
        'TextBody': (str, False),
    }


class NotifyConfigurationType(AWSProperty):
    props = {
        'BlockEmail': (NotifyEmailType, False),
        'From': (str, False),
        'MfaEmail': (NotifyEmailType, False),
        'NoActionEmail': (NotifyEmailType, False),
        'ReplyTo': (str, False),
        'SourceArn': (str, True),
    }


class AccountTakeoverRiskConfigurationType(AWSProperty):
    props = {
        'Actions': (AccountTakeoverActionsType, True),
        'NotifyConfiguration': (NotifyConfigurationType, False),
    }


class CompromisedCredentialsActionsType(AWSProperty):
    props = {
        'EventAction': (str, True),
    }


class CompromisedCredentialsRiskConfigurationType(AWSProperty):
    props = {
        'Actions': (CompromisedCredentialsActionsType, True),
        'EventFilter': ([str], False),
    }


class RiskExceptionConfigurationType(AWSProperty):
    props = {
        'BlockedIPRangeList': ([str], False),
        'SkippedIPRangeList': ([str], False),
    }


class UserPoolRiskConfigurationAttachment(AWSObject):
    resource_type = "AWS::Cognito::UserPoolRiskConfigurationAttachment"

    props = {
        'AccountTakeoverRiskConfiguration':
            (AccountTakeoverRiskConfigurationType, False),
        'ClientId': (str, True),
        'CompromisedCredentialsRiskConfiguration':
            (CompromisedCredentialsRiskConfigurationType, False),
        'RiskExceptionConfiguration':
            (RiskExceptionConfigurationType, False),
        'UserPoolId': (str, True),
    }


class UserPoolUICustomizationAttachment(AWSObject):
    resource_type = "AWS::Cognito::UserPoolUICustomizationAttachment"

    props = {
        'CSS': (str, False),
        'ClientId': (str, True),
        'UserPoolId': (str, True),
    }


class AttributeType(AWSProperty):
    props = {
        'Name': (str, True),
        'Value': (str, False),
    }


class UserPoolUser(AWSObject):
    resource_type = "AWS::Cognito::UserPoolUser"

    props = {
        'ClientMetadata': (dict, False),
        'DesiredDeliveryMediums': ([str], False),
        'ForceAliasCreation': (boolean, False),
        'UserAttributes': ([AttributeType], False),
        'MessageAction': (str, False),
        'Username': (str, False),
        'UserPoolId': (str, True),
        'ValidationData': ([AttributeType], False),
    }


class UserPoolUserToGroupAttachment(AWSObject):
    resource_type = "AWS::Cognito::UserPoolUserToGroupAttachment"

    props = {
        'GroupName': (str, True),
        'Username': (str, True),
        'UserPoolId': (str, True),
    }
