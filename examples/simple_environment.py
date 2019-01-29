import uuid
from compute import *
from base import ARMTemplate, ARMParameter
from network import *
from storage import StorageAccount, StorageAccountSku

template = ARMTemplate(customerUsageAttributionGuid='pid-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX')

vm_password_param = ARMParameter('vmPassword',
                                 template=template,
                                 type='secureString',
                                 description='The password for the VM access. User is "adminuser"')

vnet = VirtualNetwork("myvnet",
                      addressSpace=AddressSpace(addressPrefixes=['10.0.0.0/24']),
                      subnets=[Subnet('subnet1', addressPrefix='10.0.0.0/24')],
                      tags={'Key1': 'tag-key1', 'Key2': 'tag-key2', 'Key3': 'tag-key3'})

nsg = NetworkSecurityGroup("testvmNsg",
                           securityRules=[
                               SecurityRule('ssh',
                                            description='public ssh access',
                                            protocol='Tcp',
                                            destinationPortRange="22",
                                            destinationAddressPrefix="*",
                                            sourceAddressPrefix='Internet',
                                            sourcePortRange='*',
                                            access='Allow',
                                            direction='Inbound',
                                            priority=200
                                            )])

publicIp = PublicIPAddress('testvm_nic1_pubip', publicIPAllocationMethod='dynamic')

networkInterface = NetworkInterface('tesmvm_nic1',
                                    ipConfigurations=
                                        [NetworkInterfaceIPConfiguration('tesmvm_nic1_ip_config',
                                                                     privateIPAllocationMethod='Dynamic',
                                                                     subnet=SubResource(id=vnet.subnet_ref('subnet1')),
                                                                     publicIPAddress=SubResource(id=publicIp.Ref()))],
                                    networkSecurityGroup=SubResource(id=nsg.Ref()))
networkInterface.with_depends_on([publicIp, vnet])


vm = VirtualMachine('testvm',
                    hardwareProfile=HardwareProfile(vmSize='Basic_A0'),
                    storageProfile=StorageProfile(imageReference=ImageReference(publisher='Canonical',
                                                                                offer='UbuntuServer',
                                                                                sku='16.04-LTS'),
                                                  osDisk=OsDisk(createOption='FromImage',
                                                                diskSizeGB=50,
                                                                managedDisk=ManagedDiskParameters(storageAccountType='Standard_LRS'))),
                    osProfile=OSProfile(computerName='alextesm',
                                        adminUsername='adminuser',
                                        adminPassword=vm_password_param.Ref(),
                                        linuxConfiguration=LinuxConfiguration(disablePasswordAuthentication=False)),
                    networkProfile=NetworkProfile(networkInterfaces=
                                                  [NetworkInterfaceReference(id=networkInterface.Ref())]))
vm.with_depends_on(networkInterface)

storage = StorageAccount(str(uuid.uuid4())[-12:],
                         sku=StorageAccountSku(name='Standard_LRS'),
                         kind='StorageV2',
                         tags={'tag1': 'bla1'})

template.add_resource([vnet, nsg, publicIp, networkInterface, vm, storage])

print(template.to_json())
