from base import ARMObject


class UserAssignedIdentity(ARMObject):
    resource_type = 'Microsoft.ManagedIdentity/userAssignedIdentities'
    apiVersion = '2018-11-30'
    location = True
    root_props = {
        'tags': (dict, False)
    }
    props = {}

