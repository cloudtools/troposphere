# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer


class AcceptedPortfolioShare(AWSObject):
    resource_type = "AWS::ServiceCatalog::AcceptedPortfolioShare"

    props = {
        'AcceptLanguage': (str, False),
        'PortfolioId': (str, True),
    }


class ProvisioningArtifactProperties(AWSProperty):
    props = {
        'Description': (str, False),
        'DisableTemplateValidation': (boolean, False),
        'Info': (dict, True),
        'Name': (str, False),
    }


class CloudFormationProduct(AWSObject):
    resource_type = "AWS::ServiceCatalog::CloudFormationProduct"

    props = {
        'AcceptLanguage': (str, False),
        'Description': (str, False),
        'Distributor': (str, False),
        'Name': (str, True),
        'Owner': (str, True),
        'ProvisioningArtifactParameters':
            ([ProvisioningArtifactProperties], True),
        'ReplaceProvisioningArtifacts': (boolean, False),
        'SupportDescription': (str, False),
        'SupportEmail': (str, False),
        'SupportUrl': (str, False),
        'Tags': (Tags, False),
    }


class ProvisioningParameter(AWSProperty):
    props = {
        'Key': (str, True),
        'Value': (str, True),
    }


class ProvisioningPreferences(AWSProperty):
    props = {
        'StackSetAccounts': ([str], False),
        'StackSetFailureToleranceCount': (integer, False),
        'StackSetFailureTolerancePercentage': (integer, False),
        'StackSetMaxConcurrencyCount': (integer, False),
        'StackSetMaxConcurrencyPercentage': (integer, False),
        'StackSetOperationType': (str, False),
        'StackSetRegions': ([str], False),
    }


class CloudFormationProvisionedProduct(AWSObject):
    resource_type = "AWS::ServiceCatalog::CloudFormationProvisionedProduct"

    props = {
        'AcceptLanguage': (str, False),
        'NotificationArns': ([str], False),
        'PathId': (str, False),
        'PathName': (str, False),
        'ProductId': (str, False),
        'ProductName': (str, False),
        'ProvisionedProductName': (str, False),
        'ProvisioningArtifactId': (str, False),
        'ProvisioningArtifactName': (str, False),
        'ProvisioningParameters': ([ProvisioningParameter], False),
        'ProvisioningPreferences': (ProvisioningPreferences, False),
        'Tags': (Tags, False),
    }


class LaunchNotificationConstraint(AWSObject):
    resource_type = "AWS::ServiceCatalog::LaunchNotificationConstraint"

    props = {
        'AcceptLanguage': (str, False),
        'Description': (str, False),
        'NotificationArns': ([str], True),
        'PortfolioId': (str, True),
        'ProductId': (str, True),
    }


class LaunchRoleConstraint(AWSObject):
    resource_type = "AWS::ServiceCatalog::LaunchRoleConstraint"

    props = {
        'AcceptLanguage': (str, False),
        'Description': (str, False),
        'LocalRoleName': (str, False),
        'PortfolioId': (str, True),
        'ProductId': (str, True),
        'RoleArn': (str, False),
    }


class LaunchTemplateConstraint(AWSObject):
    resource_type = "AWS::ServiceCatalog::LaunchTemplateConstraint"

    props = {
        'AcceptLanguage': (str, False),
        'Description': (str, False),
        'PortfolioId': (str, True),
        'ProductId': (str, True),
        'Rules': (str, True),
    }


class Portfolio(AWSObject):
    resource_type = "AWS::ServiceCatalog::Portfolio"

    props = {
        'AcceptLanguage': (str, False),
        'Description': (str, False),
        'DisplayName': (str, True),
        'ProviderName': (str, True),
        'Tags': (Tags, False),
    }


class PortfolioPrincipalAssociation(AWSObject):
    resource_type = "AWS::ServiceCatalog::PortfolioPrincipalAssociation"

    props = {
        'AcceptLanguage': (str, False),
        'PortfolioId': (str, True),
        'PrincipalARN': (str, True),
        'PrincipalType': (str, True),
    }


class PortfolioProductAssociation(AWSObject):
    resource_type = "AWS::ServiceCatalog::PortfolioProductAssociation"

    props = {
        'AcceptLanguage': (str, False),
        'PortfolioId': (str, True),
        'ProductId': (str, True),
        'SourcePortfolioId': (str, False),
    }


class PortfolioShare(AWSObject):
    resource_type = "AWS::ServiceCatalog::PortfolioShare"

    props = {
        'AcceptLanguage': (str, False),
        'AccountId': (str, True),
        'PortfolioId': (str, True),
        'ShareTagOptions': (boolean, False),
    }


def validate_tag_update(update):
    valid_tag_update_values = [
        "ALLOWED",
        "NOT_ALLOWED",
    ]
    if update not in valid_tag_update_values:
        raise ValueError(
            "{} is not a valid tag update value".format(update)
        )
    return update


class ResourceUpdateConstraint(AWSObject):
    resource_type = "AWS::ServiceCatalog::ResourceUpdateConstraint"

    props = {
        'AcceptLanguage': (str, False),
        'Description': (str, False),
        'PortfolioId': (str, True),
        'ProductId': (str, True),
        'TagUpdateOnProvisionedProduct': (validate_tag_update, True),
    }


class DefinitionParameter(AWSProperty):
    props = {
        'Key': (str, True),
        'Value': (str, True),
    }


class ServiceAction(AWSObject):
    resource_type = "AWS::ServiceCatalog::ServiceAction"

    props = {
        'AcceptLanguage': (str, False),
        'Definition': ([DefinitionParameter], True),
        'DefinitionType': (str, True),
        'Description': (str, False),
        'Name': (str, True),
    }


class ServiceActionAssociation(AWSObject):
    resource_type = "AWS::ServiceCatalog::ServiceActionAssociation"

    props = {
        'ProductId': (str, True),
        'ProvisioningArtifactId': (str, True),
        'ServiceActionId': (str, True),
    }


class StackSetConstraint(AWSObject):
    resource_type = "AWS::ServiceCatalog::StackSetConstraint"

    props = {
        'AcceptLanguage': (str, False),
        'AccountList': ([str], True),
        'AdminRole': (str, True),
        'Description': (str, True),
        'ExecutionRole': (str, True),
        'PortfolioId': (str, True),
        'ProductId': (str, True),
        'RegionList': ([str], True),
        'StackInstanceControl': (str, True),
    }


class TagOption(AWSObject):
    resource_type = "AWS::ServiceCatalog::TagOption"

    props = {
        'Active': (boolean, False),
        'Key': (str, True),
        'Value': (str, True),
    }


class TagOptionAssociation(AWSObject):
    resource_type = "AWS::ServiceCatalog::TagOptionAssociation"

    props = {
        'ResourceId': (str, True),
        'TagOptionId': (str, True),
    }
