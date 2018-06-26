# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean


class AcceptedPortfolioShare(AWSObject):
    resource_type = "AWS::ServiceCatalog::AcceptedPortfolioShare"

    props = {
        'AcceptLanguage': (basestring, False),
        'PortfolioId': (basestring, True),
    }


class ProvisioningArtifactProperties(AWSProperty):
    props = {
        'Description': (basestring, False),
        'Info': (dict, True),
        'Name': (basestring, False),
    }


class CloudFormationProduct(AWSObject):
    resource_type = "AWS::ServiceCatalog::CloudFormationProduct"

    props = {
        'AcceptLanguage': (basestring, False),
        'Description': (basestring, False),
        'Distributor': (basestring, False),
        'Name': (basestring, True),
        'Owner': (basestring, True),
        'ProvisioningArtifactParameters':
            ([ProvisioningArtifactProperties], True),
        'SupportDescription': (basestring, False),
        'SupportEmail': (basestring, False),
        'SupportUrl': (basestring, False),
        'Tags': (Tags, False),
    }


class ProvisioningParameter(AWSProperty):
    props = {
        'Key': (basestring, False),
        'Value': (basestring, False),
    }


class CloudFormationProvisionedProduct(AWSObject):
    resource_type = "AWS::ServiceCatalog::CloudFormationProvisionedProduct"

    props = {
        'AcceptLanguage': (basestring, False),
        'NotificationArns': ([basestring], False),
        'PathId': (basestring, False),
        'ProductId': (basestring, False),
        'ProductName': (basestring, False),
        'ProvisionedProductName': (basestring, False),
        'ProvisioningArtifactId': (basestring, False),
        'ProvisioningArtifactName': (basestring, False),
        'ProvisioningParameters': ([ProvisioningParameter], False),
        'Tags': (Tags, False),
    }


class LaunchNotificationConstraint(AWSObject):
    resource_type = "AWS::ServiceCatalog::LaunchNotificationConstraint"

    props = {
        'AcceptLanguage': (basestring, False),
        'Description': (basestring, False),
        'NotificationArns': ([basestring], True),
        'PortfolioId': (basestring, True),
        'ProductId': (basestring, True),
    }


class LaunchRoleConstraint(AWSObject):
    resource_type = "AWS::ServiceCatalog::LaunchRoleConstraint"

    props = {
        'AcceptLanguage': (basestring, False),
        'Description': (basestring, False),
        'PortfolioId': (basestring, True),
        'ProductId': (basestring, True),
        'RoleArn': (basestring, True),
    }


class LaunchTemplateConstraint(AWSObject):
    resource_type = "AWS::ServiceCatalog::LaunchTemplateConstraint"

    props = {
        'AcceptLanguage': (basestring, False),
        'Description': (basestring, False),
        'PortfolioId': (basestring, True),
        'ProductId': (basestring, True),
        'Rules': (basestring, True),
    }


class Portfolio(AWSObject):
    resource_type = "AWS::ServiceCatalog::Portfolio"

    props = {
        'AcceptLanguage': (basestring, False),
        'Description': (basestring, False),
        'DisplayName': (basestring, True),
        'ProviderName': (basestring, True),
        'Tags': (Tags, False),
    }


class PortfolioPrincipalAssociation(AWSObject):
    resource_type = "AWS::ServiceCatalog::PortfolioPrincipalAssociation"

    props = {
        'AcceptLanguage': (basestring, False),
        'PortfolioId': (basestring, True),
        'PrincipalARN': (basestring, True),
        'PrincipalType': (basestring, True),
    }


class PortfolioProductAssociation(AWSObject):
    resource_type = "AWS::ServiceCatalog::PortfolioProductAssociation"

    props = {
        'AcceptLanguage': (basestring, False),
        'PortfolioId': (basestring, True),
        'ProductId': (basestring, True),
        'SourcePortfolioId': (basestring, False),
    }


class PortfolioShare(AWSObject):
    resource_type = "AWS::ServiceCatalog::PortfolioShare"

    props = {
        'AcceptLanguage': (basestring, False),
        'AccountId': (basestring, True),
        'PortfolioId': (basestring, True),
    }


class TagOption(AWSObject):
    resource_type = "AWS::ServiceCatalog::TagOption"

    props = {
        'Active': (boolean, False),
        'Key': (basestring, True),
        'Value': (basestring, True),
    }


class TagOptionAssociation(AWSObject):
    resource_type = "AWS::ServiceCatalog::TagOptionAssociation"

    props = {
        'ResourceId': (basestring, True),
        'TagOptionId': (basestring, True),
    }
