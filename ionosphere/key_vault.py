from base import ARMObject, ARMProperty


class VaultAccessPolicyPermission(ARMProperty):
    props = {
        'keys': ([str], False),
        'secrets': ([str], False),
        'certificates': ([str], False),
        'storage': ([str], False),
    }


class VaultAccessPolicy(ARMProperty):
    props = {
        'tenantId': (str, True),
        'objectId': (str, True),
        'applicationId': (str, False),
        'permissions': (VaultAccessPolicyPermission, True),
    }


class VaultAccessPolicies(ARMObject):
    resource_type = 'Microsoft.KeyVault/vaults/accessPolicies'
    apiVersion = '2018-02-14'
    props = {
        'accessPolicies': ([VaultAccessPolicy], True),
    }

    def validate_title(self):
        if all((action not in self.title for action in ['add', 'replace', 'remove'])):
            raise ValueError('KeyVault AccessPolicies name must contain an action (add, remove, or replace)')
