from base import ARMObject, ARMProperty


class StorageAccountSku(ARMProperty):
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
        # 'customDomain':
        # 'encryption':
        'networkAcls': (NetworkRuleSet, False),
        'supportsHttpsTrafficOnly': (bool, False),
        'accessTier': (str, False)
    }

    root_props = {
        'sku': (StorageAccountSku, True),
        'kind': (str, True),  # Required. Indicates the type of storage account. - Storage, StorageV2, BlobStorage
        'tags': (dict, False)
    }
