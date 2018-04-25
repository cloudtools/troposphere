from . import ARMObject, ARMRootProperty, ARMProperty


class Plan(ARMRootProperty):
    props = {
        'name': (str, False),
        'publisher': (str, False),
        'product': (str, False),
        'promotionCode': (str, False)
    }


class HardwareProfile(ARMProperty):
    # todo add validations
    props = {
        'vmSize': (str, False)
    }


class ImageReference(ARMProperty):
    def __init__(self, title=None, version='latest', **kwargs):
        kwargs['version'] = version
        ARMProperty.__init__(self, title, **kwargs)

    # todo add validations
    props = {
        'publisher': (str, False),
        'offer': (str, False),
        'sku': (str, False),
        'version': (str, False)
    }


class VirtualHardDisk(ARMProperty):
    props = {
        'uri': (str, False)
    }


class ManagedDiskParameters(ARMProperty):
    props = {
        'id': (str, False),
        'storageAccountType': (str, False)  # todo add validation - Standard_LRS or Premium_LRS
    }


class OsDisk(ARMProperty):
    props = {
        'osTpe': (str, False),  # todo add validations: Linux/Windows
        # 'encryptionSettings': (object, False),  # todo add support for encryptionSettings
        'name': (str, False),
        'vhd': (VirtualHardDisk, False),
        'image': (VirtualHardDisk, False),
        # 'caching': (str, False),  # todo add support
        'createOption': (str, True),  # todo add validations
        'diskSizeGB': (int, False),  # todo add validations on max size
        'managedDisk': (ManagedDiskParameters, False)
    }


class StorageProfile(ARMProperty):
    props = {
        'imageReference': (ImageReference, False),
        'osDisk': (OsDisk, False)
        # 'dataDisks':  # todo add support
    }


class WindowsConfiguration(ARMProperty):
    props = {
        'provisionVMAgent': (bool, False),
        'enableAutomaticUpdates': (bool, False),
        'timeZone': (str, False),
        # 'additionalUnattendContent': (str, False),  # todo add support
        # 'winRM': (str, False)  # todo add support
    }


class SshPublicKey(ARMProperty):
    props = {
        'path': (str, False),
        'keyData': (str, False)
    }


class SshConfiguration(ARMProperty):
    props = {
        'publicKeys': ((list, SshPublicKey), False)
    }


class LinuxConfiguration(ARMProperty):
    props = {
        'disablePasswordAuthentication': (bool, False),
        'ssh': (SshConfiguration, False)
    }


class OSProfile(ARMProperty):
    # todo add valiation: https://docs.microsoft.com/en-us/azure/templates/microsoft.compute/virtualmachines#OSProfile
    props = {
        'computerName': (str, False),
        'adminUsername': (str, False),
        'adminPassword': (str, False),
        'customData': (str, False),
        'windowsConfiguration': (WindowsConfiguration, False),
        'linuxConfiguration': (LinuxConfiguration, False)
        # 'secrets': (, False)  # todo add support
    }


class NetworkInterfaceReferenceProperties(ARMProperty):
    props = {
        'primary': (bool, False)
    }


class NetworkInterfaceReference(ARMProperty):
    props = {
        'id': (str, False),
        'properties': (NetworkInterfaceReferenceProperties, False)
    }


class NetworkProfile(ARMProperty):
    props = {
        'networkInterfaces': ((list, NetworkInterfaceReference), False)
    }


class BootDiagnostics(ARMProperty):
    props = {
        'enabled': (bool, False),
        'storageUri': (str, False)
    }


class DiagnosticsProfile(ARMProperty):
    props = {
        'bootDiagnostics': (BootDiagnostics, False)
    }


class VirtualMachine(ARMObject):
    resource_type = 'Microsoft.Compute/virtualMachines'
    apiVersion = "2017-12-01"
    location = True

    def __init__(self, title, template=None, validation=True, **kwargs):
        ARMObject.__init__(self, title, template, validation, **kwargs)

    props = {
        'hardwareProfile': (HardwareProfile, False),
        'storageProfile': (StorageProfile, False),
        'osProfile': (OSProfile, False),
        'networkProfile': (NetworkProfile, False),
        'diagnosticsProfile': (DiagnosticsProfile, False),
        # 'availabilitySet': (),  # todo add support
        # 'licenseType': ()  # todo add support
        'plan': (Plan, False),
    }
