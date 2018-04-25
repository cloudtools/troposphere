import unittest

from azure import ARMTemplate
from azure.compute import VirtualMachine, HardwareProfile, StorageProfile, ImageReference, OsDisk, \
    ManagedDiskParameters, OSProfile, LinuxConfiguration, NetworkProfile, NetworkInterfaceReference
from azure.network import NetworkInterface


class TestAzureCompute(unittest.TestCase):
    def test_simple_vm(self):
        template = ARMTemplate()
        network_interface = NetworkInterface('tesmvm_nic1')
        vm = VirtualMachine('testvm',
                            template=template,
                            hardwareProfile=HardwareProfile(vmSize='Basic_A0'),
                            storageProfile=StorageProfile(imageReference=ImageReference(publisher='Canonical',
                                                                                        offer='UbuntuServer',
                                                                                        sku='16.04-LTS'),
                                                          osDisk=OsDisk(createOption='FromImage',
                                                                        diskSizeGB=50,
                                                                        managedDisk=ManagedDiskParameters(
                                                                            storageAccountType='Standard_LRS'))),
                            osProfile=OSProfile(computerName='testvm',
                                                adminUsername='adminuser',
                                                adminPassword='S0m3Str0ngP@ss0wd',
                                                linuxConfiguration=LinuxConfiguration(
                                                    disablePasswordAuthentication=False)),
                            networkProfile=NetworkProfile(networkInterfaces=
                                                          [NetworkInterfaceReference(id=network_interface.Ref())]))
        vm.to_dict()
        self.assertIn(vm, template.resources)


if __name__ == '__main__':
    unittest.main()

