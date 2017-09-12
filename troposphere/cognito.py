# Copyright (c) 2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, positive_integer


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
        'VerifyAuthChallengeResponse': (basestring, False),
    }


class PasswordPolicy(AWSProperty):
    props = {
        'MinimumLength': (positive_integer, False),
        'RequireLowercase': (boolean, False),
        'RequireNumbers': (boolean, False),
        'RequireSymbols': (boolean, False),
        'RequireUppercase': (boolean, False),
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


class UserPool(AWSObject):
    resource_type = "AWS::Cognito::UserPool"

    props = {
        'AdminCreateUserConfig': (AdminCreateUserConfig, False),
        'AliasAttributes': ([basestring], False),
        'AutoVerifiedAttributes': ([basestring], False),
        'DeviceConfiguration': (DeviceConfiguration, False),
        'EmailConfiguration': (EmailConfiguration, False),
        'EmailVerificationMessage': (basestring, False),
        'EmailVerificationSubject': (basestring, False),
        'LambdaConfig': (LambdaConfig, False),
        'MfaConfiguration': (basestring, False),
        'Policies': (Policies, False),
        'UserPoolName': (basestring, True),
        'Schema': ([SchemaAttribute], False),
        'SmsAuthenticationMessage': (basestring, False),
        'SmsConfiguration': (SmsConfiguration, False),
        'SmsVerificationMessage': (basestring, False),
        'UserPoolTags': (dict, False),
    }


class UserPoolClient(AWSObject):
    resource_type = "AWS::Cognito::UserPoolClient"

    props = {
        'ClientName': (basestring, False),
        'ExplicitAuthFlows': ([basestring], False),
        'GenerateSecret': (boolean, False),
        'ReadAttributes': ([basestring], False),
        'RefreshTokenValidity': (positive_integer, False),
        'UserPoolId': (basestring, True),
        'WriteAttributes': ([basestring], False),
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


class AttributeType(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Value': (basestring, False),
    }


class UserPoolUser(AWSObject):
    resource_type = "AWS::Cognito::UserPoolUser"

    props = {
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
