# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from troposphere import Tags


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
