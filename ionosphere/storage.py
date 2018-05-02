from base import ARMObject, ARMRootProperty, ARMProperty


class Sku(ARMRootProperty):
    props = {
        'name': (str, True)  # todo - add validation: Gets or sets the sku name.
        # todo - Required for account creation; optional for update
        # todo - values: Standard_LRS, Standard_GRS, Standard_RAGRS, Standard_ZRS, Premium_LRS
    }


class VirtualNetworkRule(ARMProperty):
    props = {
        'id': (str, True)
    }


class IPRule(ARMProperty):
    props = {
        'value': (str, True)  # Specifies the IP or IP range in CIDR format. Only IPV4 address is allowed.
    }


class NetworkRuleSet(ARMProperty):
    props = {
        # 'bypass': (str, False)
        'virtualNetworkRules': ((list, VirtualNetworkRule), False),
        'ipRules': ((list, IPRule), False),
        'defaultAction': (str, True)  # Allow/Deny
    }


# todo add title validaton: 3-24 chars lengths, numbers and lower case letters
class StorageAccount(ARMObject):
    resource_type = 'Microsoft.Storage/storageAccounts'
    apiVersion = "2017-10-01"
    location = True

    props = {
        'sku': (Sku, True),  # Required
        'kind': (str, True),  # Required. Indicates the type of storage account. - Storage, StorageV2, BlobStorage
        # 'customDomain':
        # 'encryption':
        'networkAcls': (NetworkRuleSet, False),
        'supportsHttpsTrafficOnly': (bool, False),
        'accessTier': (str, False),
        'tags': (dict, False)
    }

    def __init__(self, title, template=None, validation=None, **kwargs):
        ARMObject.__init__(self, title, template, validation, **kwargs)

        super(StorageAccount, self)._validate_props()
        # move kind to root
        self.resource['kind'] = self.properties['kind']
        del self.properties['kind']
        del self.props['kind']

    def to_dict(self):
        self._move_prop_to_root('sku')
        return ARMObject.to_dict(self)
